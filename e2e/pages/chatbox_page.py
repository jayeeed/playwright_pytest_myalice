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
        self.chatbox_attachment = '[id="headlessui-popover-button-15"]'
        self.attachment_image = '//span[contains(text(), "Image")]'
        self.attachment_video = '//span[contains(text(), "Video")]'
        self.attachment_audio = '//span[contains(text(), "Audio")]'
        self.attachment_document = '//span[contains(text(), "Document")]'
        self.attachment_dropzone = '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div'
        self.attachment_send = '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[4]/div[1]/div[2]/button'
        self.chatbox_send = '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/button'

    def goto_chatbox(self):
        self.page.wait_for_selector(self.agent_div, state="visible")
        self.page.click(self.chatbox_nav)

    def text_send_confirm(self, message: str):
        self.page.wait_for_selector(self.chatbox_textarea, state="visible")
        self.page.fill(self.chatbox_textarea, message)
        self.page.click(self.chatbox_send)
        self.page.wait_for_selector(f'//p[contains(text(), "{message}")]')

    def attachment_send_confirm(self, file_type: str, file_path: str):
        self.page.click(self.chatbox_attachment)

        if file_type == "image":
            self.page.click(self.attachment_image)
        elif file_type == "video":
            self.page.click(self.attachment_video)
        elif file_type == "audio":
            self.page.click(self.attachment_audio)
        elif file_type == "document":
            self.page.click(self.attachment_document)
        else:
            raise ValueError(
                "Invalid file type provided. Choose from 'image', 'video', 'audio', 'document'."
            )

        # Upload the file by setting the input files in the drag-and-drop area
        self.page.set_input_files(self.attachment_dropzone, file_path)

        # Optionally, click the send button if needed
        self.page.click(self.attachment_send)
