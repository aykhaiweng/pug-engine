from django.db import models

from .mixins import (
    UUIDFieldMixin,
    TimestampMixin
)


class BaseModel(
    UUIDFieldMixin,
    TimestampMixin,
    models.Model
):

    class Meta:
        abstract = True
