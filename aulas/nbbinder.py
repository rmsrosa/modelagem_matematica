#!/anaconda3/envs/nbbinder/bin/python
# -*- coding: utf-8 -*-
"""
**NBBinder** generates a navigable book-like structure to a collection of
Jupyter notebooks.
"""

__author__ = "Ricardo M. S. Rosa <rmsrosa@gmail.com>"
__homepage__ = "http://github.com/rmsrosa/nbbinder"
__copyright__ = """Modified work Copyright (c) 2019 Ricardo M S Rosa
Original work Copyright (c) 2016 Jacob VanderPlas
"""
__license__ = "MIT"
__version__ = "0.12a2"
__config_version__ = "0.12a"

import os
import sys
import re
import itertools
import logging

from typing import Iterable

from packaging import version

import yaml

import nbformat
from nbformat.v4.nbbase import new_markdown_cell

from nbconvert import exporters

# Logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.WARNING)

# Regular expression for indexing the notebooks
# Tested in https://regexr.com/ (which is not the same flavor as python)
# in https://regex101.com/ (many flavors)
# in https://pythex.org/ (python flavor regex)

IDX_GRP = r'([0-9]{2}|[A-Z][0-9A-Z])'
COMPL_GRP = r'(\*[^#*]*[\*|\#]?[^#*]*[\*|\#]?[:.]?|)'
COMPL_SUBGRPS = r'^\*([^#*]*)([\*|\#]?)([^#*]*)([\*|\#]?)([:.]?)$'
MAIN_GRP = r'([^\)]*|[^\)]*\([^\)]*\)[^\)]*)'  # no open right parentheses
INS_GRP = r'(\&[a-z]?|)'

REG_IDX = re.compile('^' + IDX_GRP + '$')
REG = re.compile('^' + IDX_GRP + r'\.' + IDX_GRP + COMPL_GRP
                 + '-' + MAIN_GRP + r'(\.ipynb)$')
REG_INS = re.compile('^' + IDX_GRP + INS_GRP + r'\.'
                     + IDX_GRP + INS_GRP + COMPL_GRP
                     + '-' + MAIN_GRP + r'(\.ipynb)$')
REG_LINK = re.compile(r'(\]\()' + IDX_GRP + r'\.'
                      + IDX_GRP + COMPL_GRP
                      + '-' + MAIN_GRP + r'(\.ipynb)\)')
REG_COMPL = re.compile(COMPL_SUBGRPS)

# Markers for the affected notebook cells
TOC_MARKER = "<!--TABLE_OF_CONTENTS-->"
HEADER_MARKER = "<!--HEADER-->"
BADGES_MARKER = "<!--BADGES-->"
NAVIGATOR_MARKER = "<!--NAVIGATOR-->"

# Navigator templates
PREV_TEMPLATE = "[<- {title}]({url}) "
CENTER_TEMPLATE = "| [{title}]({url}) "
NEXT_TEMPLATE = "| [{title} ->]({url})"

# Link templates for the badges
BADGE_LINK = \
    """<a href="{badge_url}/{badge_filename}"><img align="left" \
src="{badge_src}" alt="{badge_alt}" title="{badge_title}"></a>
"""
BADGE_SHIELD_SRC = "https://img.shields.io/badge/\
{badge_label}-{badge_message}-{badge_color}"

# Metadata to flag cells for the slides
SLIDE_SHOW = {
    "slideshow": {
        "slide_type": "slide"
    }
}

SLIDE_SKIP = {
    "slideshow": {
        "slide_type": "skip"
    }
}


def indexed_notebooks(path_to_notes: str = None) -> list:
    """Returns a sorted list with the filenames of the "indexed notebooks".

    The notebooks are expected to be in the folder indicated by the
    argument `path_to_notes`. The "indexed notebooks" are those that
    match the regular expression REG. Filenames that do not match
    this regular expression are ignored.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    Returns
    -------
    : list of str
        A list with the filenames of the notebooks that match the regular
        expression, ordered by the lexicographycal order.
    """
    return sorted(nb for nb in os.listdir(path_to_notes) if REG.match(nb))


def increase_index(idx: str) -> str:
    """Increases an index by one unit.

    If the index is numeric, in the range '00' to '98', it adds one
    to the index and returns an index in the range '01' to '99'.
    If the index is already '99', there is an Exception error.

    If the index is alphanumeric, with the first character being a
    letter and the second character being a digit in the range '0' to
    '8', the digit is increased by one, and the function returns an
    index with the same first letter and with the digit in the range '1'
    to '9'. If the digit is already '9', there is an Exception error.

    If the index is purely alphabetical, then the ordinal ascii number
    of the letter is increased by 1, with the function returning
    an index with the same first character and with the second character
    in the range 'B' to 'Z'. If the second character is already 'Z',
    there is an Exception error.

    It also raises an exception if the given argument is not an index.

    Parameters
    ----------
    idx : str
        The index to be increased by one unit.

    Returns
    -------
    : str
        The index increased by one unit.

    Raises
    ------
    Exception if string is not an index.

    Exception if index is increasead beyond the allowed range.
    """
    if not REG_IDX.match(idx):
        raise Exception('String is not an index')

    if idx.isdecimal():
        n = int(idx) + 1
        if n > 99:
            raise Exception('Numeric index cannot be increased beyond 99')
        idx_plus_one = str(n).zfill(2)
    else:
        if idx[1] == '9' or idx[1] == 'Z':
            raise Exception('Index cannot be increased beyond allowed range')
        idx_plus_one = idx[0] + chr(ord(idx[1])+1)

    return idx_plus_one


