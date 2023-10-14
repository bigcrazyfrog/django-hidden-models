from typing import Optional, Type

from django.db import models

from hidden_models.config import VISIBLE_FIELD_NAME
from hidden_models.queryset import VisibleQueryset


class VisibleManager(models.Manager):
    """Default manager for the VisibleModel.

    :attribute _queryset_class: define which class for queryset should be used
        This attribute allows to add custom queryset class. It is ``VisibleQueryset``
        by default. Custom queryset classes should be inherited from ``VisibleQueryset``.
    """

    _queryset_class = VisibleQueryset

    def __init__(self, queryset_class: Optional[Type[VisibleQueryset]] = None):
        """Hook for setting custom ``_queryset_class``.

        Example:

            class CustomQueryset(models.VisibleQueryset):
                ...

            class MyModel(models.Model):
                my_field = models.TextField()

                objects = VisibleManager(CustomQuerySet)
        """
        super(VisibleManager, self).__init__()
        if queryset_class:
            self._queryset_class = queryset_class

    def get_queryset(self) -> VisibleQueryset:
        """Return a new ``VisibleQueryset`` object that contains
        only visible models.
        """
        return super().get_queryset().filter(**{VISIBLE_FIELD_NAME: True})


class VisibleHiddenManager(VisibleManager):
    """Manager for VisibleModel provided to interact with hided models.

    VisibleManager with overwrite ``get_queryset`` method.

    .. note::
        This is used in :py:attr:`hidden_models.models.VisibleModel.hidden_objects`.
    """

    def get_queryset(self) -> VisibleQueryset:
        return super(VisibleManager, self).get_queryset().filter(**{VISIBLE_FIELD_NAME: False})


class VisibleAllManager(VisibleManager):
    """Manager for VisibleModel provided to interact with all models (visible and hidden).

    VisibleManager with overwrite ``get_queryset`` method.

    .. note::
        This is used in :py:attr:`hidden_models.models.VisibleModel.hidden_objects`.
    """

    def get_queryset(self) -> VisibleQueryset:
        return super(VisibleManager, self).get_queryset()
