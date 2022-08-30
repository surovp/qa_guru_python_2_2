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
    browser.open_url('https://google.com/ncr')
    yield
    browser.close()

# находим селктор q, прописываем туда selene и жмем enter
# находим селектор search и проверяем есть ли там текст - User-oriented Web UI browser tests in Python
def test_google(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]')\
        .should(have.text('Selene - User-oriented Web UI browser tests in Python'))

