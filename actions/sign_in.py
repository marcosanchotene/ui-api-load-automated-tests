from page_objects.header import Header
from page_objects.home_page import HomePage
from page_objects.sign_in import SignInPage


class SignIn:

    def __init__(self, page, user):
        self.page = page
        self.user = user

    def execute(self):
        self.page.goto(HomePage.URL)
        self.page.click(Header.SIGN_IN_BUTTON)
        self.page.click(SignInPage.REGISTERED_EMAIL_ADDRESS_INPUT)
        self.page.fill(SignInPage.REGISTERED_EMAIL_ADDRESS_INPUT, self.user.email)
        self.page.press(SignInPage.REGISTERED_EMAIL_ADDRESS_INPUT, "Tab")
        self.page.fill(SignInPage.PASSWORD_INPUT, self.user.password)
        self.page.click(SignInPage.SIGN_IN_BUTTON)
