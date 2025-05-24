from decimal import Decimal

from core.discounts.coupon.conditions.min_purchase_condition import MinPurchaseCondition
from core.discounts.coupon.coupon import Coupon
from core.discounts.coupon.discounts.fixed_discount import FixedDiscount

CONDITION_REGISTRY = {
    'min_purchase': lambda value: MinPurchaseCondition(Decimal(value))
}

DISCOUNT_REGISTRY = {
    'fixed': lambda value: FixedDiscount(Decimal(value))
}

class CouponFactory:

    @staticmethod
    def build_coupon(row: dict[str, str]) -> Coupon:
        condition_factory = CONDITION_REGISTRY[row["condition_type"]]
        discount_factory = DISCOUNT_REGISTRY[row["discount_type"]]

        condition = condition_factory(row['condition_value'])
        discount = discount_factory(row['discount_value'])

        return Coupon(row['code'], condition, discount)
