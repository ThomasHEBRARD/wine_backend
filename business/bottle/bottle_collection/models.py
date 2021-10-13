from django.db import models
from django.core.validators import MinValueValidator

from business.shared.models import BaseModel, TimeStampedModel
from business.appellation.models import Appellation


class WineColor(models.TextChoices):
    red = "Red"
    white = "White"
    rose = "Rosé"
    rose_effervescent = "Effervescent Rosé"
    amber = "Amber"
    effervescent = "Effervescent"
    white_medium_dry = "White Medium-Dry"
    white_dry = "White Dry"
    mutated_wine = "Mutated Wine"
    green = "Green"


class WineViticulture(models.TextChoices):
    not_specified = "Not specified"
    natural = "Natural"
    bio = "Organic"
    bio_nature = "Organic and natural"
    biodynamism = "Biodynamic"
    biodynamism_natural = "Biodynamic and natural"
    sustainable = "Sustainable"
    conventional = "Conventional"
    ecological = "Ecological"
    triple_a = "Triple A"
    triple_a_biodynamic = "Triple A and biodynamic"
    triple_a_bio = "Triple A and organic"


class BottleCollection(BaseModel, TimeStampedModel):
    id = models.BigIntegerField(primary_key=True)  # uuid
    color = models.CharField(
        max_length=64,
        choices=WineColor.choices,
        default=WineColor.red,
        null=False,
    )
    bottle_size = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=255, null=True)
    ranking = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    soil = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    garde = models.CharField(max_length=255, null=True)
    apogee = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)
    winery = models.CharField(max_length=255, null=True)
    viticulture = models.CharField(
        max_length=64,
        choices=WineViticulture.choices,
        default=WineViticulture.not_specified,
        null=True,
    )
    alcool = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(limit_value=0, message="Should be greater than 0")
        ],
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(limit_value=0, message="Should be greater than 0")
        ],
    )
    vintage = models.IntegerField(
        null=False,
        validators=[
            MinValueValidator(limit_value=0, message="Should be greater than 0")
        ],
        default=0000,
    )
    appellation = models.OneToOneField(
        Appellation,
        related_name="bottles",
        on_delete=models.DO_NOTHING,
        blank=False,
        null=True,
    )
