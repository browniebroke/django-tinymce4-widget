# Installation

Install **django-tinymce4-widget** from PyPI:

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

For TinyMCE spellchecker plugin you need to install [pyenchant](http://pythonhosted.org/pyenchant/) package:

    $ pip install pyenchant

On some Linux systems you may also need to install binary `enchant` libraries prior to installing `pyenchant`. For example, on Debian/Ubuntu use the following command:

    $ sudo apt-get install enchant

Also you need to add the necessary spelling dictionaries if they are missing from `pyenchant` default installation on your system.

Read {ref}`"Language Configuration"<language_config>` subsection about configuring the **tinymce4-widget** spellchecker.
