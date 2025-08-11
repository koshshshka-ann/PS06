# Попробуй написать spider для нахождения всех источников освещения с сайта divan.ru
# Нужно взять название источника освещения, цену и ссылку

import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lightening = response.css('div.WdR1o')
        for light in lightening:
            yield {
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('div.q5Uds span::text').get(),
                'link': light.css('a').attrib['href']
            }