from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import schedule
import time

# Download chromedriver from https://chromedriver.chromium.org/downloads


def idbScript():
    options = Options()
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get("https://www.interview-db.com/")
    driver.find_element("link text", "Student Sign in with Github").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.NAME, "login"))).send_keys(
        ""
    )  # enter your github username
    wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(
        ""
    )  # enter your github password
    wait.until(EC.element_to_be_clickable((By.NAME, "commit"))).click()

    time.sleep(3)
    driver.find_element("xpath", "//*[contains(text(), 'Attendance')]").click()
    time.sleep(3)
    buttons = driver.find_elements(By.XPATH, "//button")
    for button in buttons:
        button.click()

    time.sleep(5)
    driver.quit()


# idbScript()

for i in ["09:50", "17:20"]:
    schedule.every().monday.at(i).do(idbScript)
    schedule.every().tuesday.at(i).do(idbScript)
    schedule.every().wednesday.at(i).do(idbScript)
    schedule.every().thursday.at(i).do(idbScript)
    schedule.every().friday.at(i).do(idbScript)

while True:
    schedule.run_pending()
    time.sleep(60)

# run with nohup python3 idbScript.py &
