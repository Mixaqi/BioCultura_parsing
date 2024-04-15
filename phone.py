from __future__ import annotations

import requests
from bs4 import BeautifulSoup

# Загрузка содержимого страницы
url = "https://www.biocultura.org/expositor/150086/"
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг HTML с помощью BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Находим элемент с классом "expositor-contact" и извлекаем текст из всех тегов <p>
    # expositor_phone = soup.find(class_="expositor-contact").next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
    expositor_phone = soup.find(class_="expositor-contact").find_next_sibling()
    print(expositor_phone)
