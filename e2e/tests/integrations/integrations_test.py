import allure
from tests.base_test import login
from pages.integrations.integrations_page import IntegrationsPage


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
        integrations_page = IntegrationsPage(page)
        integrations_page.goto_integrations()

    with allure.step("Verify store integrations"):
        integrations_page.goto_woocommerce()
        integrations_page.goto_salla()

    with allure.step("Verify channel integrations"):
        integrations_page.goto_messenger()
        integrations_page.goto_ig_feed()

    allure.attach(
        page.screenshot(),
        name="Chatbox Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
