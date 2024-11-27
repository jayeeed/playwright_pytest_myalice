from playwright.sync_api import Page


class IntegratedPage:
    SELECTORS = {
        "integration_nav": '//*[@id="root"]/div[1]/div/div/div[2]/nav/div[2]/div/button[8]',
        "integrations_card": "//div[2]/div/div[2]/div/div",
        "three_dot": 'svg path[d="M3 10a1.5 1.5 0 113 0 1.5 1.5 0 01-3 0zM8.5 10a1.5 1.5 0 113 0 1.5 1.5 0 01-3 0zM15.5 8.5a1.5 1.5 0 100 3 1.5 1.5 0 000-3z"]',
        "integration_menu_delete": "//span[contains(text(), 'Delete')]",
        "integration_disconnect": '[data-testid="button-element"]:text("Disconnect")',
        "integration_delete": '[data-testid="button-element"]:text("Delete")',
    }

    def __init__(self, page: Page):
        self.page = page

    def goto_integrations(self):
        self.page.locator(self.SELECTORS["integration_nav"]).click()
        self.page.wait_for_timeout(3000)

    def delete_integrations(self):
        integration_boxes = self.page.locator(self.SELECTORS["integrations_card"]).all()

        for box in integration_boxes:
            if "Salla Livechat" in box.inner_text():
                self._delete_integration(box)
                break
        else:
            assert False, "No Salla integration found"

    def _delete_integration(self, box):
        box.locator(self.SELECTORS["three_dot"]).click()
        self.page.locator(self.SELECTORS["integration_menu_delete"]).click()
        self.page.locator(self.SELECTORS["integration_disconnect"]).click()
        box.locator(self.SELECTORS["three_dot"]).click()
        self.page.locator(self.SELECTORS["integration_menu_delete"]).click()
        self.page.get_by_placeholder("Type 'DELETE' Here").fill("delete")
        self.page.locator(self.SELECTORS["integration_delete"]).click()
