using Luxor

"""
    drawpendulum(img_width::Int)

Draw the schematics of a pendulum with dimensions `img_width × img_width`.
"""
function drawpendulum(img_width::Int)

    base_width = 1024
    s = img_width/base_width

    origin() # Set origin to center of image
    scale(s) # Call to scale() must come after origin()

    pt_fix = Point(0.0, -0.45)*base_width
    pt_bob = Point(0.35, 0.20)*base_width
    pt_down = Point(0.0, 0.1)*base_width
    pt_right = Point(0.1, 0.0)*base_width
    fix_radius = 0.02*base_width
    bob_radius = 0.08*base_width
    line_width = 0.005*base_width
    arrow_width = 0.003*base_width
    arrowhead_length = 0.03*base_width
    path_width = 0.002*base_width
    fix_color = "royalblue"
    line_color = fix_color
    ceiling_color = "gray"
    bob_color = "mediumorchid3"
    arrow_color = "brown3"
    path_color = "forestgreen"
    fontface("JuliaMono")
    fontsize(60)

    @layer begin
        setcolor(ceiling_color)
        setline(path_width)
        for j = -0.9:0.4:0.7
            line(pt_fix + j*pt_right, pt_fix + (j+0.3)*pt_right - 0.3*pt_down, :stroke)
        end
        line(pt_fix - pt_right, pt_fix + pt_right, :stroke)
        setcolor(line_color)
        setline(line_width)
        line(pt_fix, pt_bob, :stroke)
        circle(pt_fix, fix_radius, :fill)
        text("ℓ", between(pt_fix, pt_bob, 0.45) + 0.2*pt_right)
        text("m", pt_bob, halign=:center)
        setcolor(arrow_color)    
        arrow(pt_bob, pt_bob + 2.5*pt_down,
            linewidth=arrow_width,
            arrowheadlength=arrowhead_length,
            arrowheadangle=pi/4,
        )
        text("(0,-mg)", pt_bob + 2*pt_down - 0.4*pt_right, halign=:right)
        setcolor(path_color)
        setdash("longdashed")
        setline(path_width)
        sector(pt_fix, distance(pt_fix,pt_bob), distance(pt_fix,pt_bob), π/4 + π/32, 3π/4 -π/32, 15, :stroke)
        setcolor(bob_color)
        circle(pt_bob, bob_radius, :fill)
        text("m", pt_bob - pt_down, halign=:center)
    end  
end

img_width = 256
Drawing(img_width, img_width, joinpath(@__DIR__, "..", "img", "pendulum_"*string(img_width)*"x"*string(img_width)*".png"))
drawpendulum(img_width)
finish()
