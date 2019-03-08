# Tools

These are tools for managing the collection of notebooks in this repository, giving them a book-like structure, with a table of contents, notebook headers, and top and bottom navigators.

## Files

- `jupyterbookmaker.py`: this is the main script/module that adds a table of contents, notebook headers and top and bottom navigators, according to some given parameters. 
- `config.yml`: this is the configuration file, in YAML format, to be passed to `jupyterbookmaker.py`, with the parameters used to create the book-like structure of the collection of jupyter notebooks in this repository.

## How to use them

In a `bash` terminal, within the `tools` directory, issue the command
```bash
./jupyterbookmaker.py config.yml
```

This populates (or updates) the notebooks with the table of contents, notebook headers, and top and bottom navigators.

## License

The codes within this subdirectory `tools` are licensed under the [MIT license](https://opensource.org/licenses/MIT), with copyright to Ricardo M. S. Rosa

## Credits

The `jupyterbookmaker.py` module/script is my own modification of the set of tools found in the [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) 
by [Jake VanderPlas](http://vanderplas.com/).