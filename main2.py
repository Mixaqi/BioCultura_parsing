from __future__ import annotations

from typing import List

import requests
from bs4 import BeautifulSoup


class Expositor:
    baseurl = "https://www.biocultura.org/"
    expositor_list: list[Expositor] = []

    def __init__(self, link: str, title: str, phone: str) -> None:
        self.link = link
        self.title = title
        self.phone = phone

    def __str__(self) -> str:
        return f"Expositor(link={self.link}, title={self.title}, phone={self.phone})"

    @classmethod
    def get_expositor_titles(cls, start_id: int, end_id: int) -> None:
        cls.expositor_list = []  # Clear the list before populating it again

        for page_id in range(start_id, end_id + 1):
            response = requests.get(f"{cls.baseurl}expositor/{page_id}/")
            soup = BeautifulSoup(response.content, "lxml")
            expositor_titles = soup.find_all("h2", class_="expositor-title")

            for title in expositor_titles:
                expositor = cls(link="https://www.example.com", title=title.text.strip(), phone="123-456-7890")
                cls.expositor_list.append(expositor)

if __name__ == "__main__":
    Expositor.get_expositor_titles(start_id=150100, end_id=150110)
    for expositor in Expositor.expositor_list:
        print(expositor)
