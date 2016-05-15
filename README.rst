=============================
django-shortcircuit
=============================

.. image:: https://badge.fury.io/py/django-shortcircuit.png
    :target: https://badge.fury.io/py/django-shortcircuit

.. image:: https://travis-ci.org/comandrei/django-shortcircuit.png?branch=master
    :target: https://travis-ci.org/comandrei/django-shortcircuit

.. image:: https://landscape.io/github/comandrei/django-shortcircuit/master/landscape.svg?style=flat
   :target: https://landscape.io/github/comandrei/django-shortcircuit/master
   :alt: Code Health

Shortcircuit Django middlewares for a list of views you want skipped

Documentation
-------------

The full documentation is at https://django-shortcircuit.readthedocs.org.

Quickstart
----------

Install django-shortcircuit::

    pip install django-shortcircuit

Then use it in a project::

    Include it in your middleware classes, BEFORE middlewares you potentially want skipped
    ::
       MIDDLEWARE_CLASSES = ( ... 'shortcircuit.middleware.ShortCircuitMiddleware', ... )

    Define a list of urlpatterns you want skipped

    ::
       SHORTCIRCUIT_URL_PATTERNS = (r'^/skip_me', r'^/also_me')



Features
--------

* This middleware allows skipping middlewares that aren't usefull for certain URL patterns.
  It's targeted to applications where there is heavy processing done in middleware and for various reasons (code ownership, lack of time) it's hard to do proper refactoring
  Bear in mind, this only skips process_view methods of middlewares used after ShortCircuitMiddleware

Running Tests
--------------

Does the code actually work?

::
   tox -e py27-django19


Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
