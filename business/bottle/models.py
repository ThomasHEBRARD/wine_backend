from django.db import models
from business.shared.models import BaseModel
from django.core.validators import MinValueValidator
from business.cellar.models import Cellar
from business.cepage.models import Cepage
from business.appelation.models import Appelation


class Bottle(BaseModel):
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)]
    )
    #vin peut il avoir plusieurs appelations?
    appelation = models.ForeignKey(Appelation, related_name="bottles", on_delete=models.DO_NOTHING, blank=False, null=True)
    cepage = models.ManyToManyField(Cepage, related_name="bottles")
