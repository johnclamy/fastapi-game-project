from fastapi import APIRouter
from model.gem import Gem
from mockdata import gem as service


router = APIRouter(prefix="/gem")


@router.get('/')
async def get_gems() -> list[Gem]:
    return await service.get_gems()


@router.get('/{name}')
async def get_gem_by_name(name: str) -> Gem | None:
    return await service.get_gem_by_name(name)


# some remaining endpoints do nothing yet:

@router.post('/')
async def add(gem: Gem) -> Gem:
    return await service.add(gem)


@router.patch('/{name}')
async def update(name: str, gem: Gem) -> Gem | None:
    return await service.update(name, gem)


@router.put('/{name}')
async def replace(name: str, gem: Gem) -> Gem | None:
    return await service.replace(name, gem)


@router.delete('/{name}')
async def delete(name: str) -> bool:
    return await service.delete(name)
