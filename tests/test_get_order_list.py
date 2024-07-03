import allure
import requests
from data import Data


class TestGetOrderList:
    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверка получения общего списка заказов, с получением статуса 200 и что список не пуст')
    def test_get_order_list(self):
        # Выполняем GET-запрос на указанный URL для получения общего списка заказов
        response = requests.get(Data.Url_create_order)
        # Проверяем, что код ответа от сервера равен 200 и что список не пуст
        assert response.status_code == 200 and response.json()["orders"] != []

