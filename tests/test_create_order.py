import allure
import pytest
import requests
from data import OrderDate, Data
import json


class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @allure.description('Проверка создания заказа с указанием любого цвета')
    @pytest.mark.parametrize('color',
                             [
                                 OrderDate.order_data_scooter_black,
                                 OrderDate.order_data_scooter_grey,
                                 OrderDate.order_data_scooter_grey_and_black,
                                 OrderDate.order_data_scooter_no_color
                             ]
                             )
    def test_create_order_with_color(self, color):
        # Преобразовываем данные о цвете заказа в формат JSON с помощью функции json.dumps
        order_data = json.dumps(color)
        # Выполняем POST-запрос на указанный URL с данными о заказе
        response = requests.post(Data.Url_create_order, data=order_data)
        # Проверяем, что код ответа от сервера равен 201 (Created) и что в тексте ответа есть слово 'track'
        assert response.status_code == 201, 'track' in response.text
