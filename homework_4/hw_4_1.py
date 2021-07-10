from lxml import html
import requests

news = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = "https://news.mail.ru/"
response = requests.get(url, headers=headers)
dom = html.fromstring(response.text)

news_links = dom.xpath('//li[@class = "list__item"]')
news_text = dom.xpath('//li[@class = "list__item"]/text()')

for i in range(len(news_text)):
    news_text[i] = news_text[i].replace(u'\xa0', u' ')

print(news_links)
print(news_text)
