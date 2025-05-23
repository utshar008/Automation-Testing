from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your credentials
EMAIL = "utshar21@gmail.com"
PASSWORD = "My Pass"

# Initialize the browser
driver = webdriver.Chrome()

# Open YouTube
driver.get("https://www.youtube.com/")
time.sleep(2)

# Click on 'Sign In'
sign_in = driver.find_element(By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]]')
sign_in.click()
time.sleep(3)

# Enter email
another=driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[5]/div/div/div[2]')
another.click()
email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_input.send_keys(EMAIL)
email_input.send_keys(Keys.ENTER)
time.sleep(3)

# Enter password
password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)
time.sleep(5)

# You should now be logged in (if no CAPTCHA or 2FA)
print("Logged in!")

# Close the browser
driver.quit()
