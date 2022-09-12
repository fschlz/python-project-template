# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.relpath("../../src"))

import dotenv
config = dotenv.dotenv_values(dotenv_path="/secrets/.env")

import importlib.metadata

# -- Project information -----------------------------------------------------

DISTRIBUTION_METADATA = importlib.metadata.metadata("{{ cookiecutter.package_name }}")

project = "{{ cookiecutter.project_name }}"
copyright = "{{ cookiecutter.license }}"
author = DISTRIBUTION_METADATA["authors"]

# The full version, including alpha/beta/rc tags
release = DISTRIBUTION_METADATA["version"]


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinxcontrib.confluencebuilder",
    "docxbuilder",
    "pydata_sphinx_theme",
    "recommonmark",
    "readthedocs_ext.readthedocs",
    "rinoh.frontend.sphinx",
    "rst2pdf.pdfbuilder",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]  # specific to some themes, breaks pydata themea

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
source_suffix = [".rst"]

# The master toctree document.
master_doc = "index"


autodoc_mock_imports = ["logging"]

# Additional settings for rhinotype PDF
rinoh_documents = [
    (
        "index",  # top-level file (index.rst)
        "{{ cookiecutter.project_folder_name }}",  # output (target.pdf)
        "{{ cookiecutter.project_name }}" + " Dokumentation",  # document title
        author
    )
]

pdf_documents = [
    (
        "index",  # top-level file (index.rst)
        "{{ cookiecutter.project_folder_name }}",  # -> output (target.pdf)
        "{{ cookiecutter.project_name }}" + " Dokumentation",  # document title
        author
    )
]

docx_documents = [
    (
        "index",
        "{{ cookiecutter.project_folder_name }}" + ".docx",
        {
            "title": "{{ cookiecutter.project_name }}" + " Dokumentation",
            "created": "Francisco Schulz",
            "subject": "Version: " + release
        },
        True
    ),
]

docx_update_fields = True
docx_pagebreak_before_section = 1
docx_pagebreak_before_table_of_contents = 1
docx_pagebreak_after_table_of_contents = 1


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"

# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# html_logo = "_static/logo.jpg"
