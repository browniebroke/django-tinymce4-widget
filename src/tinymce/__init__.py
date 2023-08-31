"""
TinyMCE Django widget.

This application provides a rich-text WYSIWYG `TinyMCE 4`_ widget
for Django forms and models.

.. _TinyMCE 4: https://www.tinymce.com/
"""

from .models import HTMLField
from .widgets import AdminTinyMCE, TinyMCE

__version__ = "7.0.0"
__all__ = ["HTMLField", "TinyMCE", "AdminTinyMCE"]
