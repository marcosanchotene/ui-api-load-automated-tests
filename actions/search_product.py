from page_objects.header import Header


class SearchProduct:

    def __init__(self, page, product):
        self.page = page
        self.product = product

    def execute(self):
        self.page.click(Header.SEARCH_FIELD)
        self.page.fill(Header.SEARCH_FIELD, self.product)
        self.page.click(Header.SEARCH_BUTTON)
