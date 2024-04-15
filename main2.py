from __future__ import annotations

import requests
from bs4 import BeautifulSoup


class ExpositorCollector:
    baseurl = "https://www.biocultura.org/"
    def __init__(self) -> None:
        self.expositors: list[str] = []

    def add_expositor_title(self, title: str) -> None:
        self.expositors.append(title)

    def get_expositor_titles(self, start_id: int, end_id: int, baseurl: str) -> None:
        for page_id in range(start_id, end_id + 1):
            response = requests.get(f"{baseurl}expositor/{page_id}/")
            soup = BeautifulSoup(response.content, "lxml")
            expositor_titles = soup.find_all("h2", class_="expositor-title")
            for title in expositor_titles:
                self.add_expositor_title(title.text.strip())

if __name__ == "__main__":
    collector = ExpositorCollector()
    collector.get_expositor_titles(start_id=150100, end_id=150110, baseurl=ExpositorCollector.baseurl)
    print(collector.expositors)
