import pytest

from src.Category import Category
from src.Categoty_iter import CategoryIterator
from src.LawnGrass import LawnGrass
from src.Product import Product
from src.Smartphone import Smartphone


@pytest.fixture
def some_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7),
        ],
    )


@pytest.fixture
def product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_iterator(second_category):
    return CategoryIterator(second_category)


@pytest.fixture
def product_smartphone1():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def product_smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_lawn_grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture


def without_category():
    return Category(
        name="Пустая категория",
        description="Категория без продуктов",
        products=[]
    )
