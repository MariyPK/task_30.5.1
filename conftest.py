import pytest
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver():
  driver = webdriver.Chrome()

   # Переходим на страницу авторизации
   driver.get('https://petfriends.skillfactory.ru/login')

   driver.maximize_window()
   yield

   driver.quit()


@pytest.fixture()
def go_to_my_pets():

   element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   driver.find_element_by_id('email').send_keys(valid_email)

   element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим пароль
   driver.find_element_by_id('pass').send_keys(valid_password)

   element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element_by_css_selector('button[type="submit"]').click()

   element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
   # Нажимаем на ссылку "Мои питомцы"
   driver.find_element_by_link_text("Мои питомцы").click()