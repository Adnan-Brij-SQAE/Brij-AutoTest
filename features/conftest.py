# import pyautogui
# import datetime
# import logging
#
# log = logging.getLogger(__name__)
#
# class Utility:
#     @staticmethod
#     def capture_screenshot():
#         try:
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#             screenshot_filename = f"screenshot_{timestamp}.png"
#             screenshot = pyautogui.screenshot()
#             screenshot.save(screenshot_filename)
#             log.info(f"Screenshot saved as {screenshot_filename}")
#             print(f"Screenshot saved as {screenshot_filename}")
#         except Exception as e:
#             log.error(f"An error occurred while capturing the screenshot: {e}")
#             print(f"An error occurred: {e}")
#             log.error("Screenshot capturing failed")
#             return None
