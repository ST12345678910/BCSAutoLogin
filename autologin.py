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
    driver = webdriver.Chrome(options=options, executable_path='/Users/shaun/Desktop/PythonTestProject/chromedriver')

    driver.get("https://bootcampspot.com/login")

    driver.find_element(By.ID, "emailAddress").send_keys(username)

    driver.find_element(By.ID, "password").send_keys(password)
    
    driver.find_element(By.CLASS_NAME, "btn-submit").click()

    WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    LoggedIn = driver.find_element(By.CLASS_NAME, "btn-submit")
    # LoggedIn = driver.find_element(By.CLASS_NAME, "virtualclassroom")
    if (LoggedIn):
        print("\033[;32mLogin Success\033[0m\n")
    else:
        print("test")


# schedule.every().day.at("09:15").do(AutoLoginBCS)
AutoLoginBCS()
# driver.close()