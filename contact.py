from __future__ import annotations
import re
import requests
from bs4 import BeautifulSoup

# Загрузка содержимого страницы
url = "https://www.biocultura.org/expositor/150407/"
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг HTML с помощью BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Находим все теги <p> с классом "team-subtitle" на странице
    team_subtitles = soup.find_all("p")

    # Проверяем наличие контактной информации в каждом теге <p>
    for subtitle in team_subtitles:
        if "Contacto:" in subtitle.text.strip():
            # Получаем текст после слова "Contacto:"
            contact_text = subtitle.text.strip().split("Contacto:")[1].strip()

            # Извлекаем имя из текста контакта с помощью регулярного выражения
            name_match = re.match(r"^([^,\n]+)", contact_text)
            if name_match:
                name = name_match.group(1).strip()
            else:
                name = "Имя не найдено"

            print(name)
else:
    print(f"Ошибка при загрузке страницы: {response.status_code}")
