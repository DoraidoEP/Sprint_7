import allure
import requests
from data import Data, ResponseText
from helpers import generate_login_courier, generate_courier_pass, generate_courier_name


class TestCreateCourier:
    @allure.title('Проверка создания нового курьера')
    @allure.description('Создание курьера и проверка, что запрос возвращает статус 201')
    def test_create_courier(self):
        courier_data = {'login': generate_login_courier(),
                        'password': generate_courier_pass(),
                        'name': generate_courier_name()
                        }
        # Отправляем POST-запрос на указанный URL с данными о логине, пароле и имени курьера
        response = requests.post(Data.Url_create_courier, data=courier_data)
        # Проверяем, что статус ответа равен 201 и что текст ответа '{"ok":true}'
        assert response.status_code == 201, response.json == ResponseText.create_courier

    @allure.title('Проверка того, что нельзя создать двух курьеров с одинаковым логином')
    @allure.description('Отправка двух запросов на создание курьера с одинаковыми данными')
    def test_create_courier_double_login_not_created(self):
        courier_data = {'login': Data.login,
                        'password': generate_courier_pass(),
                        'name': generate_courier_name
                        }
        # Отправляем два запроса на создание курьера с одинаковыми данными
        requests.post(Data.Url_create_courier, data=courier_data)
        response = requests.post(Data.Url_create_courier, data=courier_data)
        # Проверяем, что статус ответа равен 409 и что текст ответа 'Этот логин уже используется. Попробуйте другой.'
        assert response.status_code == 409, response.json()['message'] == ResponseText.double_login_courier

    @allure.title('Проверка создания нового курьера без обязательного поля')
    @allure.description('Отправка запроса на создание курьера без заполненного поля "Пароль"')
    def test_create_courier_missing_field_error(self):
        courier_data = {'login': generate_login_courier(),
                        'name': generate_courier_name()
                        }
        # Отправляем запрос на создание курьера без заполненного поля "Пароль"
        response = requests.post(Data.Url_create_courier, data=courier_data)
        # Проверяем, что статус ответа равен 400 и что текст ответа 'Недостаточно данных для создания учетной записи'
        assert response.status_code == 400 and response.json()['message'] == ResponseText.missing_field

