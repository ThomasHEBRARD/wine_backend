from django.db import models


class BaseModel(models.Model):
    name = models.CharField(unique=False, max_length=255)
    code = models.CharField(unique=True, max_length=255)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
