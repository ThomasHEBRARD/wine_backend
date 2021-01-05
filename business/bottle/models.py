from django.db import models
from business.shared.models import BaseModel
from django.core.validators import MinValueValidator

class Bottle(BaseModel):
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)]
    )
