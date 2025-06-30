from datetime import datetime
import logging
import os
import allure

log_path = os.path.join(os.path.abspath(__file__ + '/../'), "current_log_file.log")

# Add this global variable at the module level
active_page = None

class AllureLoggingHandler(logging.Handler):
    def log(self, level_name, message):
        with allure.step(f"Log ({level_name}) {message}"):
            if level_name.lower() == "error":
                attach_screenshot_in_report()

    def emit(self, record):
        self.log(record.levelname, record.getMessage())

# Add this function to set the active page
def set_active_page(page):
    global active_page
    active_page = page
    logging.info(f"Active page set for screenshot functionality")

def get_logs():
    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)",
                      datefmt='%d/%m/%Y %I:%M:%S %p')
    allure_handler = AllureLoggingHandler()
    filehandler = logging.FileHandler(log_path, mode="w")
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    logger.addHandler(allure_handler)
    return logger

def attach_screenshot_in_report():
    global active_page

    if active_page is None:
        # Use standard logging to avoid infinite recursion
        logging.error("No Playwright page is set for screenshot attachment.")
        return

    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        screenshot_dir = os.path.normpath(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "../Screenshots"
            )
        )
        os.makedirs(screenshot_dir, exist_ok=True)

        screenshot_path = os.path.join(
            screenshot_dir,
            f"screenshot_{timestamp}.png"
        )

        active_page.screenshot(path=screenshot_path, full_page=True)

        allure.attach.file(
            source=screenshot_path,
            name=f"Screenshot {timestamp}",
            attachment_type=allure.attachment_type.PNG
        )

        logging.info(f"Screenshot captured and attached: {screenshot_path}")

    except Exception as e:
        logging.error(f"Failed to capture and attach screenshot: {str(e)}")