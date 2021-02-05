from django.db import models
from business.shared.models import BaseModel

class ActionType(models.TextChoices):
    addition = "Addition"
    deleteion = "Deletion"

# TODO : verify that an addition of 5 bottles adds 5 diffrents records
class BottleRecords(BaseModel):
    bottle = models.ForeignKey(Bottle, related_name="bottle_records", on_delete=models.DO_NOTHING, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    cellar = models.ForeignKey(Cellar, related_name="bottle_records", on_delete=models.DO_NOTHING, null=False)
    action = models.CharField(
        max_length=64,
        choices=ActionType.choices,
        default=ActionType.addition,
        null=False
        )
