from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

op = Options()
op.headless = False

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=op)

url_base = 'http://www.allitebooks.org/'

# driver.get(url)
css_selector_content = 'div.main-content-inner'
css_selector_paginator = 'div.pagination a'
tag_name = 'article'
ebooks = {}


def get_url_content(driver, url, css_selector):
    driver.get(url)
    return driver.find_element_by_css_selector(css_selector)


def get_itens_page(content, tag_name):
    return content.find_elements_by_tag_name(tag_name)


def get_last_page(content, css_selector):
    pages = content.find_elements_by_css_selector(css_selector_paginator)
    return int(pages[len(pages)-1].text)


def shutdown(driver=driver):
    driver.close()


last_page = 1
i = 1

while(i <= last_page):
    url = url_base + 'page/' + str(i)
    content = get_url_content(driver, url, css_selector_content)
    itens = get_itens_page(content, tag_name)

    if (last_page == 1):
        last_page = get_last_page(content, css_selector_paginator)

    for item in itens:
        ebook = {'id': item.get_attribute('id'),
                 'url': item.find_element_by_css_selector(
            'div.entry-thumbnail a').get_attribute('href'),
            'capa': item.find_element_by_css_selector(
            'div.entry-thumbnail img').get_attribute('src'),
            'autor': item.find_element_by_css_selector(
            'div.entry-body a').text,
            'resumo': item.find_element_by_css_selector(
            'div.entry-summary p').text,
            'fonte': url_base, }
        ebooks[ebook['id']] = ebook

    print('Page: {}/{}'.format(i, last_page))
    i = i + 1
    time.sleep(5)

shutdown(driver)

filename = 'ebooks.json'
if filename:
    with open(filename, 'w') as f:
        json.dump(ebooks, f)


"""
ebooks = {}

for item in ebooks_html:

    ebook = {'id': item.get_attribute('id'),
             'url': item.find_element_by_css_selector(
        'div.entry-thumbnail a').get_attribute('href'),
        'capa': item.find_element_by_css_selector(
        'div.entry-thumbnail img').get_attribute('src'),
        'autor': item.find_element_by_css_selector(
        'div.entry-body a').text,
        'resumo': item.find_element_by_css_selector(
        'div.entry-summary p').text, }

    ebooks[ebook['id']] = ebook
    break
"""
# driver.close()

# print(ebooks)
