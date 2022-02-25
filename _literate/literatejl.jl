# # Literated Julia Script

# This page was generated from a **julia script**, automatically converted to markdown with [Literate.jl](https://github.com/fredrikekre/Literate.jl). The conversion happens automatically when the menu is constructed.

# ## Julia Dots

# PNG with path relative to site, i.e. `/assets/images/julia-logo-dots-small.png`:

# ![Julia dots](/assets/images/julia-logo-dots-small.png)

# ## Julia Speeder

# GIF with path relative to file but within `_assets/`, i.e. `../_assets/images/juliaspeeder32x32.gif`, and postprocessed accordingly, so it works both in Franklin and in Literate:

# ![Julia speeder](../_assets/images/juliaspeeder32x32.gif)

# ## Math

# $$
# \exp(i\pi) + 1 = 0
# $$

# ## Code chunks

# Here is a julia chunk:

x = 1

# and another:

println("hello world!")

# ## Plot

using Plots

x = 0.0:0.01:2π
y = sin.(2x) + sin.(5x)

plot(x, y)
