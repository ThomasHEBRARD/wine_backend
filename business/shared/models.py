from django.db import models

class BaseModel(models.Model):
    code = models.CharField(unique=True, max_length=255)
    name = models.CharField(unique=False, max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
