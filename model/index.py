from datetime import date
from decimal import Decimal
from enum import auto
from functools import reduce

from core.products.model.index import Product


class Address:

    def __init__(self, name: str, street: str, number: str, zip_code: str, country: str, city: str, cel: str):
        self.name = name
        self.street = street
        self.number = number
        self.zip_code = zip_code
        self.country = country
        self.city = city
        self.cel = cel

class User:

    def __init__(self, id: int, name: str, address: Address):
        self.id = id
        self.name = name
        self.address = address

class Cart:
    def __init__(self, id: int, products: list[Product]):
        self.id = id
        self.products = products

    def get_products(self):
        return self.products

    def get_total_value(self):
        return reduce(lambda acc, current: acc + (Decimal(str(current.price)) * Decimal(str(current.quantity))), self.products, 0)

class PaymentMethod[Enum]:
    CREDIT_CARD = auto()
    PIX = auto()
    MONEY = auto()
    CHECK = auto()
    POINTS = auto()
    TICKET = auto()


class CardFlag:
    VISA: auto()
    MASTERCARD: auto()
    CIELO: auto()
    AMERICAN_CARD: auto()

class CardInformation:

    def __init__(self, number: str, owner_name: str, expiration_date: date, secure_code: str, flag: CardFlag):
        self.number = number
        self.owner = owner_name
        self.expiration_date = expiration_date
        self.secure_code = secure_code
        self.flag = flag

class PaymentInformationDTO:

    def __init__(self, card: CardInformation, address: Address, value: Decimal):
        self.card = card
        self.address = address
        self.value = value

class PurchaseDTO:

    def __init__(self, cart: Cart, delivery_address: Address, payment_method: PaymentMethod, coupon: str):
        self.cart = cart
        self.delivery_address= delivery_address
        self.payment_method = payment_method
        self.coupon = coupon

    def get_address(self):
        return self.delivery_address

    def get_coupon(self):
        return self.coupon

    def get_total_value(self):
        return self.cart.get_total_value()


