from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import webbrowser

# Download chromedriver from https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome("../chromedriver")
driver.get("https://www.interview-db.com/")
link = driver.find_element("link text", "Student Sign in with Github")
link.click()

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.NAME, "login"))).send_keys(
    ""
)  # enter your github username
wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(
    ""
)  # enter your github password
gh = wait.until(EC.element_to_be_clickable((By.NAME, "commit"))).click()

wait.until(EC.element_to_be_clickable)((By.XPATH, "//*[@id='react-tabs-2']")).click()
wait.until(EC.element_to_be_clickable)(
    (By.ID, "sc-dnqmqq eZdSMY sc-jnlKLf kSIKvw")
).click()
wait.until(EC.element_to_be_clickable)(
    (By.ID, "sc-dnqmqq eKQKYW sc-jnlKLf kdusnr")
).click()
