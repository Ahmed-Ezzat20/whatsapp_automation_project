import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class WhatsAppBot:
    def __init__(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.wait = WebDriverWait(self.driver, 30)
        except Exception as e:
            print(f"Failed to initialize Chrome WebDriver: {str(e)}")
            raise

    def login_to_whatsapp(self):
        try:
            self.driver.get("https://web.whatsapp.com")
            print("Please scan the QR code within 30 seconds...")
            
            # Wait for QR code scanning
            time.sleep(30)
            
            # Wait for WhatsApp to load completely
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="chat-list"]')
            ))
            print("Successfully logged in to WhatsApp Web")
            return True
        except Exception as e:
            print(f"Failed to login: {str(e)}")
            return False

    def send_message(self, contact_name, message):
        try:
            # Wait for and click search box
            search_box = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="search"]')
            ))
            search_box.click()
            search_box.send_keys(contact_name)
            time.sleep(2)  # Wait for search results
            
            # Select the contact
            contact = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//span[@title='{contact_name}']")
            ))
            contact.click()
            
            # Wait for and fill message box
            message_box = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="conversation-compose-box-input"]')
            ))
            message_box.send_keys(message + Keys.ENTER)
            
            print(f"Message sent to {contact_name}")
            return True
        except Exception as e:
            print(f"Failed to send message: {str(e)}")
            return False

    def close(self):
        """
        Close the Selenium driver.
        """
        self.driver.quit()
