from random import randint
from bs4 import BeautifulSoup
from threading import Thread
import cloudscraper
import requests
import os


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
    try:
        with open(f"{os.getcwd()}/images/{name_file}.jpg", "wb") as file:
            for i in response:
                file.write(i)
    except:
        os.mkdir(os.getcwd() + "/images/")
        with open(f"{os.getcwd()}/images/{name_file}.jpg", "wb") as file:
            for i in response:
                file.write(i)


def main():
    while True:
        random_name = create_name_page()
        save_image(parse_html_page(get_html(random_name)), random_name)


for i in range(4):
    thread = Thread(target=main(), args=(i,))
    thread.start()
