# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from os import path
import sys

sys.path.insert(0, path.abspath('..'))


# Read the __version__ variable from rclone_manager/__version__.py
PATH = path.abspath(path.dirname(__file__))
about = {}
with open(path.join(PATH, '..', 'rclone_manager', '__version__.py'), encoding='utf-8') as f:
    exec(f.read(), about)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RClone Manager'
copyright = about['__copyright__']
author = about['__author__']
release = about['__version__']

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx_mdinclude']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
