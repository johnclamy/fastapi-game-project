from model.explorer import Explorer
from mockdata import explorer as data


async def get_explorers() -> list[Explorer]:
    return await data.get_explorers()


async def get_explorer(name: str) -> Explorer | None:
    return await data.get_explorer(name)


async def add(explorer: Explorer) -> Explorer:
    return await data.add(explorer)


async def update(name: str, explorer: Explorer) -> Explorer:
    return await data.update(name, explorer)


async def replace(name: str, explorer: Explorer) -> Explorer:
    return await data.replace(name, explorer)
