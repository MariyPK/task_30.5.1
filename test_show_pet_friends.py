import pytest
from settings import valid_email, valid_password

def test_show_pet_friends():
   '''Проверка карточек питомцев'''

   # Устанавливаем неявное ожидание
   driver.implicitly_wait(10)

   # Вводим email
   driver.find_element_by_id('email').send_keys(valid_email)

   # Вводим пароль
   driver.find_element_by_id('pass').send_keys(valid_password)

   # Нажимаем на кнопку входа в аккаунт
   driver.find_element_by_css_selector('button[type="submit"]').click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

   images = driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = driver.find_elements_by_css_selector('.card-deck .card-text')

   assert names[0].text != ''

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ',' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
