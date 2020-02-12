# The Jupyter Bookmaker

The `jupyterbookmaker.py` is a module/script that generate a book-like structure for a collection of [Jupyter](https://jupyter.org/) notebooks, giving them a table of contents, notebook headers, and top and bottom navigators.

The script is included here and its package can be found in the github repository [rmsrosa/jupyterbookmaker](https://github.com/rmsrosa/jupyterbookmaker)

As a script, `jupyterbookmaker.py` reads a given configuration file, in the [YAML](https://en.wikipedia.org/wiki/YAML) format, to properly construct the book-like structure in a desired way.

As a module, it can build the structure out of a configuration file and also provides some extra features. See the github repository for more details.

Within this [rmsrosa/modelagem_matematica](https://github.com/rmsrosa/modelagem_matematica) repository, the module is copied verbatim in the `tools` folder and it is imported and used in the Jupyter notebook [../notebooks/Estrutura_livro.ipynb] to build the book-like structure.

The `jupyterbookmaker.py` is licensed under the [GNU GPLv3 license](https://www.gnu.org/licenses/gpl.html). It is my own modification of the set of tools found in the [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) 
by [Jake VanderPlas](http://vanderplas.com/), which are originally realeased under the [MIT license](https://opensource.org/licenses/MIT)