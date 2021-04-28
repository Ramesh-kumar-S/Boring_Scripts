import requests
from bs4 import BeautifulSoup
page=requests.get("https://www.google.com")
print(page.status)