from selene.support.shared import browser
from selene import be, have
import pytest

# устанавливаем размер окна
@pytest.fixture()
def configure_browser_size():
    browser.config.window_width = 500
    browser.config.window_height = 500

# открываем браузер, подтягивая размер окна
@pytest.fixture()
def open_browser(configure_browser_size):
    browser.open_url('https://google.com')
    yield
    browser.close()

# находим селктор q, прописываем туда selene и жмем enter
# находим селектор search и проверяем есть ли там текст -
def test_google(open_browser):
    browser.element('[name="q"]').should(be.blank).type('юыююайцюпйцуцзлицщои430').press_enter()
    browser.element('[id="topstuff"]')\
        .should(have.text('ничего не найдено'))
