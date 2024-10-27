from playwright.sync_api import Page


class IntegrationsPage:
    def __init__(self, page: Page):
        self.page = page

        self.selectors = {
            "integration_nav": '//*[@id="root"]/div[1]/div/div/div[2]/nav/div[2]/div/button[7]',
            "integrations_div": '//span[contains(text(), "Available Integrations")]',
            "woocommerce": '//h3[contains(text(), "WooCommerce")]',
            "salla": '//h3[contains(text(), "Salla")]',
            "messenger": '//h3[contains(text(), "Messenger")]',
            "ig_feed": '//h3[contains(text(), "Instagram Feed")]',
            "store_continue": '[data-testid="button-element"]',
            "channel_next": '[data-testid="button-element"]:text("Next")',
            "channel_continue": '//button[contains(text(), "Connect With")]',
            "close_icon": "path[d='M6.28 5.22a.75.75 0 00-1.06 1.06L8.94 10l-3.72 3.72a.75.75 0 101.06 1.06L10 11.06l3.72 3.72a.75.75 0 101.06-1.06L11.06 10l3.72-3.72a.75.75 0 00-1.06-1.06L10 8.94 6.28 5.22z']",
            "close_toast": "path[d='M18 6 6 18']",
        }

    def goto_integrations(self):
        self.page.wait_for_selector(
            self.selectors["integration_nav"], state="visible"
        ).click()
        self.page.wait_for_selector(
            self.selectors["integrations_div"], state="visible"
        ).click()

    def goto_woocommerce(self):
        self.page.click(self.selectors["woocommerce"])
        self.page.wait_for_selector(
            self.selectors["store_continue"], state="visible"
        ).click()

        new_tab = self.page.context.wait_for_event("page")
        new_tab.wait_for_load_state("domcontentloaded")
        assert "https://wordpress.org/plugins/myaliceai/" in new_tab.url
        new_tab.close()
        self.page.locator(self.selectors["close_icon"]).click()

    def goto_salla(self):
        self.page.click(self.selectors["salla"])
        self.page.wait_for_selector(
            self.selectors["store_continue"], state="visible"
        ).click()
        self.page.locator(self.selectors["close_icon"]).click()
        self.page.wait_for_selector(self.selectors["close_toast"]).click()

    def goto_messenger(self):
        self.page.click(self.selectors["messenger"])
        self.page.wait_for_selector(
            self.selectors["channel_next"], state="visible"
        ).click()
        self.page.click(self.selectors["channel_continue"])

    def goto_ig_feed(self):
        self.page.click(self.selectors["ig_feed"])
        self.page.wait_for_selector(
            self.selectors["channel_next"], state="visible"
        ).click()
        # self.page.locator(self.selectors["close_icon"]).click()
