# Configuration

## Application Configuration

The following options can be defined for **tinymce4-widget** in your Django project's {file}`settings.py` file.

(TINYMCE_DEFAULT_CONFIG)=
`TINYMCE_DEFAULT_CONFIG` -- TinyMCE 4 widget configuration. **tinymce4-widget** provides a reasonable default configuration with essential editing capabilities, so you need to use this option only if you want to create your own custom TinyMCE configuration.

```{note}
In **tinymce4-widget** the TinyMCE configuration is defined as a Python {class}`dict`. The {class}`dict` configuration is then translated to JSON configuration according to {class}`json.JSONEncoder` rules.
```

Default configuration:

```python
DEFAULT = {
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': 'link image preview codesample contextmenu table code',
    'toolbar1': 'bold italic underline | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | table | link image | codesample | preview code',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'inline': False,
    'statusbar': True,
    'height': 360,
}
```

`TINYMCE_SPELLCHECKER` -- enables spellchecker function for TinyMCE. For the default configuration it also adds a spellcheck button to TinyMCE toolbar. Default: `False`.

```{note}
If you are using a custom TinyMCE configuration, don't forget to add [spellchecker](https://www.tinymce.com/docs/plugins/spellchecker/) plugin to your configuration, and add the necessary menu item/toolbar button. Also read [Language Configuration](#language-configuration) subsection about how to configure the spellchecker.
```

`TINYMCE_JS_URL` -- a path to TinyMCE JavaScript library. Default: `https://cdn.tiny.cloud/1/no-api-key/tinymce/4/tinymce.min.js`.
The following example shows how to load the TinyMCE library from another location:

    TINYMCE_JS_URL = 'https://cdn.tiny.cloud/1/no-api-key/tinymce/4/tinymce.min.js'

`TINYMCE_ADDITIONAL_JS_URLS` -- a {class}`list` of URLs for additional JavaScript files to be used with the TinyMCE widget, for example, custom TinyMCE plugins. Default: None.

`TINYMCE_CSS_URL` -- a path to a CSS file with additional styles for TinyMCE. Unlike content_style and content_css TinyMCE settings (see {ref}`Applying custom CSS<custom-css>`), this CSS is applied to the TinyMCE widget itself, for example to correct the widget position on a page. The default CSS here is rendered from a template and used to correct TinyMCE widget position in Django Admin interface.

`TINYMCE_CALLBACKS` -- allows to define custom TinyMCE callbacks, for example `file_browser_callback` or `spellchecker_callback`. This is a Python {class}`dict` where keys are the names of callbacks and values are JavaScript objects as Python strings. Default: `{}` (an empty {class}`dict`). Read [TinyMCE documentation](https://www.tinymce.com/docs/) to learn about available callbacks.

```{note}
Custom `file_browser_callback` and `spellchecker_callback` options defined in `TINYMCE_CALLBACKS` override **tinymce4-widget** built-in callbacks.
```

(language_config)=

## Language Configuration

By default **tinymce4-widget** uses [LANGUAGE_CODE](https://docs.djangoproject.com/en/stable/ref/settings/#language-code) and [LANGUAGES](https://docs.djangoproject.com/en/stable/ref/settings/#languages) Django options to automatically set up TinyMCE interface language and available spellchecker dictionaries. That is why it is recommended to define both options in your project's {file}`settings.py`.

`LANGUAGE_CODE` option defines TinyMCE interface language and writing directionality.

`LANGUAGES` option defines the list of available spellchecker languages. The first language in this list is used as the default one. The list of spellchecker languages also depends on available **pyenchant** dictionaries. For example, on Windows the default **pyenchant** installation includes only English, German and French spellchecker dictionaries. Read [pyenchant documentation](http://pythonhosted.org/pyenchant/tutorial.html#adding-language-dictionaries) to learn how to add additional spellchecker dictionaries.

You can view the list available spellchecker dictionaries by running `enchant.list_languages()` function in a console from your working Python environment. For example:

    >>> import enchant
    >>> enchant.list_languages()
    ['de_DE', 'en_AU', 'en_GB', 'en_US', 'fr_FR']

Additional spellchecker dictionaries can be downloaded from [this page](http://www.softmaker.com/en/download/dictionaries). Unpack a {file}`.sox` file using an archive manager, for example [7zip](http://www.7-zip.org/), and copy {file}`.dic` and {file}`.aff` for your language into **pyenchant**/**enchant** installation.

```{note}
Django language codes in `LANGUAGES` must match dictionary filenames. For example, `'en-us'` in `LANGUAGES` (with a country code) corresponds to {file}`en_US.dic`/{file}`en_US.aff` dictionary files, and `'uk'` (no country code) corresponds to {file}`uk.dic`/{file}`uk.aff` dictionary files.
```

Also you can completely override TinyMCE automatic language configuration by defining the necessary language options in {ref}`TINYMCE_DEFAULT_CONFIG <TINYMCE_DEFAULT_CONFIG>`.
