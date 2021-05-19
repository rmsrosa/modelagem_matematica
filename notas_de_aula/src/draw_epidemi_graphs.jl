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
    arrow_color = "black"

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
    arrow_color = "black"

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
    arrow_color = "black"

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

img_dim = 192
Drawing(3*img_dim, img_dim, joinpath(@__DIR__, "..", "img", "sir_graph_"*string(2*img_dim)*"x"*string(img_dim)*".png"))
draw_sir(img_dim)
finish()

Drawing(3*img_dim, img_dim, joinpath(@__DIR__, "..", "img", "sis_graph_"*string(2*img_dim)*"x"*string(img_dim)*".png"))
draw_sis(img_dim)
finish()

Drawing(3*img_dim, img_dim, joinpath(@__DIR__, "..", "img", "si_graph_"*string(2*img_dim)*"x"*string(img_dim)*".png"))
draw_si(img_dim)
finish()