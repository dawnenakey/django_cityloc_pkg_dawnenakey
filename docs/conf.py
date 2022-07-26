# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# - - Path set up --------------------------------------------

# If extentions (or modules to document with autodoc) are in another directory, 
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here. 
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

# - - Project information -------------------------------------------

project = 'django_cityloc_pkg'
copyright = '2022, Dawnena Key'
author = 'Author Name'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# - - Gengeral configuration --------------------------------

# Add any Sphinx extension module names here, as strings. 
# extensions coming with Sphinx (named 'sphinx.ext.*') or
# ones.
extensions = [
    'sphinx.ext.autodoc',
]