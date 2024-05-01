import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.signup_button_xpath = "//a[normalize-space()='Sign up for Facebook']"
        self.firstname_textbox_name = "firstname"
        self.lastname_textbox_name = "lastname"
        self.email_textbox_name = "reg_email__"
        self.re_email_textbox_name = "reg_email_confirmation__"
        self.password_textbox_name = "reg_passwd__"
        self.select_date_id = "day"
        self.select_date_by_index = 5
        self.select_month_id = "month"
        self.select_month_by_visible_text = "May"
        self.select_year_id = "year"
        self.select_year_by_value = "2000"
        self.select_gender_label = "//label[normalize-space()='Male']"
        self.click_signup_button = "websubmit"

    def signup_button(self):
        self.driver.find_element(By.XPATH, self.signup_button_xpath).click()

    def enter_firstname(self, username):
        self.driver.find_element(By.NAME, self.firstname_textbox_name).clear()
        self.driver.find_element(By.NAME, self.firstname_textbox_name).send_keys(username)

    def enter_lastname(self, username):
        self.driver.find_element(By.NAME, self.lastname_textbox_name).clear()
        self.driver.find_element(By.NAME, self.lastname_textbox_name).send_keys(username)

    def enter_email(self, username):
        self.driver.find_element(By.NAME, self.email_textbox_name).clear()
        self.driver.find_element(By.NAME, self.email_textbox_name).send_keys(username)
        time.sleep(5)

    def enter_re_email(self, username):
        self.driver.find_element(By.NAME, self.re_email_textbox_name).clear()
        self.driver.find_element(By.NAME, self.re_email_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def select_date(self):
        date = self.driver.find_element(By.ID, self.select_date_id)
        drp_date = Select(date)
        drp_date.select_by_index(self.select_date_by_index)

    def select_month(self):
        month = self.driver.find_element(By.ID, self.select_month_id)
        drp_month = Select(month)
        drp_month.select_by_visible_text(self.select_month_by_visible_text)

    def select_year(self):
        year = self.driver.find_element(By.ID, self.select_year_id)
        drp_year = Select(year)
        drp_year.select_by_value(self.select_year_by_value)

    def select_gender(self):
        self.driver.find_element(By.XPATH, self.select_gender_label).click()

    def sign_up_button(self):
        self.driver.find_element(By.NAME, self.click_signup_button).click()
        time.sleep(10)
