# from business.bottle.bottle.models import Bottle
import pandas as pd
import psycopg2


def connector_db():
    connection = psycopg2.connect(
        host="db",
        database="wine_crawling",
        user="postgres",
        password="1234",
        port=5433,
    )
    return connection


connection = connector_db()


def postgresql_to_dataframe(select_query, column_names):
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


crawled_bottles_columns = [
    "name",
    "pays",
    "domaine",
    "producteur",
    "appellation",
    "millesime",
    "color",
    "cepage",
    "degre_alcool",
    "viticulture",
    "apogee",
    "price",
    "classement",
    "note_wa",
    "note_wd",
    "note_ws",
    "note_jmq",
    "website",
    "url",
]


def get_crawled_bottles():
    return tuple(
        postgresql_to_dataframe(
            select_query="""
        select * from public.crawled_bottles
        """,
            column_names=crawled_bottles_columns,
        )
    )


bottles = get_crawled_bottles()
print(bottles)