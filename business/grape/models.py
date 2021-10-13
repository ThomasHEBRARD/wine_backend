from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from business.shared.models import BaseModel
from business.bottle.bottle_collection.models import BottleCollection


class Grape(BaseModel):
    # other_names/variantes = ?
    pass


class GrapeBottleCollection(models.Model):
    bottle_collection = models.ForeignKey(
        BottleCollection,
        related_name="grape_bottle_collection",
        on_delete=models.DO_NOTHING,
        null=True,
    )
    grape = models.ForeignKey(
        Grape,
        related_name="grape_bottlecollection",
        on_delete=models.DO_NOTHING,
        null=True,
    )
    percentage = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(limit_value=0, message="Should be between 0 and 100"),
            MaxValueValidator(limit_value=100, message="Should be between 0 and 100"),
        ],
    )