def cleanup_marker_cells(path_to_notes: str = None, marker: str = None,
                         mode: str = 'remove') -> None:
    """Removes or clears the contents of any cell with the given `marker`.

    Depending on the value of the argument `mode`, it removes all the cells
    with the given `marker` from all the indexed notebooks in `path_to_notes`,
    if `mode == 'remove'`, or clears the contents of these cells (leaving
    the marker in the cell), if `mode == 'clear'`.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    marker : str
        The marker to be searched for.

    mode : str
        A string which should be either 'remove' or 'clear'.
    """
    if marker and (mode in ('clear', 'remove')):
        for nb_name in indexed_notebooks(path_to_notes):
            nb_file = os.path.join(path_to_notes, nb_name)
            nb = nbformat.read(nb_file, as_version=4)

            new_cells = []
            for cell in nb.cells:
                if not cell.source.startswith(marker):
                    new_cells.append(cell)
                elif mode == 'clear':
                    LOGGER.info("- clearing contents of '%s' cell from %s",
                                marker, nb_name)
                    new_cells.append(cell)
                    new_cells[-1].source = marker
                elif mode == 'remove':
                    LOGGER.info("- removing '%s' cell from %s",
                                marker, nb_name)

            nb.cells = new_cells

            nbformat.write(nb, nb_file)


def get_nb_title(path_to_notes: str = None, nb_name: str = None) -> str:
    """Returns the title of a juyter notebook.

    It looks for the first cell, in the notebook, that starts with
    a single markdown symbol '#' and returns the contents of the first
    line of this cell, striped out of '# ' and of any remaining lines.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    nb_name : str
        The name of the jupyter notebook file.

    Returns
    -------
    : str
        The desired title of the notebook or `None` if not found.
    """
    nb = nbformat.read(os.path.join(path_to_notes, nb_name), as_version=4)
    for cell in nb.cells:
        if cell.source.startswith('# '):
            return cell.source[1:].splitlines()[0].strip()
    return None


def get_nb_full_entry(path_to_notes: str = None,
                      nb_name: str = None) -> list:
    """Returns the full entry of a notebook.

    This entry is to be used for the link to the notebook from the
    table of contents and from the navigators.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    nb_name : str
        The name of the jupyter notebook file.

    Returns
    -------
    md_pre_entry : str
        The type of markdown header or identation for the entry in
        Table of Contents

    idx_entry : str
        The index entry, with the Chapter and Section numbers or letters.

    title : str
        The title of the notebook, as obtained from `get_nb_title()`.
    """
    chapter, section, complement = REG.match(nb_name).group(1, 2, 3)

    if chapter.isdecimal():
        chapter = chapter.lstrip('0')
    elif chapter[0] == 'A':
        chapter = chapter[1]
    elif not chapter[1].isdecimal():
        chapter = ''

    if section.isdecimal():
        section = section.lstrip('0')
    elif section[0] == 'A':
        section = section[1]
    elif not section[1].isdecimal():
        section = ''

    title = get_nb_title(path_to_notes, nb_name)

    if not complement or set(complement) in ({'*'}, {'#', '*'}):
        if not chapter or set(complement) == {'*'}:
            md_pre_entry = '### '
            idx_entry = ''
        elif not section or complement == '*#' or complement == '*#*':
            md_pre_entry = '### '
            idx_entry = '{}. '.format(chapter)
        else:
            md_pre_entry = '&nbsp;&nbsp;&nbsp;&nbsp; '
            idx_entry = '{}.{}. '.format(chapter, section)
    else:
        comp_reg = REG_COMPL.match(complement)
        if not comp_reg.group(4):
            md_pre_entry = '### '
        else:
            md_pre_entry = '&nbsp;&nbsp;&nbsp;&nbsp; '

        idx_entry = comp_reg.group(1)

        if comp_reg.group(2) == '#':
            idx_entry += ' ' + chapter

        if comp_reg.group(3):
            idx_entry += ' ' + comp_reg.group(3) + ' '

        if comp_reg.group(4) == '#':
            idx_entry += section

        if comp_reg.group(5):
            idx_entry += comp_reg.group(5) + ' '
        else:
            idx_entry += '. '

        idx_entry = idx_entry.lstrip()

    return md_pre_entry, idx_entry, title


