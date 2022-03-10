using Weave
using Literate

"""
    function hfun_menubar()

Return the html code to display the menu bar, with the table of contents and other book info.
"""
@delay function hfun_menubar()
    menu = globvar(:menu)
    isnothing(menu) && return ""
    page_numbering = globvar(:page_numbering) === true
    toc = build_toc(menu, page_numbering)
    getfield.(last.(toc), :title)
    io = IOBuffer()

    write(
        io,
        """
        <div class="books-menu-content">
        """,
    )
    for entry in last.(toc)
        item =
            entry.filename === nothing ? entry.title :
            "<a href=\"/$(entry.filename)\">$(entry.title)</a>"
        write(
            io,
            """
                <div class="menu-level-$(entry.level)">
                <li>$item</li>
                </div>
            """,
        )
    end
    write(
        io,
        """
        <div>
        """,
    )

    return String(take!(io))
end

"""
    function hfun_get_title()

Return the title of the page, prepended with the section number.
"""
@delay function hfun_get_title(section = nothing)
    menu = globvar(:menu)
    filename = section === nothing ? locvar(:fd_rpath) : "$(section[1]).md"
    title = pagevar(filename, :title)
    isnothing(title) && return filename
    isnothing(menu) && return pagevar(filename, :title)

    filename_noext = first(splitext(filename))

    page_numbering = globvar(:page_numbering) === true
    toc = build_toc(menu, page_numbering)
    entries = toc[map(x -> x.filename, last.(toc)).==filename_noext]
    return length(entries) == 1 ? only(last.(entries)).title : "Title not found"
end

"""
    function hfun_navigation()

Return the html code to display the navigation buttons on the top and/or bottom of each page.
"""
@delay function hfun_navigation()
    io = IOBuffer()

    menu = globvar(:menu)
    isnothing(menu) && return String(take!(io))

    filename = locvar(:fd_rpath)

    filename_noext = first(splitext(filename))

    page_numbering = globvar(:page_numbering) === true
    toc = build_toc(menu, page_numbering)

    prevnext = build_prevnext(toc)
    entry = prevnext[first.(prevnext).==filename_noext]
    length(entry) == 1 || return String(take!(io))
    prev, next = last(only(entry))

    if prev !== nothing || next !== nothing
        write(
            io,
            """
            <div class="navbar">
                <p id="nav">
            """,
        )
    end

    if prev !== nothing
        prev_link = "/$prev"
        prev_title = only(last.(toc[getfield.(last.(toc), :filename).==prev])).title
        write(
            io,
            """
            <span id="nav-prev" style="float: left;">
            <a class="menu-level-1" href="$prev_link">$prev_title <kbd>←</kbd></a>
            </span>
            """,
        )
    end

    if next !== nothing
        next_link = "/$next"
        next_title = only(last.(toc[getfield.(last.(toc), :filename).==next])).title
        write(
            io,
            """
            <span id="nav-next" style="float: right;">
                <a class="menu-level-1" href="$next_link"><kbd>→</kbd> $next_title</a>
            </span>
            """,
        )
    end

    if prev !== nothing || next !== nothing
        write(
            io,
            """
                </p>
            </div>
            </br></br>
            """,
        )
    end

    return String(take!(io))
end

"""
    function hfun_github_repo_link()

Return the html code to display the link to the github repo.
"""
function hfun_github_repo_link()
    github_repo = globvar(:github_repo)
    (github_repo === nothing || github_repo == "") && return ""

    io = IOBuffer()

    write(
        io,
        """
        <a href="$github_repo"><img src="/assets/images/GitHub-Mark-32px.png" alt="GitHub repo" width="18" style="margin:5px 5px" align="left"></a>
        """,
    )

    return String(take!(io))
end

"""
    function build_toc(menu, page_numbering = true, level = 1, pre = "")

Build the table of contents out of the given `menu` variable, in a recursive way.
"""
function build_toc(menu, page_numbering = true, level = 1, pre = "")
    toc = []
    isnothing(menu) && return toc
    i = 0
    for m in menu
        sec, subsecs = m isa Pair ? m : (m, nothing)
        this_page_numbering = page_numbering * !startswith(sec, '*')
        sec = lstrip(sec, '*')

        new_pre = this_page_numbering === false ? "" : "$pre$(i += 1)."

        filename = process_it(sec)
        filename_noext = filename !== nothing ? first(splitext(filename)) : nothing

        title = filename === nothing ? sec : pagevar(filename, :title)
        if this_page_numbering !== false
            title = "$new_pre $title"
        end

        push!(toc, sec => (filename = filename_noext, title = title, level = level))
        if subsecs !== nothing
            append!(toc, build_toc(subsecs, this_page_numbering, level + 1, new_pre))
        end
    end
    return toc
