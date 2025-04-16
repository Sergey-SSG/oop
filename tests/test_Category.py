def test_category_init(some_category, second_category):
    assert some_category.name == "Смартфоны"
    assert some_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(some_category.products) == 2

    assert some_category.category_count == 2
    assert second_category.category_count == 2
    assert some_category.product_count == 4
    assert second_category.product_count == 4
