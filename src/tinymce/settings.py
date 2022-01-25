"""The django-tinymce4-lite configuration options"""

from django.conf import settings

TOOLBAR = [
    "bold italic underline",
    "alignleft aligncenter alignright alignjustify",
    "bullist numlist",
    "outdent indent",
    "table",
    "link image",
    "codesample",
    "preview code",
]

PLUGINS = ["link", "image", "preview", "codesample", "contextmenu", "table", "code"]

# Default TinyMCE 4 configuration
DEFAULT = {
    "selector": "textarea",
    "theme": "modern",
    "plugins": " ".join(PLUGINS),
    "toolbar1": " | ".join(TOOLBAR),
    "contextmenu": " | ".join(["formats", "link image"]),
    "menubar": False,
    "inline": False,
    "statusbar": True,
    "height": 360,
}
# Use tinymce4 built-in spellchecker service
USE_SPELLCHECKER = getattr(settings, "TINYMCE_SPELLCHECKER", False)
if USE_SPELLCHECKER:
    DEFAULT["plugins"] += " spellchecker"
    DEFAULT["toolbar1"] += " | spellchecker"

# TinyMCE 4 configuration
CONFIG = getattr(settings, "TINYMCE_DEFAULT_CONFIG", DEFAULT)

# TinyMCE 4 JavaScript code
JS_URL = getattr(settings, "TINYMCE_JS_URL", "//cdn.tinymce.com/4/tinymce.min.js")

# Additional JS files for TinyMCE (e.g. custom plugins)
ADDITIONAL_JS_URLS = getattr(settings, "TINYMCE_ADDITIONAL_JS_URLS", None)

# Additional CSS styles for TinyMCE 4
# The default CSS is used to fix TinyMCE 4 position in Django Admin.
CSS_URL = getattr(settings, "TINYMCE_CSS_URL", None)

# TinyMCE 4 callback JavaScript functions
CALLBACKS = getattr(settings, "TINYMCE_CALLBACKS", {})
