from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your credentials
EMAIL = "utsharoyrudra44"
PASSWORD = "A100100#"

# Initialize the browser
driver = webdriver.Chrome()


# Open YouTube
driver.get("https://codeforces.com/")
time.sleep(2)
driver.maximize_window()

# Click on 'Sign In'
sign_in = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[2]/a[1]')
sign_in.click()
time.sleep(100)

# Enter email
# another=driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[5]/div/div/div[2]')
# another.click()
email_input = driver.find_element(By.XPATH, '//*[@id="handleOrEmail"]')
email_input.send_keys(EMAIL)

# Enter password
password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
password_input.send_keys(PASSWORD)
driver.find_element(By.XPATH,'//*[@id="enterForm"]/table/tbody/tr[4]/td/div[1]/input').click()
# password_input.send_keys(Keys.ENTER)
# time.sleep(5)


print("Logged in!")

# Close the browser
#driver.quit()
