from business.bottle.bottle.models import Bottle
from business.cepage.models import Cepage
from business.appelation.models import Appelation

cepage = Cepage.objects.get()
appelation = Appelation.objects.get()
cellar = Cellar.objects.get()

Bottle.objects.create(
    name="Château Margaux",
    code="margaux",
    millesime=2017,
    cellar=cellar,
    appelation=appelation,
    degre_alcool=13.4,
    color="Red",
    viticulture="Ecological",
)