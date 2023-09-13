from django.db import models

from hidden_models.managers import (
    VisibleAllManager,
    VisibleHiddenManager,
    VisibleManager
)


class VisibleModel(models.Model):
    """Abstract Visible model.

    .. note::
        To create your visible models, you have to make them inherit from this model.

    :attribute objects:
        The :class:`hidden_models.managers.VisibleManager` returns the visible models.

    :attribute all_objects:
        The :class:`hidden_models.managers.VisibleAllManager` returns all the models (visible and hidden).

    :attribute hidden_objects:
        The :class:`hidden_models.managers.VisibleHiddenManager` returns hidden models.
    """

    visible = models.BooleanField(default=True)

    objects = VisibleManager()
    all_objects = VisibleAllManager()
    hidden_objects = VisibleHiddenManager()

    class Meta:
        abstract = True
