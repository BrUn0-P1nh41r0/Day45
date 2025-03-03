import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

top100 = []

response = requests.get(URL)
ar_web_page = response.text

soup = BeautifulSoup(ar_web_page, "html.parser")
h3s = soup.find_all(name = "h3", class_="title")
for title in h3s:
    titles = title.getText()
    top100.append(titles)
reverse_top100 = top100[:: -1]
print(reverse_top100)

with open ("Top100_Movies.txt", "w") as file:
    for movie in reverse_top100:
        file.write(f"{movie}\n")