import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        links = response.css(
            "#numerical-index tbody tr td:nth-child(3) a::attr(href)"
        ).getall()
        for link in links:
            title = response.css(f'a[href="{link}"]::attr(title)').get()
            yield response.follow(
                link, callback=self.parse_pep, cb_kwargs={"title": title}
            )

    def parse_pep(self, response, title):
        title_parts = title.split(" – ", 1)
        if len(title_parts) != 2:
            title_parts = title.split(" - ", 1)

        number_part = title_parts[0]
        name = title_parts[1]
        number = number_part.split()[1]
        status = response.css("abbr::text").get()

        item = PepParseItem(number=int(number), name=name, status=status)
        yield item
