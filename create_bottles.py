from business.bottle.bottle_collection.models import BottleCollection
from business.bottle.bottle.models import Bottle
from business.cepage.models import Cepage
from business.cellar.models import Cellar
from business.appellation.models import Appellation

# ./manage.py shell < create_bottles.py

Cepage.objects.all().delete()
cepage1, cepage2 = (
    Cepage.objects.create(name="Cabernet France", code="cabernet", proportion=0.5),
    Cepage.objects.create(name="Duras", code="duras", proportion=0.5),
)
Bottle.objects.all().delete()
BottleCollection.objects.all().delete()
Appellation.objects.all().delete()
appellation1, appellation2 = (
    Appellation.objects.create(name="AOC", code="aoc"),
    Appellation.objects.create(name="AOP", code="aop"),
)


def connector_db():
    connection = psycopg2.connect(
        host="localhost",
        database="postgres_ana",
        user="postgres_ana",
        password="1234",
        port=5432,
    )
    return connection


def postgresql_to_dataframe(connection, select_query, column_names):
    cursor = connection.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    tupples = cursor.fetchall()
    cursor.close()

    df = pd.DataFrame(tupples, columns=column_names)
    return df


cellar1, cellar2 = Cellar.objects.get(code="m@gmail.com"), Cellar.objects.get(
    code="m2@gmail.com"
)

bottles1 = [
    {
        "name": "Château Margaux",
        "code": "margaux_2017",
        "millesime": 2017,
        "appellation": appellation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Margaux",
        "code": "margaux_2016",
        "millesime": 2016,
        "appellation": appellation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Margaux",
        "code": "margaux_2015",
        "millesime": 2015,
        "appellation": appellation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Crozes-Hermitage",
        "code": "crozes_hermitage",
        "millesime": 2016,
        "appellation": appellation2,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Balaran",
        "code": "balaran",
        "millesime": 2017,
        "appellation": appellation1,
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
        "appellation": appellation2,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Cambon la pelouse",
        "code": "la_pelouse",
        "millesime": 2018,
        "appellation": appellation1,
        "degre_alcool": 11.4,
        "color": "White",
        "viticulture": "Biodynamique",
    },
    {
        "name": "Château Coutet",
        "code": "coutet_2017",
        "millesime": 2017,
        "appellation": appellation1,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    },
    {
        "name": "Château Syrah",
        "code": "syrah",
        "millesime": 2016,
        "appellation": appellation2,
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

for i in range(1, 10000):
    j = {
        "name": f"Château{i} Syrah{i}",
        "code": f"syrah{i}",
        "millesime": 2016,
        "appellation": appellation2,
        "degre_alcool": 13.4,
        "color": "Red",
        "viticulture": "Ecological",
    }
    BottleCollection.objects.create(**j)
