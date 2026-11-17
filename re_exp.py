# Импортируйте модуль для работы с регулярными выражениями.
import re

addresses = [
    (
        'Он проживал в городе Иваново на улице Наумова. '
        'Номер дома 125 был зеркальной копией его номера квартиры 521'
    ),
    'Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.',
]

for address in addresses:
    # Напишите регулярное выражение.
    pattern = (
        r'город\w* (?P<city>\w+).*?'
        r'улиц\w* (?P<street>\w+).*?'
        r'дом\w* (?P<house>\d+).*?'
        r'квартир\w* (?P<apartment>\d+)'
    )

    # Примените метод регулярных выражений, который
    # найдёт шаблон pattern в строке address.
    address_match = re.search(pattern=pattern, string=address)
    if address_match:
        city, street, house, apartment = address_match.groups()
        # Распечатайте названия городов и улиц, номера домов и квартир
        # из обеих строк.
        print(city, street, house, apartment)
