import requests
from bs4 import BeautifulSoup


response = requests.get("https://lenta.ru/")
response.raise_for_status()

content = response.content

soup = BeautifulSoup(content, 'html.parser')
print(soup.title.text)


for item in list(map(lambda x: (x.text[:-5], x.text[-5:], x["href"]), soup.find_all("a", {"class": "_topnews"}))):
    print(item)


if __name__ == "__main__":
    print("qwe")
