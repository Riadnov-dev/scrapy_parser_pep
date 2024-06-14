import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        links = response.css(
            'a[class="pep reference internal"]::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css(".page-title::text").get()
        number = title.split(" ")[1]
        name = " ".join(title.split(" ")[3:])
        status = response.css("abbr::text").get()

        item = PepParseItem(number=number, name=name, status=status)
        yield item
