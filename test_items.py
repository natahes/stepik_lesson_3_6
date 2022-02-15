import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_add_to_basket_button_exists(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)

    try:
        btn = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    except NoSuchElementException:
        btn = None

    assert btn, '"Add to basket" button is missing'
