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
    rose_effervescent = "Effervescent Rosé"
    amber = "Amber"
    effervescent = "Effervescent"
    white_medium_dry = "White Medium-Dry"
    white_dry = "White Dry"
    mutated_wine = "Mutated Wine"
    green = "Green"



# {' Blanc demi-sec', ' Verte', ' Rosé', ' Rosé Effervescent',
#  ' Blanc sec', ' Vin Muté', ' Rouge Effervescent', ' Blanc Liquoreux', 
#  ' Blanc', ' ', ' Ambré', ' Divers', ' Blanc Demi Sec', ' Orange', ' Jaune', ' Rouge', ' Blanc Effervescent'}

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


class Bottle(BaseModel):
    color = models.CharField(
        max_length=64,
        choices=WineColor.choices,
        default=WineColor.red,
        null=False,
    )
    # domaine
    # apogee = 
    # website = models.CharField(max_length=255, null=True)
    # classement = 
    # {' Cru Bourgeois', ' 1er Cru Classé Supérieur', ' 2ème Grand Cru Classé', ' Cru d Alsace', 
    # ' Grand Cru', ' 5ème Grand Cru Classé', ' GG', ' Cru Bourgeois Exceptionnel', ' IGT', ' DOC', 
    # ' Grand Cru Classé', ' Vin de Pays', ' 1er Grand Cru Classé', ' 1er Grand Cru Classé A', ' Second Vin', 
    # ' Cuvée des Dames', ' Second vin', ' DOCG', ' 3ème Grand Cru Classé', ' 1er Cru', None, ' 1er Cru ', 
    # ' 1er Grand Cru Classé B (depuis 2012)', ' 1er Grand Cru Classé B', ' Cru classé', ' DOCa', ' IGP', 
    # ' 1er cru', ' Cru Classé de Graves', ' 4ème Grand Cru Classé', ' Cru Classé', ' DO'}
    # viticulture = models.CharField(
    #     max_length=64,
    #     choices=WineViticulture.choices,
    #     default=WineViticulture.not_specified,
    #     null=False,
    # )
    degre_alcool = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, 
        validators=[MinValueValidator(limit_value=0, message="Should be greater than 0")]
    )
    cellar = models.ForeignKey(
        Cellar, related_name="bottles", on_delete=models.DO_NOTHING, null=True
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(limit_value=0, message="Should be greater than 0")]
    )
    # millesime = models.IntegerField(max_digits=4, null=False, validators=[MinValueValidator(limit_value=0, message="Should be greater than 0")])
    appelation = models.ForeignKey(
        Appelation, related_name="bottles", on_delete=models.DO_NOTHING, blank=False, null=True
    )
    cepage = models.ManyToManyField(Cepage, related_name="bottles")
