from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://bigtesty.ru/simulators/interview')
        await page.screenshot(path='screenshot/interwiew.png')
        await browser.close()


asyncio.run(main())