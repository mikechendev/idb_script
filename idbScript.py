from selenium import webdriver
import webbrowser

driver = webdriver.Chrome()
driver.get("https://www.interview-db.com/")
gbutton = driver.find_element_by_id("fa fa-github")
gbutton.click()
button = driver.find_element_by_id("sc-dnqmqq eZdSMY sc-jnlKLf kSIKvw")
button.click()
button2 = driver.find_element_by_id("sc-dnqmqq eKQKYW sc-jnlKLf kdusnr")
button2.click()
