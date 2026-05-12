from model.gem import Gem


# Mock data for gems

_gems = [
    Gem(
        name="Ruby",
        country_of_origin="Myanmar",
        area_of_discovery="Mogok Valley",
        color="Red",
        value=10000,
        description="A precious gemstone known for its vibrant red color and rarity."
    ),
    Gem(
        name="Sapphire",
        country_of_origin="Sri Lanka",
        area_of_discovery="Ratnapura",
        color="Blue",
        value=8000,
        description="A precious gemstone known for its deep blue color and durability."
    ),
    Gem(
        name="Emerald",
        country_of_origin="Colombia",
        area_of_discovery="Muzo",
        color="Green",
        value=12000,
        description="A precious gemstone known for its rich green color and rarity."
    )
]


async def get_gems():
    """Returns a list of mock gems."""
    return _gems


async def get_gem_by_name(name: str) -> Gem | None:
    """Returns a mock gem by name."""
    for _gem in _gems:
        if _gem.name == name:
            return _gem

    return None


# Define the non-functional CRUD operations as placeholders

async def add(gem: Gem) -> Gem:
    """Creates a new gem (mock implementation)."""
    _gems.append(gem)
    return gem


async def update(name: str, updated_gem: Gem) -> Gem | None:
    """Partially modify a gem by name (mock implementation)."""
    for i, _gem in enumerate(_gems):
        if _gem.name == name:
            _gems[i] = updated_gem
            return updated_gem
    return None


async def replace(name: str, new_gem: Gem) -> Gem | None:
    """Fully replace a gem by name (mock implementation)."""
    for i, _gem in enumerate(_gems):
        if _gem.name == name:
            _gems[i] = new_gem
            return new_gem
    return None


async def delete(name: str) -> bool:
    """Deletes a gem by name (mock implementation)."""
    global _gems
    _gems = [gem for gem in _gems if gem.name != name]
    return True

