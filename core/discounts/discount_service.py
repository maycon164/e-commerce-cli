from functools import reduce
from typing import List

from core.discounts.discount_rule import DiscountApplier
from model.index import PurchaseDTO


class DiscountService:

    _appliers: List[DiscountApplier]

    def __init__(self, appliers: List[DiscountApplier]):
        self._appliers = appliers

    def calculate_for_purchase(self, purchase_dto: PurchaseDTO):

        return reduce(
            lambda acc, applier: acc + applier.execute(purchase_dto),
            self._appliers
        )



