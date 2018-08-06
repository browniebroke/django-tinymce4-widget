django-tinymce4-widget
======================

.. image:: https://travis-ci.org/browniebroke/django-tinymce4-widget.svg?branch=master
    :target: https://travis-ci.org/browniebroke/django-tinymce4-widget
.. image:: https://codecov.io/gh/browniebroke/django-tinymce4-widget/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/browniebroke/django-tinymce4-widget
.. image:: https://readthedocs.org/projects/django-tinymce4-widget/badge/?version=latest
    :target: http://django-tinymce4-widget.readthedocs.io/en/latest/?badge=latest
.. image:: https://badge.fury.io/py/django-tinymce4-widget.svg
    :target: https://badge.fury.io/py/django-tinymce4-widget
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

**django-tinymce4-widget** is a reworked fork of `django-tinymce4-lite`_. It provides a minimal `TinyMCE 4`_
editor widget that can be used in Django forms.
The application can use `django-filebrowser`_ or `django-filebrowser-no-grappelli`_
as a file manager for TinyMCE 4 to insert images and file links into edited text.

This version **does not** include any static files, it's using the TinyMCE from the CDN by default.

**Warning**: TinyMCE 4 is incompatible with TinyMCE 3. Read `TinyMCE`_ docs for more information
about how to configure TimyMCE 4 editor widget.

.. _django-tinymce4-lite: https://github.com/romanvm/django-tinymce4-lite
.. _TinyMCE 4: https://www.tinymce.com/
.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _TinyMCE: https://www.tinymce.com/

Compatibility
-------------

- **Python**: 3.5-3.7
- **Django**: 1.11-2.1

Quick Start
===========

Install **django-tinymce4-widget**::

  $ pip install django-tinymce4-widget

Add ``tinymce`` to ``INSTALLED_APPS`` in ``settings.py`` for your Django project:

.. code-block:: python

  INSTALLED_APPS = (
      ...
      'tinymce',
  )

Add ``tinymce.urls`` to ``urls.py`` for your project:

.. code-block:: python

  urlpatterns = [
      ...
      url(r'^tinymce/', include('tinymce.urls')),
      ...
  ]

In your code:

.. code-block:: python

    from django.db import models
    from tinymce import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField('Content')

In Django Admin the widget is used automatically for all models that have ``HTMLField`` fields.
If you are using TinyMCE 4 in your website forms, add ``form.media`` variable into your templates:

.. code-block:: django

  <!DOCTYPE html>
  <html>
  <head>
    ...
    {{ form.media }}
  </head>
  <body>
  ...
  </body>
  </html>


Documentation
=============

The full documentation is available at http://django-tinymce4-widget.readthedocs.io/en/latest/
