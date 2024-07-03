class Data:
    login = 'ninja'
    password = '1234'
    name = 'saske'
    courier = {'login': 'ninja', 'password': '1234', 'name': 'saske'}
    wrong_name_courier = {'login': 'ninja', 'password': '1234'}
    wrong_password = {'login': 'ninja', 'password': '123456789'}

    Url_main_page = 'https://qa-scooter.praktikum-services.ru/'
    Url_create_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    Url_create_login = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    Url_create_order = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'


class OrderDate:
    order_data_scooter_black = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 3,
        "phone": "+7 800 355 35 35",
        "rentTime": '1',
        "deliveryDate": '05-07-2024',
        "comment": "Saske, come back to Konoha",
        "color": [
            'BLACK'
        ]
    }

    order_data_scooter_grey = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 3,
        "phone": "+7 800 355 35 35",
        "rentTime": '1',
        "deliveryDate": '06-07-2024',
        "comment": "Saske, come back to Konoha",
        "color": [
            'GREY'
        ]
    }

    order_data_scooter_grey_and_black = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 3,
        "phone": "+7 800 355 35 35",
        "rentTime": '1',
        "deliveryDate": '07-07-2024',
        "comment": "Saske, come back to Konoha",
        "color": [
            'BLACK',
            'GREY'
        ]
    }

    order_data_scooter_no_color = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 3,
        "phone": "+7 800 355 35 35",
        "rentTime": '1',
        "deliveryDate": '08-07-2024',
        "comment": "Saske, come back to Konoha",
        "color": []
    }


class ResponseText:
    create_courier = '{"ok":true}'
    double_login_courier = 'Этот логин уже используется. Попробуйте другой.'
    missing_field = 'Недостаточно данных для создания учетной записи'
    not_login_courier = 'Недостаточно данных для входа'
    not_password_courier = 'Недостаточно данных для входа'
    invalid_login_error = 'Учетная запись не найдена'

