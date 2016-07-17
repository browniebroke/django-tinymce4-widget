Welcome to django-tinymce4-widget documentation!
================================================

**django-tinymce4-widget** is a reworked fork of `django-tinymce4-lite`_. It provides a `TinyMCE 4`_
editor widget that can be used in Django forms and models.

This fork had 2 objectives as compared to `django-tinymce4-lite`_:

- **Do not** include any static files, it's using the TinyMCE from the CDN by default.
- Provide Django 1.7 support.

**django-tinymce4-widget** can use `django-filebrowser`_ or `django-filebrowser-no-grappelli`_
as a file manager for TinyMCE 4 to insert images and file links into edited text.
In addition to that, the application includes a spellchecker service for TinyMCE 4 spellchecker plugin.

Compatibility
-------------

- **Python**: 2.7, 3.4, 3.5
- **Django**: 1.7, 1.8, 1.9, 1.10

License
-------

`MIT license <https://en.wikipedia.org/wiki/MIT_License>`_.


Naming Conventions
------------------

In this documentation **django-tinymce4-widget** or **tinymce4-widget** (all lowercase) refers to this
Python/Django application, and **TinyMCE 4** or **TinyMCE** (CamelCase) refers to
a JavaScript `TinyMCE`_ editor widget. If a version number is omitted, TinyMCE v.4.x.x is assumed.

.. _django-tinymce4-lite: https://github.com/romanvm/django-tinymce4-lite
.. _TinyMCE 4: https://www.tinymce.com/
.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _TinyMCE: https://www.tinymce.com/

Contents:
---------

.. toctree::
  :maxdepth: 2

  installation
  configuration
  usage
  advanced
  test
  modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
