from model.gem import Gem
from service import gem as code


sample = Gem(
    name="Diamond",
    country_of_origin="South Africa",
    area_of_discovery="Kimberley",
    color="Clear",
    value=50000,
    description="A precious gemstone known for its brilliance and hardness."
)


async def test_create():
    """Test adding a gem."""
    result = await code.add(sample)
    assert result == sample


async def test_get_exists():
    """Test getting an existing gem by name."""
    result = await code.get_gem_by_name(sample.name)
    assert result == sample


async def test_get_missing():
    """Test getting a non-existent gem by name."""
    result = await code.get_gem_by_name("Turquoise")
    assert result is None
