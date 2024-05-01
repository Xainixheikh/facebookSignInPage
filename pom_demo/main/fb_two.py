import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pom_demo.page.fb_login_page import LoginPage
from pom_demo.page.sign_up import HomePage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()


def test_login_valid():
    driver.get("https://www.facebook.com/login/")
    # self_driver = self.driver

    login = LoginPage(driver)
    login.enter_email("beingzainsheikh@gmail.com")
    login.enter_password("aaasss@22")
    login.click_login()
    time.sleep(2)
    driver.back()

    homepage = HomePage(driver)
    homepage.signup_button()
    homepage.enter_firstname("zeeshan")
    homepage.enter_lastname("demo")
    homepage.enter_email("beingzainsheikh@gmail.com")
    homepage.enter_re_email("beingzainsheikh@gmail.com")
    homepage.enter_password("sssaaa@22")
    homepage.select_date()
    homepage.select_month()
    homepage.select_year()
    homepage.select_gender()
    homepage.sign_up_button()


test_login_valid()
