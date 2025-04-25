import json
import os

from src.Category import Category
from src.Product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_object_json(data):
    categorys = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categorys.append(Category(**category))
    return categorys


if __name__ == "__main__":
    row_data = read_json("../data/products.json")
    categorys_data = create_object_json(row_data)
    print(categorys_data)
    print(categorys_data[0].name)
    print(categorys_data[0].products)
