from business.bottle.bottle_collection.models import BottleCollection
from business.bottle.bottle.models import Bottle
from business.grape.models import Grape
from business.cellar.models import Cellar
from business.appellation.models import Appellation

import unidecode

# ./manage.py shell < create_bottles.py


def postgresql_to_dataframe(select_query, column_names):
    import psycopg2
    import pandas as pd

    connection = psycopg2.connect(
        host="db_crawling",
        database="postgres",
        user="postgres",
        password="1234",
        port=5432,
    )
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


select_query = """
    SELECT * FROM public.crawled_bottles
    """

column_names = [
    "id",
    "website_id",
    "name",
    "vintage",
    "winery",
    "country",
    "region",
    "appellation",
    "soil",
    "color",
    "bottle_size",
    "grape",
    "viticulture",
    "apogee",
    "garde",
    "alcool",
    "price",
    "ranking",
    "image",
    "url",
    "website",
]


df = postgresql_to_dataframe(select_query, column_names)

Grape.objects.all().delete()
Bottle.objects.all().delete()
BottleCollection.objects.all().delete()
Appellation.objects.all().delete()

cellar = Cellar.objects.get(code="michael.scott@gnail.com")

for row, col in df.iterrows():
    dic = {
        "id": col.id,
        # "website_id": col.website_id,
        "name": col["name"],
        "code": col["name"] + str(col.id),
        "vintage": col.vintage,
        "vintage": col.vintage,
        "winery": col.winery,
        "country": col.country,
        "region": col.region,
        "soil": col.soil,
        "color": col.color,
        "bottle_size": col.bottle_size,
        "viticulture": col.viticulture,
        "apogee": col.apogee,
        "garde": col.garde,
        "alcool": col.alcool,
        "price": col.price,
        "ranking": col.ranking,
        "image": col.image,
        "url": col.url,
        "website": col.website,
    }

    ## Process grapes
    grapes = col.grape
    grapes_objects = []
    if grapes:
        grapes = grapes.split("/")
        for grape in grapes:
            percentage, grape_name = None, None
            if "_" in grape:
                percentage, grape_name = grape.split("_")
            else:
                grape_name = grape

            grape_object, _ = Grape.objects.get_or_create(
                name=grape_name,
                code=unidecode.unidecode(grape_name.lower()).replace(" ", "_"),
                percentage=percentage,
            )
            grapes_objects.append(grape_object)

    appellation, _ = Appellation.objects.get_or_create(
        name=col.appellation, code=col.appellation
    )

    bottle_collection = BottleCollection.objects.create(**dic)
    for grape_object in grapes_objects:
        bottle_collection.grape.add(grape_object)
    bottle_collection.save()

    bottle = Bottle.objects.create(
        bottle_collection=bottle_collection, cellar=cellar, stock=1
    )
    print(bottle)
