django-tinymce4-widget
======================

.. image:: https://travis-ci.org/browniebroke/django-tinymce4-widget.svg?branch=master
  :target: https://travis-ci.org/browniebroke/django-tinymce4-widget

**django-tinymce4-widget** is a reworked fork of `django-tinymce4-lite`_. It provides a minimal `TinyMCE 4`_
editor widget that can be used in Django forms.
The application can use `django-filebrowser`_ or `django-filebrowser-no-grappelli`_
as a file manager for TinyMCE 4 to insert images and file links into edited text.

This version **does not** include any static files, it's using the TinyMCE `from the CDN`_ by default. 
As compared to the original fork, this package provides Django 1.7 support.

**Warning**: TinyMCE 4 is incompatible with TinyMCE 3. Read `TinyMCE docs`_ for more information
about how to configure TimyMCE 4 editor widget.

Compatibility
-------------

- **Python**: 2.7, 3.4, 3.5
- **Django**: 1.7, 1.8, 1.9, 1.10

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

http://romanvm.github.io/django-tinymce4-lite

License
=======

MIT license. See LICENSE.txt

.. _django-tinymce4-lite: https://github.com/romanvm/django-tinymce4-lite
.. _TinyMCE 4: https://www.tinymce.com/
.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _TinyMCE docs: https://www.tinymce.com/docs/
.. _from the CDN: https://www.tinymce.com/download/
