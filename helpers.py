from faker import Faker

faker = Faker()


def generate_login_courier():
    return faker.text(max_nb_chars=7) + str(faker.random_int(0, 999))


def generate_courier_pass():
    return faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)


def generate_courier_name():
    return faker.name()

