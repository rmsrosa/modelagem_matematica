using Luxor

"""
    drawmathmoddiag(base_length::Int)

Draw a diagram of the processos of mathematical modeling with dimensions 2base_length x base_length
"""
function drawmathmoddiag(base_length::Int)

    base_width = 1024
    s = 2*base_length/base_width

    origin() # Set origin to center of image
    scale(s) # Call to scale() must come after origin()

    pt_a = Point(-1.4, -0.55)*base_length
    pt_b = Point(0.0, -0.55)*base_length
    pt_c = Point(1.4, -0.55)*base_length
    pt_d = Point(-1.4, 0.55)*base_length
    pt_e = Point(0.0, 0.55)*base_length
    pt_f = Point(1.4, 0.55)*base_length

    pt_down = Point(0.0, 0.06)*base_length

    circle_color = "royalblue"
    circle_radius = 0.4*base_length
    circle_line_width = 0.01*base_length

    arrow_width = 0.002*base_width
    arrowhead_length = 0.02*base_width
    arrow_color = "royalblue"

    text_color = "brown3"
    fontface("Menlo")
    font_size = 30
    fontsize(font_size)
    
    setline(circle_line_width)

    @layer begin
        setcolor(circle_color)
        circle(pt_a, circle_radius, :stroke)
        setcolor(text_color)
        text("problema", pt_a - pt_down, halign=:center, valign=:middle)
        text("real", pt_a + pt_down, halign=:center, valign=:middle)
        setcolor(arrow_color)
        arrow(between(pt_a, pt_b, 0.32), between(pt_a, pt_b, 0.68),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(circle_color)
        circle(pt_b, circle_radius, :stroke)
        setcolor(text_color)
        text("modelo(s)", pt_b, halign=:center, valign=:middle)
        setcolor(arrow_color)
        arrow(between(pt_b, pt_c, 0.32), between(pt_b, pt_c, 0.68),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(circle_color)
        circle(pt_c, circle_radius, :stroke)
        setcolor(text_color)
        text("testes", pt_c, halign=:center, valign=:middle)
        setcolor(arrow_color)
        arrow(between(pt_c, pt_d, 0.15), between(pt_c, pt_d, 0.85),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )        

        setcolor(circle_color)
        circle(pt_d, circle_radius, :stroke)
        setcolor(text_color)
        text("validação", pt_d, halign=:center, valign=:middle)
        setcolor(arrow_color)
        arrow(between(pt_d, pt_e, 0.32), between(pt_d, pt_e, 0.68),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )
        arrow(between(pt_d, pt_b, 0.27), between(pt_d, pt_b, 0.73),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(circle_color)
        circle(pt_e, circle_radius, :stroke)
        setcolor(text_color)
        text("escolha", pt_e - pt_down, halign=:center, valign=:middle)
        text("do modelo", pt_e + pt_down, halign=:center, valign=:middle)
        setcolor(arrow_color)
        arrow(between(pt_e, pt_f, 0.32), between(pt_e, pt_f, 0.68),
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )

        setcolor(circle_color)
        circle(pt_f, circle_radius, :stroke)
        setcolor(text_color)
        text("análise,", pt_f - 2*pt_down, halign=:center, valign=:middle)
        text("previsões,", pt_f, halign=:center, valign=:middle)
        text("desenv.", pt_f + 2pt_down, halign=:center, valign=:middle)
    end
end

img_dim = 256
Drawing(2*img_dim, img_dim, joinpath(@__DIR__, "..", "img", "mathmoddiag_"*string(2*img_dim)*"x"*string(img_dim)*".png"))
drawmathmoddiag(img_dim)
finish()