import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# Facebook login page link
driver.get("https://www.facebook.com/login/")
driver.maximize_window()

# Login page
driver.find_element(By.NAME, "email").send_keys("beingzainsheikh389@gmail.com")
driver.find_element(By.ID, "pass").send_keys("aaasss@22")
driver.find_element(By.NAME, "login").click()
time.sleep(2)
driver.back()

# Click on login button
driver.find_element(By.XPATH, "//*[@id='login_link']/a[2]").click()

# Sign In Page
driver.find_element(By.NAME, "firstname").send_keys("Test")
driver.find_element(By.NAME, "lastname").send_keys("Demo")
driver.find_element(By.NAME, "reg_email__").send_keys("beingzainsheikh@gmail.com")
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("beingzainsheikh@gmail.com")
driver.find_element(By.NAME, "reg_passwd__").send_keys("aaasss@22")

# Select Day / Month / Year
# Select By Index Number
day = driver.find_element(By.ID, "day")
day_drp = Select(day)
day_drp.select_by_index(3)

# Select By Visible_Text
month = driver.find_element(By.ID, "month")
month_drp = Select(month)
month_drp.select_by_visible_text("May")

# Select By Value
year = driver.find_element(By.ID, "year")
year_drp = Select(year)
year_drp.select_by_value("2000")

driver.find_element(By.XPATH, "//label[text()='Male']").click()

# Click on SignIn button
driver.find_element(By.NAME, "websubmit").click()
time.sleep(5)
driver.close()
driver.quit()
