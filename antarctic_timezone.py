from time import sleep

# Импортируйте библиотеку requests_cache.
import requests_cache

TIME_API_URL = 'http://worldtime.timezone.io/api/'
ITERATIONS_MAX_COUNT = 2
ITERATIONS_COUNT = 5

if __name__ == '__main__':
    # Создайте сессию, кеширующую результаты загрузки страниц.
    session = requests_cache.CachedSession()
    # Уточнение местоположения.
    vostok_url = TIME_API_URL + 'timezone/Antarctica/Vostok'
    # Загружаем текущее время станции "Восток" пять раз.
    data = None
    for iteration in range(ITERATIONS_COUNT):
        # После третьей загрузки — очистка кеша.
        if iteration > ITERATIONS_MAX_COUNT:
            # Очистите кеш.
            session.cache.clear()
        # Загрузите веб-страницу из переменной vostok_url,
        # используя созданную сессию.
        response = session.get(vostok_url)
        # Ответ от сервера приходит в формате JSON,
        # поэтому нужно преобразовать его методом .json(),
        # чтобы дальше работа велась с данными, как со словарём.
        data = response.json()
        # Получение текущего времени на станции "Восток".
        result = data.get('datetime')
        # Печать номера итерации и текущего времени.
        print(iteration, result)
        # Пауза на одну секуду.
        sleep(1)
    # Получение часового пояса.
    if data:
        utc_offset = data.get('utc_offset')
        # Печать часового пояса.
        print('Часовой пояс антарктической станции «Восток»:', utc_offset)
