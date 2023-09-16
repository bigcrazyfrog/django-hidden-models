====================
django-hidden-models
====================

.. image:: https://github.com/bigcrazyfrog/django-hidden-models/actions/workflows/tests.yaml/badge.svg
   :target: https://github.com/bigcrazyfrog/django-hidden-models/actions/
.. image:: https://coveralls.io/repos/bigcrazyfrog/django-hidden-models/badge.png
    :target: https://coveralls.io/r/bigcrazyfrog/django-hidden-models
.. image:: https://img.shields.io/pypi/pyversions/django-hidden-models.svg
   :target: https://pypi.python.org/pypi/django-hidden-models
.. image:: https://img.shields.io/pypi/frameworkversions/django/django-hidden-models.svg
   :target: https://pypi.python.org/pypi/django-hidden-models

Simply hiding a useless data from query results.

Example
-------

.. code-block:: python

    # imports
    from hidden_models.models import VisibleModel
    from django.db import models

    # Models
    class Article(VisibleModel):
        name = models.CharField(max_length=100)


    # Example of use

    >>> Article.objects.create(name='article1')
    >>> Article.objects.create(name='article2')
    
    >>> Article.objects.all() # Queryset [<Article: (1)>, <Article: (2)>]
    
    # This article will be hided, but not deleted from the database
    >>> Article.objects.filter(name='article1').hide()

    >>> Article.objects.all() # Queryset [<Article: (2)>]


Installation
------------

Installing from pypi (using pip). ::

    pip install django-hidden-models

Add ``hidden_models`` in your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        'hidden_models',
        [...]
    ]
