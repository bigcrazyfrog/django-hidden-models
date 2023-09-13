from django.db.models import query


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
        return super().update(visible=False)

    def show(self) -> int:
        """Make objects in queryset visible."""
        return super().update(visible=True)
