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

    # Находим все теги <p> с классом "team-subtitle" на странице
    team_subtitles = soup.find_all("a", class_="red-button")

    # Выводим содержимое найденных тегов <p> с классом "team-subtitle"
    for subtitle in team_subtitles:
        print(subtitle.text.strip())
else:
    print(f"Ошибка при загрузке страницы: {response.status_code}")
