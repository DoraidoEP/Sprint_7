import allure
import requests
from data import Data, ResponseText
from helpers import generate_login_courier, generate_courier_pass, generate_courier_name


class TestLoginCourier:
    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Создание и вход на аккаунт курьера, с получением статуса запроса и id курьера')
    def test_login_courier_success(self):
        courier_data = {'login': generate_login_courier(),
                        'password': generate_courier_pass(),
                        'name': generate_courier_name()
                        }
        # Отправляем POST-запрос на указанный URL с данными о логине, пароле и имени курьера с последующей авторизацией
        requests.post(Data.Url_create_courier, data=courier_data)
        response = requests.post(Data.Url_create_login, data=courier_data)
        # Проверяем, что статус ответа равен 200 и с указанием id курьера в теле ответа
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка авторизации курьера без заполненного поля login')
    @allure.description(
        'Проверка авторизации курьера без заполненного поля login, с получением статуса запроса 400 и текста ошибки')
    def test_login_courier_empty_login_field_error(self):
        courier_data = {'login': '',
                        'password': generate_courier_pass(),
                        'name': generate_courier_name()
                        }
        # Отправляем POST-запрос на указанный URL с данными о пароле и имени курьера с последующей авторизацией
        response = requests.post(Data.Url_create_login, data=courier_data)
        # Проверяем, что статус ответа равен 400 и что текст ответа 'Недостаточно данных для входа'
        assert response.status_code == 400 and response.json()['message'] == ResponseText.not_login_courier

    @allure.title('Проверка авторизации курьера без заполненного поля password')
    @allure.description(
        'Проверка авторизации курьера без заполненного поля password, с получением статуса запроса 400 и текста ошибки')
    def test_login_courier_empty_pass_field_error(self):
        courier_data = {'login': generate_login_courier(),
                        'password': '',
                        'name': generate_courier_name()
                        }
        # Отправляем POST-запрос на указанный URL с данными о логине и имени курьера с последующей авторизацией
        response = requests.post(Data.Url_create_login, data=courier_data)
        # Проверяем, что статус ответа равен 400 и что текст ответа 'Недостаточно данных для входа'
        assert response.status_code == 400 and response.json()['message'] == ResponseText.not_password_courier

    @allure.title('Проверка авторизации, отсутствующем в базе данных, курьером ')
    @allure.description(
        'Проверка авторизации, отсутствующем в базе данных, курьером , с получением статуса запроса 400 и текста ошибки')
    def test_login_courier_invalid_courier_error(self):
        courier_data = {'login': Data.wrong_name_courier,
                        'password': generate_courier_pass(),
                        'name': generate_courier_name()
                        }
        # Отправляем POST-запрос на указанный URL с данными о логине, пароле и имени курьера с последующей авторизацией
        response = requests.post(Data.Url_create_login, data=courier_data)
        # Проверяем, что статус ответа равен 404 и что текст ответа 'Учетная запись не найдена'
        assert response.status_code == 404, response.json()['message'] == ResponseText.invalid_login_error

    @allure.title('Проверка авторизации курьера с неверным паролем')
    @allure.description(
        'Проверка авторизации курьера с неверным паролем, с получением статуса запроса 404 и теста ошибки')
    def test_login_courier_invalid_login_error(self):
        courier_data = {'login': generate_login_courier(),
                        'password': Data.wrong_password,
                        'name': generate_courier_name()
                        }
        # Отправляем POST-запрос на указанный URL с данными о логине, пароле и имени курьера с последующей авторизацией
        response = requests.post(Data.Url_create_login, data=courier_data)
        # Проверяем, что статус ответа равен 404 и что текст ответа 'Учетная запись не найдена'
        assert response.status_code == 404, response.json()['message'] == ResponseText.invalid_login_error

