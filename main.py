from platform import architecture

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

articles = []
article_texts = []
article_links = []


soup = BeautifulSoup(yc_web_page,"html.parser")
span_tag = soup.find_all(name="span", class_ = "titleline")
for span in span_tag:
    article = span.find_all(name="a")
    articles.append(article)

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.p)
# all_anchor_tags= soup.find_all(name="a")
# #print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)
