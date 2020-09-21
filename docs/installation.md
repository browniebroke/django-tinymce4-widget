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

If you want to use [django-filebrowser](https://github.com/sehmaschine/django-filebrowser) or [django-filebrowser-no-grappelli](https://github.com/smacker/django-filebrowser-no-grappelli) file manager, install one of those packages. Refer to [django-filebrowser documentation](https://django-filebrowser.readthedocs.org/en/latest/) to learn how to install and configure the filebrowser application.

For TinyMCE spellchecker plugin you need to install [pyenchant](http://pythonhosted.org/pyenchant/) package:

    $ pip install pyenchant

On some Linux systems you may also need to install binary `enchant` libraries prior to installing `pyenchant`. For example, on Debian/Ubuntu use the following command:

    $ sudo apt-get install enchant

Also you need to add the necessary spelling dictionaries if they are missing from `pyenchant` default installation on your system.

Read {ref}`"Language Configuration"<language_config>` subsection about configuring the **tinymce4-widget** spellchecker.
