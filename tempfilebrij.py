import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rc.brij.it/brand/login?returnUrl=%2Fbrand%2Fdashboard%2Fregistrations")
    page.locator("#float-input").click()
    page.locator("#float-input").fill("testers366@gmail.com")
    page.get_by_role("button", name="Continue with Email").click()
    page.locator("#float-input1").click()
    page.locator("#float-input1").fill("P@$$w0rd!@")
    page.get_by_role("button", name="Continue with Email").click()
    page.get_by_text("Test Results").click()
    page.get_by_role("button", name="New Test Result").click()
    page.locator("div").filter(has_text=re.compile(r"^empty$")).first.click()
    page.get_by_text("Heavy Metals", exact=True).click()
    page.get_by_text("Heavy Metals", exact=True).first.click()
    page.locator("#pn_id_31").get_by_role("combobox", name="Click to select").click()
    page.get_by_text("New Lab").click()
    page.locator("#name").fill("testlab")
    page.locator("#pc243").get_by_role("button", name="Save").click()
    page.locator("div").filter(has_text=re.compile(r"^Lot Number\*$")).get_by_placeholder("Enter here...").click()
    page.locator("div").filter(has_text=re.compile(r"^Lot Number\*$")).get_by_placeholder("Enter here...").fill("test")
    page.locator("div").filter(has_text=re.compile(r"^Lot Number\*$")).get_by_placeholder("Enter here...").press("Tab")
    page.locator("div").filter(has_text=re.compile(r"^Test ID \(leave blank to auto-generate\)$")).get_by_placeholder("Enter here...").fill("test")
    page.locator("div").filter(has_text=re.compile(r"^Sample ID$")).get_by_placeholder("Enter here...").click()
    page.locator("div").filter(has_text=re.compile(r"^Sample ID$")).get_by_placeholder("Enter here...").fill("213")
    page.locator("div").filter(has_text=re.compile(r"^Order ID$")).get_by_placeholder("Enter here...").click()
    page.locator("div").filter(has_text=re.compile(r"^Order ID$")).get_by_placeholder("Enter here...").fill("345")
    page.locator("input[name=\"expirationDate\"]").click()
    page.get_by_text("30", exact=True).click()
    page.get_by_role("combobox", name="Click to select").click()
    page.get_by_role("option", name="digits").click()
    page.locator("div").filter(has_text=re.compile(r"^Arsenic \(ppb\)$")).get_by_placeholder("Enter here...").click()
    page.locator("div").filter(has_text=re.compile(r"^Arsenic \(ppb\)$")).get_by_placeholder("Enter here...").fill("10")
    page.locator("div").filter(has_text=re.compile(r"^Cadmium \(ppb\)$")).get_by_placeholder("Enter here...").click()
    page.locator("div").filter(has_text=re.compile(r"^Cadmium \(ppb\)$")).get_by_placeholder("Enter here...").fill("10")
    page.locator("div").filter(has_text=re.compile(r"^Lead \(ppb\)$")).get_by_placeholder("Enter here...").click()
    page.locator("div").filter(has_text=re.compile(r"^Lead \(ppb\)$")).get_by_placeholder("Enter here...").fill("10")
    page.locator("div").filter(has_text=re.compile(r"^Mercury \(ppb\)$")).get_by_placeholder("Enter here...").click()
    page.locator("div").filter(has_text=re.compile(r"^Mercury \(ppb\)$")).get_by_placeholder("Enter here...").fill("10")
    page.get_by_text("Click or Drag File Here").click()
    page.locator("body").set_input_files("testfile.pdf")
    page.get_by_role("button", name="Save").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

