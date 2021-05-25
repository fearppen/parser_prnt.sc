from random import randint
from bs4 import BeautifulSoup
import cloudscraper
import requests


def create_name_page():
    name = ""
    for i in range(5):
        name += chr(randint(97, 122))
    name += str(randint(0, 9))

    return name


def get_html(name):
    page = "https://prnt.sc/" + name
    print(page)
    scraper = cloudscraper.create_scraper()
    return scraper.get(page).text


def parse_html_page(html):
    soup = BeautifulSoup(html, "html.parser")
    string = soup.find_all("img", alt="Lightshot screenshot")
    return string[0]["src"]


def save_image(url, name_file):
    response = requests.get(url).iter_content()
    with open(f"{name_file}.jpg", "wb") as file:
        for i in response:
            file.write(i)


if __name__ == '__main__':
    while True:
        name = create_name_page()
        save_image(parse_html_page(get_html(name)), name)
