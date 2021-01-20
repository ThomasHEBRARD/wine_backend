from django.db import models
from business.shared.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator


class Cepage(BaseModel):
    proportion = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(limit_value=0, message="Should be between 0 and 1"),
            MaxValueValidator(limit_value=1, message="Should be between 0 and 1"),
        ],
    )
