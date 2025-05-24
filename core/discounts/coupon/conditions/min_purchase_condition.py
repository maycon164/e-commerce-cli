from abc import ABC
from decimal import Decimal

from core.discounts.discount_rule import Condition
from model.index import PurchaseDTO

class MinPurchaseCondition(Condition, ABC):

    def __init__(self, value: Decimal):
        self.value = value

    def evaluate(self, purchase_dto: PurchaseDTO) -> bool:
        return purchase_dto.get_total_value() >= self.value

