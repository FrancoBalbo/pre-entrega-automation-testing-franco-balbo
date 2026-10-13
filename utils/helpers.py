from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"


def login(driver, username="standard_user", password="secret_sauce"):

    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    username_input = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )

    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button.click()

    wait.until(
        EC.url_contains("/inventory.html")
    )