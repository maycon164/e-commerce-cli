import csv
from decimal import Decimal

from core.discounts.coupon.repository.coupon_csv_repository import CouponCsvRepository
from core.products.repository.product_csv_repository import ProductCsvRepository
from model.index import Product, PurchaseDTO, Cart, Address, PaymentMethod

def run():
    products_file = '../resources/products.csv'
    product_repository = ProductCsvRepository(products_file)

    products = product_repository.find_all()

    print(type(products[0].price))

    cart = Cart(1, products)
    address = Address('John Doe', 'Rua dos bobos', 12, '09098-199', "BRAZIL", 'São Paulo', '11928816221')
    payment_method = PaymentMethod.PIX
    coupon = 'ABC2912A'
    purchase_dto = PurchaseDTO(cart, address, payment_method, coupon)

    file = "../resources/coupons.csv"
    coupon_repository = CouponCsvRepository(file)

    coupon = coupon_repository.find_by_code("IFP1X1O")

    print(coupon)

    print(coupon.condition.evaluate(purchase_dto))
    print(coupon.discount.calculate_discount(Decimal('2000.99')))


run()