from __future__ import annotations

from typing import Optional

import requests
from bs4 import BeautifulSoup


def parse_page(url: str) -> Optional[list[str]]:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        expositor_titles = soup.find_all("h2", class_="expositor-title")
        web_site_links = soup.find_all("a", class_="red-button")
        titles_list = [title.text.strip() for title in expositor_titles]
        links_list = [link["href"] for link in web_site_links]
        return titles_list, links_list
    else:
        print(f"Ошибка при загрузке страницы: {response.status_code}")
        return None

def print_titles_and_links(url: str, titles_list: list[str], links_list: list[str]) -> None:
    if titles_list and links_list:
        print(f"Данные на странице {url}:")
        for title, link in zip(titles_list, links_list):
            print(f"Название: {title}, Ссылка: {link}")
        print("\n")

if __name__ == "__main__":
    base_url = "https://www.biocultura.org/expositor/"
    for page_id in range(150100, 151000):
        url = f"{base_url}{page_id}/"
        titles_list, links_list = parse_page(url)
        if titles_list and links_list:
            print_titles_and_links(url, titles_list, links_list)


