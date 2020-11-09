# django-tinymce4-widget

<p align="center">
  <a href="https://github.com/browniebroke/django-tinymce4-widget/actions?query=workflow%3ACI">
    <img alt="CI Status" src="https://img.shields.io/github/workflow/status/browniebroke/django-tinymce4-widget/CI?label=CI&logo=github&style=flat-square">
  </a>
  <a href="https://django-tinymce4-widget.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/django-tinymce4-widget.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
  <a href="https://codecov.io/gh/browniebroke/django-tinymce4-widget">
    <img src="https://img.shields.io/codecov/c/github/browniebroke/django-tinymce4-widget.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
  <a href="https://github.com/ambv/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?amp;style=flat-square" alt="black">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/django-tinymce4-widget/">
    <img src="https://img.shields.io/pypi/v/django-tinymce4-widget.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPi Status">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/django-tinymce4-widget.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="pyversions">
  <img src="https://img.shields.io/pypi/l/django-tinymce4-widget.svg?style=flat-square" alt="license">
  <a href="https://github.com/browniebroke/django-tinymce4-widget">
    <img src="https://tokei.rs/b1/github/browniebroke/django-tinymce4-widget/" alt="LoC">
  </a>
</p>

**django-tinymce4-widget** is a reworked fork of [django-tinymce4-lite](https://github.com/romanvm/django-tinymce4-lite). It provides a minimal [TinyMCE 4](https://www.tinymce.com/) editor widget that can be used in Django forms.

This version **does not** include any static files, it's using the TinyMCE from the CDN by default.

**Warning**: TinyMCE 4 is incompatible with TinyMCE 3. Read [TinyMCE](https://www.tinymce.com/) docs for more information about how to configure TimyMCE 4 editor widget.

## Compatibility

-   **Python**: 3.6-3.8
-   **Django**: 2.2-3.1

## Quick Start

Install `django-tinymce4-widget`:

    $ pip install django-tinymce4-widget

Add `tinymce` to `INSTALLED_APPS` in `settings.py` for your Django project:

```python
INSTALLED_APPS = (
    ...
    'tinymce',
)
```

Add `tinymce.urls` to `urls.py` for your project:

```python
urlpatterns = [
    ...
    url(r'^tinymce/', include('tinymce.urls')),
    ...
]
```

In your code:

```python
from django.db import models
from tinymce import HTMLField

class MyModel(models.Model):
    ...
    content = HTMLField('Content')
```

In Django Admin the widget is used automatically for all models that have `HTMLField` fields. If you are using TinyMCE 4 in your website forms, add `form.media` variable into your templates:

```django
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
```

## Documentation

The full documentation is available at <http://django-tinymce4-widget.readthedocs.io>
