import requests
from bs4 import BeautifulSoup

html = """
<html>
<body>
    <h1> python web scriping</h1>
<body>
<html> """


soup = BeautifulSoup(html, "html.parser")
print(soup)

heading = soup.find("h1")
print(heading)
print(heading.text)

#exersise 2

html = """
<html>
<body>
    <p>Python</P>
    <p>Java</P>
    <p>C++</P>

<body>
<html> """

soup = BeautifulSoup(html, "html.parser")
print(soup)

paragraph = soup.find("p")
print(paragraph)
print(paragraph.text)

#exercise 3


html = """
<html>
<ul>
    <li>Python</li>
    <li>Java</li>
    <li>C#</li>
    <li>go</li>

<ul>
<html> 
"""


soup = BeautifulSoup(html, "html.parser")

items = soup.find_all("li")
for item in items:
    print(item.text)

#exercise 4

html = """

<a href ="https://google.com"> Google </a>
<a href ="https://github.com"> Github </a>
<a href ="https://python.org"> Python </a>
"""

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a")
for link in links:
    print(link["href"])



#exersice 5
html = """
<div class = "product"> iphone</div>
<div class = "product"> samusung</div>
<div class = "product"> pixel</div>


"""

soup = BeautifulSoup(html, "html.parser")

products = soup.find_all( class_="product")
for product in products:
    print(product.text)







response = requests.get("https://quotes.toscrape.com")


soup = BeautifulSoup(response.text, "html.parser")


quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    print("Quote:", text)
    print("Author:", author)
    print()




