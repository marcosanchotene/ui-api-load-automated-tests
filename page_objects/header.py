class Header:
    SIGN_IN_BUTTON = "text=Sign in"
    SEARCH_FIELD = "#search_query_top"
    SEARCH_BUTTON = "[name='submit_search']"
    CART_DROP_DOWN = "[title='View my shopping cart']"
    CART_PRODUCT_NAME = ".cart_block_product_name"
    CHECKOUT_BUTTON = "button_order_cart"

    @staticmethod
    def product_in_cart(product_title):
        return f"a[data-id=cart_block_product_1_1_0]:has(a[title={product_title}])"
