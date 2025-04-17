def test_category_init(some_category, second_category):
    assert some_category.name == "Смартфоны"
    assert some_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(some_category.add_product_in_list) == 2

    assert some_category.category_count == 2
    assert second_category.category_count == 2
    assert some_category.product_count == 190
    assert second_category.product_count == 190


def test_category_products_property(some_category):
    assert some_category.products == (" Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                                      "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n")
