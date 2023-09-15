from django.db import models

from hidden_models.models import VisibleModel


class Article(VisibleModel):
    name = models.CharField(max_length=100)
