from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_name = "email"
        self.password_textbox_id = "pass"
        self.login_button_name = "login"

    def enter_email(self, email):
        self.driver.find_element(By.NAME, self.email_textbox_name).clear()
        self.driver.find_element(By.NAME, self.email_textbox_name).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_id).clear()
        self.driver.find_element(By.NAME, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.NAME, self.login_button_name).click()
