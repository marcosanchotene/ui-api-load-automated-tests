from page_objects.cart_modal import CartModal
from page_objects.product_container import ProductContainer


class AddProductToCart:

    def __init__(self, page, product_number, product_button):
        self.page = page
        self.product_number = product_number
        self.product_button = product_button

    def execute(self):
        self.page.focus(f"{ProductContainer.COMMON_CLASS} >> nth={self.product_number}")
        self.page.hover(f"{ProductContainer.COMMON_CLASS} >> nth={self.product_number}")
        self.page.click(self.product_button)
        self.page.click(CartModal.CONTINUE_SHOPPING_BUTTON, delay=1)
