from page_objects.my_account import MyAccountPage
from actions.sign_in import SignIn


def test_login(page, user):
    user.attempts_to(SignIn(page, user))
    assert page.url == MyAccountPage.URL
