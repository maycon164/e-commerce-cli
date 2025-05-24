from decimal import Decimal


class Product:

    def __init__(self, id: int, name: str, quantity: int, price: Decimal):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price