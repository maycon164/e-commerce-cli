from abc import ABC
from decimal import Decimal

from model.index import Product, Address

class DeliveryTaxDTO:

    def __init__(self, products: [Product], address: Address ):
        self.products = products
        self.address = address

class DeliveryTaxResponseDTO:

    def __init__(self, products: [Product], tax: Decimal):
        self.products = products
        self.tax = tax

class DeliveryTaxCalculator(ABC):

    @classmethod
    def execute(self, delivery_tax_dto: DeliveryTaxDTO) -> DeliveryTaxResponseDTO:
        pass

