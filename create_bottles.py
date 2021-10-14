from django.db.models import CharField
from django.db.models.functions import Lower

CharField.register_lookup(Lower)

from business.bottle.bottle_collection.models import BottleCollection
from business.bottle.bottle.models import Bottle
from business.grape.models import Grape, GrapeBottleCollection
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
    SELECT * FROM public.cleaned_crawled_bottles
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

GrapeBottleCollection.objects.all().delete()
Bottle.objects.all().delete()
BottleCollection.objects.all().delete()
# Grape.objects.all().delete()
Appellation.objects.all().delete()

cellar = Cellar.objects.get(code="michael.scott@gnail.com")


for row, col in df.iterrows():
    appellation, _ = Appellation.objects.get_or_create(
        name=col.appellation,
        code=unidecode.unidecode(col.appellation.lower()).replace(" ", "_"),
    )
    dic = {
        "id": col.id,
        "name": col["name"],
        "code": unidecode.unidecode(col["name"].lower()).replace(" ", "_")
        + "_"
        + str(col.id),
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
        "appellation": appellation,
    }

    bottle_collection = BottleCollection.objects.create(**dic)

    ## Process grapes
    grapes = col.grape
    grapes_objects = []

    if grapes:
        # Tous de la forme percentage_grape/percentage_grape/...
        # ou grape/grape/grape si pas de percentage
        grapes = grapes.split("/")
        for grape in grapes:
            percentage, grape_name = None, None
            if "_" in grape:
                percentage, grape_name = grape.split("_")
            else:
                grape_name = grape

            grape_object = None

            print(grape_name)
            try:
                grape_object = Grape.objects.get(
                    code=unidecode.unidecode(grape_name.lower()).replace(" ", "_")
                )
            except Grape.DoesNotExist:
                grape_object = None
            if not grape_object:
                try:
                    grape_object = Grape.objects.get(
                        variants__lower__icontains=unidecode.unidecode(
                            grape_name.lower()
                        )
                    )
                except Grape.DoesNotExist:
                    grape_object = None
                if not grape_object:
                    try:
                        grape_object = Grape.objects.get(
                            variants__icontains=unidecode.unidecode(grape_name)
                        )
                    except Grape.DoesNotExist:
                        grape_object = None

                    if not grape_object:
                        grape_object = Grape.objects.create(
                            name=grape_name,
                            code=unidecode.unidecode(grape_name.lower()).replace(
                                " ", "_"
                            ),
                            verified=False,
                        )
                        print("pipi", grape_name)

            #On peu faire par exmemple : Si merlott, on prend tous les grapes percentages et on leur change les grapes id
            # fuzzywuzz ??? levenshtein ??

            grape_bottle_collection_object = GrapeBottleCollection.objects.create(
                grape=grape_object,
                bottle_collection=bottle_collection,
                percentage=percentage,
            )
            grapes_objects.append(grape_bottle_collection_object)

    bottle = Bottle.objects.create(
        bottle_collection=bottle_collection, cellar=cellar, stock=1
    )
    # print(bottle)
