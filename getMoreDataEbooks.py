import json
from crawler import Crawler

with open('ebooks.json') as json_file:
    ebooks = json.load(json_file)

ebook = ebooks[list(ebooks.keys())[0]]

print(ebook['url'])

crawler = Crawler()

page_content = crawler.get_url_content(
    crawler.driver, ebook['url'], 'div.main-content-inner')


crawler.shutdown(crawler.driver)