def get_nb_entry(path_to_notes: str = None,
                 nb_name: str = None,
                 show_index: bool = True) -> str:
    """Returns the entry of a notebook.

    This entry is to be used for the link to the notebook from the
    table of contents and from the navigators. Depending on the
    value of the argument `show_index`, the entry can be either
    the full entry provided by the function `get_nb_full_entry()`
    or simply the title of the notebook, provided by the function
    `get_nb_title()`.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    nb_name : str
        The name of the jupyter notebook file.

    show_index : boolean
        Indicates whether to include the chapter and section numbers
        of the notebook in the table of contents (if True) or just
        the title (if False).

    Returns
    -------
    entry : str
        A string with the entry name.
    """
    if show_index:
        entry = ''.join(list(get_nb_full_entry(path_to_notes, nb_name)[1:3]))
    else:
        entry = get_nb_title(path_to_notes, nb_name)
    return entry


def yield_contents(path_to_notes: str = None,
                   show_index_in_toc: bool = True) -> Iterable[str]:
    """Iterable with entries for each of the indexed notebooks.

    It takes all the indexed notebooks and it creates a generator
    function to iterate from one notebook to the next, returning,
    each time, the navigator entry associated with that notebook.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    show_index_in_toc : bool
        Whether to display the navigator with the chapter
        and section number of each notebook or just their title.

    Yields
    ------
    : Iterable[str]
        Next navigator entry in the iterator
    """
    for nb_name in indexed_notebooks(path_to_notes):
        md_pre_entry, idx_entry, title \
            = get_nb_full_entry(path_to_notes, nb_name)
        if show_index_in_toc:
            yield '{}[{}]({})\n'.format(md_pre_entry,
                                        idx_entry + title,
                                        nb_name)
        else:
            yield '{}[{}]({})\n'.format(md_pre_entry, title, nb_name)


def get_contents(path_to_notes: str = None,
                 toc_title: str = '',
                 show_index_in_toc: bool = True) -> str:
    """Returns the 'Table of Contents'.

    Returns a string with the 'Table of Contents' constructed
    from the collection of notebooks in the folder indicated by
    the argument `path_to_notes`.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    toc_title : str
        Text to be displayed as the title for the table of contents cell,
        e.g. 'Contents', 'Table of Contents', or in other languages,
        'Conteúdo', 'Table des Matières', and so on.

    show_index_in_toc : bool
        Whether to display the table of contents with the chapter
        and section number of each notebook or just their title.

    Returns
    -------
    : str
        The table of contents.
    """

    contents = TOC_MARKER + "\n## [" + toc_title + "](#)\n\n"
    for item in yield_contents(path_to_notes, show_index_in_toc):
        contents += item + "\n"

    return contents


def insert_notebooks(path_to_notes: str = None) -> None:
    """Includes a notebook in the colllection.

    Checks whether there is any notebook that matches the regular expression
    indicating it is to be incuded in the collection of indexed notebooks
    and, if so, renames the affected notebooks in the appropriate order.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.
    """

    nb_names_ins = sorted(nb for nb in os.listdir(path_to_notes)
                          if REG_INS.match(nb))
    nb_names_new = nb_names_ins.copy()

    for j, _ in enumerate(nb_names_new):
        nbj_reg = REG_INS.match(nb_names_new[j])
        if nbj_reg.group(4):
            nb_names_new[j] = nbj_reg.group(1) + nbj_reg.group(2) \
                        + '.' + nbj_reg.group(3) \
                        + nbj_reg.group(5) + '-' + nbj_reg.group(6) \
                        + nbj_reg.group(7)
            for k in range(j+1, len(nb_names_new)):
                nbk_reg = REG_INS.match(nb_names_new[k])
                if nbk_reg.group(1, 2) == nbj_reg.group(1, 2):
                    gk3 = nbk_reg.group(3)
                    if ((gk3.isdecimal() and nbj_reg.group(3).isdecimal)
                            or gk3[0] == nbj_reg.group(3)[0]):
                        gk3_new = increase_index(gk3)
                    else:
                        gk3_new = gk3
                    if nbk_reg.group(3, 4) == nbj_reg.group(3, 4):
                        gk4_new = ''
                    else:
                        gk4_new = nbk_reg.group(4)
                    nb_names_new[k] = nbk_reg.group(1) + nbk_reg.group(2) \
                        + '.' + gk3_new + gk4_new + nbk_reg.group(5) + '-' \
                        + nbk_reg.group(6) + nbk_reg.group(7)
            nb_names_new[j] = nbj_reg.group(1) + nbj_reg.group(2) \
                + '.' + nbj_reg.group(3) \
                + nbj_reg.group(5) + '-' + nbj_reg.group(6) \
                + nbj_reg.group(7)
        if nbj_reg.group(2):
            for k in range(j+1, len(nb_names_new)):
                nbk_reg = REG_INS.match(nb_names_new[k])
                if ((nbk_reg.group(1).isdecimal() and
                     nbj_reg.group(1).isdecimal())
                        or nbk_reg.group(1)[0] == nbj_reg.group(1)[0]):
                    if nbk_reg.group(1, 2) == nbj_reg.group(1, 2):
                        gk1_new = nbk_reg.group(1)
                        gk2_new = ''
                    else:
                        gk1_new = increase_index(nbk_reg.group(1))
                        gk2_new = nbk_reg.group(2)
                    nb_names_new[k] = gk1_new + gk2_new + '.' \
                        + nbk_reg.group(3) + nbk_reg.group(4) \
                        + nbk_reg.group(5) + '-' \
                        + nbk_reg.group(6) + nbk_reg.group(7)
            nb_names_new[j] = nb_names_new[j][:nbj_reg.start(2)] \
                + nb_names_new[j][nbj_reg.end(2):]

    if nb_names_new == nb_names_ins:
        LOGGER.info('- no files need renaming, no reindexing needed')
    else:
        count = 0
        for f_ins, f_new in zip(nb_names_ins, nb_names_new):
            count += 1
            if f_ins != f_new:
                LOGGER.info('- replacing %s with %s', f_ins, f_new)
            else:
                LOGGER.info('- keeping %s', f_ins)
            os.rename(os.path.join(path_to_notes, f_ins),
                      os.path.join(path_to_notes, str(count) + '-' + f_new))
        count = 0
        for f_new in nb_names_new:
            count += 1
            os.rename(os.path.join(path_to_notes, str(count) + '-' + f_new),
                      os.path.join(path_to_notes, f_new))


