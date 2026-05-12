from fastapi import APIRouter
from model.explorer import Explorer
from mockdata import explorer as service


router = APIRouter(prefix="/explorer")


@router.get('/')
async def get_explorers() -> list[Explorer]:
    return await service.get_explorers()


@router.get('/{name}')
async def get_explorer(name: str) -> Explorer | None:
    return await service.get_explorer(name)


# all remaining endpoints do nothing yet:

@router.post('/')
async def add(explorer: Explorer) -> Explorer:
    return await service.add(explorer)


@router.patch('/')
async def update(name: str, explorer: Explorer) -> Explorer:
    return await service.update(name, explorer)


@router.put('/')
async def replace(name: str, explorer: Explorer) -> Explorer:
    return await service.update(name, explorer)


@router.delete('/{name}')
async def delete(name: str) -> bool:
    return await service.delete(name)
