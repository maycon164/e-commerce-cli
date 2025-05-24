from abc import ABC, abstractmethod
from decimal import Decimal

from model.index import PurchaseDTO

class Condition(ABC):

    @abstractmethod
    def evaluate(self, purchase_dto: PurchaseDTO) -> bool:
        pass

class Discount(ABC):

    @abstractmethod
    def calculate_discount(self, value: Decimal) -> Decimal:
        pass

class DiscountApplier(ABC):

    @abstractmethod
    def execute(self, purchase_dto: PurchaseDTO) -> Decimal:
        pass