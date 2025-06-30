import os
from datetime import datetime

class FileHandler:
    def __init__(self, page):
        self.page = page

    def save_screenshot(self, name="screenshot"):
        os.makedirs("screenshots", exist_ok=True)
        filename = f"screenshots/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        self.page.screenshot(path=filename, full_page=True)
        return filename