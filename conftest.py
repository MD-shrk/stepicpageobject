import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ec or fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    # return request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    print("\nstart chrome browser for test..")
    yield browser
    browser.quit()
