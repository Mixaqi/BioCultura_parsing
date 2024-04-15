from bs4 import BeautifulSoup

# Пример HTML-кода с информацией о контакте экспонента
html_content = """
<div class="expositor-contact">
    <p>
        <span>Email:</span>
        example@email.com
    </p>
</div>
"""

# Создание объекта BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html_content, "html.parser")

# Находим тег <div> с классом "expositor-contact"
expositor_contact = soup.find("div", class_="expositor-contact")

# Если тег <div> с классом "expositor-contact" найден, извлекаем электронную почту
if expositor_contact:
    email_span = expositor_contact.find("span", text="Email:")
    if email_span:
        email = email_span.find_next_sibling("p").get_text(strip=True)
        print("Email:", email)
    else:
        print("Email не найден.")
else:
    print("Тег <div class='expositor-contact'> не найден.")