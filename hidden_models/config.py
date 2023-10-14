from django.conf import settings

VISIBLE_FIELD_NAME = getattr(settings, 'VISIBLE_FIELD_NAME', 'visible')
