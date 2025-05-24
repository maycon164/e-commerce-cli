from abc import ABC
from decimal import Decimal

from core.discounts.coupon.repository.coupon_repository import CouponRepository
from core.discounts.discount_rule import DiscountApplier
from model.index import PurchaseDTO

class CouponDiscountApplier(DiscountApplier, ABC):

    _coupon_repository: CouponRepository

    def __init__(self, coupon_repository: CouponRepository):
        self._coupon_repository = coupon_repository

    def execute(self, purchase_dto: PurchaseDTO) -> Decimal:
        if not purchase_dto.coupon:
            return Decimal('0,0')

        coupon = self._coupon_repository.find_by_code(purchase_dto.coupon)

        if coupon:
            if coupon.condition.evaluate(purchase_dto):
                return coupon.discount.calculate_discount(purchase_dto.get_total_value())

        return Decimal('0, 0')

