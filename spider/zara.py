import asyncio
from spider.parser import SiteParser
from spider.response import Response


class ZaraSpider(object):
    def __init__(self):
        self.products = []
        self.response = Response()

    async def run(self):
        driver = await self.response.get("https://www.zara.com/id/en/man-new-in-collection-l6164.html?v1=2431921")
        parser = SiteParser(driver=driver)
        products =  await parser.parse_products()
        print(products)




