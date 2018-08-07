#!/usr/bin/env python
from setuptools import setup


def read(filename):
    with open(filename) as fp:
        return fp.read()


long_description = read('README.rst')

setup(
    name='django-tinymce4-widget',
    version='4.0.0',
    packages=['tinymce'],
    include_package_data=True,
    author='Bruno Alla',
    author_email='alla.brunoo@gmail.com',
    description='A Django application that provides a TinyMCE 4 editor widget '
                'for models and forms, without any static files.',
    long_description=long_description,
    license='MIT License',
    keywords='django wysiwyg widget tinymce',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Editors',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    platforms=['any'],
    url='https://github.com/browniebroke/django-tinymce4-widget',
    zip_safe=False
)
