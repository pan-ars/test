from selenium import webdriver
from selenium.webdriver.chrome.service import Service as СhromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--window-size=1920,800")
options.add_argument("--headless")

driver = webdriver.chrome.webdriver.WebDriver(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.implicitly_wait(10)

# Константы
URL = "https://www.saucedemo.com/"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"

driver.get(URL)

# Заполнение полей логина и пароля
input_login = driver.find_element(By.ID, "user-name")
input_password = driver.find_element(By.ID, "password")
input_login.send_keys(LOGIN)
input_password.send_keys(PASSWORD)

# Нажатие кнопки логина
login_page_button = driver.find_element(By.ID, "login-button")
login_page_button.click()

driver.quit()