def tighten_notebooks(path_to_notes: str = None) -> None:
    """Tighten the indices of the notebooks in the colllection.

    Checks whether there are gaps in the indices of the notebooks
    and, if so, renames the affected notebooks in the appropriate
    order.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.
    """

    nb_names = sorted(nb for nb in os.listdir(path_to_notes) if REG.match(nb))
    nb_names_new = nb_names.copy()

    nb_regs = [REG.match(nb_name) for nb_name in nb_names]
    nb_new_regs = nb_regs.copy()

    for j, nb_regj in enumerate(nb_regs[1:], 1):
        if nb_regj.group(1).isdecimal():
            if nb_regj.group(1) == nb_regs[j-1].group(1):
                nb_names_new[j] = nb_new_regs[j-1].group(1) \
                    + nb_names[j][nb_regj.end(1):]
            elif (nb_regj.group(1)
                  > increase_index(nb_new_regs[j-1].group(1))):
                nb_names_new[j] = \
                    increase_index(nb_new_regs[j-1].group(1)) \
                    + nb_names[j][nb_regj.end(1):]
        else:
            if nb_regj.group(1) == nb_regs[j-1].group(1):
                nb_names_new[j] = nb_new_regs[j-1].group(1) \
                    + nb_names[j][nb_regj.end(1):]
            elif (nb_regj.group(1)[0] == nb_regs[j-1].group(1)[0]
                  and nb_regj.group(1)
                  > increase_index(nb_new_regs[j-1].group(1))):
                nb_names_new[j] = \
                    increase_index(nb_new_regs[j-1].group(1)) \
                    + nb_names[j][nb_regj.end(1):]
        nb_new_regs[j] = REG.match(nb_names_new[j])

    nb_names_newest = nb_names_new.copy()

    nb_new_regs = [REG.match(nb_name_new) for nb_name_new in nb_names_new]
    nb_newest_reg = nb_new_regs.copy()

    for j, nb_new_regj in enumerate(nb_new_regs[1:], 1):
        if nb_new_regj.group(1) == nb_newest_reg[j-1].group(1):
            if (nb_new_regj.group(2).isdecimal()
                    or (not nb_newest_reg[j-1].group(2).isdecimal()
                        and nb_new_regj.group(2)[0]
                        == nb_newest_reg[j-1].group(2)[0])):
                if nb_new_regj.group(2) \
                        > increase_index(nb_newest_reg[j-1].group(2)):
                    nb_names_newest[j] \
                        = nb_names_new[j][:nb_new_regj.start(2)] \
                        + increase_index(nb_newest_reg[j-1].group(2)) \
                        + nb_names_new[j][nb_new_regj.end(2):]
                    nb_newest_reg[j] = REG.match(nb_names_newest[j])

    if nb_names_newest == nb_names:
        LOGGER.info('- no files need renaming, no reindexing needed')
    else:
        count = 0
        for f_cur, f_newest in zip(nb_names, nb_names_newest):
            count += 1
            if f_cur != f_newest:
                LOGGER.info('- replacing %s with %s',
                            f_cur, f_newest)
            os.rename(os.path.join(path_to_notes, f_cur),
                      os.path.join(path_to_notes, str(count) + '-' + f_newest))
        count = 0
        for f_newest in nb_names_newest:
            count += 1
            os.rename(os.path.join(path_to_notes, str(count) + '-' + f_newest),
                      os.path.join(path_to_notes, f_newest))


