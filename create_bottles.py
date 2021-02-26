from business.bottle.bottle_collection.models import BottleCollection
from business.bottle.bottle.models import Bottle
from business.cepage.models import Cepage
from business.cellar.models import Cellar
from business.appelation.models import Appelation

# ./manage.py shell < create_bottles.py

Cepage.objects.all().delete()
cepage1, cepage2 = (
    Cepage.objects.create(name="Cabernet France", code="cabernet", proportion=0.5),
    Cepage.objects.create(name="Duras", code="duras", proportion=0.5),
)
Bottle.objects.all().delete()
BottleCollection.objects.all().delete()
Appelation.objects.all().delete()
appelation1, appelation2 = (
    Appelation.objects.create(name="AOC", code="aoc"),
    Appelation.objects.create(name="AOP", code="aop"),
)

cellar1, cellar2 = Cellar.objects.get(code="m@gmail.com"), Cellar.objects.get(
    code="m2@gmail.com"
)

bottles1 = [
    {
        "name": "Château Margaux",
        "code": "margaux_2017",
        "millesime": 2017,
        "appelation": appelation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Margaux",
        "code": "margaux_2016",
        "millesime": 2016,
        "appelation": appelation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Margaux",
        "code": "margaux_2015",
        "millesime": 2015,
        "appelation": appelation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Crozes-Hermitage",
        "code": "crozes_hermitage",
        "millesime": 2016,
        "appelation": appelation2,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Balaran",
        "code": "balaran",
        "millesime": 2017,
        "appelation": appelation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
]
bottles2 = [
    {
        "name": "Château Ratatouille",
        "code": "ratatouile",
        "millesime": 2017,
        "appelation": appelation2,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Cambon la pelouse",
        "code": "la_pelouse",
        "millesime": 2018,
        "appelation": appelation1,
        "degre_alcool": 11.4,
        "color": "White",
        "viticulture": "Biodynamique",
    },
    {
        "name": "Château Coutet",
        "code": "coutet_2017",
        "millesime": 2017,
        "appelation": appelation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Syrah",
        "code": "syrah",
        "millesime": 2016,
        "appelation": appelation2,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
]

for bottle in bottles1:
    b = BottleCollection.objects.create(**bottle)
    b.cepage.add(cepage1)
    b.save()
    Bottle.objects.create(bottle_collection=b, cellar=cellar1, stock=1)

for bottle in bottles2:
    b = BottleCollection.objects.create(**bottle)
    b.cepage.add(cepage2)
    b.save()
    Bottle.objects.create(bottle_collection=b, cellar=cellar2, stock=1)

for i in range (1, 10000):
    j = {
        "name": f"Château{i} Syrah{i}",
        "code": f"syrah{i}",
        "millesime": 2016,
        "appelation": appelation2,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    }
    BottleCollection.objects.create(**j)