import psycopg2
import pandas as pd

# from business.bottle.bottle.models import Bottle

credentials = {
    "host": "localhost",
    "user": "postgres",
    "database": "postgres",
    "password": "1234",
    "port": "5432",
}


def connector_db():
    connection = psycopg2.connect(**credentials)
    return connection


def postgresql_to_dataframe(select_query, column_names):
    cursor = connector_db().cursor()
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


column_names = [
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


def get():
    return postgresql_to_dataframe(
        select_query="""select * from public.crawled_bottles""", column_names=column_names
    ).domaine


print(set(get()))

# for bottle in list(set(get())):
#     Bottle.objects.create(name=bottle, code=bottle)


# def ok():
# return [{"name": elt} for elt in list(set(get()))]


# import json
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(ok(), f, ensure_ascii=False, indent=4)
