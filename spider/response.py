import asyncio
import os

from asynciolimiter import Limiter
from selenium_driverless import webdriver
from selenium_driverless.types.by import By

class Response(object):
    def __init__(self):
        self.proxy: str | None = None
        self.options = webdriver.ChromeOptions()
        self.base_url: str | None = None

    async def get(self, url: str):
        async with webdriver.Chrome(options=self.options) as driver:
            await driver.get(url, wait_load=True)

            # setting sleep
            await asyncio.sleep(10)

            return driver

