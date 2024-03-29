from app.application import Application
import pytest
import json
import functools
import allure
from allure_commons.types import AttachmentType
# from allure.constants import AttachmentType
import os.path

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'], config=config)
    return fixture


@pytest.fixture(scope="module", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def capture_screenshot(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            allure.attach('Screenshot', kwargs['app'].driver.get_screenshot_as_png(),
                          attachment_type=AttachmentType.PNG)
            raise

    return wrapper


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
