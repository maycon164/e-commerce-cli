from typing import Dict

from model.index import PurchaseDTO, PaymentMethod
from core.payment.payment_processor_strategy import PaymentProcessorStrategy


class PaymentService:

    _payment_strategy: Dict[PaymentMethod, PaymentProcessorStrategy]

    def __init__(self, payment_strategy: Dict[PaymentMethod, PaymentProcessorStrategy]):
        self._payment_strategy = payment_strategy

    def pay(self, purchase_dto: PurchaseDTO):
        ## TODO: implement
        payment_processor = self._payment_strategy.get(purchase_dto.payment_method)
        payment_processor.execute(purchase_dto.payment_information_dto)




