# django-tinymce4-widget

<p align="center">
  <a href="https://github.com/browniebroke/django-tinymce4-widget/actions/workflows/ci.yml?query=branch%3Amain">
    <img alt="CI Status" src="https://img.shields.io/github/actions/workflow/status/browniebroke/django-tinymce4-widget/ci.yml?branch=main&label=CI&logo=github&style=flat-square">
  </a>
  <a href="https://django-tinymce4-widget.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/django-tinymce4-widget.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
  <a href="https://codecov.io/gh/browniebroke/django-tinymce4-widget">
    <img src="https://img.shields.io/codecov/c/github/browniebroke/django-tinymce4-widget.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage">
  </a>
  <a href="https://results.pre-commit.ci/latest/github/browniebroke/django-tinymce4-widget/main">
    <img src="https://results.pre-commit.ci/badge/github/browniebroke/django-tinymce4-widget/main.svg" alt="pre-commit.ci status">
  </a>
</p>
<p align="center">
  <a href="https://python-poetry.org/">
    <img src="https://img.shields.io/badge/packaging-poetry-299bd7?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAASCAYAAABrXO8xAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJJSURBVHgBfZLPa1NBEMe/s7tNXoxW1KJQKaUHkXhQvHgW6UHQQ09CBS/6V3hKc/AP8CqCrUcpmop3Cx48eDB4yEECjVQrlZb80CRN8t6OM/teagVxYZi38+Yz853dJbzoMV3MM8cJUcLMSUKIE8AzQ2PieZzFxEJOHMOgMQQ+dUgSAckNXhapU/NMhDSWLs1B24A8sO1xrN4NECkcAC9ASkiIJc6k5TRiUDPhnyMMdhKc+Zx19l6SgyeW76BEONY9exVQMzKExGKwwPsCzza7KGSSWRWEQhyEaDXp6ZHEr416ygbiKYOd7TEWvvcQIeusHYMJGhTwF9y7sGnSwaWyFAiyoxzqW0PM/RjghPxF2pWReAowTEXnDh0xgcLs8l2YQmOrj3N7ByiqEoH0cARs4u78WgAVkoEDIDoOi3AkcLOHU60RIg5wC4ZuTC7FaHKQm8Hq1fQuSOBvX/sodmNJSB5geaF5CPIkUeecdMxieoRO5jz9bheL6/tXjrwCyX/UYBUcjCaWHljx1xiX6z9xEjkYAzbGVnB8pvLmyXm9ep+W8CmsSHQQY77Zx1zboxAV0w7ybMhQmfqdmmw3nEp1I0Z+FGO6M8LZdoyZnuzzBdjISicKRnpxzI9fPb+0oYXsNdyi+d3h9bm9MWYHFtPeIZfLwzmFDKy1ai3p+PDls1Llz4yyFpferxjnyjJDSEy9CaCx5m2cJPerq6Xm34eTrZt3PqxYO1XOwDYZrFlH1fWnpU38Y9HRze3lj0vOujZcXKuuXm3jP+s3KbZVra7y2EAAAAAASUVORK5CYII=" alt="Poetry">
  </a>
  <a href="https://github.com/ambv/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square" alt="black">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/django-tinymce4-widget/">
    <img src="https://img.shields.io/pypi/v/django-tinymce4-widget.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPi Status">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/django-tinymce4-widget.svg?style=flat-square&logo=python&logoColor=fff" alt="pyversions">
  <img src="https://img.shields.io/pypi/l/django-tinymce4-widget.svg?style=flat-square" alt="license">
</p>

**django-tinymce4-widget** is a reworked fork of [django-tinymce4-lite](https://github.com/romanvm/django-tinymce4-lite). It provides a minimal [TinyMCE 4](https://www.tinymce.com/) editor widget that can be used in Django forms.

This version **does not** include any static files, it's using the TinyMCE from the CDN by default.

**Warning**: TinyMCE 4 is incompatible with TinyMCE 3. Read [TinyMCE](https://www.tinymce.com/) docs for more information about how to configure TimyMCE 4 editor widget.

## Compatibility

- **Python**: 3.8-3.11
- **Django**: 3.2-4.2

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
