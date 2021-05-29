from django.db import models


class UUIDFieldMixin(models.Model):
    """
    Uses a UUID field as the models' primarykey field
    """
    uuid = models.UUIDField(primary_key=True, editable=False, db_index=True)

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    """
    Uses a UUID field as the models' primarykey field
    """
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
