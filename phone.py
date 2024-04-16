from __future__ import annotations
import re

import requests
from bs4 import BeautifulSoup

# Загрузка содержимого страницы
url = "https://www.biocultura.org/expositor/150402/"
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг HTML с помощью BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    expositor_phone = soup.find(class_="expositor-contact").next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
    print(expositor_phone)