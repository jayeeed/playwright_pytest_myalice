from playwright.sync_api import Page


class IntegrationsPage:
    SELECTORS = {
        "integration_nav": '//*[@id="root"]/div[1]/div/div/div[2]/nav/div[2]/div/button[7]',
        "integrations_div": 'text="Available Integrations"',
        ################################################
        "woocommerce": 'h3:text("WooCommerce")',
        "shopify": 'h3:text("Shopify")',
        "salla": 'h3:text("Salla")',
        "zid": 'h3:text("Zid")',
        "fb_feed": 'h3:text("Facebook Feed")',
        "fb_chat": 'h3:text("Messenger")',
        "ig_feed": 'h3:text("Instagram Feed")',
        "ig_chat": 'h3:text("Instagram Chat")',
        "whatsapp": 'h3:text("WhatsApp")',
        "email": 'h3:text("Email")',
        "viber": 'h3:text("Viber")',
        "telegram": 'h3:text("Telegram")',
        "line": 'h3:text("Line")',
        "live_chat": 'h3:text("Live Chat Plugin")',
        "mobile_app": 'h3:text("Mobile App Plugin")',
        "wit": 'h3:text("Wit.ai")',
        "checkout": 'h3:text("Checkout.com")',
        "moengage": 'h3:text("MoEngage")',
        ################################################
        "store_continue": '[data-testid="button-element"]',
        "channel_next": '[data-testid="button-element"]:text("Next")',
        "wa_next": '[data-testid="button-element"]:text("Connect Whatsapp")',
        "channel_continue": 'button:text("Connect With")',
        "close_icon": 'svg path[d="M6.28 5.22a.75.75 0 00-1.06 1.06L8.94 10l-3.72 3.72a.75.75 0 101.06 1.06L10 11.06l3.72 3.72a.75.75 0 101.06-1.06L11.06 10l3.72-3.72a.75.75 0 00-1.06-1.06L10 8.94 6.28 5.22z"]',
        "close_toast": 'svg path[d="M18 6 6 18"]',
    }

    def __init__(self, page: Page):
        self.page = page

    def goto_integrations(self):
        self.page.locator(self.SELECTORS["integration_nav"]).click()
        self.page.locator(self.SELECTORS["integrations_div"]).click()

    def goto_woocommerce_shopify_zid(self, integration, url):
        self.page.locator(self.SELECTORS[integration]).click()
        self.page.locator(self.SELECTORS["store_continue"]).click()

        new_tab = self.page.context.wait_for_event("page")
        new_tab.wait_for_load_state("domcontentloaded")
        assert url in new_tab.url
        new_tab.close()
        self.page.locator(self.SELECTORS["close_icon"]).click()

    def goto_salla(self):
        self.page.locator(self.SELECTORS["salla"]).click()
        self.page.locator(self.SELECTORS["store_continue"]).click()
        self.page.locator(self.SELECTORS["close_icon"]).click()
        self.page.locator(self.SELECTORS["close_toast"]).click()

    def goto_meta(self, integration, url):
        self.page.locator(self.SELECTORS[integration]).click()

        if integration == "whatsapp":
            self.page.locator(self.SELECTORS["wa_next"]).click()
        else:
            self.page.locator(self.SELECTORS["channel_next"]).click()
            self.page.locator(self.SELECTORS["channel_continue"]).click()

        child_page = self.page.context.wait_for_event("page")
        child_page.wait_for_load_state("domcontentloaded")
        assert url in child_page.url
        child_page.close()
        self.page.locator(self.SELECTORS["close_icon"]).click()
