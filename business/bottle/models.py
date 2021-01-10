from django.db import models
from business.shared.models import BaseModel
from django.core.validators import MinValueValidator
from business.cellar.models import Cellar
from business.cepage.models import Cepage
from business.appelation.models import Appelation

class WineColor(models.TextChoices):
    red = "Red"
    white = "White"
    rose = "Rosé"
    amber = "Amber"
    effervescent = "Effervescent"

class Bottle(BaseModel):
    color = models.CharField(
        max_length=64,
        choices=WineColor.choices,
        default=WineColor.red,
        null=False,
    )
    cellar = models.ForeignKey(Cellar, related_name="bottles", on_delete=models.DO_NOTHING, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)]
    )
    appelation = models.ForeignKey(Appelation, related_name="bottles", on_delete=models.DO_NOTHING, blank=False, null=True)
    cepage = models.ManyToManyField(Cepage, related_name="bottles")