def reindex(path_to_notes: str = None,
            insert: bool = True,
            tighten: bool = False) -> None:
    """Reindex the collection of notebooks.

    Reindex the notebooks by inserting (via `insert_notebooks()`) and/or
    tightening (calling `tighten_notebooks()`) the collection of notebooks,
    depending on whether the corresponding arguments are `True` or `False`.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    insert : bool
        Whether to insert notebooks in the collection or not.

    tighten : bool
        Whether to tighten the indices of notebooks or not.
    """
    if insert:
        insert_notebooks(path_to_notes)

    if tighten:
        tighten_notebooks(path_to_notes)


def export_notebooks(path_to_notes: str = None,
                     export_path: str = None,
                     exporter_name: str = None,
                     exporter_args: dict = None) -> None:
    """
    Export notebooks via nbconvert.

    It reads all the indexed notebooks in `path_to_notes` and export them
    to the directory `export_path` using the exporter defined by
    `exporter_name`, with the arguments in `exporter_args`.

    The name of the exporter (`exporter_name`) must be one of the default
    exporters listed in `nbconvert.exporters.get_export_names()`.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    export_path : str
        The path to the directory where the exported, or converted,
        files should be saved in.

    exporter_name : str
        The name of the exporter to be used in `nbconvert` via
        `nbconvert.exporters.get_exporter(exporter_name)`. Possible
        choices are 'markdown', 'pdf', 'slides', 'latex', etc.

    exporter_args : dict
        Arguments, if any, to be passed on to the exporter via
        `nbconvert.exporters.get_exporter(exporter_name)(**exporter_args)`.
    """
    assert isinstance(export_path, str), \
        "Argument `export_path` should be a string"
    assert exporter_name in exporters.get_export_names(), \
        "The `exporter_name` argument with value {} is not in the \
list of available exporters listed in \
`nbconvert.exporters.get_export_names()`".format(exporter_name)

    if os.path.isdir(export_path):
        for file in os.listdir(export_path):
            os.remove(os.path.join(export_path, file))
    else:
        os.mkdir(export_path)

    if exporter_args:
        exporter = exporters.get_exporter(exporter_name)(**exporter_args)
    else:
        exporter = exporters.get_exporter(exporter_name)()
    extension = exporter.file_extension

    for nb_name in indexed_notebooks(path_to_notes):
        nb_file = os.path.join(path_to_notes, nb_name)
        nb = nbformat.read(nb_file, as_version=4)
        body = exporter.from_notebook_node(nb)[0]
        for cell in nb.cells:
            for marker in (NAVIGATOR_MARKER, TOC_MARKER):
                if cell.source.startswith(marker):
                    source_new = ''
                    i = 0
                    for m in REG_LINK.finditer(cell.source):
                        source_new += cell.source[i:m.start(6)] + extension
                        i = m.end(6)
                    source_new += cell.source[i:]
                    cell.source = source_new

        LOGGER.info("Adjusting links for %s", export_path)
        body = exporter.from_notebook_node(nb)[0]
        export_filename = \
            os.path.join(export_path,
                         nb_name[:REG.match(nb_name).start(5)]
                         + extension)
        if isinstance(body, str):
            export_file = open(export_filename, 'w+')
        else:
            export_file = open(export_filename, 'wb+')
        export_file.write(body)
        export_file.close()


