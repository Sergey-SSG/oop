import pytest


def test_lawn_grass_init(product_lawn_grass):
    assert product_lawn_grass.name == "Газонная трава"
    assert product_lawn_grass.description == "Элитная трава для газона"
    assert product_lawn_grass.price == 500.0
    assert product_lawn_grass.quantity == 20
    assert product_lawn_grass.country == "Россия"
    assert product_lawn_grass.germination_period == "7 дней"
    assert product_lawn_grass.color == "Зеленый"


def test_lawn_grass_add(product_lawn_grass, product_lawn_grass2):
    assert product_lawn_grass + product_lawn_grass2 == 16750.0


def test_lawn_grass_add_error(product_lawn_grass):
    with pytest.raises(TypeError):
        _ = product_lawn_grass + 1
