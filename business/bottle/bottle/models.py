from django.db import models
from business.cellar.models import Cellar
from business.bottle.bottle_collection.models import BottleCollection

class Bottle(models.Model):
    bottle_collection = models.ForeignKey(BottleCollection, related_name="bottle_collection", on_delete=models.DO_NOTHING, null=True)
    stock = models.IntegerField(null=False, default=0)
    cellar = models.ForeignKey(
        Cellar, related_name="bottles", on_delete=models.DO_NOTHING, null=True
    )