import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pom_demo.page.fb_login_page import LoginPage
from pom_demo.page.sign_up import HomePage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds
driver.maximize_window()


def test_login_valid():
    driver.get("https://www.facebook.com/login/")
    # self_driver = self.driver
    expected_title = "Log in to Facebook"
    login = LoginPage(driver)
    login.enter_email("beingzainsheikh@gmail.com")
    login.enter_password("aaasss@22")
    login.click_login()
    actual_title = driver.title
    # element = driver.find_element(By.XPATH, "//div[@id='error_box']")  # wait.until()
    # is_element_present = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='error_box']")))
    if actual_title != expected_title:
        print("Login successfully")
    else:
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
        print("Sign Up successfully")


test_login_valid()
