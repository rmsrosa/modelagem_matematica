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
__version__ = "0.3.2"
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
REG = re.compile(r'(\b\d\d|\b[A][A-Z]|\b[B][A-Z])\.(\d{2}|)-(.*)\.ipynb') 

TOC_MARKER = "<!--TABLE_OF_CONTENTS-->"    
HEADER_MARKER = "<!--HEADER-->"   
NAVIGATOR_MARKER = "<!--NAVIGATOR-->"

def indexed_notebooks(app_to_notes_path='.'):
    '''
    Returns a sorted list with the filenames of the 'indexed notebooks'
    in the given 'app_to_notes_path'. The 'indexed notebooks' are those that
    match the regular expression REG. Filenames that do not
    match the regular expression are ignored.

    Argument:
    ---------
        app_to_notes_path: string
            The path to the directory that contains the notebooks, 
            either the absolute path or the path relative from 
            where the code is being ran.

    Returns:
    -------
        : list of strings
            A list with the filenames of the notebooks that match 
            the regular expression (the 'indexed notebooks'), 
            ordered by the lexicographycal order.

    Raises:
    -------
    
    '''
    return sorted(nb for nb in os.listdir(app_to_notes_path) if REG.match(nb))

def is_marker_cell(MARKER, cell):
    return  cell.source.startswith(MARKER)

def remove_marker_cell(MARKER, app_to_notes_path='.'):
    for nb_name in indexed_notebooks(app_to_notes_path):
        nb_file = os.path.join(app_to_notes_path, nb_name)
        nb = nbformat.read(nb_file, as_version=4)

        new_cells = []
        for cell in nb.cells:
            if not is_marker_cell(MARKER, cell):
                new_cells.append(cell)
            else:
                print(f"- removing '{MARKER}' cell from {nb_name}")

        nb.cells = new_cells
        nbformat.write(nb, nb_file)

def get_notebook_title(nb_name, app_to_notes_path='.'):
    '''
    Returns the title of a juyter notebook.

    It looks for the first cell, in the notebook, that starts with
    the markdown symbol '#' and returns the contents of the first line
    of this cell, striped out of '#' and the remaining lines.

    Input:
    ------
        nb_name: string
            The name of the jupyter notebook file.
        app_to_notes_path: string
            The path to the directory that contains the notebooks, 
            either the absolute path or the path relative from 
            where the code is being ran.
    
    Output:
    -------
        : string
            The desired title of the notebook or None if not found.

    '''
    nb = nbformat.read(os.path.join(app_to_notes_path, nb_name), as_version=4)
    for cell in nb.cells:
        if cell.source.startswith('#'):
            return cell.source[1:].splitlines()[0].strip()


