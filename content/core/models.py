import uuid 
from django.db import models

class Extension(models.Model):
    class Meta:
        abstract = True
        ordering = ['-created_at']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
