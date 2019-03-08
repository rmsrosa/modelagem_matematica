#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Adds a book-like structure to a collection of Jupyter notebooks.
'''

import os
import re
import itertools
import sys
import yaml

import nbformat
from nbformat.v4.nbbase import new_markdown_cell

version = '0.1.0'

# Regular expression for indexing the notebooks
# Tested in https://regexr.com/
REG = re.compile(r'(\b\d\d|[A][A-Z]|[B][A-Z])\.(\d{2}|)-(.*)\.ipynb') 

   
def iter_notebooks(directory=''):
    '''
    Returns a sorted list of the filenames in the given 'directory' 
    that matches the regular expression REG. Filenames that do not
    match the regular expression are ignored.

    Input:
    ------
        directory: string
            The directory that contains the notebooks. 
    Output:
    -------
        : list of strings
            A list, ordered by the lexicographycal order, with the 
            filenames of the notebooks that match the regular 
            expression.
    Raises:
    -------
    
    '''
    return sorted(nb for nb in os.listdir(directory) if REG.match(nb))


def get_notebook_title(nb_file, directory=''):
    '''
    Returns the title of a juyter notebook.

    It looks for the first cell, in the notebook, that starts with
    the markdown symbol '#' and returns the contents of the first line
    of this cell, striped out of '#' and the remaining lines.

    Input:
    ------
        directory: string
            The directory that contains the notebook.
        nb_file: string
            The name of the jupyter notebook file.
    
    Output:
    -------
        : string
            The desired title of the notebook or None if not found.

    '''
    nb = nbformat.read(os.path.join(directory, nb_file), as_version=4)
    for cell in nb.cells:
        if cell.source.startswith('#'):
            return cell.source[1:].splitlines()[0].strip()


def get_notebook_full_entry(nb_name, directory=''):
    '''
    Returns the entry of a notebook to be used in the Table of Contents

    Input:
    ------
        directory: string
            The directory that contains the notebooks.
        nb_name: string
            The name of the jupyter notebook file. 
    Output:
    -------
        markdown_entry: string
            The type of markdown header or identation for the entry in
            Table of Contents
        
        notebook_entry: strings
            The full notebook entry, with the title, preceeded, 
            depending on the case, of the Chapter and Section numbers
            or letters.

    '''
    chapter, section, title = REG.match(nb_name).groups()

    if chapter.isdecimal():
        chapter_clean = int(chapter)
    else:
        chapter_clean = chapter[1]
    title = get_notebook_title(nb_name, directory)

    if chapter=='00' or chapter[0]=='B' or section=='':
        markdown_entry, notebook_entry = '\n### ', '{0}'.format(title)
    elif section=='00':
        markdown_entry, notebook_entry= '\n### ', '{0}. {1}'.format(chapter_clean, title)
    else:
        markdown_entry, notebook_entry = '\n&nbsp;&nbsp;&nbsp;&nbsp; ', '{0}.{1}. {2}'.format(chapter_clean, int(section), title)

    return markdown_entry, notebook_entry

def get_notebook_entry(nb_name, directory='', show_full_entry=True):
    if show_full_entry:
        entry = get_notebook_full_entry(nb_name, directory)[1]
    else:
        entry = get_notebook_title(nb_name, directory)
    return entry   

def gen_contents(directory=''):
    for nb_name in iter_notebooks(directory):
        markdown_entry, notebook_entry = get_notebook_full_entry(nb_name, directory)
        yield f'{markdown_entry}[{notebook_entry}]({nb_name})'

def print_contents(directory=''):
    print('\n'.join(gen_contents(directory)))


def get_contents(directory=''):
    """
    Returns a string with the 'Table of Contents' constructed 
    from the collection of notebooks in the 'directory' given
    as argument.
    """

    contents = ""
    for item in gen_contents(directory):
        contents += item + "\n"
    
    return contents

def add_contents(toc_nb_name, directory=''):

    # error handling
    assert(type(directory)==str), "Argument 'directory' should be a string"
    assert(type(toc_nb_name)==str), "Argument 'toc_nb_name' should be a string"


    TOC_COMMENT = "<!--TABLE_OF_CONTENTS-->\n"

    contents = TOC_COMMENT + "\n\n"
    for item in gen_contents(directory):
        contents += item + "\n"

    if directory:
        toc_nb_file = os.path.join(directory, toc_nb_name)
    else:
        toc_nb_file = toc_nb_name

    toc_nb = nbformat.read(toc_nb_file, as_version=4)
    is_comment = lambda cell: cell.source.startswith(TOC_COMMENT)

    toc_cell_found = False
    for cell in toc_nb.cells:
        if is_comment(cell):
            cell.source = contents
            toc_cell_found = True
            
    if toc_cell_found:
        nbformat.write(toc_nb, toc_nb_file)
        print(f'Table of contents inserted in {toc_nb_name}')
    else:
        print(f'No markdown cell starting with {TOC_COMMENT} found in {toc_nb_name}')

def add_book_header(book_header, directory=''):
    BOOK_COMMENT = "<!--BOOK_INFORMATION-->\n"
    for nb_name in iter_notebooks(directory):
        nb_file = os.path.join(directory, nb_name)
        nb = nbformat.read(nb_file, as_version=4)

        is_comment = lambda cell: cell.source.startswith(BOOK_COMMENT)

        if is_comment(nb.cells[0]):
            print('- amending comment for {0}'.format(nb_name))
            nb.cells[0].source = BOOK_COMMENT + book_header
        else:
            print('- inserting comment for {0}'.format(nb_name))
            nb.cells.insert(0, new_markdown_cell(BOOK_COMMENT + book_header))
        nbformat.write(nb, nb_file)

def prev_this_next(it):
    a, b, c = itertools.tee(it,3)
    next(c)
    return zip(itertools.chain([None], a), b, itertools.chain(c, [None]))

def iter_navbars(center_nav, directory='', 
                 repository = None, branch = None, 
                 show_full_entry = True):

    PREV_TEMPLATE = "[<- {title}]({url}) "
    CENTER_TEMPLATE = "| [{title}]({url}) "
    NEXT_TEMPLATE = "| [{title} ->]({url})"

    COLAB_LINK = """
<a href="https://colab.research.google.com/github/{repository}/blob/{branch}/notebooks/{notebook_filename}"><img align="left" src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" title="Open and Execute in Google Colaboratory"></a>
"""
    BINDER_LINK = """
<a href="https://mybinder.org/v2/gh/{repository}/{branch}?filepath=notebooks/{notebook_filename}"><img align="left" src="https://mybinder.org/badge.svg" alt="Open in binder" title="Open and Execute in Binder"></a>
"""

    for prev_nb, nb, next_nb in prev_this_next(iter_notebooks(directory)):
        navbar = ""
        if prev_nb:
            entry = get_notebook_entry(prev_nb, directory, show_full_entry)
            navbar += PREV_TEMPLATE.format(title=entry, url=prev_nb)

        for center_nb in center_nav:
            entry = get_notebook_entry(center_nb, directory, show_full_entry)
            navbar += CENTER_TEMPLATE.format(title=entry, url=center_nb)

        if next_nb:
            entry = get_notebook_entry(next_nb, directory, show_full_entry)
            navbar += NEXT_TEMPLATE.format(title=entry, url=next_nb)

        this_colab_link = COLAB_LINK.format(repository=repository, 
            branch=branch, notebook_filename=os.path.basename(nb))
        this_binder_link = BINDER_LINK.format(repository=repository, 
            branch=branch, notebook_filename=os.path.basename(nb))
            
        yield os.path.join(directory, nb), navbar, this_colab_link, this_binder_link

def add_navbars(center_nav='', directory='', repository = '', branch = '', 
                show_colab=False, show_binder=False, 
                show_full_entry=True):
    NAV_COMMENT = "<!--NAVIGATION-->\n"
    for nb_name, navbar, this_colab_link, this_binder_link in iter_navbars(center_nav, directory, repository, branch, show_full_entry):
        nb = nbformat.read(nb_name, as_version=4)
        nb_file = os.path.basename(nb_name)
        is_comment = lambda cell: cell.source.startswith(NAV_COMMENT)

        navbar_top = navbar_bottom = NAV_COMMENT
        navbar_bottom = NAV_COMMENT + "\n---\n" + navbar
        if show_colab and show_binder:
            navbar_top += this_colab_link + "&nbsp;" + this_binder_link + "&nbsp;\n"
            navbar_bottom += "\n" + this_colab_link + this_binder_link + "&nbsp;" 
        elif show_colab:
            navbar_top += this_colab_link + "&nbsp;\n"
            navbar_bottom += "\n" + this_colab_link
        elif show_binder:
            navbar_top += this_binder_link + "&nbsp;\n" 
            navbar_bottom += "\n" + this_binder_link

        navbar_top += "\n" + navbar + "\n\n---\n"

        if is_comment(nb.cells[1]):
            print("- amending navbar for {0}".format(nb_file))
            nb.cells[1].source = navbar_top
        else:
            print("- inserting navbar for {0}".format(nb_file))
            nb.cells.insert(1, new_markdown_cell(source=navbar_top))

        if is_comment(nb.cells[-1]):
            nb.cells[-1].source = navbar_bottom
        else:
            nb.cells.append(new_markdown_cell(source=navbar_bottom))
        nbformat.write(nb, nb_name)

def make_book(toc_nb_name, book_header, center_nav,
              directory='', repository='', branch='', 
              show_colab=False, show_binder=False, show_full_entry=True):

    add_contents(toc_nb_name = toc_nb_name, directory = directory)
    add_book_header(book_header = book_header, directory = directory)
    add_navbars(center_nav=center_nav, directory=directory, 
                repository=repository, branch=branch, 
                show_colab=show_colab, show_binder=show_binder,
                show_full_entry=show_full_entry)

def make_book_from_configfile(config_file):
    with open(config_file, 'r') as f:
        config = yaml.load(f)
    if 'makebook' in config:
        make_book(**config['makebook'])
    else:
        if 'contents' in config:
            add_contents(**config['contents'])
        if 'book_header' in config:
            add_book_header(**config['book_header'])
        if 'navbars' in config:
            add_navbars(**config['navbars'])

if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] == '--help' or sys.argv[1] == '-h':
        print("\n Run the script with a configuration file as argument, e.g.")
        print("\n   ./jupyterbookmaker.py config.yml")
        print("\nFor the documentation, type 'pydoc3 jupyterbook.py'.\n")
    else:
        try:
            make_book_from_configfile(sys.argv[1])
        except NotImplementedError:
            print('provided argument is not a file or not a properly formated yaml configuration file.')
