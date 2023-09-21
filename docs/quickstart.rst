=============
Documentation
=============

Creating models
---------------

To create your visible models, you have to make them inherit from an abstract model.

.. code-block:: python

    # imports
    from hidden_models.models import VisibleModel
    from django.db import models

    # your model
    class Article(VisibleModel):
        name = models.CharField(max_length=100)


Model managers
--------------

There are three managers to get results:

.. code-block:: python

    # get visible objects
    Article.objects.all()

    # get hidden objects
    Article.hidden_objects.all()

    # get all objects, it works as base manager
    Article.all_objects.all()


Methods
-------

Model managers use ``VisibleQuerySet`` that provides to hide or make available your objects.

.. code-block:: python

    # hide all objects, returns number of hidden objects
    Article.objects.all().hide()

    # all hidden objects will available
    Article.hidden_objects.all().show()

``show`` method also return number of available objects.