def add_contents(path_to_notes: str = None,
                 toc_nb_name: str = None,
                 toc_title: str = '',
                 show_index_in_toc: bool = True) -> None:
    """Adds the table of contents to a selected notebook.

    It adds the table of contents, generated from the collection of
    notebooks in the directory `path_to_notes`, to the notebook
    `toc_nb_name`, with `toc_title` as the title of the Table
    of Contents. The inclusion, or not, of the Chapter and Section
    numbers in the table of contents is indicaded by the argument
    `show_index_in_toc`.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    toc_nb_name : str
        filename of the notebook in which the table of contents
        is to be inserted

    toc_title : str
        Text to be displayed as the title for the table of contents cell,
        e.g. 'Contents', 'Table of Contents', or in other languages,
        'Conteúdo', 'Table des Matières', and so on.

    show_index_in_toc : bool
        Whether to display the navigator with the chapter
        and section number of each notebook or just their title.
    """
    # error handling
    assert isinstance(path_to_notes, str), \
        "Argument `path_to_notes` should be a string"
    assert isinstance(toc_nb_name, str), \
        "Argument `toc_nb_name` should be a string"
    assert isinstance(toc_title, str), \
        "Argument `toc_title` should be a string"

    contents = get_contents(path_to_notes, toc_title, show_index_in_toc)

    toc_nb_file = os.path.join(path_to_notes, toc_nb_name)

    toc_nb = nbformat.read(toc_nb_file, as_version=4)

    toc_cell_found = False
    for cell in toc_nb.cells:
        if cell.source.startswith(TOC_MARKER):
            cell.source = contents
            cell.metadata = SLIDE_SHOW
            toc_cell_found = True

    if toc_cell_found:
        nbformat.write(toc_nb, toc_nb_file)
        LOGGER.info('- Table of contents updated in %s', toc_nb_name)
    else:
        LOGGER.info('* No markdown cell starting with %s found in %s',
                    TOC_MARKER, toc_nb_name)
        LOGGER.info("- inserting table of contents in %s",
                    toc_nb_name)
        if toc_nb.cells \
                and toc_nb.cells[-1].source.startswith(NAVIGATOR_MARKER):
            toc_nb.cells.insert(-1, new_markdown_cell(source=contents,
                                                      metadata=SLIDE_SHOW))
        else:
            toc_nb.cells.append(new_markdown_cell(source=contents,
                                                  metadata=SLIDE_SHOW))

    nbformat.write(toc_nb, toc_nb_file)


def add_headers(path_to_notes: str = None, header: str = None) -> None:
    """Adds header to each notebook in the collection.

    It adds the provided `header`as the first cell of each notebook
    in the collection of indexed notebooks in the folder `path_to_notes`.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    header : str
        The string with the contents to be included in the header cell.
    """
    cleanup_marker_cells(path_to_notes, HEADER_MARKER, 'remove')

    for nb_name in indexed_notebooks(path_to_notes):
        nb_file = os.path.join(path_to_notes, nb_name)
        nb = nbformat.read(nb_file, as_version=4)

        LOGGER.info('- inserting header for %s', nb_name)
        nb.cells.insert(0, new_markdown_cell(
            source=HEADER_MARKER + '\n' + header,
            metadata=SLIDE_SKIP))

        nbformat.write(nb, nb_file)


def get_badge_entries(path_to_notes: str = None,
                      badges: list = None) -> Iterable[tuple]:
    """Iterable with the bagdes info for each notebook.

    It reads the indexed notebooks in the folder `path_to_notes` and
    generates an iterable with the information needed to build the
    badges for each notebook.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    badges : list of dict
        A list of dictionaries with the necessary information
        to add badges. See the docstring of `add_badges()` for
        the explanation of required and optional key-value pairs
        in each dictionary.

    Yields
    ------
    : str
        Path to current notebook in the iterator.
    : list
        The list of badge links for the current notebook
        in the iterator.
    """

    for this_nb in indexed_notebooks(path_to_notes):

        this_nb_badge_links = list()

        if badges:
            for badge in badges:
                this_nb_badge_links.append(
                    BADGE_LINK.format(
                        badge_alt=badge['alt'],
                        badge_title=badge['title'],
                        badge_url=badge['url'],
                        badge_filename=this_nb if 'extension' not in badge
                        else this_nb[:REG.match(this_nb).start(5)]
                        + badge['extension'],
                        badge_src=badge['src'] if 'src' in badge
                        else BADGE_SHIELD_SRC.format(
                            badge_label=badge['label'],
                            badge_message=badge['message'],
                            badge_color=badge['color'])))

        yield os.path.join(path_to_notes, this_nb), \
            this_nb_badge_links


def add_badges(path_to_notes: str = None,
               badges: list = None) -> None:
    """Adds badges to each notebook in the collection.

    Adds a badge cell with one or more badges to each notebook in the
    collection of indexed notebooks in the folder `path_to_notes`.
    The information for creating each badge is in the list `badges`.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    badges: list of dict
        A list of dictionaries with the necessary information
        to add the badges.

        Each item in the list is a dictionary which should have
        the keys `alt` (str), `title` (str), `url` (str), an optional
        `extension` (str), and either `src` or the three keys
        `label` (str), `message` (str), and `color` (str).

        The key `url` is used for building link address, with the `href`
        argument being composed of the given `url` appended by the nam
        of the corresponding notebook.

        The keys `label`, `message`, and `color` are used to build
        the badge image via the `shields.io` constructor, which will then
        become the argument `src` of the badge image. Alternatively,
        one can provide a direct `src` link to the badge image.
        The keys `alt` and `title` complement the information of the image.

        The key `extension` is used in case there is a need to replace
        the `.ipynb` extension of each notebook to the appropriate
        extension, e.g `.md`, `.slides.html`, `.pdf`, `.py`, `.tex`,
        and so on. If `extension` is omitted, no replacement occurs.
    """
    cleanup_marker_cells(path_to_notes, BADGES_MARKER, 'remove')

    for nb_filename, this_nb_badge_links \
            in get_badge_entries(path_to_notes, badges):
        nb = nbformat.read(nb_filename, as_version=4)
        nb_name = os.path.basename(nb_filename)

        badges_top = BADGES_MARKER + "\n"

        for badge_link in this_nb_badge_links:
            badges_top += badge_link + "&nbsp;"

        if not nb.cells or not nb.cells[0].source.startswith(HEADER_MARKER):
            LOGGER.info("- inserting badges for %s", nb_name)
            nb.cells.insert(0, new_markdown_cell(source=badges_top,
                                                 metadata=SLIDE_SKIP))
        else:
            LOGGER.info("- inserting badges for %s", nb_name)
            nb.cells.insert(1, new_markdown_cell(source=badges_top,
                                                 metadata=SLIDE_SKIP))

        nbformat.write(nb, nb_filename)


