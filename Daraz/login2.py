from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

user = "0175045454"
password = "*******"
url = "https://www.daraz.com.bd"

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get(url)
    wait = WebDriverWait(driver, 15)

    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[4]/a'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/input'))).send_keys(user)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/input'))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div/div/div/div/div[2]/div/div[2]/button/div'))).click()

    time.sleep(5)
    wait.until(EC.presence_of_element_located((By.XPATH, '\html')))
    print("Login successful!")

except Exception as e:
    print(" Login failed or error occurred.")
    print("Error details:", str(e))

finally:
    input("Press Enter to close the browser...")
    driver.quit()
