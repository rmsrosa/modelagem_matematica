"""
Display WAV with audio controls and caption.

Creates a new scruct `CWAVArray` based on `WAV.WAVArray` from `WAV.jl` that
contains an extra `caption` field (AbstractString) and a corresponding `show`
method that wraps the html audio controls in an html figure element with
the caption contained in the `CWAVArray`.
"""
module AudioCaptionDisplay

import Base.show
import WAV: wavwrite

using Base64: base64encode

export show
export CWAVArray

struct CWAVArray{T,N}
    Fs::Number
    data::AbstractArray{T,N}
    caption::AbstractString
end

CWAVArray(Fs::Number, data::AbstractArray) = CWAVArray(Fs, data, "")

wavwrite(x::CWAVArray, io::IO) = wavwrite(x.data, io; Fs=x.Fs)

function show(io::IO, ::MIME"text/html", x::CWAVArray)
    buf = IOBuffer()
    wavwrite(x, buf)
    data = base64encode(String(take!(copy(buf))))
    markup = """<figure>
                $(ifelse(x.caption !== "", "<figcaption>$(x.caption)</figcaption>", ""))
                <audio controls="controls" {autoplay}>
                <source src="data:audio/wav;base64,$data" type="audio/wav" />
                Your browser does not support the audio element.
                </audio>
                </figure>"""
    print(io, markup)
end
end