## radtest

Стандартный radtest (freeradius) не дает возможности задавать дополнительные атрибуты, поэтому создан этот небольшой сервис сугубо для тестирования iptv radius серверов. Сервис через **GET** получает **mac** адрес абонента, **ip** адрес видео канала подписки. Возвращает при успешном запросе **True**, при отказе **False**. При внутренней ошибки (например, не доступен radius сервер) **Error**. Параметры **RADIUS_HOST** и **RADIUS_SECRET** передаются как переменные окружения при создании контейнера.


**gunicorn**

Пример:

```
gunicorn -b 0.0.0.0:8080 -w 10 --pythonpath src radtest:app

```

**Тестирование с использованием curl :**

Передаются mac адрес и ip адрес

```
curl -X GET http://127.0.0.1:8080/90E6BA8B16C5/239.1.21.3
Error

```