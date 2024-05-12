import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)

# Facebook login page link
driver.get("https://acemoneytransfer.com/")
driver.maximize_window()

# Create
driver.find_element(By.XPATH, "//a[normalize-space()='Create An Account']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='email-sign']").send_keys("Zeeshan@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("aaasss@22")

sec_from = driver.find_element(By.ID, "country_iso_code")
select_from = Select(sec_from)
select_from.select_by_visible_text("Austria")
print("Select Country")

driver.find_element(By.NAME, "phone").send_keys("345647688")

sec_to = driver.find_element(By.ID, "send_to")
select_to = Select(sec_to)
select_to.select_by_visible_text("Benin")
print("To Country")

hearedFromDrp = driver.find_element(By.ID, "heared_from")
text_box = Select(hearedFromDrp)
text_box.select_by_visible_text("Billboard")
print("Select Box")


driver.find_element(By.XPATH, "//*[@id='sign_up_form']/div[13]/div[2]/label").click()
driver.find_element(By.NAME, "referral_code").send_keys("223344")

driver.find_element(By.XPATH, "//*[@id='sign_up_form']/div[17]/div[2]/label").click()
driver.find_element(By.ID, "register_btn").click()
print("process finis")
time.sleep(3)