Test Project
============

The **tinymce4-widget** sources include **test_tinymce** project that can be used to run automated tests
or to try a live TinyMCE 4 editor widget. The test project can also serve as a basic example of
**tinymce4-widget** usage.

To use the test project, first you need to install the necessary dependencies::

  $ pip install -r requirements.txt

Then you need to create the test database::

  $ python manage.py migrate

If you want to try TinyMCE in Django Admin, create a superuser to access the Admin interface::

  $ python manage.py createsuperuser

To run automated tests, enter in the console::

  $ python manage.py test test_tinymce

To open TinyMCE 4 editor, run the test server::

  $ python manage.py runserver

Then open the project's start page in your browser: http://127.0.0.1:8000.
The browser will open a webpage with a TinyMCE 4 editor.

.. note:: The commands described in this section need to be run from the **tinymce4-widget**
  sources root directory.

The test project is very basic and does nothing else, except for displaying the TinyMCE 4 editor.
