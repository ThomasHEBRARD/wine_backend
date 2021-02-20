from business.bottle.bottle.models import Bottle
from business.cepage.models import Cepage
from business.cellar.models import Cellar
from business.appelation.models import Appelation

# ./manage.py shell < create_bottles.py 

Cepage.objects.all().delete()
cepage1, cepage2 = Cepage.objects.create(name="Cabernet France", code="cabernet", proportion=0.5), Cepage.objects.create(name="Duras", code="duras", proportion=0.5)
Bottle.objects.all().delete()
Appelation.objects.all().delete()
appelation1, appelation2 = Appelation.objects.create(name="AOC", code="aoc"), Appelation.objects.create(name="AOP", code="aop")

cellar = Cellar.objects.get(code="M@gmail.com")

bottles = [
    {
        "name": "Château Margaux",
        "code": "margaux",
        "millesime": 2017,
        "cellar": cellar,
        "appelation": appelation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Crozes-Hermitage",
        "code": "crozes_hermitage",
        "millesime": 2016,
        "cellar": cellar,
        "appelation": appelation2,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Balaran",
        "code": "balaran",
        "millesime": 2017,
        "cellar": cellar,
        "appelation": appelation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Ratatouille",
        "code": "ratatouile",
        "millesime": 2017,
        "cellar": cellar,
        "appelation": appelation2,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Cambon la pelouse",
        "code": "la_pelouse",
        "millesime": 2018,
        "cellar": cellar,
        "appelation": appelation1,
        "degre_alcool": 11.4,
        "color": "White",
        "viticulture": "Biodynamique",
    },
    {
        "name": "Château Coutet",
        "code": "coutet_2017",
        "millesime": 2017,
        "cellar": cellar,
        "appelation": appelation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Syrah",
        "code": "syrah",
        "millesime": 2016,
        "cellar": cellar,
        "appelation": appelation2,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    }
]



for bottle in bottles:
    b = Bottle.objects.create(**bottle)
    b.cepage.add(cepage1) 
    b.save()