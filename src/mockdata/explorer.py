from model.explorer import Explorer


# List to be replaced by a real database and SQL

_explorers = [
    Explorer(
        name="Marcella Paloma",
        gender="Female",
        nationality="Italian",
        age=35,
        experience=10,
        description="A famous treasure hunter from Italy."
    ),

    Explorer(
        name="Pepe Rodriguez",
        gender="Male",
        nationality="Spanish",
        age=45,
        experience=15,
        description="A famous treasure hunter from Spain."
    ),

    Explorer(
        name="Jane H. James",
        gender="Female",
        nationality="British",
        age=38,
        experience=14,
        description="A famous treasure hunter from the United Kingdom."
    )
]


async def get_explorers() -> list[Explorer]:
    """Return all explorers"""
    return _explorers


async def get_explorer(name: str) -> Explorer | None:
    """Return an explorer by name"""
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer

    return None


# Define the non-functional CRUD operations as placeholders

async def add(explorer: Explorer) -> Explorer:
    """Create a new explorer"""
    return explorer


async def update(name: str, explorer: Explorer) -> Explorer:
    """Partially modify an existing explorer"""
    return explorer


async def replace(name: str, explorer: Explorer) -> Explorer:
    """Fully replace an existing explorer"""
    return explorer


async def delete(name: str) -> bool:
    """Delete an explorer by name"""
    return False