#
#
#
#
#
#
#
#
#
# import webbrowser
#
# from pyautogui import click
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# import time
# import pyautogui
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from Locators import locators
# from Helper.enviHelper import Envi_Helper
#
#
#
#
#
#
# from Helper.enviHelper import Envi_Helper
#
# # driver = webdriver.Chrome()
# #
# # url = 'https://brij.it/c/6IRP/'
# #
# # for i in range(100):
# #     print(f"Opening {url} - attempt {i+1}")
# #     # driver.get(url)
# #     webbrowser.open_new_tab(url)
# #     time.sleep(10)
# driver = webdriver.Chrome()
# try:
#     driver.get("https://staging.brij.it/c/ER62")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//button[contains(@class,'relative w-full flex flex-row items-center justify-center flex-shrink-0 px-3 rounded-full text-xs sm:text-base font-semibold duration-200 focus-visible:ring-2 focus-visible:ring-black/60')]").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//p[normalize-space()='Agree to hand over data?']").click()
#     driver.find_element(By.XPATH,"//*[@id='bottom-drawer-closed-container']/div[2]/div[2]/div/div/div[2]/div/div/form/button[1]/span").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@name='email']").send_keys("adnan+9111111@brij.it")
#     time.sleep(2)
#     # driver.find_element(By.XPATH,"//*[@id='bottom-drawer-closed-container']/div[2]/div[2]/div/div/div[2]/div/div[2]/form/div[2]/button[1]").click()
#     # driver.find_element(By.XPATH,"//div[contains(text(),'I confirm that i have read and agree to Testing Br')]").click()
#     driver.find_element(By.XPATH,"//span[contains(text(),'Register')]").click()
#     time.sleep(6)
#     driver.find_element(By.XPATH, "//input[@name='textArea']").send_keys("random text ")
#     driver.find_element(By.XPATH, "//*[@id='bottom-drawer-closed-container']/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/button/span").click()
#     driver.find_element(By.XPATH, "//span[normalize-space()='Multiple 1']").click()
#     driver.find_element(By.XPATH,"//*[@id='bottom-drawer-closed-container']/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/button/span").click()
#     time.sleep(6)
#     driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys("Adnan")
#     driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys("Auto")
#     driver.find_element(By.XPATH,"//input[@name='phone-number-input']").click()
#     driver.find_element(By.XPATH,"//input[@name='phone-number-input']").send_keys("(+92) 090 078 6010")
#     time.sleep(2)
#     # driver.find_element(By.XPATH,"//input[contains(@name,'retail-channel')]").click()
#     # time.sleep(2)
#     # # driver.find_element(By.XPATH,"//li[@aria-label='Custom Value']").click()
#     # # driver.find_element(By.XPATH,"//input[@name='retail-channel']").send_keys("Adnan Jamil")
#     # time.sleep(2)
#     driver.find_element(By.XPATH,"//span[normalize-space()='Continue']").click()
#     time.sleep(10)
# except Exception as e:
#     print("not done ")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # try:
# #     driver.get("https://brij.it/c/6IRP/custom")
# #     time.sleep(2)
# #     driver.find_element(By.XPATH, "//span[normalize-space()='More']").click()
# #     time.sleep(2)
# #     driver.find_element(By.XPATH,"//span[normalize-space()='test warramty']").click()
# #     time.sleep(2)
# #     driver.find_element(By.XPATH,"//input[@name='email']").send_keys("adnan+987129@brij.it")
# #     # driver.find_element(By.XPATH,"//*[@id='bottom-drawer-closed-container']/div[2]/div[2]/div/div/div[2]/div/div[2]/form/div[2]/button[1]").click()
# #     # driver.find_element(By.XPATH,"//div[contains(text(),'I confirm that i have read and agree to Testing Br')]").click()
# #     driver.find_element(By.XPATH,"//span[contains(text(),'Register')]").click()
# #     time.sleep(5)
# #     driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys("Adnan")
# #     driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys("Auto")
# #     driver.find_element(By.XPATH,"//input[@name='phone-number-input']").click()
# #     driver.find_element(By.XPATH,"//input[@name='phone-number-input']").send_keys("(+92) 090 078 6010")
# #     time.sleep(2)
# #     # driver.find_element(By.XPATH,"//input[contains(@name,'retail-channel')]").click()
# #     # time.sleep(2)
# #     # # driver.find_element(By.XPATH,"//li[@aria-label='Custom Value']").click()
# #     # # driver.find_element(By.XPATH,"//input[@name='retail-channel']").send_keys("Adnan Jamil")
# #     # time.sleep(2)
# #     driver.find_element(By.XPATH,"//button[@type='submit']").click()
# #     time.sleep(10)
# # except Exception as e:
# #     print("not done ")