from __future__ import annotations

import requests
from bs4 import BeautifulSoup


class Expositor:
    baseurl = "https://www.biocultura.org/"
    expositor_list: list[Expositor] = []

    def __init__(self, title: str, link: str, email: str) -> None:
        self.title = title
        self.link = link
        self.email = email

    def __str__(self) -> str:
        return f"Expositor(title={self.title}, link={self.link}, email={self.email})"

    @classmethod
    def get_expositor_data(cls, start_id: int, end_id: int) -> None:
        cls.expositor_list = []

        for page_id in range(start_id, end_id + 1):
            response = requests.get(f"{cls.baseurl}expositor/{page_id}/")
            soup = BeautifulSoup(response.content, "lxml")
            expositor_titles = soup.find_all("h2", class_="expositor-title")
            expositor_links = soup.find_all("a", class_="red-button")
            expositor_emails = soup.find_all("p")

            for email in expositor_emails:
                if "Email:" in email.text.strip():
                    email = email.text.strip().split()[1]
                    break
            else:
                email = ""

            for title, link in zip(expositor_titles, expositor_links):
                expositor = cls(title=title.text.strip(), link=link["href"], email=email)
                cls.expositor_list.append(expositor)


if __name__ == "__main__":
    Expositor.get_expositor_data(start_id=150100, end_id=150105)
    for expositor in Expositor.expositor_list:
        print(expositor)
