from __future__ import annotations

import logging
import re

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


class Expositor:
    baseurl = "https://www.biocultura.org/"
    expositor_list: list[Expositor] = []

    def __init__(self, title: str, link: str, email: str, phone: str, contact_name: str, country: str) -> None:
        self.title = title
        self.link = link
        self.email = email
        self.phone = phone
        self.contact_name = contact_name
        self.country = country

    def __str__(self) -> str:
        return f"Expositor(title={self.title}, link={self.link}, email={self.email}, phone={self.phone}, contact_name={self.contact_name}, country={self.country})"

    @classmethod
    def get_expositor_data(cls, start_id: int, end_id: int) -> None:
        cls.expositor_list = []

        logging.basicConfig(filename="expositor.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

        for page_id in range(start_id, end_id + 1):
            try:
                response = requests.get(f"{cls.baseurl}expositor/{page_id}/")
                response.raise_for_status()
            except requests.HTTPError as e:
                logging.exception(f"Error fetching page {page_id}: {e}")
                continue

            soup = BeautifulSoup(response.content, "lxml")
            expositor_titles = soup.find_all("h2", class_="expositor-title")
            expositor_links = soup.find_all("a", class_="red-button")
            expositor_emails = soup.find_all("p")

            expositor_contact = soup.find(class_="expositor-contact")
            country = expositor_contact.find_all("p")[-1].text.strip()

            for email in expositor_emails:
                if "Email:" in email.text.strip():
                    email_parts = email.text.strip().split()
                    email = email_parts[1] if len(email_parts) > 1 else ""
                    break
            else:
                email = ""

            expositor_contact_text = expositor_contact.text
            phone_match = re.search(r"Teléfono:\s*(\+?\d[\d\s()-]*)", expositor_contact_text)
            phone = phone_match.group(1).strip() if phone_match else ""

            for title, link in zip(expositor_titles, expositor_links):
                contact_text = expositor_contact_text.strip()
                name_match = re.search(r"Contacto:\s*(.+)", contact_text)
                name = name_match.group(1).strip() if name_match else ""

                expositor = cls(title=title.text.strip(), link=link["href"], email=email, phone=phone, contact_name=name, country=country)
                cls.expositor_list.append(expositor)

    @classmethod
    def write_to_excel(cls, filename: str) -> None:
        wb = Workbook()
        ws = wb.active

        headers = ["Title", "Link", "Email", "Phone", "Contact Name", "Country"]
        ws.append(headers)

        for expositor in cls.expositor_list:
            row = [expositor.title, expositor.link, expositor.email, expositor.phone, expositor.contact_name, expositor.country]
            ws.append(row)

        for col in ws.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            ws.column_dimensions[column].width = adjusted_width

        wb.save(filename)

if __name__ == "__main__":
    Expositor.get_expositor_data(start_id=150318, end_id=150600)
    Expositor.write_to_excel("expositors.xlsx")
