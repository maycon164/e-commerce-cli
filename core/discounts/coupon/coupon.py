from core.discounts.discount_rule import Condition, Discount


class Coupon:

    code: str

    def __init__(self, code: str, condition: Condition, discount: Discount):
        self.code = code
        self.condition = condition
        self.discount = discount