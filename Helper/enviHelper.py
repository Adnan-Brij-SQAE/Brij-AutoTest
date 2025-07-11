import os
import random
import allure
from playwright.sync_api import TimeoutError, Page
from datetime import datetime
from Logs import logs_file

log = logs_file.get_logs()


class Envi_Helper:
    def __init__(self, page: Page):
        self.page = page

    def open_page(self, url: str):
        log.info(f"Navigating to: {url}")
        self.page.goto(url)

    def insert_text_in_input_field(self, selector, text: str, timeout=10000):
        """
        Fills the input field identified by a single locator or a list of locators.
        Raises an exception if no field could be filled.
        """
        try:
            if isinstance(selector, (list, tuple)):
                for sel in selector:
                    log.info(f"Trying to fill {sel} with: {text}")
                    try:
                        element = self.page.locator(sel)
                        element.clear()
                        element.fill(text)
                        log.info(f"Filled successfully: {sel}")
                        return
                    except TimeoutError:
                        log.warning(f"Timeout waiting for {sel}, trying next...")
                    except Exception as e:
                        log.warning(f"Error trying {sel}: {e}")
                log.error(f"No input field found to fill in: {selector}")
                self.capture_screenshot()
                raise Exception(f"Could not fill any input field in selector list: {selector}")
            else:
                log.info(f"Filling {selector} with: {text}")
                element = self.page.locator(selector)
                element.wait_for(state='visible', timeout=timeout)
                element.fill(text)
                log.info(f"Filled successfully: {selector}")
        except Exception as e:
            log.error(f"Error filling {selector} with '{text}': {e}")
            self.capture_screenshot()
            raise Exception(f"Fill failed on selector: {selector} | Reason: {e}")

    def wait_till_element_is_present_to_click(self, selector, timeout=10000):
        try:
            if isinstance(selector, (list, tuple)):
                for sel in selector:
                    log.info(f"Trying to click: {sel}")
                    try:
                        element = self.page.locator(sel)
                        element.wait_for(state='visible', timeout=timeout)
                        element.click()
                        log.info(f"Clicked successfully: {sel}")
                        return
                    except TimeoutError:
                        log.warning(f"Timeout waiting for {sel}, trying next...")
                    except Exception as e:
                        log.warning(f"Error trying {sel}: {e}")
                log.error(f"No selectable element found in: {selector}")
                self.capture_screenshot()
                raise Exception(f"Could not click any selector in list: {selector}")
            else:
                log.info(f"Clicking: {selector}")
                element = self.page.locator(selector)
                element.wait_for(state='visible', timeout=timeout)
                element.click()
                log.info(f"Clicked successfully: {selector}")
        except Exception as e:
            log.error(f"Error clicking {selector}: {e}")
            self.capture_screenshot()
            raise Exception(f"Click failed on selector: {selector} | Reason: {e}")

    def ensure_checkbox_is_checked(self, selector: str, timeout=10000):
        log.info(f"Ensuring checkbox is checked: {selector}")
        try:
            checkbox = self.page.locator(selector)
            checkbox.wait_for(state='visible', timeout=timeout)
            checkbox.wait_for(state='attached', timeout=timeout)
            is_checked = checkbox.is_checked()
            if is_checked:
                log.info(f"Checkbox {selector} is already checked.")
            else:
                checkbox.check()
                log.info(f"Checkbox {selector} has been checked.")
            return True

        except Exception as e:
            log.error(f"Error ensuring checkbox {selector} is checked: {e}")
            self.capture_screenshot()
            return False

    def wait_for_element(self, selector: str, timeout=10000):
        log.info(f"Waiting for: {selector}")
        try:
            self.page.locator(selector).wait_for(timeout=timeout)
            return True
        except TimeoutError as e:
            log.error(f"Element not found: {selector} - {e}")
            self.capture_screenshot()
            return False

    def get_value(self, selector: str, timeout=10000):
        log.info(f"Getting text from selector: {selector}")
        try:
            value = self.page.locator(selector).text_content(timeout=timeout)
            log.info(f"Retrieved value from {selector}: {value}")
            return value

        except Exception as e:
            log.error(f"Error getting text from {selector}: {e}")
            self.capture_screenshot()
            return None

    def upload_file_using_file_chooser(self, trigger_selector: str, file_path: str, timeout=10000):

        log.info(f"Uploading file '{file_path}' using trigger: {trigger_selector}")
        try:
            with self.page.expect_file_chooser(timeout=timeout) as fc_info:
                self.page.locator(trigger_selector).click()
            file_chooser = fc_info.value
            file_chooser.set_files(file_path)
            return True
        except TimeoutError as e:
            log.error(f"Timeout while trying to upload file using {trigger_selector}: {e}")
            self.capture_screenshot()
            return False
        except Exception as e:
            log.error(f"Unexpected error during file upload: {e}")
            self.capture_screenshot()
            return False



    def hide_left_panel(page):
        try:
            page.evaluate("document.querySelector('.main-menu ng-star-inserted').style.display = 'none';")
            print("Left panel hidden successfully.")
        except Exception as e:
            print(f"Error hiding left panel: {e}")

    def capture_screenshot(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshots/screenshot_{timestamp}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

        try:
            self.page.screenshot(path=screenshot_path)
            log.info(f"Screenshot saved: {screenshot_path}")
            allure.attach(
                self.page.screenshot(),
                name=f"screenshot_{timestamp}",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            log.error(f"Screenshot failed: {e}")

    # Additional helper methods
    def hover(self, selector: str):
        self.page.locator(selector).hover()

    def drag_and_drop(self, source: str, target: str):
        self.page.drag_and_drop(source, target)

    def switch_frame(self, selector: str):
        frame = self.page.frame_locator(selector)
        return frame

    async def evaluate(self, param):
        pass


def generate_random_number(self, length: int):
        return ''.join(str(random.randint(0, 9)) for _ in range(length))