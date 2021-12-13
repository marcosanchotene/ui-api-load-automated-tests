from actions.add_product_to_cart import AddProductToCart
from actions.checkout import Checkout
from actions.sign_in import SignIn
from page_objects.order import Order
from page_objects.product_container import ProductContainer
from page_objects.home_page import HomePage

CONFIRMATION_MESSAGE = "Your order on My Store is complete."


def test_checkout_process(page, user):
    user.attempts_to(SignIn(page, user))
    page.goto(HomePage.URL)
    user.attempts_to(AddProductToCart(page, 1, ProductContainer.FIRST_PRODUCT_ADD_TO_CART_BUTTON))
    user.attempts_to(AddProductToCart(page, 2, ProductContainer.SECOND_PRODUCT_ADD_TO_CART_BUTTON))
    user.attempts_to(AddProductToCart(page, 3, ProductContainer.THIRD_PRODUCT_ADD_TO_CART_BUTTON))
    user.attempts_to(Checkout(page))
    assert CONFIRMATION_MESSAGE == page.inner_text(Order.ORDER_CONFIRMATION_MESSAGE)
