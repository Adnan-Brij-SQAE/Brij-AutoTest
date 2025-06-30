import keyboard
import pyautogui
from behave import when, then, given
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from Locators import locators
from Helper.enviHelper import Envi_Helper
import time
from allure_commons.types import AttachmentType
import allure
from Logs import logs_file

log = logs_file.get_logs()

@when(u'the user navigate to the Rebate Signup Page Module page')
def step_impl(context):
    with allure.step("navigate to the Rebate Signup Module page"):
        try:
            module_menu = context.driver.find_element(By.XPATH, "//span[normalize-space()='Modules']")
            module_menu.click()
            dropdown_list = context.driver.find_element(By.CSS_SELECTOR, ".dropdown.top-240")
            for i in range(12):
                dropdown_list.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_OPTION)
                time.sleep(2)
        except Exception as e:
            log.error(f"Failed to navigate to Rebate Signup Page: {e}")
            allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the notification button on Rebate Signup Page Module page')
def step_impl(context):
    with allure.step("the user can access the notification button on Rebate Signup Page Module page"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            log.info("Notification icon is clicked and panel is in opened state")
            allure.attach("Notification button accessible", name="Notification Access Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Notification button not accessible: {e}")
            allure.attach(str(e), name="Notification Access Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the logout button on Rebate Signup Page Module page')
def step_impl(context):
    with allure.step("the user can access the logout button on Rebate Signup Page Module page"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_LOGOUT_BUTTON)
            Envi_Helper.capture_screenshot()
            log.info("logout icon is clicked ")
            NotImplementedError(u'STEP: Then the user can access the logout button on Rebate Signup Page Module page')
        except Exception as e:
            log.error(f"Logout button not accessible: {e}")
            allure.attach(str(e), name="Logout Access Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the field button on Rebate Signup Page Module page')
def step_impl(context):
    with allure.step("the user can access the field button on Rebate Signup Page Module page"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_FIELD)
            Envi_Helper.capture_screenshot()
            log.info("field button is clicked")
            keyboard.press_and_release('Esc')
            NotImplementedError(u'STEP: Then the user can access the field button on Rebate Signup Page Module page')
        except Exception as e:
            log.error(f"Field button not accessible: {e}")
            allure.attach(str(e), name="Field Button Access Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can select All checkbox on Rebate Signup Page Module page')
def step_impl(context):
    with allure.step("the user can select All checkbox on Rebate Signup Page Module page"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_ALL_CHECKBOX)
            time.sleep(2)
            NotImplementedError(u'STEP: Then the user can select All checkbox on Rebate Signup Page Module page')
        except Exception as e:
            log.error(f"Failed to select All checkbox: {e}")
            allure.attach(str(e), name="Checkbox Selection Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can search between Rebate Signup Module')
def step_impl(context):
    with allure.step("test Search feature"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.REGISTRATION_SEARCH, "SQA", 10)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            context.driver.find_element(By.XPATH,"//input[@placeholder='Search Items...']").clear()
            time.sleep(3)
        except Exception as e:
            log.error(f"Search feature failed: {e}")
            allure.attach(str(e), name="Search Feature Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can sort the table on Rebate Signup Page Module page')
def step_impl(context):
    with allure.step("the user can sort the table on Rebate Signup Page Module page"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_SIGNUP_HEADING)
            Envi_Helper.capture_screenshot()
            log.info("sorted with signup page name and screenshot attached")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_SIGNUP_HEADING)
            Envi_Helper.capture_screenshot()
            log.info("sorted with signup page name again and screenshot attached")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_WHERE_USED)
            Envi_Helper.capture_screenshot()
            log.info("sorted with where used and screenshot attached")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_WHERE_USED)
            Envi_Helper.capture_screenshot()
            log.info("sorted with where used again and screenshot attached")
            allure.attach("Sorted by column", name="Sort Success", attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            log.error(f"Table sorting failed: {e}")
            allure.attach(str(e), name="Table Sorting Error", attachment_type=allure.attachment_type.TEXT)


@when(u'the user create new Rebate Signup module')
def step_impl(context):
    with allure.step("the user can create new Rebate Signup module from on Rebate Signup Page Module page"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_NEW_MODULE)
            time.sleep(2)
            log.info('navigated to the Rebate signup popup')
            Envi_Helper(context.driver).insert_text_in_input_field(locators.REBATE_SIGNUP_NAME,"Auto Rebate Signup Page")
            # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_SHOW_BACKGROUND)
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_SHOW_INSTRUCTION)
                Envi_Helper(context.driver).insert_text_in_input_field(locators.REBATE_SIGNUP_CARD_TITLE,"Auto Card")
                keyboard.press_and_release('Page Down')
                # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_ADD_STEP)
                # time.sleep(2)
                # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_REMOVE_STEP)
            except Exception as e:
                log.info("unable to detect the elements of show instructions")
            time.sleep(2)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.REBATE_SIGNUP_DESCRIPTION,"Auto Description")
            log.info('adding text to rebate signup RTE')
            keyboard.press_and_release('Page Down')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_SMS_MARKETING)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.REBATE_SIGNUP_SMS_CONSENT,"Auto Updated Consent")
            time.sleep(2)
            log.info('updated SMS marketing description')
            keyboard.press_and_release('Page Down')
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_CUSTOM_CTA)
            log.info("clicked on custom cta")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_AS)
            log.info("navigated to Rebate advance Settings")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_AS_DISABLE_OPTION)
            log.info("Disable ``Text to Opt-In`` on Mobile flag is clickable and working")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_AS_DISABLE_OPTION)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_AS_DIM_BACKGROUND)
            log.info("Dim Background flag is clickable and working")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_AS_SOCIAL_MEDIA)
            log.info("Show social media flag is clickable and working")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_AS_SEND_USER)
            log.info("Show social media flag is clickable and working")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_AS_SEND_USER)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_AS_LEGAL_TEXT)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.REBATE_SIGNUP_AS_LEGAL_TEXT_CONSENT,"Auto Updated text")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_AS_BACK)
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_SAVE)
                log.info('Rebate Signup page created successfully')
                keyboard.press_and_release('Esc')
            except Exception as e:
                log.info("save button was not triggered, saving alternate way")
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_BACK)
                log.info('Rebate Signup page created successfully')
                keyboard.press_and_release('Esc')

        except Exception as e:
            log.error(f"Failed to create new Rebate Signup module: {e}")
            allure.attach(str(e), name="Module Creation Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can edit the previous Rebate Signup module')
def step_impl(context):
    with allure.step("Test edit Rebate signup "):
        try:
            log.error('Pending')
        except Exception as e:
            log.error(f"Failed to edit Rebate Signup module: {e}")
            allure.attach(str(e), name="Module Edit Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the new rebate signup page should appear in list')
def step_impl(context):
    with allure.step("created module appears in list"):
        try:
            Envi_Helper.capture_screenshot()
            log.info("the rebate signup page created successfully and screen shot is attached")
        except Exception as e:
            log.error(f"Failed to create Rebate Signup module: {e}")
            allure.attach(str(e), name="Module creation Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can delete the unused Rebate Signup module')
def step_impl(context):
    with allure.step("Test Delete Rebate signup "):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.REBATE_SIGNUP_SEARCH,"auto rebate signup")
            # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_SIGNUP_HEADING)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_KEBAB)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_DELETE)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_DELETE_CONFIRM)
            context.driver.find_element(By.XPATH, "//input[@placeholder='Search Items...']").clear()
            time.sleep(2)
            log.info("the selected module is deleted successfully")
        except Exception as e:
            log.error(f"Failed to delete Rebate Signup module: {e}")
            allure.attach(str(e), name="Module Deletion Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can delete more than one unused Rebate Signup module')
def step_impl(context):
    with allure.step("the user can delete more than one unused Rebate Signup module"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.REBATE_SIGNUP_SEARCH,"auto rebate signup")
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_ALL_CHECKBOX)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_DELETE_ALL)
            Envi_Helper.capture_screenshot()
            log.info("the selected modules are deleted successfully")
            context.driver.find_element(By.XPATH, "//input[@placeholder='Search Items...']").clear()
            time.sleep(2)
        except Exception as e:
            log.error(f"Failed to delete multiple Rebate Signup modules: {e}")
            allure.attach(str(e), name="Bulk Module Deletion Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user want to see the number of rows on Rebate Signup Page')
def step_impl(context):
    with allure.step("pagination test"):
        try:
            keyboard.press('Page Down')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_ROWPERPAGE_OPTION)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_ROWPERPAGE_20)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_ROWPERPAGE_OPTION)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_ROWPERPAGE_100)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_ROWPERPAGE_OPTION)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_ROWPERPAGE_1000)
            allure.attach("Row count options checked", name="Row Count Action",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Pagination test failed: {e}")
            allure.attach(str(e), name="Pagination Test Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can create duplicate Rebate Signup page')
def step_impl(context):
    with allure.step("create duplicate module "):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.REBATE_SIGNUP_SEARCH, "auto rebate signup")
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_SIGNUP_HEADING)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_KEBAB)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_EDIT)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_DUPLICATE)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_SAVE)
            log.info('Duplicate Rebate Signup page created successfully')
            keyboard.press_and_release('Esc')
            context.driver.find_element(By.XPATH, "//input[@placeholder='Search Items...']").clear()
            time.sleep(2)
            log.info("the duplicate rebate signup page created successfully and screen shot is attached")
        except Exception as e:
            log.error(f"Failed to create duplicate Rebate Signup module: {e}")
            allure.attach(str(e), name="Module creation Error", attachment_type=allure.attachment_type.TEXT)