# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
#sys.path.insert(0, os.path.abspath('../lib_xud/doc/rst'))




from sphinx.builders.html import StandaloneHTMLBuilder

# -- Project information -----------------------------------------------------

# TODO
# WHAT TO DO ABOUT COPYRIGHTS - this is for all the docs! not the cof.py file itself!
#
copyright = '2021, XMOS Ltd'
author = 'XMOS Ltd'

# ----------------------------------------------
# reads the version and the title form the module_build_info file
# note that I added "TITLE = " to the module build info file to support this.
#
import re
def read_mbi(mbi_file, key_str, val_str):
    mbi = open(mbi_file, 'r')
    Lines = mbi.readlines()
    result_re = re.compile(val_str)
    search_re = re.compile('^\s*' + key_str + '\s*=\s*' + val_str)

    for line in Lines:
        m = re.findall(search_re, line)
        try:
            p = m[0].split('=')[1].lstrip()
            n = re.findall(result_re, p)[0]
            break
        except:
            n = 'no match'
    return n

project = 'XMOS Docs'
release = 'NOT FOUND'

project = read_mbi('../lib_xud/module_build_info', 'TITLE', '.*')
release = read_mbi('../lib_xud/module_build_info', 'VERSION', '[0-9]*\.[0-9]*\.[0-9]*')



# TODO
# think about how to move the script and path to the mbi file outside the conf.py, so we can use a standtrad conf.py everywhere.




StandaloneHTMLBuilder.supported_image_types = [
    "image/svg+xml",
    "image/gif",
    "image/png",
    "image/jpeg",
]

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "breathe",
    'sphinx.ext.autosectionlabel',
    'sphinx-multiversion'
]


# Breathe Configuration
breathe_projects = {"TMP": "./_build/_doxygen/xml/"}
breathe_default_project = "TMP"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/README.rst', '**/CHANGELOG.rst', '**/LICENSE.rst', '**/CONTRIBUTIONS.rst', 'COPYRIGHTS.rst']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "./rst/images/xmos_logo.png"
html_theme_options = {
    "sidebar_hide_name" : False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# -- Options for sphinx_copybutton -------------------------------------------

copybutton_prompt_text = r"\$ |\(gdb\) "
copybutton_prompt_is_regexp = True

#My setup for figures
numfig = True
numfig_secnum_depth = 1


autosectionlabel_prefix_document = True

html_sidebars = {
    '**': [
        'versioning.html',
    ],
}