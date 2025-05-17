import requests
from bs4 import BeautifulSoup

def get_page_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()
