import uuid

from django.db import models


class User(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=64, blank=True, db_index=True)
    last_name = models.CharField(max_length=256, blank=True, db_index=True)
    address = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
