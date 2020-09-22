# django-tinymce4-widget

[![image](https://github.com/browniebroke/django-tinymce4-widget/workflows/Test/badge.svg)](https://github.com/browniebroke/django-tinymce4-widget/actions?query=workflow%3ATest)
[![image](https://codecov.io/gh/browniebroke/django-tinymce4-widget/branch/master/graph/badge.svg)](https://codecov.io/gh/browniebroke/django-tinymce4-widget)
[![image](https://readthedocs.org/projects/django-tinymce4-widget/badge/?version=latest)](http://django-tinymce4-widget.readthedocs.io/en/latest/?badge=latest)
[![image](https://badge.fury.io/py/django-tinymce4-widget.svg)](https://badge.fury.io/py/django-tinymce4-widget)
[![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

**django-tinymce4-widget** is a reworked fork of
[django-tinymce4-lite](https://github.com/romanvm/django-tinymce4-lite).
It provides a minimal [TinyMCE 4](https://www.tinymce.com/) editor
widget that can be used in Django forms. The application can use
[django-filebrowser](https://github.com/sehmaschine/django-filebrowser)
or
[django-filebrowser-no-grappelli](https://github.com/smacker/django-filebrowser-no-grappelli)
as a file manager for TinyMCE 4 to insert images and file links into
edited text.

This version **does not** include any static files, it's using the
TinyMCE from the CDN by default.

**Warning**: TinyMCE 4 is incompatible with TinyMCE 3. Read
[TinyMCE](https://www.tinymce.com/) docs for more information about how
to configure TimyMCE 4 editor widget.

## Compatibility

-   **Python**: 3.5-3.8
-   **Django**: 1.11-2.2

## Quick Start

Install `django-tinymce4-widget`:

    $ pip install django-tinymce4-widget

Add `tinymce` to `INSTALLED_APPS` in `settings.py` for your Django
project:

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

In Django Admin the widget is used automatically for all models that
have `HTMLField` fields. If you are using TinyMCE 4 in your website
forms, add `form.media` variable into your templates:

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

The full documentation is available at
<http://django-tinymce4-widget.readthedocs.io>
