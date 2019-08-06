import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.careerguide.com/career-options")

soup = BeautifulSoup(response.text, "html.parser")

main_container = soup.select_one("div.c-body")
container = main_container.select("div.col-md-4")
# category_soup = soup.select("h2.c-font-bold")

print(len(container))

category_list = []
subcategory_list = []

for item in container:
    cat = item.select_one("h2.c-font-bold")
    cat_text = cat.select_one("a").get_text()

    sub_cat_soup = item.select_one("ul")
    sub_cat_list = []

    for x in sub_cat_soup:
        sub_cat_text = x.select_one("li a").get_text()
        sub_cat_link = x.select_one("li a").get("href")
        sub_cat_list.append({'text': sub_cat_text, 'link': sub_cat_link})

    category_list.append({'category': cat_text, 'sub_category': sub_cat_list})


print(len(category_list))
print(category_list)
