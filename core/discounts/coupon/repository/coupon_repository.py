from abc import ABCMeta, ABC, abstractmethod

from core.discounts.coupon.coupon import Coupon


class CouponRepository(ABC):

    @abstractmethod
    def find_by_code(self, coupon_code: str) -> Coupon:
        pass