def get_notebook_full_entry(nb_name, app_to_notes_path='.'):
    '''
    Returns the entry of a notebook to be used in the Table of Contents

    Input:
    ------
        nb_name: string
            The name of the jupyter notebook file. 
        app_to_notes_path: string
            The path to the directory that contains the notebooks, 
            either the absolute path or the path relative from 
            where the code is being ran.

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
    title = get_notebook_title(nb_name, app_to_notes_path)

    if chapter=='00' or chapter[0]=='B' or section=='':
        markdown_entry = '### '
        num_entry = ''
    elif section=='00':
        markdown_entry = '### '
        num_entry = f'{chapter_clean}. '
    else:
        markdown_entry = '&nbsp;&nbsp;&nbsp;&nbsp; '
        num_entry = f'{chapter_clean}.{int(section)}. '
    
    return markdown_entry, num_entry, title

def get_notebook_entry(nb_name, app_to_notes_path='.', 
                       show_full_entry=True):
    if show_full_entry:
        entry = ''.join(list(get_notebook_full_entry(nb_name, app_to_notes_path)[1:3]))
    else:
        entry = get_notebook_title(nb_name, app_to_notes_path)
    return entry   

def yield_contents(app_to_notes_path='.', show_full_entry_in_toc=True):
    for nb_name in indexed_notebooks(app_to_notes_path):
        markdown_entry, num_entry, title = get_notebook_full_entry(nb_name, app_to_notes_path)
        if show_full_entry_in_toc:
            yield f'{markdown_entry}[{num_entry + title}]({nb_name})\n'
        else:
            yield f'{markdown_entry}[{title}]({nb_name})\n'
 

def print_contents(app_to_notes_path='.', 
                   show_full_entry_in_toc=True):
    print('\n'.join(yield_contents(app_to_notes_path, 
                                   show_full_entry_in_toc)))


def get_contents(app_to_notes_path='.', show_full_entry_in_toc=True):
    """
    Returns a string with the 'Table of Contents' constructed 
    from the collection of notebooks in the 'app_to_notes_path' given
    as argument.
    """

    contents = ""
    for item in yield_contents(app_to_notes_path, show_full_entry_in_toc):
        contents += item + "\n"
    
    return contents

def add_contents(toc_nb_name, app_to_notes_path='.',
                 show_full_entry_in_toc=True):
    # error handling
    assert(type(app_to_notes_path)==str), "Argument 'app_to_notes_path' should be a string"
    assert(type(toc_nb_name)==str), "Argument 'toc_nb_name' should be a string"

    contents = TOC_MARKER + "\n\n"
    for item in yield_contents(app_to_notes_path, show_full_entry_in_toc):
        contents += item + "\n"

    toc_nb_file = os.path.join(app_to_notes_path, toc_nb_name)

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

def add_headers(header, app_to_notes_path='.'):
    for nb_name in indexed_notebooks(app_to_notes_path):
        nb_file = os.path.join(app_to_notes_path, nb_name)
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

def get_navigator_entries(core_navigators = [], app_to_notes_path='.', 
                          repository = '', branch = '',
                          github_nb_dir = '', 
                          show_full_entry_in_nav = True):

    PREV_TEMPLATE = "[<- {title}]({url}) "
    CENTER_TEMPLATE = "| [{title}]({url}) "
    NEXT_TEMPLATE = "| [{title} ->]({url})"

    COLAB_LINK = """
<a href="https://colab.research.google.com/github/{repository}/blob/{branch}/{github_nb_dir}/{notebook_filename}"><img align="left" src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" title="Open and Execute in Google Colaboratory"></a>
"""
    BINDER_LINK = """
<a href="https://mybinder.org/v2/gh/{repository}/{branch}?filepath={github_nb_dir}/{notebook_filename}"><img align="left" src="https://mybinder.org/badge.svg" alt="Open in binder" title="Open and Execute in Binder"></a>
"""

    for prev_nb, this_nb, next_nb in prev_this_next(indexed_notebooks(app_to_notes_path)):
        navbar = ""
        if prev_nb:
            entry = get_notebook_entry(prev_nb, app_to_notes_path, 
                                       show_full_entry_in_nav)
            navbar += PREV_TEMPLATE.format(title=entry, url=prev_nb)

        for center_nb in core_navigators:
            entry = get_notebook_entry(center_nb, app_to_notes_path, 
                                       show_full_entry_in_nav)
            navbar += CENTER_TEMPLATE.format(title=entry, url=center_nb)

        if next_nb:
            entry = get_notebook_entry(next_nb, app_to_notes_path, 
                                       show_full_entry_in_nav)
            navbar += NEXT_TEMPLATE.format(title=entry, url=next_nb)

        this_colab_link = COLAB_LINK.format(repository=repository, 
            branch=branch, github_nb_dir=github_nb_dir, 
            notebook_filename=os.path.basename(this_nb))
        this_binder_link = BINDER_LINK.format(repository=repository, 
            branch=branch, github_nb_dir=github_nb_dir, 
            notebook_filename=os.path.basename(this_nb))
            
        yield os.path.join(app_to_notes_path, this_nb), navbar, this_colab_link, this_binder_link

def add_navigators(core_navigators=[], app_to_notes_path='.', 
                   repository = '', branch = '', 
                   github_nb_dir = '',
                   show_colab=False, show_binder=False, 
                   show_full_entry_in_nav=True):
    for nb_file, navbar, this_colab_link, this_binder_link in get_navigator_entries(core_navigators, app_to_notes_path, repository, 
                          branch, github_nb_dir, show_full_entry_in_nav):
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
              app_to_notes_path='.', repository='', branch='', 
              github_nb_dir ='',
              show_colab=False, show_binder=False,
              show_full_entry_in_toc=True,
              show_full_entry_in_nav=True):

    add_contents(toc_nb_name=toc_nb_name, 
                 app_to_notes_path=app_to_notes_path,
                 show_full_entry_in_toc=show_full_entry_in_toc)

    add_headers(header = header, app_to_notes_path = app_to_notes_path)

    add_navigators(core_navigators=core_navigators,
                   app_to_notes_path=app_to_notes_path, 
                   repository=repository, branch=branch, 
                   github_nb_dir=github_nb_dir,
                   show_colab=show_colab, show_binder=show_binder,
                   show_full_entry_in_nav=show_full_entry_in_nav)

def make_book_from_configfile(config_file):
    with open(config_file, 'r') as f:
        config = yaml.load(f)

    if 'directory' in config:
        app_to_notes_path = config['directory']['app_to_notes_path']
    else:
        app_to_notes_path = '.'

    if 'book' in config:
        make_book(**config['book'], 
                app_to_notes_path=app_to_notes_path)
    else:
        if 'contents' in config:
            add_contents(**config['contents'], 
                app_to_notes_path=app_to_notes_path)

        if 'header' in config:
            add_headers(**config['header'], 
                app_to_notes_path=app_to_notes_path)
        else:
            remove_marker_cell(HEADER_MARKER, app_to_notes_path)

        if 'navigator' in config:
            add_navigators(**config['navigator'], 
                app_to_notes_path=app_to_notes_path)
        else:
            remove_marker_cell(NAVIGATOR_MARKER, app_to_notes_path)

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
