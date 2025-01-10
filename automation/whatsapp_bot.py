import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class WhatsAppBot:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login_to_whatsapp(self):
        """
        Login to WhatsApp Web by scanning the QR code.
        """
        self.driver.get("https://web.whatsapp.com")
        print("Please scan the QR code to log in.")
        time.sleep(20)  # Wait for QR code to be scanned

    def send_message(self, phone_number, message):
        """
        Send a message to a given phone number.
        :param phone_number: Phone number in international format.
        :param message: Message text to send.
        """
        # Open WhatsApp chat using URL
        url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"
        self.driver.get(url)
        time.sleep(10)  # Wait for chat to load

        # Press Enter to send the message
        try:
            send_button = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
            send_button.click()
            print(f"Message sent to {phone_number}")
        except Exception as e:
            print(f"Failed to send message to {phone_number}: {e}")

    def close(self):
        """
        Close the Selenium driver.
        """
        self.driver.quit()