def prev_this_next(collection: list = None) -> None:
    """Iterable with previous, current, and next notebooks in `collection`.

    It reads a list of indexed notebooks and gives an iterable with the
    previous, current, and next notebooks for each notebook in the list.

    Parameters
    ----------
    collection : list of str
        The collection of indexed notebooks.

    Yields
    ------
    : str
        A string with the filename of the previous notebook in the iteration.
    : str
        A string with the filename of the current notebook in the iteration.
    : str
        A string with the filename of the next notebook in the iteration.
    """
    a, b, c = itertools.tee(collection, 3)
    next(c)
    return zip(itertools.chain([None], a), b, itertools.chain(c, [None]))


def get_navigator_entries(path_to_notes: str = None,
                          core_navigators: list = None,
                          show_nb_title_in_nav: bool = True,
                          show_index_in_nav: bool = True) -> Iterable[str]:
    """Iterable with the navigator info for each notebook.

    It reads the indexed notebooks in the folder `path_to_notes` and
    generates an iterable with the information needed to build the
    navigators for each notebook.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    core_navigators : list of str
        A lists of strings with the filenames of each notebook to be
        included in the navigators, in between the links to the
        "previous" and the "next" notebooks.

    show_nb_title_in_nav : bool
        Whether to diplay the title of the notebook in the previous
        and next links or just display the words 'Previous' and 'Next'.

    show_index_in_nav : bool
        Whether to display the navigator with the chapter
        and section numbers of each notebook or just their title.

    Yields
    ------
    : str
        Path to current notebook in the iterator.
    : str
        Contents of the navigation bar for the current notebook in the
        iterator.
    """
    for prev_nb, this_nb, next_nb \
            in prev_this_next(indexed_notebooks(path_to_notes)):
        navbar = ""
        if prev_nb:
            if show_nb_title_in_nav:
                entry = get_nb_entry(path_to_notes, prev_nb,
                                     show_index_in_nav)
                navbar += PREV_TEMPLATE.format(title=entry, url=prev_nb)
            else:
                navbar += PREV_TEMPLATE.format(title='Previous', url=prev_nb)

        for center_nb in core_navigators:
            entry = get_nb_entry(path_to_notes, center_nb,
                                 show_index_in_nav)
            navbar += CENTER_TEMPLATE.format(title=entry, url=center_nb)

        if next_nb:
            if show_nb_title_in_nav:
                entry = get_nb_entry(path_to_notes, next_nb,
                                     show_index_in_nav)
                navbar += NEXT_TEMPLATE.format(title=entry, url=next_nb)
            else:
                navbar += NEXT_TEMPLATE.format(title='Next', url=next_nb)

        yield os.path.join(path_to_notes, this_nb), navbar


