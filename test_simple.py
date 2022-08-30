import pytest


@pytest.fixture()
def open_browser():
    print("Я вызываюсь перед текстом")
    yield # разделитель (происходит тест)
    print("Я вызываюсь после теста")

@pytest.fixture()
def configure_browser():
    print("Дексктоп")


def test_first(open_browser):
    pass

def test_second():
    assert 1==1

def test_third():
    pass
