import pytest
from actions.search_product import SearchProduct
from page_objects.home_page import HomePage
from test_data.products import Popular

PRODUCT_1 = (Popular.PRODUCT_1['title'], f".product-name[title='{Popular.PRODUCT_1['title']}']")
PRODUCT_5 = (Popular.PRODUCT_5['title'], f".product-name[title='{Popular.PRODUCT_5['title']}'][itemprop='url']")
PRODUCT_7 = (Popular.PRODUCT_7['title'], f".product-name[title='{Popular.PRODUCT_7['title']}'][itemprop='url']")


@pytest.mark.parametrize("product,selector", [PRODUCT_1, PRODUCT_5, PRODUCT_7])
def test_search(page, user, product, selector):
    page.goto(HomePage.URL)
    user.attempts_to(SearchProduct(page, product))
    assert product == page.inner_text(selector)
