"""
Display movies within browsers.
"""
module DisplayMovie

using Base64

export display_movie

function display_movie(filename; width = 512, embed = false)
    fmt = split(filename, '.')[end]
    if fmt in ("mp4", "avi")
        if embed == true
            src = "data:video/$fmt;base64, $(base64encode(open(read, filename)))"
        else
            src = filename
        end
        display(
            "text/html",
            string(
                """<video autoplay controls width="$width" src="$src" type="video/$fmt">
                Sorry, your browser doesn't support embedded videos.
                </video>"""
                )
            )
    else
        throw(
            ArgumentError(
                "Format not supported. Only `mp4` and `avi` currently implemented"
            )
        )
    end
    return nothing
end

end