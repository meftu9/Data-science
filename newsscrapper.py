import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.thereporterethiopia.com"
response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})

soup = BeautifulSoup(response.text, "html.parser")

headlines = []

for article in soup.find_all("h4"):
	title = article.get_text(strip=True)

	if title:
		headlines.append({"title": title})
print ("collected", len(headlines))

df = pd.DataFrame(headlines)

df.to_csv("ethiopian_news.csv", index= False)
print(df.head())



url = "https://www.thereporterethiopia.com"
response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})

soup = BeautifulSoup(response.text, "html.parser")

data = []

for article in soup.find_all("h4"):
	link = article.find("a")

	if link:
		title = link.get_text(strip=True)
		href = link.get("href")

		data.append({"title":title,"url":href})
df =pd.DataFrame(data)
df.to_csv("ethiopian_news.csv", index=False)
print("saved:",len(df))