def add_navigators(path_to_notes: str = None,
                   core_navigators: list = None,
                   show_nb_title_in_nav: bool = True,
                   show_index_in_nav: bool = True) -> None:
    """Adds navigators to each notebook in the collection.

    Adds top and bottom navigators to each notebook in the collection
    of indexed notebooks in the folder `path_to_notes`.

    Parameters
    ----------
    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    core_navigators : list of str
        A lists of strings with the filenames of each notebook to be
        included in the navigators, in between the links to the
        "previous" and the "next" notebooks.

    show_nb_title_in_nav : bool
        Whether to diplay the title of the notebook in the previous
        and next links or just display the words 'Previous' and 'Next'.

    show_index_in_nav : bool
        Whether to display the navigator with the chapter
        and section number of each notebook or just their title.
    """
    cleanup_marker_cells(path_to_notes, NAVIGATOR_MARKER, 'remove')

    for nb_file, navbar \
        in get_navigator_entries(path_to_notes,
                                 core_navigators,
                                 show_nb_title_in_nav,
                                 show_index_in_nav):
        nb = nbformat.read(nb_file, as_version=4)
        nb_name = os.path.basename(nb_file)

        navbar_top = NAVIGATOR_MARKER + "\n" + navbar + "\n\n---\n"
        navbar_bottom = NAVIGATOR_MARKER + "\n\n---\n" + navbar

        if not nb.cells or not \
                (nb.cells[0].source.startswith(HEADER_MARKER)
                 or nb.cells[0].source.startswith(BADGES_MARKER)):
            LOGGER.info("- inserting navbar for %s", nb_name)
            nb.cells.insert(0, new_markdown_cell(source=navbar_top,
                                                 metadata=SLIDE_SKIP))
        elif len(nb.cells) == 1 or not \
                (nb.cells[1].source.startswith(HEADER_MARKER)
                 or nb.cells[1].source.startswith(BADGES_MARKER)):
            LOGGER.info("- inserting navbar for %s", nb_name)
            nb.cells.insert(1, new_markdown_cell(source=navbar_top,
                                                 metadata=SLIDE_SKIP))
        else:
            LOGGER.info("- inserting navbar for %s", nb_name)
            nb.cells.insert(2, new_markdown_cell(source=navbar_top,
                                                 metadata=SLIDE_SKIP))

        if (len(nb.cells) == 2
                and not nb.cells[1].source.startswith(NAVIGATOR_MARKER)) \
                or (len(nb.cells) > 2
                    and not nb.cells[-1].source.startswith(NAVIGATOR_MARKER)):
            nb.cells.append(new_markdown_cell(source=navbar_bottom,
                                              metadata=SLIDE_SHOW))

        nbformat.write(nb, nb_file)


def bind(aux: str = None,
         path_to_notes: str = None,
         reindexing: list = None,
         contents: list = None,
         header: str = '',
         navigators: list = None,
         badges: list = None,
         exports: list = None,
         config_filename: str = None) -> None:
    """Binds the collection of notebooks.

    It binds the collection of notebooks from either a configuration
    file `config_filename` or from the given arguments.

    Parameters
    ----------

    aux : str
        It allows for the first argument to be a non keyword argument
        which can be either the `config_filename` (if it ends in `.yaml`
        or `.yml`) or the `path_to_notes` (otherwise). These can also
        be given with the corresponding keyword arguments mentioned below.

    path_to_notes : str
        The path to the directory that contains the notebooks, either
        absolute or relative to the script that calls `nbbinder.bind()`.

    reindexing: list of bool
        A list with the arguments `insert` and `tighten` for the function
        `reindex()`.

    contents: list
        A list with the arguments `toc_nb_name`, `toc_title`, and
        `show_index_in_toc` for the function `add_contents()`.

    header : str
        The string to be included as the contents of the header cell.

    navigators: list
        A list with the arguments `core_navigators`, `show_nb_title_in_nav`,
        and `show_index_in_nav` for the function `add_navigators()`

    config_filename : str
        The filename of the configuration file.
    """

    if aux:
        if not config_filename and aux.endswith(('.yml', '.yaml')):
            config_filename = aux
        elif not path_to_notes:
            path_to_notes = aux
        else:
            raise Exception('No path to notebooks nor config file given.')

    if config_filename:
        with open(config_filename, 'r') as config_file:
            config = yaml.load(config_file, Loader=yaml.FullLoader)
        config_version = config.pop('version', None)
        if version.parse(config_version) < \
                version.parse(__config_version__):
            LOGGER.warning(
                "Version '%s' of config file '%s' lower than minimal \
version '%s' for fully compatible configuration.",
                version.parse(config_version),
                config_filename,
                version.parse(__config_version__))
        bind(**config)
    else:
        if reindexing:
            reindex(path_to_notes, **reindexing)

        if contents:
            add_contents(path_to_notes=path_to_notes, **contents)
        else:
            cleanup_marker_cells(path_to_notes, TOC_MARKER, 'remove')

        if header:
            add_headers(path_to_notes=path_to_notes, header=header)
        else:
            cleanup_marker_cells(path_to_notes, HEADER_MARKER, 'remove')

        if badges:
            add_badges(path_to_notes=path_to_notes, badges=badges)
        else:
            cleanup_marker_cells(path_to_notes, BADGES_MARKER, 'remove')

        if navigators:
            add_navigators(path_to_notes=path_to_notes, **navigators)
        else:
            cleanup_marker_cells(path_to_notes, NAVIGATOR_MARKER, 'remove')

        if exports:
            for export in exports:
                export_notebooks(path_to_notes=path_to_notes, **export)


if __name__ == '__main__':
    if len(sys.argv) == 1 or set(sys.argv).intersection({'--help', '-h'}):
        LOGGER.warning("\n Run the script with a configuration file \
as argument, e.g.")
        LOGGER.warning("\n   ./nbbinder.py config.yml")
        LOGGER.warning("\nFor the documentation, type 'pydoc3 nbbinder.py'.\n")
    else:
        try:
            bind(sys.argv[1])
        except NotImplementedError:
            LOGGER.info('provided argument is not a yaml file or not \
a properly formated yaml configuration file.')
