from core.delivery_tax.delivery_tax_calculator import DeliveryTaxCalculator, DeliveryTaxDTO
from core.discounts.discount_service import DiscountService
from model.index import PurchaseDTO
from core.payment.payment_service import PaymentService


class PurchaseService:

    _payment_service:PaymentService
    _delivery_tax_calculator: DeliveryTaxCalculator
    _discount_service: DiscountService

    def __init__(self, payment_service: PaymentService, delivery_tax_calculator: DeliveryTaxCalculator, discount_service: DiscountService):
        self._payment_service = payment_service
        self._delivery_tax_calculator = delivery_tax_calculator
        self._discount_service = discount_service

    def process_purchase(self, purchase_dto: PurchaseDTO):

        total_value_products = purchase_dto.cart.get_total_value()
        delivery_tax_calculator = self._delivery_tax_calculator.execute(DeliveryTaxDTO(products=purchase_dto.cart.get_products(), address= purchase_dto.delivery_address))
        discount_value = self._discount_service.calculate_for_purchase(purchase_dto)

        return total_value_products + delivery_tax_calculator - discount_value
