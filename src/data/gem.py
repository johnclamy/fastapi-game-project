from .init import conn, curs
from model.gem import Gem


curs.execute("""
    CREATE TABLE IF NOT EXISTS gem (
        name TEXT PRIMARY KEY,
        country_of_origin TEXT,
        area_of_discovery TEXT,
        color TEXT,
        value INT,
        description TEXT
    )
""")


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

    return row_to_model(curs.fetchone())


def get_all() -> list[Gem]:
    qry = "SELECT * FROM gem"
    curs.execute(qry)

    return [row_to_model(row) for row in curs.fetchall()]


def create(gem: Gem) -> Gem | None:
    qry = '''
        INSERT INTO gem VALUES (
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

    return get_one(gem.name)


def modify(gem: Gem) -> Gem:
    qry = '''
        UPDATE gem SET
            country_of_origin =:country_of_origin,
            area_of_discovery =:area_of_discovery,
            color =:color,
            value =:value,
            description =:description
        WHERE name =:name
    '''
    params = model_to_dict(gem)
    params["name"] = gem.name
    _ = curs.execute(qry, params)

    return get_one(gem.name)


def replace(gem: Gem) -> Gem | None:
    qry = '''
        REPLACE INTO gem VALUES (
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

    return get_one(gem.name)


def delete(gem: Gem):
    qry = "DELETE FROM gem WHERE name =:name"
    params = {"name": gem.name}
    curs.execute(qry, params)
