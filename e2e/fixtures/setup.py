import pytest
from playwright.sync_api import sync_playwright


class PlaywrightManager:
    def __init__(self, headless: bool = False, no_viewport: bool = True):
        self.headless = headless
        self.no_viewport = no_viewport
        self.browser = None
        self.context = None

    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context(no_viewport=self.no_viewport)
        self.context.set_default_timeout(60000)
        return self.context.new_page()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.context.close()
        self.browser.close()
        self.playwright.stop()


@pytest.fixture(scope="function", autouse=True)
def browser_context():
    with PlaywrightManager() as page:
        yield page
