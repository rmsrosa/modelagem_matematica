#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Generates a book-like structure to a collection of Jupyter notebooks.
'''

__author__ = "Ricardo M. S. Rosa <rmsrosa@gmail.com>"
__homepage__ = "http://github.com/rmsrosa/jupyterbookmaker"
__copyright__ = '''
Original work Copyright (c) 2016 Jacob VanderPlas
Modified work licensed under GNU GPLv3
'''
__license__ = "GNU GPLv3"
__version__ = "0.2.0"
__status__ = "beta"

import os
import re
import itertools
import sys
import yaml

import nbformat
from nbformat.v4.nbbase import new_markdown_cell

# Regular expression for indexing the notebooks
# Tested in https://regexr.com/
REG = re.compile(r'(\b\d\d|[A][A-Z]|[B][A-Z])\.(\d{2}|)-(.*)\.ipynb') 

TOC_MARKER = "<!--TABLE_OF_CONTENTS-->"    
HEADER_MARKER = "<!--HEADER-->"   
NAVIGATOR_MARKER = "<!--NAVIGATOR-->"

def indexed_notebooks(directory='.'):
    '''
    Returns a sorted list with the filenames of the 'indexed notebooks'
    in the given 'directory'. The 'indexed notebooks' are those that
    match the regular expression REG. Filenames that do not
    match the regular expression are ignored.

    Argument:
    ---------
        directory: string
            The directory that contains the notebooks. 

    Returns:
    -------
        : list of strings
            A list with the filenames of the notebooks that match 
            the regular expression (the 'indexed notebooks'), 
            ordered by the lexicographycal order.

    Raises:
    -------
    
    '''
    return sorted(nb for nb in os.listdir(directory) if REG.match(nb))

def is_marker_cell(MARKER, cell):
    return  cell.source.startswith(MARKER)

def remove_marker_cell(MARKER, directory='.'):
    for nb_name in indexed_notebooks(directory):
        nb_file = os.path.join(directory, nb_name)
        nb = nbformat.read(nb_file, as_version=4)

        new_cells = []
        for cell in nb.cells:
            if not is_marker_cell(MARKER, cell):
                new_cells.append(cell)
            else:
                print(f"- removing '{MARKER}' cell from {nb_name}")

        nb.cells = new_cells
        nbformat.write(nb, nb_file)

def get_notebook_title(nb_name, directory='.'):
    '''
    Returns the title of a juyter notebook.

    It looks for the first cell, in the notebook, that starts with
    the markdown symbol '#' and returns the contents of the first line
    of this cell, striped out of '#' and the remaining lines.

    Input:
    ------
        directory: string
            The directory that contains the notebook.
        nb_name: string
            The name of the jupyter notebook file.
    
    Output:
    -------
        : string
            The desired title of the notebook or None if not found.

    '''
    nb = nbformat.read(os.path.join(directory, nb_name), as_version=4)
    for cell in nb.cells:
        if cell.source.startswith('#'):
            return cell.source[1:].splitlines()[0].strip()


def get_notebook_full_entry(nb_name, directory='.'):
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

def get_notebook_entry(nb_name, directory='.', show_full_entry=True):
    if show_full_entry:
        entry = get_notebook_full_entry(nb_name, directory)[1]
    else:
        entry = get_notebook_title(nb_name, directory)
    return entry   

def yield_contents(directory='.'):
    for nb_name in indexed_notebooks(directory):
        markdown_entry, notebook_entry = get_notebook_full_entry(nb_name, directory)
        yield f'{markdown_entry}[{notebook_entry}]({nb_name})'

def print_contents(directory='.'):
    print('\n'.join(yield_contents(directory)))


def get_contents(directory='.'):
    """
    Returns a string with the 'Table of Contents' constructed 
    from the collection of notebooks in the 'directory' given
    as argument.
    """

    contents = ""
    for item in yield_contents(directory):
        contents += item + "\n"
    
    return contents

def add_contents(toc_nb_name, directory='.'):
    # error handling
    assert(type(directory)==str), "Argument 'directory' should be a string"
    assert(type(toc_nb_name)==str), "Argument 'toc_nb_name' should be a string"

    contents = TOC_MARKER + "\n\n"
    for item in yield_contents(directory):
        contents += item + "\n"

    toc_nb_file = os.path.join(directory, toc_nb_name)

    toc_nb = nbformat.read(toc_nb_file, as_version=4)

    toc_cell_found = False
    for cell in toc_nb.cells:
        if is_marker_cell(TOC_MARKER, cell):
            cell.source = contents
            toc_cell_found = True
            
    if toc_cell_found:
        nbformat.write(toc_nb, toc_nb_file)
        print(f'- Table of contents updated in {toc_nb_name}')
    else:
        print(f'* No markdown cell starting with {TOC_MARKER} found in {toc_nb_name}')

def add_headers(header, directory='.'):
    for nb_name in indexed_notebooks(directory):
        nb_file = os.path.join(directory, nb_name)
        nb = nbformat.read(nb_file, as_version=4)

        if nb.cells and is_marker_cell(HEADER_MARKER, nb.cells[0]):    
            print('- updating header for {0}'.format(nb_name))
            nb.cells[0].source = HEADER_MARKER + '\n' + header
        else:
            print('- inserting header for {0}'.format(nb_name))
            nb.cells.insert(0, new_markdown_cell(HEADER_MARKER + '\n' + header))
        nbformat.write(nb, nb_file)

def prev_this_next(it):
    a, b, c = itertools.tee(it,3)
    next(c)
    return zip(itertools.chain([None], a), b, itertools.chain(c, [None]))

def get_navigator_entries(core_navigators = [], directory='.', 
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

    for prev_nb, this_nb, next_nb in prev_this_next(indexed_notebooks(directory)):
        navbar = ""
        if prev_nb:
            entry = get_notebook_entry(prev_nb, directory, show_full_entry)
            navbar += PREV_TEMPLATE.format(title=entry, url=prev_nb)

        for center_nb in core_navigators:
            entry = get_notebook_entry(center_nb, directory, show_full_entry)
            navbar += CENTER_TEMPLATE.format(title=entry, url=center_nb)

        if next_nb:
            entry = get_notebook_entry(next_nb, directory, show_full_entry)
            navbar += NEXT_TEMPLATE.format(title=entry, url=next_nb)

        this_colab_link = COLAB_LINK.format(repository=repository, 
            branch=branch, notebook_filename=os.path.basename(this_nb))
        this_binder_link = BINDER_LINK.format(repository=repository, 
            branch=branch, notebook_filename=os.path.basename(this_nb))
            
        yield os.path.join(directory, this_nb), navbar, this_colab_link, this_binder_link

def add_navigators(core_navigators=[], directory='.', 
                   repository = '', branch = '', 
                   show_colab=False, show_binder=False, 
                   show_full_entry=True):
    for nb_file, navbar, this_colab_link, this_binder_link in get_navigator_entries(core_navigators, directory, repository, branch, show_full_entry):
        nb = nbformat.read(nb_file, as_version=4)
        nb_name = os.path.basename(nb_file)

        navbar_top = navbar_bottom = NAVIGATOR_MARKER + "\n"
        navbar_bottom = NAVIGATOR_MARKER + "\n\n---\n" + navbar
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

        if len(nb.cells) > 1 and is_marker_cell(NAVIGATOR_MARKER, nb.cells[1]):         
            print("- updating navbar for {0}".format(nb_name))
            nb.cells[1].source = navbar_top
        else:
            print("- inserting navbar for {0}".format(nb_name))
            nb.cells.insert(1, new_markdown_cell(source=navbar_top))

        if nb.cells and is_marker_cell(NAVIGATOR_MARKER, nb.cells[-1]):
            nb.cells[-1].source = navbar_bottom
        else:
            nb.cells.append(new_markdown_cell(source=navbar_bottom))
        nbformat.write(nb, nb_file)

def make_book(toc_nb_name, header, core_navigators,
              directory='.', repository='', branch='', 
              show_colab=False, show_binder=False, show_full_entry=True):

    add_contents(toc_nb_name = toc_nb_name, directory = directory)
    add_headers(header = header, directory = directory)
    add_navigators(core_navigators=core_navigators, directory=directory, 
                   repository=repository, branch=branch, 
                   show_colab=show_colab, show_binder=show_binder,
                   show_full_entry=show_full_entry)

def make_book_from_configfile(config_file):
    with open(config_file, 'r') as f:
        config = yaml.load(f)
    if 'book' in config:
        make_book(**config['book'])
    else:
        directory = '.'
        for sec in config:
            if 'directory' in config[sec]:
                directory = config[sec]['directory']

        if 'contents' in config:
            add_contents(**config['contents'])

        if 'header' in config:
            add_headers(**config['header'])
        else:
            remove_marker_cell(HEADER_MARKER, directory)

        if 'navigator' in config:
            add_navigators(**config['navigator'])
        else:
            remove_marker_cell(NAVIGATOR_MARKER, directory)

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
