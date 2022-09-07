import requests
from bs4 import BeautifulSoup
domen = "https://lenta.ru/"
response = requests.get(domen)
response.raise_for_status()

content = response.content

soup = BeautifulSoup(content, 'html.parser')
print(soup.title.text)


def get_news():
    return [
        item for item in list(
            map(
                lambda x: (x.text[:-5], x.text[-5:], domen+x["href"]),
                soup.find_all("a", {"class": "_topnews"})
            )
        )
    ]


if __name__ == "__main__":
    print("qwe")
