import csv
from abc import ABC

from core.discounts.coupon.coupon import Coupon
from core.discounts.coupon.factory.coupon_factory import CouponFactory
from core.discounts.coupon.repository.coupon_repository import CouponRepository


class CouponCsvRepository(CouponRepository, ABC):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def find_by_code(self, coupon_code: str) -> Coupon:

        with open(self.file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['code'] == coupon_code:
                    return CouponFactory.build_coupon(row)
            return None

