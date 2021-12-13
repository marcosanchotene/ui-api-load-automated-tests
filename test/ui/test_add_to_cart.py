from actions.add_product_to_cart import AddProductToCart
from actions.sign_in import SignIn
from page_objects.header import Header
from page_objects.product_container import ProductContainer
from page_objects.home_page import HomePage
from test_data.products import Popular


def test_add_products_to_cart(page, user):
    user.attempts_to(SignIn(page, user))
    page.goto(HomePage.URL)
    user.attempts_to(AddProductToCart(page, 1, ProductContainer.FIRST_PRODUCT_ADD_TO_CART_BUTTON))
    user.attempts_to(AddProductToCart(page, 2, ProductContainer.SECOND_PRODUCT_ADD_TO_CART_BUTTON))
    user.attempts_to(AddProductToCart(page, 3, ProductContainer.THIRD_PRODUCT_ADD_TO_CART_BUTTON))
    page.hover(Header.CART_DROP_DOWN)
    products_list = page.query_selector_all(Header.CART_PRODUCT_NAME)
    assert Popular.PRODUCT_1['title'] == products_list[0].get_attribute('title')
    assert Popular.PRODUCT_2['title'] == products_list[1].get_attribute('title')
    assert Popular.PRODUCT_3['title'] == products_list[2].get_attribute('title')
