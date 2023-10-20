from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8080/#/dashboard")
    page.get_by_label("帳號").click()
    page.get_by_label("帳號").fill("shang112522105")
    page.get_by_label("帳號").press("Tab")
    page.locator("#password").fill("112522105")
    page.get_by_role("button", name="登入").click()

    # ---------------------
    context.close()
    browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
