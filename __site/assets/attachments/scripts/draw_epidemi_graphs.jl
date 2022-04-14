using Luxor

"""
    draw_sir(base_length::Int)

Draw a compartment flux-type diagram of the SIR epidemiological model.
"""
function draw_sir(base_length::Int)

    base_width = 1024
    s = 2*base_length/base_width

    origin() # Set origin to center of image
    scale(s) # Call to scale() must come after origin()

    pt_sus = Point(-3.0, 0.0)*base_length
    pt_inf = Point(0.0, 0.0)*base_length
    pt_rec = Point(3.0, 0.0)*base_length

    sus_color = "forestgreen"
    inf_color = "brown3"
    rec_color = "royalblue"

    circle_radius = 0.8*base_length
    circle_line_width = 0.01*base_length

    arrow_width = 0.002*base_width
    arrowhead_length = 0.02*base_width
    arrow_color = "gray30"

    text_color = "white"
    fontface("Menlo")
    font_size = 34
    fontsize(font_size)
    
    setline(circle_line_width)

    @layer begin
        setcolor(sus_color)
        circle(pt_sus, circle_radius, :fill)
        setcolor(text_color)
        text("Suscetiveis", pt_sus, halign=:center, valign=:middle)

        setcolor(arrow_color)
        arrow(between(pt_sus, pt_inf, 0.32), between(pt_sus, pt_inf, 0.68),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(inf_color)
        circle(pt_inf, circle_radius, :fill)
        setcolor(text_color)
        text("Infectados", pt_inf, halign=:center, valign=:middle)

        setcolor(arrow_color)
        arrow(between(pt_inf, pt_rec, 0.32), between(pt_inf, pt_rec, 0.68),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(rec_color)
        circle(pt_rec, circle_radius, :fill)
        setcolor(text_color)
        text("Recuperados", pt_rec, halign=:center, valign=:middle)
    end
end

"""
    draw_sis(base_length::Int)

Draw a compartment flux-type diagram of the SIS epidemiological model.
"""
function draw_sis(base_length::Int)

    base_width = 1024
    s = 2*base_length/base_width

    origin() # Set origin to center of image
    scale(s) # Call to scale() must come after origin()

    pt_sus = Point(-2.0, 0.0)*base_length
    pt_inf = Point(2.0, 0.0)*base_length

    pt_displacement = Point(0.0, 0.1)*base_length

    sus_color = "forestgreen"
    inf_color = "brown3"

    circle_radius = 0.8*base_length
    circle_line_width = 0.01*base_length

    arrow_width = 0.002*base_width
    arrowhead_length = 0.02*base_width
    arrow_color = "gray30"

    text_color = "white"
    fontface("Menlo")
    font_size = 34
    fontsize(font_size)
    
    setline(circle_line_width)

    @layer begin
        setcolor(sus_color)
        circle(pt_sus, circle_radius, :fill)
        setcolor(text_color)
        text("Suscetiveis", pt_sus, halign=:center, valign=:middle)

        setcolor(arrow_color)
        arrow(between(pt_sus - pt_displacement, pt_inf - pt_displacement, 0.26),
            between(pt_sus - pt_displacement, pt_inf - pt_displacement, 0.74),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(inf_color)
        circle(pt_inf, circle_radius, :fill)
        setcolor(text_color)
        text("Infectados", pt_inf, halign=:center, valign=:middle)

        setcolor(arrow_color)
        arrow(between(pt_inf + pt_displacement, pt_sus + pt_displacement, 0.26), 
            between(pt_inf + pt_displacement, pt_sus + pt_displacement, 0.74),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )
    end
end

"""
    draw_si(base_length::Int)

Draw a compartment flux-type diagram of the SI epidemiological model.
"""
function draw_si(base_length::Int)

    base_width = 1024
    s = 2*base_length/base_width

    origin() # Set origin to center of image
    scale(s) # Call to scale() must come after origin()

    pt_sus = Point(-2.0, 0.0)*base_length
    pt_inf = Point(2.0, 0.0)*base_length

    sus_color = "forestgreen"
    inf_color = "brown3"

    circle_radius = 0.8*base_length
    circle_line_width = 0.01*base_length

    arrow_width = 0.002*base_width
    arrowhead_length = 0.02*base_width
    arrow_color = "gray30"

    text_color = "white"
    fontface("Menlo")
    font_size = 34
    fontsize(font_size)
    
    setline(circle_line_width)

    @layer begin
        setcolor(sus_color)
        circle(pt_sus, circle_radius, :fill)
        setcolor(text_color)
        text("Suscetiveis", pt_sus, halign=:center, valign=:middle)

        setcolor(arrow_color)
        arrow(between(pt_sus, pt_inf, 0.26),
            between(pt_sus, pt_inf, 0.74),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(inf_color)
        circle(pt_inf, circle_radius, :fill)
        setcolor(text_color)
        text("Infectados", pt_inf, halign=:center, valign=:middle)
    end
end

"""
    draw_sis_struct(base_length::Int)

Draw a compartment flux-type diagram of a structured SIS epidemiological 
model, with high and low risks.
"""
function draw_sis_struct(base_length::Int)

    base_width = 1024
    s = 2*base_length/base_width

    origin() # Set origin to center of image
    scale(s) # Call to scale() must come after origin()

    pt_sus_low = Point(-2.0, -1.0)*base_length
    pt_inf_low = Point(2.0, -1.0)*base_length
    pt_sus_high = Point(-2.0, 1.0)*base_length
    pt_inf_high = Point(2.0, 1.0)*base_length

    pt_displacement = Point(0.0, 0.1)*base_length

    sus_color = "forestgreen"
    inf_color = "brown3"

    circle_radius = 0.8*base_length
    circle_line_width = 0.01*base_length

    arrow_width = 0.002*base_width
    arrowhead_length = 0.02*base_width
    arrow_color = "gray30"

    text_color = "white"
    fontface("Menlo")
    font_size = 34
    fontsize(font_size)
    
    setline(circle_line_width)

    @layer begin
        setcolor(sus_color)
        circle(pt_sus_low, circle_radius, :fill)
        setcolor(text_color)
        text("Suscetiveis", pt_sus_low - pt_displacement, halign=:center, valign=:middle)
        text("baixo risco", pt_sus_low + pt_displacement, halign=:center, valign=:middle)

        setcolor(arrow_color)
        arrow(between(pt_sus_low + pt_displacement, pt_inf_low + pt_displacement, 0.26),
            between(pt_sus_low + pt_displacement, pt_inf_low + pt_displacement, 0.74),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(inf_color)
        circle(pt_inf_low, circle_radius, :fill)
        setcolor(text_color)
        text("Infectados", pt_inf_low - pt_displacement, halign=:center, valign=:middle)
        text("baixo risco", pt_inf_low + pt_displacement, halign=:center, valign=:middle)

        setcolor(arrow_color)
        arrow(between(pt_inf_low - pt_displacement, pt_sus_low - pt_displacement, 0.26), 
            between(pt_inf_low - pt_displacement, pt_sus_low - pt_displacement, 0.74),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(sus_color)
        circle(pt_sus_high, circle_radius, :fill)
        setcolor(text_color)
        text("Suscetiveis", pt_sus_high - pt_displacement, halign=:center, valign=:middle)
        text("alto risco", pt_sus_high + pt_displacement, halign=:center, valign=:middle)

        setcolor(arrow_color)
        arrow(between(pt_sus_high - pt_displacement, pt_inf_high - pt_displacement, 0.26),
            between(pt_sus_high - pt_displacement, pt_inf_high - pt_displacement, 0.74),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(inf_color)
        circle(pt_inf_high, circle_radius, :fill)
        setcolor(text_color)
        text("Infectados", pt_inf_high - pt_displacement, halign=:center, valign=:middle)
        text("alto risco", pt_inf_high + pt_displacement, halign=:center, valign=:middle)

        setcolor(arrow_color)
        arrow(between(pt_inf_high + pt_displacement, pt_sus_high + pt_displacement, 0.26), 
            between(pt_inf_high + pt_displacement, pt_sus_high + pt_displacement, 0.74),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(arrow_color)
        setdash("dotted")
        arrow(between(pt_inf_high, (pt_sus_low + pt_inf_low)/2, 0.32), 
            between(pt_inf_high, (pt_sus_low + pt_inf_low)/2, 0.90),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )
        arrow(between(pt_inf_low, (pt_sus_high + pt_inf_high)/2, 0.32), 
        between(pt_inf_low, (pt_sus_high + pt_inf_high)/2, 0.90),
        linewidth=arrow_width,
        arrowheadlength=arrowhead_length,
        arrowheadangle=pi/4,
    )
    end
end

"""
    draw_sites(base_length::Int)

Draw sites for a network epimiological model.
"""
function draw_sites(base_length::Int)

    base_width = 1024
    s = 2*base_length/base_width

    origin() # Set origin to center of image
    scale(s) # Call to scale() must come after origin()

    pt_A = Point(-2.0, 0.0)*base_length
    pt_B = Point(0.0, 1.0)*base_length
    pt_C = Point(2.0, -1.0)*base_length

    site_color = "forestgreen"

    circle_radius_A = 0.8*base_length
    circle_radius_B = 0.6*base_length
    circle_radius_C = 0.4*base_length
    circle_line_width = 0.01*base_length

    arrow_width = 0.002*base_width
    arrowhead_length = 0.02*base_width
    arrow_color = "gray30"

    text_color = "white"
    fontface("Menlo")
    font_size = 34
    fontsize(font_size)
    
    setline(circle_line_width)

    @layer begin
        for (p, c, n) in (
                (pt_A, circle_radius_A, "Zona A"),
                (pt_B, circle_radius_B, "Zona B"),
                (pt_C, circle_radius_C, "Centro")
        )
            setcolor(site_color)
            circle(p, c, :fill)
            setcolor(text_color)
            text(n, p, halign=:center, valign=:middle)
        end

        setcolor(arrow_color)
        for (p,q,α,β) in (
                (pt_A, pt_B, 0.38, 0.71),
                (pt_A, pt_C, 0.21, 0.89),
                (pt_B, pt_C, 0.23, 0.84)
            )
            arrow(between(p, q, α),
                between(p, q, β),
                linewidth=arrow_width,
                arrowheadlength=arrowhead_length,
                arrowheadangle=pi/4,
            )
            arrow(between(p, q, β),
                between(p, q, α),
                linewidth=arrow_width,
                arrowheadlength=arrowhead_length,
                arrowheadangle=pi/4,
            )
        end
    end
end

img_dim = 192
Drawing(3*img_dim, img_dim, joinpath(@__DIR__, "..", "img", "sir_graph.png"))
draw_sir(img_dim)
finish()

Drawing(3*img_dim, img_dim, joinpath(@__DIR__, "..", "img", "sis_graph.png"))
draw_sis(img_dim)
finish()

Drawing(3*img_dim, img_dim, joinpath(@__DIR__, "..", "img", "si_graph.png"))
draw_si(img_dim)
finish()

Drawing(3*img_dim, 1.5*img_dim, joinpath(@__DIR__, "..", "img", "sis_struct_graph.png"))
draw_sis_struct(img_dim)
finish()

Drawing(3*img_dim, 1.5*img_dim, joinpath(@__DIR__, "..", "img", "sites_graph.png"))
draw_sites(img_dim)
finish()
