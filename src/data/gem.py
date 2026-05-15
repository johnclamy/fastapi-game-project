import sqlite3
from model.gem import Gem


DB_NAME = 'gem_quest.db'
conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()


def init():
    curs.execute('''
        CREATE TABLE gem (
            name,
            country_of_origin,
            area_of_discovery,
            color,
            value,
            description
        )
    ''')


def row_to_model(row: tuple) -> Gem:
    return Gem(
        name=row[0],
        country_of_origin=row[1],
        area_of_discovery=row[2],
        color=row[3],
        value=row[4],
        description=row[5]
    )


def model_to_dict(gem: Gem) -> dict:
    return gem.dict()


def get_one(name: str) -> Gem:
    qry = "SELECT * FROM gem WHERE name =:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()

    return row_to_model(row)


def get_all(name: str) -> list[Gem]:
    qry = "SELECT * FROM gem"
    curs.execute(qry)
    rows = list(curs.fetchall())

    return [row_to_model(row) for row in rows]


def create(gem: Gem) -> None:
    qry = '''
        INSERT INTO gem (
            name,
            country_of_origin,
            area_of_discovery,
            color,
            value,
            description
        ) VALUES (
            :name,
            :country_of_origin,
            :area_of_discovery,
            :color,
            :value,
            :description
        )
    '''
    params = model_to_dict(gem)
    curs.execute(qry, params)


def modify(gem: Gem):
    return gem


def replace(gem: Gem):
    return gem


def delete(gem: Gem):
    qry = "DELETE FROM gem WHERE name =:name"
    params = {"name": gem.name}
    curs.execute(qry, params)
