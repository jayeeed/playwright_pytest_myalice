import allure
from tests.base_test import login
from pages.integrations.integrated_page import IntegratedPage
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
        integrated_page = IntegratedPage(page)
        integrated_page.goto_integrations()

        integrated_page.delete_integrations()

    allure.attach(
        page.screenshot(),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
