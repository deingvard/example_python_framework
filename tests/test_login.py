from model.group import Group


def test_login(app, config):
    # with pytest.allure.step("Open Login Page"):
    app.open_home_page()
    # with pytest.allure.step('Enter username'):
    app.login_page.enter_username(Group(username=config['web']['username']))
    # with pytest.allure.step('Enter password'):
    # app.login_page.enter_password(Group(password=config['web']['password']))
    # # with pytest.allure.step('Click submit button'):
    # app.login_page.click_submit_button()
    # # with pytest.allure.step('Verify sub-header text for Secure area page'):
    # assert app.secure_area_page.check_secure_area_text(
    #     'Welcome to the Secure Area. When you are done click logout below.'), \
    #     "Text could not be found on the Secure Area page"
