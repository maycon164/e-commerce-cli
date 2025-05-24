import csv
from abc import ABC
from decimal import Decimal

from core.products.model.index import Product
from core.products.repository.product_repository import ProductRepository


class ProductCsvRepository(ProductRepository, ABC):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def find_all(self):
        products:list[Product]  = []

        with open(self.file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                products.append(Product(row['id'], row['name'], row['quantity'], Decimal(row['price'])))

        return products
