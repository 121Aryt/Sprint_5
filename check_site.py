import urllib.request

url = "https://stellarburgers.education-services.ru/"
try:
    response = urllib.request.urlopen(url, timeout=10)
    print(f"✅ Сайт доступен! Код ответа: {response.getcode()}")
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")