from page_objects.header import Header
from page_objects.order import Order


class Checkout:

    def __init__(self, page):
        self.page = page

    def execute(self):
        self.page.click(Header.CART_DROP_DOWN)
        self.page.click(Order.PROCEED_TO_CHECKOUT_BUTTON)
        self.page.click(Order.CONFIRM_ORDER_BUTTON)
        self.page.click(Order.TERMS_OF_SERVICE_CHECKBOX)
        self.page.click(Order.PROCEED_TO_CHECKOUT_BUTTON)
        self.page.click(Order.PAY_BY_BANK_WIRE_BUTTON)
        self.page.click(Order.CONFIRM_ORDER_BUTTON)
