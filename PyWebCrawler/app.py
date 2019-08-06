import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.careerguide.com/career-options")

soup = BeautifulSoup(response.text, "html.parser")

container = soup.select("div.col-md-4")
category_soup = soup.select("h2.c-font-bold")

print(len(container))
print(len(category_soup))
print("heading: ", category_soup[0])
print("a tag inside heading: ", category_soup[0].select_one("a"))
print("text inside a tag: ", category_soup[0].select_one("a").get_text())

category_list = []

for item in category_soup:
    category_list.append(item.select_one('a').get_text())

print(category_list)
print(len(category_list))

subcategory_list = []
