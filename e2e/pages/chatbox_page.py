from playwright.sync_api import Page


class ChatboxPage:
    def __init__(self, page: Page):
        self.page = page

        self.selectors = {
            "chatbox_nav": '//*[@id="root"]/div[1]/div/div/div[2]/nav/div[2]/div/button[3]',
            "agent_div": '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[3]',
            "convo_bar": '[id="conversation-bar"]',
            "chatbox_textarea": '[id="reply-input"]',
            "chatbox_attachment": '[id="headlessui-popover-button-15"]',
            "attachment_image": '//span[contains(text(), "Image")]',
            "attachment_video": '//span[contains(text(), "Video")]',
            "attachment_audio": '//span[contains(text(), "Audio")]',
            "attachment_document": '//span[contains(text(), "Document")]',
            "attachment_dropzone": '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div',
            "attachment_send": '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[4]/div[1]/div[2]/button',
            "chatbox_send": '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/button',
        }

    def goto_chatbox(self):
        self.page.wait_for_selector(self.selectors["agent_div"], state="visible")
        self.page.click(self.selectors["chatbox_nav"])

    def text_send_confirm(self, message: str):
        self.page.wait_for_selector(self.selectors["chatbox_textarea"], state="visible")
        self.page.fill(self.selectors["chatbox_textarea"], message)
        self.page.click(self.selectors["chatbox_send"])
        self.page.wait_for_selector(f'//p[contains(text(), "{message}")]')

    def upload_file(self, file_type: str, file_path: str):
        self.page.click(self.selectors["chatbox_attachment"])
        self.page.click(self.selectors[f"attachment_{file_type}"])
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_text("Upload").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        self.page.click(self.selectors["attachment_send"])
        self.page.wait_for_selector(
            self.selectors["attachment_dropzone"], state="hidden"
        )

    def upload_image(self, file_path: str):
        self.upload_file("image", file_path)

    def upload_video(self, video_path: str):
        self.upload_file("video", video_path)

    def upload_audio(self, audio_path: str):
        self.upload_file("audio", audio_path)

    def upload_document(self, document_path: str):
        self.upload_file("document", document_path)
