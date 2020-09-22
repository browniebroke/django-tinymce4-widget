from django.conf.urls import url

from .views import css, spell_check

urlpatterns = [
    url(r"^spellchecker/$", spell_check, name="tinymce-spellchecker"),
    url(r"^css/$", css, name="tinymce-css"),
]
