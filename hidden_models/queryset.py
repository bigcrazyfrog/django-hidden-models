from django.db.models import query

from hidden_models.config import VISIBLE_FIELD_NAME


class VisibleQueryset(query.QuerySet):
    """Default queryset for the VisibleManager.

    :attribute model:
        This attribute allows to add custom model class.
        Custom model classes should be inherited from ``VisibleModel`` or
        contain `visible` field.
    """

    def hide(self) -> int:
        """Hide all objects in queryset.

        Hidden objects are not displayed in query results.
        """
        return super().update(**{VISIBLE_FIELD_NAME: False})

    def show(self) -> int:
        """Make objects in queryset visible."""
        return super().update(**{VISIBLE_FIELD_NAME: True})
