from abc import ABCMeta, ABC
from decimal import Decimal

from core.discounts.discount_rule import Discount

class FixedDiscount(Discount, ABC):

    def __init__(self, amount: Decimal):
        self.amount = amount

    def calculate_discount(self, value: Decimal) -> Decimal:
        return self.amount