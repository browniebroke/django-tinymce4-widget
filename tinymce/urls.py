from django.urls import path

from .views import css, spell_check

urlpatterns = [
    path("spellchecker/", spell_check, name="tinymce-spellchecker"),
    path("css/", css, name="tinymce-css"),
]
