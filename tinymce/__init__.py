# License: MIT, see LICENSE.txt
"""
django-tinymce4-lite
--------------------

This application provides a rich-text WYSIWYG `TinyMCE 4`_ widget
for Django forms and models.

.. _TinyMCE 4: https://www.tinymce.com/
"""

from .models import HTMLField
from .widgets import AdminTinyMCE, TinyMCE

__version__ = "6.1.4"
__all__ = ["HTMLField", "TinyMCE", "AdminTinyMCE"]