end

"""
    function build_prevnext(toc)

Build the list with the information about the previous and next pages of each page.
"""
function build_prevnext(toc)
    prevnext = []
    isnothing(toc) && return prevnext
    prev = nothing
    ftoc = filter(x -> x.filename !== nothing, last.(toc))
    for i = 1:length(ftoc)-1
        push!(prevnext, ftoc[i].filename => (prev = prev, next = ftoc[i+1].filename))
        prev = ftoc[i].filename
    end
    push!(prevnext, ftoc[end].filename => (prev = prev, next = nothing))
    return prevnext
end

"""
    function process_it(filename)

Process a given julia script or Juno's style markdown file `.jmd` or jupyter notebook.

Processing is done via either Weave or Literate, depending on the folder it belongs to
(whether `_weave` or `_jupyter`, for Weave, or `_literate`, for Literate)

Processing generates a Markdown file for Franklin and a Jupyter notebook for the reader, if desired.
"""
function process_it(filename)
    startswith(filename, "pages/") && return "$filename.md"
    startswith(filename, "_src/") || return nothing

    out_path =
        replace(
            dirname(filename),
            r"^_src/weave" => "pages/weaved",
            r"^_src/literate" => "pages/literated",
            r"^_src/jupyter" => "pages/jupytered",
        )
    fig_path = "images"
    processed_filename = first(splitext("$out_path/$(basename(filename))")) * ".md"

    link_download_notebook = globvar(:link_download_notebook)
    link_nbview_notebook = globvar(:link_nbview_notebook)
    link_binder_notebook = globvar(:link_binder_notebook)

    if mtime(filename) > mtime(processed_filename)
        if startswith(filename, "_src/literate/")
            Literate.markdown(
                filename,
                out_path,
                execute = true,
                credit = false,
                flavor = Literate.FranklinFlavor(),
            )
        else
            Weave.weave(filename; out_path, fig_path, doctype = "github")
        end
        postprocess_it(processed_filename, out_path, fig_path)
    end

    notebook_output_dir = "__site/generated/notebooks/$(replace(dirname(filename), r"^_src/weave" => "weaved", r"^_src/literate" => "literated", r"^_src/jupyter" => "jupytered"))"
    notebook_path =
        first(splitext("$notebook_output_dir/$(basename(filename))")) * ".ipynb"

    if any(
        ==(true),
        (link_download_notebook, link_nbview_notebook, link_binder_notebook),
    ) && mtime(filename) > mtime(notebook_path)

        if startswith(filename, "_src/weave/")
            mkpath(notebook_output_dir)
            Weave.notebook(
                filename,
                out_path = notebook_output_dir,
                nbconvert_options = "--allow-errors",
            )
        elseif startswith(filename, "_src/literate/")
            Literate.notebook(filename, notebook_output_dir)
        elseif startswith(filename, "_src/jupyter/")
            mkpath(notebook_output_dir)
            cp(filename, "$notebook_output_dir/$(basename(filename))", force = true)
            #= 
            # The following would have the advantage of forcing a clean
            # execution of the notebook, but Weave currently has some issues
            # with that
            Weave.notebook(
                filename,
                out_path = notebook_output_dir,
                nbconvert_options = "--allow-errors"
            ) =#
        end
    end

    return first(splitext(processed_filename)) # remove extension ".md"
end

