from django.db import models
from business.shared.models import BaseModel
from django.core.validators import MinValueValidator
from user.user.models import User


class Cellar(BaseModel):
    # type de cellar?
    user = models.ForeignKey(User, related_name="cellar", on_delete=models.CASCADE, null=True)