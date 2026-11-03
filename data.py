import random
import string


def generate_login():
    first_name = ''.join(random.choices(string.ascii_lowercase, k=6))
    last_name = ''.join(random.choices(string.ascii_lowercase, k=6))
    cohort = random.randint(1, 99)
    digits = ''.join(random.choices(string.digits, k=3))
    domain = random.choice(['yandex.ru', 'mail.ru', 'gmail.com'])
    return f"{first_name}_{last_name}_{cohort}_{digits}@{domain}"


def generate_password():
    length = random.randint(6, 12)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))