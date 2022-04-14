from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from logging import error
from selenium import webdriver
import schedule
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


username = "yourusername"
password = "yourpassword"


def AutoLoginBCS():
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    driver.get("https://bootcampspot.com/login")

    driver.find_element(By.ID, "emailAddress").send_keys(username)

    driver.find_element(By.ID, "password").send_keys(password)
    
    driver.find_element(By.CLASS_NAME, "btn-submit").click()

    WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    print("\033[;32mLogging In...\033[0m\n")


    driver.implicitly_wait(10)

    driver.find_element(By.LINK_TEXT, "JOIN CLASS").click()
    print("\033[;32mJoining Meeting...\033[0m\n")

schedule.every().day.at("09:15").do(AutoLoginBCS)

# AutoLoginBCS()
