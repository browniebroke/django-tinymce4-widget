from django.conf.urls import url

from .views import css, filebrowser, spell_check

urlpatterns = [
    url(r"^spellchecker/$", spell_check, name="tinymce-spellchecker"),
    url(r"^filebrowser/$", filebrowser, name="tinymce-filebrowser"),
    url(r"^css/$", css, name="tinymce-css"),
]
