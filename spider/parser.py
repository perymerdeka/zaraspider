import asyncio

from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from asynciolimiter import Limiter

class SiteParser(object):
    def __init__(self, driver: webdriver.Chrome):
        self.driver: webdriver.Chrome = driver
        self.rate_limiter = Limiter(1/5)

    async def get_products(self, url: str):
        await self.rate_limiter.wait()
        new_context = await self.driver.new_context()
        await new_context.get(url)
        schema = await new_context.find_element(By.CSS, "script[type='application/ld+json']")
        print(await schema.text)

        await new_context.close()

        
    
    async def parse_products(self):
        products = await self.driver.find_elements(By.CSS, "div.product-grid-product__figure")
        raise Exception(products)
        urls: list[str] = []
        for product in products:
            data = await product.find_element(By.CSS, "a")
            link = await data.get_attribute("href")
            urls.append(link)

        # using async to 
        tasks = [self.get_products(url) for url in urls]
        await asyncio.gather(*tasks)

