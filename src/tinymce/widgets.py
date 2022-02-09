"""
TinyMCE 4 forms widget

This TinyMCE widget was copied and extended from this code by John D'Agostino:
http://code.djangoproject.com/wiki/CustomWidgetsTinyMCE
"""
import json
import logging

from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from django.forms import Media, Textarea
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import smart_str
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.translation import get_language, get_language_bidi

from . import settings as mce_settings

logger = logging.getLogger(__name__)


def get_language_config():
    """
    Creates a language configuration for TinyMCE4 based on Django project settings

    :return: language- and locale-related parameters for TinyMCE 4
    :rtype: dict
    """
    config = {"language": get_language()[:2]}
    if get_language_bidi():
        config["directionality"] = "rtl"
    else:
        config["directionality"] = "ltr"
    if mce_settings.USE_SPELLCHECKER:
        from enchant import list_languages

        enchant_languages = list_languages()
        logger.debug(f"Enchant languages: {enchant_languages}")
        lang_names = []
        for lang, name in settings.LANGUAGES:
            lang = convert_language_code(lang)
            if lang not in enchant_languages:
                lang = lang[:2]
            if lang not in enchant_languages:
                logger.error(f"Missing {lang} spellchecker dictionary!")
                continue
            if config.get("spellchecker_language") is None:
                config["spellchecker_language"] = lang
            lang_names.append(f"{name}={lang}")
        config["spellchecker_languages"] = ",".join(lang_names)
    return config


def convert_language_code(django_lang):
    """
    Converts Django language codes "ll-cc" into ISO codes "ll_CC" or "ll"

    :param django_lang: Django language code as ll-cc
    :type django_lang: str
    :return: ISO language code as ll_CC
    :rtype: str
    """
    lang_and_country = django_lang.split("-")
    try:
        return "_".join((lang_and_country[0], lang_and_country[1].upper()))
    except IndexError:
        return lang_and_country[0]


def render_tinymce_init_js(mce_config, callbacks, id_=""):
    """
    Renders TinyMCE.init() JavaScript code

    :param mce_config: TinyMCE 4 configuration
    :type mce_config: dict
    :param callbacks: TinyMCE callbacks
    :type callbacks: dict
    :param id_: HTML element's ID to which TinyMCE is attached.
    :type id_: str
    :return: TinyMCE.init() code
    :rtype: str
    """
    if mce_settings.USE_SPELLCHECKER and "spellchecker_callback" not in callbacks:
        callbacks["spellchecker_callback"] = render_to_string("tinymce/spellchecker.js")
    if id_:
        mce_config["selector"] = mce_config.get("selector", "textarea") + "#{}".format(
            id_
        )
    mce_json = json.dumps(mce_config, indent=2)
    return render_to_string(
        "tinymce/tinymce_init.js",
        {"callbacks": callbacks, "tinymce_config": mce_json[1:-1]},
    )


class TinyMCE(Textarea):
    """
    TinyMCE 4 widget

    It replaces a textarea form widget with a rich-text WYSIWYG
    `TinyMCE 4`_ editor widget.

    :param attrs: General Django widget attributes.
    :type attrs: dict
    :param mce_attrs: Additional configuration parameters for TinyMCE 4.
        They *amend* the existing configuration.
    :type mce_attrs: dict
    :param profile: TinyMCE 4 configuration parameters.
        They *replace* the existing configuration.
    :type profile: dict

    .. _TinyMCE 4: https://www.tinymce.com/
    """

    def __init__(self, attrs=None, mce_attrs=None, profile=None):
        super().__init__(attrs)
        self.mce_attrs = mce_attrs or {}
        self.profile = get_language_config()
        default_profile = profile or mce_settings.CONFIG.copy()
        self.profile.update(default_profile)

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ""
        value = smart_str(value)
        final_attrs = self.build_attrs(attrs)
        final_attrs["name"] = name
        mce_config = self.profile.copy()
        mce_config.update(self.mce_attrs)
        if mce_config.get("inline", False):
            html = f"<div{flatatt(final_attrs)}>{escape(value)}</div>\n"
        else:
            html = "<textarea{}>{}</textarea>\n".format(
                flatatt(final_attrs), escape(value)
            )
        html += '<script type="text/javascript">{}</script>'.format(
            render_tinymce_init_js(
                mce_config, mce_settings.CALLBACKS.copy(), final_attrs["id"]
            )
        )
        return mark_safe(html)  # nosec

    @property
    def media(self):
        js = [mce_settings.JS_URL]
        if mce_settings.ADDITIONAL_JS_URLS:
            js += mce_settings.ADDITIONAL_JS_URLS
        css = {"all": [reverse("tinymce-css")]}
        if mce_settings.CSS_URL:
            css["all"].append(mce_settings.CSS_URL)
        return Media(js=js, css=css)


class AdminTinyMCE(TinyMCE, admin_widgets.AdminTextareaWidget):
    """TinyMCE 4 widget for Django Admin interface"""

    pass


__all__ = ["TinyMCE", "render_tinymce_init_js"]
