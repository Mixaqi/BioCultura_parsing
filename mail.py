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
    team_subtitles = soup.find_all("p")

    # Проверяем наличие email в каждом теге <p> и выводим только те, где email есть
    for subtitle in team_subtitles:
        if "Email:" in subtitle.text.strip():
            print(subtitle.text.strip().split()[1])
else:
    print(f"Ошибка при загрузке страницы: {response.status_code}")
