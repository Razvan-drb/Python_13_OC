# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Orange County Lettings'
copyright = '2025, Razvan DARABAN'
author = 'Razvan DARABAN'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Configuration autoapi
autoapi_type = 'python'
autoapi_dirs = ['../oc_lettings_site', '../lettings', '../profiles']
autoapi_options = ['members', 'undoc-members', 'show-inheritance', 'show-module-summary']

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  # Pour supporter les docstrings Google style
    'autoapi.extension',    # Documentation automatique
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
