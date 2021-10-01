"""
VideoTracking v0.0.2

"""
module VideoTracking

using VideoIO
using Images
using ImageDraw
using StatsBase
using ProgressMeter

import Base: intersect, show
import ImageDraw: RectanglePoints

export intersect
export RectanglePoints

struct Blob
    x::Float64
    y::Float64
    xspan::UnitRange{Int}
    yspan::UnitRange{Int}
    area::Int
end

function show(io::IO, p::Blob)
    print(io, "Blob Object\n")
    print(io, "  Centroid coordinates: (x, y) = ($(p.x), $(p.y))\n")
    print(io, "  Span values: (xspan, yspan) = ($(p.xspan), $(p.yspan))\n")
    print(io, "  Occupied: area = $(p.area)\n")
    return nothing
end

RectanglePoints(p::Blob) =
    RectanglePoints(
        Point(first(p.xspan), first(p.yspan)),
        Point(last(p.xspan), last(p.yspan))
    )

intersect(p1::Blob, p2::Blob) = 
    length(intersect(p1.xspan, p2.xspan)) > 0 && length(intersect(p1.yspan, p2.yspan)) > 0

mutable struct Track
    nspan::UnitRange{Int}
    path::Vector{Blob}
end

function show(io::IO, trk::Track)
    print(io, "Tracked blob with framespan nspan = $(trk.nspan)\n")
    return nothing
end

function locate_components(labeled)
    N = maximum(labeled)
    positions = Vector{Blob}()
    for i in 1:N
        blob = labeled .== i
        xs = sum(blob, dims = 1)
        ys = sum(blob, dims = 2)
        push!(
            positions,
            Blob(
                mean(1:length(xs), weights(xs)),
                mean(1:length(ys), weights(ys)),
                findfirst(xs[1, :] .> 0):findlast(xs[1, :] .> 0),
                findfirst(ys[:, 1] .> 0):findlast(ys[:, 1] .> 0),
                sum(xs)
            )
        )
    end
    return positions
end

function find_tracks(filename; threshold = 0.15, min_area = 500, min_span = 30)
    video = VideoIO.load(filename)
    position_list = Vector{Vector{Blob}}()
    background = convert.(RGB{Float16}, video[1])
    mask = convert.(Gray{Float16}, background) .> 1
    @showprogress "Processing $(length(video)) frames ..." for vd in video
        mask .= convert.(
            Gray{Float16},
            abs.(
                convert.(RGB{Float16}, vd) - 
                background
            )
        ) .> threshold
        labeled_components = label_components(mask)
        # colorset = distinguishable_colors(maximum(labeled_components), colorant"black", dropseed = true)
        # coloredmask = map( n -> colorset[n+1], labeled_components)
        components_location = locate_components(labeled_components)
        filter!(p -> p.area > min_area, components_location)
        push!(position_list, components_location)
    end

    tracks = Vector{Track}()

    @showprogress "Gathering tracks ..." for n in 2:length(video)
        for t in position_list[n]

            new = true
            for v in tracks
                if last(v.nspan) == n - 1 && intersect(t, v.path[end]) == true
                    cs = v.nspan
                    v.nspan = first(cs):last(cs) + 1
                    push!(v.path, t) # append path
                    new = false
                end
            end
            if new == true
                push!(tracks, Track(n:n, [t])) # append object list
            end
        end
    end

    filter!(t -> length(t.nspan) ≥ min_span, tracks)

    return tracks
end

function tracks_on_video(
        filename::AbstractString,
        tracks::Vector{Track},
        outputfile::AbstractString = "";
        encoder_options::NamedTuple = (crf=23, preset="medium")
)
    video = VideoIO.load(filename)
    trackedvideo = copy(video)
    colorset = distinguishable_colors(length(tracks), colorant"black", dropseed = true)

    @showprogress "Drawing tracks ..." for (k, v) in enumerate(tracks)
        for (n, p) in zip(v.nspan, v.path)
            draw!(trackedvideo[n], Polygon(RectanglePoints(p)), colorset[k]) 
        end
    end

    if outputfile == ""
        li = findlast(".", filename)
        outputfile = filename[1:last(li)-1] * "_tracked" * filename[first(li):end]
    end

    framerate = Int(round(length(video)/VideoIO.get_duration(filename)))
    VideoIO.save(
        outputfile,
        trackedvideo,
        framerate = framerate,
        encoder_options = encoder_options
    )
    
    @info "Video saved with $(length(video)) frames and $(length(tracks)) tracks"
    return nothing
end

end

#= 
filename = joinpath("img", "pendulo_40cm_reduzido.mov")
tracks = find_tracks(filename)
tracks_on_video(filename, tracks)

p = plot(title = "Coordinate x of $(length(tracks)) tracks", titlefont = 10, legend=:topleft)
for (n, tr) in enumerate(tracks)
    plot!(p, tr.nspan, getfield.(tr.path, :x), label="track $n")
end
display(p)

p = plot(title = "Coordinate y of $(length(tracks)) tracks", titlefont = 10, legend=:topright)
for (n, tr) in enumerate(tracks)
    plot!(p, tr.nspan, -getfield.(tr.path, :y), label="track $n")
end
display(p)

p = plot(title = "Paths of $(length(tracks)) tracks", titlefont = 10, legend=:topright)
for (n, tr) in enumerate(tracks)
    plot!(p, getfield.(tr.path, :x), -getfield.(tr.path, :y), label="track $n")
end
display(p)
 =#