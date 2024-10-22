from playwright.sync_api import Page


class ChatboxPage:
    def __init__(self, page: Page):
        self.page = page

        self.chatbox_nav = (
            '//*[@id="root"]/div[1]/div/div/div[2]/nav/div[2]/div/button[3]'
        )
        self.agent_div = (
            '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[3]'
        )
        self.convo_bar = '[id="conversation-bar"]'
        self.chatbox_textarea = '[id="reply-input"]'
        self.chatbox_send = '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/button'

    def goto_chatbox(self):
        self.page.wait_for_selector(self.agent_div, state="visible")
        self.page.click(self.chatbox_nav)

    def text_send_confirm(self, message: str):
        self.page.wait_for_selector(self.chatbox_textarea, state="visible")
        self.page.fill(self.chatbox_textarea, message)
        self.page.click(self.chatbox_send)
        self.page.wait_for_selector(f'//p[contains(text(), "{message}")]')
