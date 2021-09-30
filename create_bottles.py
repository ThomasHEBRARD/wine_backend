from business.bottle.bottle_collection.models import BottleCollection
from business.bottle.bottle.models import Bottle
from business.grape.models import Grape
from business.cellar.models import Cellar
from business.appellation.models import Appellation


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
    WHERE website = 'idealwine'
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


def process_grape_data(data):
    if data.website == "idealwine":
        # virer les \xa0 et les \t
        # if "/" not in data.grape:
            # 
        if "_" in data.grape:
            grapes = [
                {"grape": grape.split("_")[1], "percentage": grape.split("_")[0]}
                for grape in data.grape.split("/")
            ]
            # Ingérer dans Grape
        else:
            grapes = data.grape.split("/")
    if data.website == "vinsfins":
        if "_" in data.grape:
            grapes = [
                {"grape": grape.split("_")[1], "percentage": grape.split("_")[0]}
                for grape in data.grape.split(",")
            ]
            # Ingérer dans Grape
        else:
            grapes = data.grape.split(",")
    if data.website == "millesima":
        grapes = data.grape.split("/")
        # Ingérer dans Grape (pas de pourcentage)
    if data.website == "twil":
        grapes = data.grape.split(",")
        # Ingérer dans Grape (pas de pourcentage)


df = postgresql_to_dataframe(select_query, column_names)

# Grape.objects.all().delete()
# Bottle.objects.all().delete()
# BottleCollection.objects.all().delete()
# Appellation.objects.all().delete()

# cellar = Cellar.objects.get(code="michael.scott@gnail.com")

for row, col in df.iterrows():
    process_crawling_data(col)
    grape, _ = Grape.objects.get_or_create(name=col.grape, code=col.grape)
    # appellation, _ = Appellation.objects.get_or_create(
    #     name=col.appellation, code=col.appellation
    # )
    # dic = {
    #     "id": col.id,
    #     # "website_id": col.website_id,
    #     "name": col["name"],
    #     "code": col["name"] + str(col.id),
    #     "vintage": col.vintage,
    #     "vintage": col.vintage if type(col.vintage) == "int" else 0000,
    #     "winery": col.winery,
    #     "country": col.country,
    #     "region": col.region,
    #     "soil": col.soil,
    #     "color": col.color,
    #     "bottle_size": col.bottle_size,
    #     "viticulture": col.viticulture,
    #     "apogee": col.apogee,
    #     "garde": col.garde,
    #     "alcool": col.alcool,
    #     "price": col.price,
    #     "ranking": col.ranking,
    #     "image": col.image,
    #     "url": col.url,
    #     "website": col.website,
    # }

    # bottle_collection = BottleCollection.objects.create(**dic)
    # bottle_collection.grape.add(grape)
    # bottle_collection.save()

    # bottle = Bottle.objects.create(
    #     bottle_collection=bottle_collection, cellar=cellar, stock=1
    # )
    # print(bottle)
