from tests.base_test import login
from pages.chatbox_page import ChatboxPage
from utils.config_loader import load_config


def test_chatbox(browser_context):
    page = browser_context

    login(page)

    config = load_config()
    base_url = config["base_url"]

    chatbox_page = ChatboxPage(page)

    chatbox_page.goto_chatbox()
    # Replace with your project id
    page.wait_for_url(f"{base_url}/projects/1981/inbox")
    chatbox_page.text_send_confirm("Good day")
