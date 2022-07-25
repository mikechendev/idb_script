from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import schedule  # pip install schedule
import time

# Download chromedriver from https://chromedriver.chromium.org/downloads


def idbScript():
    driver = webdriver.Chrome(
        "../../chromedriver"
    )  # Point to directory where chromedriver is stored

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

    time.sleep(5)
    driver.find_element("xpath", "//*[contains(text(), 'Attendance')]").click()
    time.sleep(3)
    driver.find_element(
        "xpath", "//button[@class='sc-dnqmqq eZdSMY sc-jnlKLf kSIKvw']"
    ).click()
    driver.find_element(
        "xpath", "//button[@class='sc-dnqmqq eKQKYW sc-jnlKLf kdusnr']"
    ).click()

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

# options = webdriver.ChromeOptions()
# options.add_argument("--ignore-ssl-errors=yes")
# options.add_argument("--ignore-certificate-errors")
# driver = webdriver.Remote(
#     command_executor="http://localhost:4444/wd/hub", options=options
# )
