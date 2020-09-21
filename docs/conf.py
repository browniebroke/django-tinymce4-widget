import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_tinymce.settings")

import tinymce  # noqa E402 isort:skip

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

autodoc_member_order = "bysource"
autodoc_default_flags = ["members", "show-inheritance"]

templates_path = ["_templates"]

source_suffix = ".rst"

master_doc = "index"

# General information about the project.
project = "django-tinymce4-lite"
copyright = "2016, Roman Miroshnychenko"
author = "Roman Miroshnychenko"

version = tinymce.__version__
release = tinymce.__version__

language = None
exclude_patterns = ["_build"]

pygments_style = "sphinx"

todo_include_todos = False

html_theme = "alabaster"

html_theme_options = {
    "github_button": True,
    "github_type": "star&v=2",
    "github_user": "romanvm",
    "github_repo": "django-tinymce4-lite",
    "github_banner": True,
    "travis_button": True,
    "codecov_button": True,
    "description": "TinyMCE 4 editor for Django",
}

html_sidebars = {"**": ["about.html", "navigation.html", "searchbox.html",]}

html_static_path = ["_static"]

htmlhelp_basename = "django-tinymce4-litedoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

latex_documents = [
    (
        master_doc,
        "django-tinymce4-lite.tex",
        "django-tinymce4-lite Documentation",
        "Roman Miroshnychenko",
        "manual",
    ),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "django-tinymce4-lite",
        "django-tinymce4-lite Documentation",
        [author],
        1,
    )
]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (
        master_doc,
        "django-tinymce4-lite",
        "django-tinymce4-lite Documentation",
        author,
        "django-tinymce4-lite",
        "One line description of project.",
        "Miscellaneous",
    ),
]

intersphinx_mapping = {
    "https://docs.python.org/3.5": None,
    "https://docs.djangoproject.com/en/stable/": "https://docs.djangoproject.com/en/stable/_objects/",
}

suppress_warnings = ["image.nonlocal_uri"]
