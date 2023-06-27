# Welcome to django-tinymce4-widget documentation!

**django-tinymce4-widget** is a reworked fork of [django-tinymce4-lite](https://github.com/romanvm/django-tinymce4-lite). It provides a [TinyMCE 4](https://www.tinymce.com/) editor widget that can be used in Django forms and models.

The main difference with the original fork is that it **does not** include any static files, it's using the TinyMCE from the CDN by default.

## Compatibility

- **Python**: 3.8-3.11
- **Django**: 3.2-4.2

## License

[MIT license](https://en.wikipedia.org/wiki/MIT_License).

## Naming Conventions

In this documentation **django-tinymce4-widget** or **tinymce4-widget** (all lowercase) refers to this Python/Django application, and **TinyMCE 4** or **TinyMCE** (CamelCase) refers to a JavaScript [TinyMCE](https://www.tinymce.com/) editor widget. If a version number is omitted, TinyMCE v.4.x.x is assumed.

## Contents:

```{toctree}
:caption: Installation & Usage
:maxdepth: 2

installation
configuration
usage
advanced
test
```

```{toctree}
:caption: Project Info
:maxdepth: 2

contributing
changelog
```
