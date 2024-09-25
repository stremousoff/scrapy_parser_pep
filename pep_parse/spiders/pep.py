import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, NAME, START_URLS


class PepSpider(scrapy.Spider):
    name = NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response, **kwargs):
        for url in response.css('section#numerical-index a::attr(href)'):
            yield response.follow(url, self.parse_pep)

    @staticmethod
    def parse_pep(response):
        match = re.search(
            r'^PEP\s+(\d+)\s*–\s*(.*)',
            response.css('h1.page-title::text').get()
        )
        yield PepParseItem(
            number=match.group(1),
            name=match.group(2),
            status=response.css('dt:contains("Status") + dd abbr::text').get(),
        )
