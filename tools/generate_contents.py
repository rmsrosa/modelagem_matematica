'''
Table of Contents generator for collections of Jupyter notebooks

Based on module `generate_contents.py` in the 
[Python Data Science Handbook](in https://github.com/jakevdp/PythonDataScienceHandbook) 
by [Jake VanderPlas](http://vanderplas.com/)
'''
import os
import re
import itertools
import nbformat

NOTEBOOK_DIR = os.path.join(os.path.dirname(__file__), '..', 'notebooks')

#  tested in https://regexr.com/
REG = re.compile(r'(\b\d\d|[0][A-Z])\.(\d{2}|)-(.*)\.ipynb') 
    
def iter_notebooks():
    return sorted(nb for nb in os.listdir(NOTEBOOK_DIR) if REG.match(nb))


def get_notebook_title(nb_file):
    nb = nbformat.read(os.path.join(NOTEBOOK_DIR, nb_file), as_version=4)
    for cell in nb.cells:
        if cell.source.startswith('#'):
            return cell.source[1:].splitlines()[0].strip()


def gen_contents(directory=None):
    for nb in iter_notebooks():
        if directory:
            nb_url = os.path.join(directory, nb)
        else:
            nb_url = nb
        chapter, section, title = REG.match(nb).groups()
        if chapter.isdecimal():
            chapter_clean = int(chapter)
        else:
            chapter_clean = chapter[1]
        title = get_notebook_title(nb)
        if section == '00':
            if chapter in ['00', '98', '99']:
                yield '\n### [{0}]({1})'.format(title, nb_url)
            else:
                yield '\n### [{0}. {1}]({2})'.format(chapter_clean,
                                                     title, nb_url)
        elif section == '':
            yield '\n### {0}'.format(title)
        else:
            yield "- [{0}.{1}. {2}]({3})".format(chapter_clean, int(section), title, nb_url)


def print_contents(directory=None):
    print('\n'.join(gen_contents(directory)))


if __name__ == '__main__':
    print_contents()
    print('\n', 70 * '#', '\n')
#    print_contents('http://nbviewer.jupyter.org/github/rmsrosa/modelagem_matematica/blob/master/notebooks/')
