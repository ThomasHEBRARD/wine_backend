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

all_grapes = []
all_grapes_count = []
a = 0
for row, col in df.iterrows():
    a += 1
    ## Process grapes
    grapes = col.grape
    grapes_objects = []
    if grapes:
        count = 0
        grapes = grapes.split("/")
        for grape in grapes:
            count += 1
            percentage, grape_name = None, None
            if "_" in grape and grape.lower() != "la_folle_blanche":
                percentage, grape_name = grape.split("_")
            else:
                grape_name = grape
            all_grapes.append(grape_name)
        all_grapes_count.append(count)
import statistics
print(a)
print(sum(all_grapes_count))
print(set(all_grapes))
