import asyncio

from spider.zara import ZaraSpider

if __name__ == "__main__":
    asyncio.run(ZaraSpider().run())