import json
import logging

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt

logging.basicConfig(format="[%(asctime)s] %(module)s: %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@csrf_exempt
def spell_check(request):
    """
    Implements the TinyMCE 4 spellchecker protocol

    :param request: Django http request with JSON-RPC payload from TinyMCE 4
        containing a language code and a text to check for errors.
    :type request: django.http.request.HttpRequest
    :return: Django http response containing JSON-RPC payload
        with spellcheck results for TinyMCE 4
    :rtype: django.http.HttpResponse
    """
    data = json.loads(request.body.decode("utf-8"))
    output = {"id": data["id"]}
    error = None
    try:
        import enchant
        from enchant.checker import SpellChecker

        if data["params"]["lang"] not in enchant.list_languages():
            error = "Missing {} dictionary!".format(data["params"]["lang"])
            raise RuntimeError(error)
        checker = SpellChecker(data["params"]["lang"])
        checker.set_text(strip_tags(data["params"]["text"]))
        output["result"] = {checker.word: checker.suggest() for err in checker}
    except ImportError:
        error = "The pyenchant package is not installed!"
        logger.exception(error)
    except RuntimeError:
        logger.exception(error)
    except Exception:
        error = "Unknown error!"
        logger.exception(error)
    if error is not None:
        output["error"] = error
    return JsonResponse(output)


def css(request):
    """
    Custom CSS for TinyMCE 4 widget

    By default it fixes widget's position in Django Admin

    :param request: Django http request
    :type request: django.http.request.HttpRequest
    :return: Django http response with CSS file for TinyMCE 4
    :rtype: django.http.HttpResponse
    """
    if "grappelli" in settings.INSTALLED_APPS:
        margin_left = 0
    else:
        margin_left = 170  # For Django >= 1.9 style admin
    return render(
        request,
        "tinymce/tinymce4.css",
        {"margin_left": margin_left},
        content_type="text/css",
    )


__all__ = ["spell_check", "css"]
