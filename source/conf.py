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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

html_favicon = "images/favicon.png"
project = 'Guide'
copyright = '2021, Telenia Software'
author = 'Telenia Software'




# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#    'sphinx_rtd_theme'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_rtd_theme'
import sphinx_pdj_theme
html_theme = 'sphinx_pdj_theme'
html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/theme_overrides.css',
]

html_scaled_image_link = False

html_logo = 'images/LOGO.png'

master_doc = 'index'

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.
gettext_uuid = True

rst_epilog = """
.. |br| raw:: html

   <br />

.. |tvox| replace:: TVox OmniChannel Contact Center
.. |client| replace:: TVox WebClient
.. |winweb| replace:: TVox WinWeb Client
.. |app| replace:: TVox Team App
.. |dm| replace:: TVox Data Model
.. |tvox_pbx| replace:: TVox UC&C
.. |tvox_platform| replace:: Piattaforma TVox
.. |tvox_dr_master| replace:: TVox Master
.. |tvox_dr_client| replace:: TVox DR Client
.. |latest_tvox_release| replace:: 21.0.26
.. |latest_tconsole_release| replace:: 5.7.28
.. |tconsole_default_installdir| replace:: *C:\\\\Telenia\\\\TConsole\\\\*
.. |tconsoleserver_default_installdir| replace:: *C:\\\\Program Files (X86)\\\\Telenia\\\\TConsoleServerStd\\\\*
"""
