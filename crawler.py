from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Crawler:
    def __init__(self, headless=False):
        op = Options()
        op.headless = headless
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver.exe', options=op)

    def get_url_content(self, driver, url, css_selector):
        driver.get(url)
        return driver.find_element_by_css_selector(css_selector)

    def get_itens_page_by_tag_name(self, content, tag_name):
        return content.find_elements_by_tag_name(tag_name)

    def get_item_page_by_css_seletor(self, content, css_seletor):
        return content.find_element_by_css_selector(css_seletor)

    def get_last_page(self, content, css_selector):
        pages = content.find_elements_by_css_selector(css_selector)
        return int(pages[len(pages)-1].text)

    def shutdown(self, driver):
        driver.close()
