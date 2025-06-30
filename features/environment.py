from playwright.sync_api import sync_playwright
from Logs import logs_file

log = logs_file.get_logs()

def before_all(context):
    # Start Playwright
    playwright = sync_playwright().start()

    # Launch browser maximized (native window)
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=500,
        args=["--start-maximized"]
    )

    # Use no_viewport to respect --start-maximized
    browser_context = browser.new_context(no_viewport=True)

    # Create a new page
    page = browser_context.new_page()

    # Store references for reuse in steps
    context.playwright = playwright
    context.browser = browser
    context.page = page

    # Register Playwright page for logging
    logs_file.set_active_page(page)
    print(f"Active page set? {logs_file.active_page}")

    # Perform login on this page
    page.goto('https://rc.brij.it/')
    page.locator('#float-input').fill("testers366@gmail.com")
    page.locator("button[type='button']").click()
    page.locator('#float-input1').fill("P@$$w0rd!@")
    page.locator("button[type='submit']").click()

    log.info("Logged in and ready to test with Playwright.")

def after_all(context):
    # Clean up: Close the browser and stop Playwright
    context.browser.close()
    context.playwright.stop()
    log.info("Browser closed, Playwright stopped.")