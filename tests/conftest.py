import pytest
from selenium import webdriver

# @pytest.yield_fixture(scope="module")
@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request,browser):

    if browser == "chrome":
        path = "/Users/aravindanathdm/Documents/PythonPOM_FW/driver/chromedriver"
        driver = webdriver.Chrome(executable_path=path)
        driver.fullscreen_window()
        driver.implicitly_wait(30)
        baseURL = "https://www.amazon.in"
        driver.get(baseURL)
        print("running on chrome")
    elif browser == "firefox":
        path = "/Users/aravindanathdm/Documents/PythonPOM_FW/driver/geckodriver"
        driver = webdriver.Firefox(executable_path=path)
        driver.fullscreen_window()
        driver.implicitly_wait(30)
        baseURL = "https://www.amazon.in"
        driver.get(baseURL)
        print("running on firefox")

    if request.cls is not None:
        request.cls.driver=driver

    yield driver


@pytest.yield_fixture()
def setUp():
    print("#"*10+"One time setup one before method"+"#"*10)
    # if browser == "chrome":
    #     print("running on chrome")
    # elif browser == "firefox":
    #      print("running on firefox")
    yield
    print("#" * 10 + "One time setup one after method" + "#" * 10)




def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")