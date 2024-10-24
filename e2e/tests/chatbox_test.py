import allure
from tests.base_test import login
from pages.chatbox_page import ChatboxPage
from utils.config_loader import load_config


@allure.feature("Chatbox Functionality")
@allure.story("User sends message via chatbox")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://your_project_tracking_url", name="Project Tracking Link")
@allure.description(
    "This test verifies that the user can send a message via the chatbox after logging in."
)
def test_chatbox(browser_context):
    page = browser_context

    with allure.step("Log in to the application"):
        login(page)

    with allure.step("Load configuration and navigate to chatbox"):
        config = load_config()
        base_url = config["base_url"]
        chatbox_page = ChatboxPage(page)
        chatbox_page.goto_chatbox()

    with allure.step("Verify chatbox URL and send message"):
        # Replace with your project id
        page.wait_for_url(f"{base_url}/projects/1981/inbox")
        chatbox_page.text_send_confirm("Good day")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step("Send attachments and verify delivery"):
        # chatbox_page.attachment_send_confirm("image", "../data/1.8mb.jpg")
        # chatbox_page.attachment_send_confirm("video", "path/to/video.mp4")
        # chatbox_page.attachment_send_confirm("audio", "path/to/audio.mp3")
        # chatbox_page.attachment_send_confirm("document", "path/to/document.pdf")
        chatbox_page.attachment_send_confirm("image", "../data/1.8mb.jpg")
        page.wait_for_timeout(5000)

    allure.attach(
        page.screenshot(),
        name="Chatbox Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
