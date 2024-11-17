import allure
from tests.base_test import login
from pages.integrations.integrations_page import IntegrationsPage
from utils.config_loader import load_config


@allure.feature("Integrations Functionality")
@allure.story("User integrates with stores")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://your_project_tracking_url", name="Project Tracking Link")
@allure.description("This test verifies that the user can integrate with stores.")
def test_integrations(browser_context):
    page = browser_context

    with allure.step("Log in to the application"):
        login(page)

    with allure.step("Load configuration and navigate to integrations"):
        config = load_config()
        meta_url = config["meta_url"]
        woocommerce_url = config["woocommerce_url"]
        shopify_url = config["shopify_url"]
        zid_url = config["zid_url"]

        integrations_page = IntegrationsPage(page)
        integrations_page.goto_integrations()

    with allure.step("Verify E-COMMERCE integrations"):
        integrations = {
            "woocommerce": woocommerce_url,
            "shopify": shopify_url,
            "zid": zid_url,
        }
        for integration, url in integrations.items():
            with allure.step(f"Verify {integration} integration"):
                integrations_page.goto_woocommerce_shopify_zid(integration, url)

        with allure.step("Verify Salla integrations"):
            integrations_page.goto_salla()

    with allure.step("Verify CHANNEL integrations"):
        integrations = {
            "fb_feed": meta_url,
            "fb_chat": meta_url,
            "ig_feed": meta_url,
            "ig_chat": meta_url,
            "whatsapp": meta_url,
        }
        for integration, url in integrations.items():
            with allure.step(f"Verify {integration} integration"):
                integrations_page.goto_meta(integration, url)

    allure.attach(
        page.screenshot(),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
