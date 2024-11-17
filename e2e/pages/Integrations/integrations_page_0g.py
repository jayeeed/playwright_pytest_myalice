from playwright.sync_api import Page


class IntegrationsPage:
    def __init__(self, page: Page):
        self.page = page

        self.selectors = {
            "integration_nav": '//*[@id="root"]/div[1]/div/div/div[2]/nav/div[2]/div/button[7]',
            "integrations_div": '//span[contains(text(), "Available Integrations")]',
            ######### Integrations #########
            "woocommerce": '//h3[contains(text(), "WooCommerce")]',
            "shopify": '//h3[contains(text(), "Shopify")]',
            "salla": '//h3[contains(text(), "Salla")]',
            "zid": '//h3[contains(text(), "Zid")]',
            "fb_feed": '//h3[contains(text(), "Facebook Feed")]',
            "fb_chat": '//h3[contains(text(), "Messenger")]',
            "ig_feed": '//h3[contains(text(), "Instagram Feed")]',
            "ig_chat": '//h3[contains(text(), "Instagram Chat")]',
            "whatsapp": '//h3[contains(text(), "WhatsApp")]',
            "email": '//h3[contains(text(), "Email")]',
            "viber": '//h3[contains(text(), "Viber")]',
            "telegram": '//h3[contains(text(), "Telegram")]',
            "line": '//h3[contains(text(), "Line")]',
            "live_chat": '//h3[contains(text(), "Live Chat Plugin")]',
            "mobile_app": '//h3[contains(text(), "Mobile App Plugin")]',
            "wit": '//h3[contains(text(), "Wit.ai")]',
            "checkout": '//h3[contains(text(), "Checkout.com")]',
            "moengage": '//h3[contains(text(), "MoEngage")]',
            ######### Integrations #########
            "store_continue": '[data-testid="button-element"]',
            "channel_next": '[data-testid="button-element"]:text("Next")',
            "wa_next": '[data-testid="button-element"]:text("Connect Whatsapp")',
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

    def goto_woocommerce_shopify_zid(self, integration, url):
        self.page.click(self.selectors[integration])
        self.page.wait_for_selector(
            self.selectors["store_continue"], state="visible"
        ).click()

        new_tab = self.page.context.wait_for_event("page")
        new_tab.wait_for_load_state("domcontentloaded")
        assert url in new_tab.url
        new_tab.close()
        self.page.locator(self.selectors["close_icon"]).click()

    def goto_salla(self):
        self.page.click(self.selectors["salla"])
        self.page.wait_for_selector(
            self.selectors["store_continue"], state="visible"
        ).click()
        self.page.locator(self.selectors["close_icon"]).click()
        self.page.wait_for_selector(self.selectors["close_toast"]).click()

    def goto_meta(self, integration, url):
        parent_page = self.page
        parent_page.click(self.selectors[integration])

        if integration == "whatsapp":
            parent_page.wait_for_selector(
                self.selectors["wa_next"], state="visible"
            ).click()
        else:
            parent_page.wait_for_selector(
                self.selectors["channel_next"], state="visible"
            ).click()
            parent_page.click(self.selectors["channel_continue"])

        child_page = self.page.context.wait_for_event("page")
        child_page.wait_for_load_state("domcontentloaded")
        assert url in child_page.url
        child_page.close()
        self.page.locator(self.selectors["close_icon"]).click()
