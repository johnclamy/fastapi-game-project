from model.gem import Gem
import mockdata.gem as data


async def get_gems() -> list[Gem]:
    return await data.get_gems()


async def get_gem_by_name(name: str) -> Gem | None:
    gem: Gem | None = None
    
    if name is not None:
        gem = await data.get_gem_by_name(name)
    else:
        gem = None

    return gem


async def add(gem: Gem) -> Gem:
    return await data.add(gem)


async def update(name: str, updated_gem: Gem) -> Gem | None:
    return await data.update(name, updated_gem)


async def replace(name: str, new_gem: Gem) -> Gem | None:
    return await data.replace(name, new_gem)


async def delete(name: str) -> bool:
    return await data.delete(name)