"""
    function hfun_linkbadges()

Return the html code for displaying the badges for accessing the notebooks and the source
code associated with each page that has been processed via Weave or Literate.
"""
@delay function hfun_linkbadges()
    filename = locvar(:fd_rpath)

    link_view_source = globvar(:link_view_source)
    link_download_notebook = globvar(:link_download_notebook)
    link_nbview_notebook = globvar(:link_nbview_notebook)
    link_binder_notebook = globvar(:link_binder_notebook)

    github_repo = globvar(:github_repo)

    notebook_path = "generated/notebooks/$(replace(dirname(filename), r"^pages/?" => ""))/$(replace(basename(filename), r".md$" => ".ipynb"))"

    io = IOBuffer()
    if (
        link_view_source == true &&
        startswith(filename, r"pages/(?:weaved|literated|jupytered)/")
    ) || (
        any(
            ==(true),
            (link_download_notebook, link_nbview_notebook, link_binder_notebook),
        ) && (isfile("__site/$notebook_path"))
    )
        write(
            io,
            """
            <div class="badges">
            <p>
            """,
        )
        if link_nbview_notebook == true && isfile("__site/$notebook_path")
            website = globvar(:website)
            write(
                io,
                """
                <a href=\"https://nbviewer.org/urls/$website/$notebook_path"><img align=\"left\" src=\"https://img.shields.io/badge/view%20in-nbviewer-orange\" alt=\"View in NBViewer\" title=\"View Jupyter notebook in NBViewer\"></a>
                """,
            )
        end
        if link_binder_notebook == true && isfile("__site/$notebook_path")
            nbgitpuller_repo = globvar(:nbgitpuller_repo)
            nbgitpuller_branch = globvar(:nbgitpuller_branch)
            binder_application = globvar(:binder_application)
            prepath = globvar(:prepath)
            if all(
                !isnothing,
                (nbgitpuller_repo, nbgitpuller_branch, binder_application, prepath),
            )
                nbgitpuller_repo = replace(nbgitpuller_repo, "https://github.com/" => "")

                binder_application =
                    binder_application == "" ? "tree" :
                    binder_application in ("lab", "retro") ? "$binder_application/tree" :
                    binder_application # not sure how the others work

                prepath == "" || (prepath = "$prepath/")
                write(
                    io,
                    """
                    <a href=\"https://mybinder.org/v2/gh/$nbgitpuller_repo/$nbgitpuller_branch?urlpath=git-pull%3Frepo%3D$github_repo%26urlpath%3D$binder_application%252F$prepath$notebook_path%26branch%3Dgh-pages\"><img align=\"left\" src=\"https://mybinder.org/badge.svg\" alt=\"Open in binder\" title=\"Open in binder\"></a>
                    """,
                )
            end
        end

        if link_download_notebook == true && isfile("__site/$notebook_path")
            write(
                io,
                """
                <a href=\"/$notebook_path"><img align=\"left\" src=\"https://img.shields.io/badge/download-notebook-blue\" alt=\"Download notebook\" title=\"Download Jupyter notebook\"></a>
                """,
            )
        end

        if link_view_source == true &&
           startswith(filename, r"pages/(?:weaved|literated|jupytered)/")
            menu = globvar(:menu)
            page_numbering = globvar(:page_numbering) === true
            toc = build_toc(menu, page_numbering)
            ftoc = filter(x -> last(x).filename == first(splitext(filename)), toc)
            source_path =
                length(ftoc) > 0 ? "$github_repo/blob/main/$(first(first.(ftoc)))" : nothing
            write(
                io,
                """
                <a href=\"$source_path"><img align=\"left\" src=\"https://img.shields.io/badge/view-source-lightblue\" alt=\"View source\" title=\"View source\"></a>
                """,
            )
        end

        write(
            io,
            """
            </p>
            </div></br>
            """,
        )
    end
    return String(take!(io))
end

"""
    postprocess_it(filename, out_path, fig_path)

Post-process a markdown file generated by Weave or Literate for compatibility with
Franklin, by replacing `![...](...)`` with either a full path or with `\figalt`/`\fig`
depending on the situation; by moving any output image to the proper place; and by
properly handling the title, adding the section number, if needed.
"""
function postprocess_it(filename, out_path, fig_path)
    tmppath, tmpio = mktemp()
    no_match_so_far = true
    open(filename, "r") do io
        for line in eachline(io, keep = true)
            if (m = match(r"^#\s+(.*)$", line)) !== nothing && no_match_so_far == true
                line = "@def title = \"$(m.captures[1])\"\n\n# {{ get_title }}\n"
                no_match_so_far = false
            else
                line = replace(
                    line,
                    r"!\[([^\]]*)\]\((?:\.\./)*_assets/([^\)]*)\)" =>
                        s"![\1](/assets/\2)",
                    r"^!\[\]\(([^/)][^\)]*)\)" => s"\\fig{\1}",
                    r"^!\[([^\]]*)\]\(([^/)][^\)]*)\)" => s"\\figalt{\1}{\2}",
                    r"(?<!\!)\[[^\]]*\]\(/pages/([^\)]*)\)" => s" [{{get_title pages/\1}}](/pages/\1)"
                )
            end
            write(tmpio, line)
        end
    end
    close(tmpio)
    mv(tmppath, filename, force = true)
    if isdir("$out_path/$fig_path/")
        destination = "_assets/$(first(splitext(filename)))/code/$fig_path"
        mkpath(destination)
        mv("$out_path/$fig_path", destination, force = true)
    end
end
