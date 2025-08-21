# import scrapy
#
#
# class LightnewparsSpider(scrapy.Spider):
#     name = "lightnewpars"
#     allowed_domains = ["https://www.lampadia.ru"]
#     start_urls = ["https://www.lampadia.ru/catalog/svetilniki/"]
#
#     def parse(self, response):
#         lightening = response.css('div.product-item')
#         for light in lightening:
#             yield {
#                 'name': light.css('div.product-item-title a::text').get().strip(),
#                 'price': light.css('div.product-item-price-container span::text').get().strip(),
#                 'link': light.css('a').attrib['href']
#             }


import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = "https://www.lampadia.ru/catalog/svetilniki/"

driver.get(url)

time.sleep(3)

lights = driver.find_elements(By.CLASS_NAME, 'product-item')

print(lights)

parsed_data = []

for light in lights:
    try:
        title = light.find_element(By.CSS_SELECTOR, 'div.product-item-title a').text
        price = light.find_element(By.CSS_SELECTOR, 'span.product-item-price-current').text
        link = light.find_element(By.CSS_SELECTOR, 'div.product-item-title a').get_attribute('href')

    except:
        print("произошла ошибка при парсинге")
        continue

    parsed_data.append([title, price, link])

driver.quit()

with open("lights.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'Цена', 'Ссылка на продукт'])
    writer.writerows(parsed_data)

    writer = csv.writer(file)

    writer.writerow(['Название продукта', 'Цена', 'Ссылка на продукт'])
    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)