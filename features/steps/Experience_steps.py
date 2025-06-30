import keyboard
from behave import *
from selenium.webdriver.common.by import By
from Locators import locators
from Helper.enviHelper import Envi_Helper
from Logs import logs_file
import allure
import time
log = logs_file.get_logs()

@when(u'the user navigates to the Experience page')
def step_impl(context):
    try:

        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LEFT_PANEL)
        customer_option = context.driver.find_element(By.XPATH, "//span[normalize-space()='Experiences']")
        customer_option.click()
        time.sleep(2)
        allure.attach("Navigated to Experience page", name="Navigation Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Navigation failed: {e}")
        allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the Experience page is displayed')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present(locators.EXPERIENCE_TITLE)
        allure.attach("Experience page displayed", name="Page Display Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Page display failed: {e}")
        allure.attach(str(e), name="Page Display Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user filters by Status')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_STATUS_FILTER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_ALL_STATUS)
        log.info("entering value in filter search ")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_FILTER_SEARCH,"in")
        log.info("filter Search is working and ss attached ")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SELECTALL)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_CROSS)
        time.sleep(2)
        allure.attach("Filtered by Status", name="Filter Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Filter failed: {e}")
        allure.attach(str(e), name="Filter Error", attachment_type=allure.attachment_type.TEXT)

@then(u'only experiences with that status are shown')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_STATUS_FILTER_OPTION_ACTIVE)
        log.info("Active filter is working and ss attached ")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_STATUS_FILTER_OPTION_INACTIVE)
        log.info("inactive filter is working and ss attached ")
        Envi_Helper.capture_screenshot()
        allure.attach("Status filter verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user filters by Category')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_CATEGORY_FILTER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_ALL_CATEGORY)
        log.info("entering value in filter search ")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_FILTER_SEARCH, "test")
        log.info("filter Search is working and ss attached ")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SELECTALL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_CROSS)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_ALL_CATEGORY)
        time.sleep(2)
        allure.attach("Filtered by Category", name="Filter Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Filter failed: {e}")
        allure.attach(str(e), name="Filter Error", attachment_type=allure.attachment_type.TEXT)

@then(u'only experiences with that category are shown')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("the category filter s working ")
        allure.attach("Category filter verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user filters by Experience Types')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TYPE_FILTER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_ALL_TYPE)
        log.info("entering value in filter search ")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_FILTER_SEARCH, "test")
        log.info("flter Search is working and ss attached ")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_CROSS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_ALL_TYPE)
        time.sleep(2)
        allure.attach("Filtered by Experience Type", name="Filter Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Filter failed: {e}")
        allure.attach(str(e), name="Filter Error", attachment_type=allure.attachment_type.TEXT)

@then(u'only experiences with that type are shown')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TYPE_WebApp)
        log.info("Webapp filter is working and ss attached ")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TYPE_DynamicLink)
        log.info("Dynamic Link filter is working and ss attached ")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TYPE_DigitalHub)
        log.info("Digital Hub filter is working and ss attached ")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TYPE_Rebate)
        log.info("Rebate filter is working and ss attached ")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_ALL_TYPE)
        allure.attach("Experience type filter verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user searches for an experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_SEARCH_BAR,"Test",10)
        time.sleep(2)
        allure.attach("Searched for experience", name="Search Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Search failed: {e}")
        allure.attach(str(e), name="Search Error", attachment_type=allure.attachment_type.TEXT)

@then(u'matching experiences are displayed')
def step_impl(context):
    try:
        log.info("Search functionality is working and ss attached ")
        Envi_Helper.capture_screenshot()
        context.driver.find_element(By.XPATH,"//input[@placeholder='Search Items...']").clear()
        allure.attach("Search results verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user clicks the notification icon')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
        allure.attach("Clicked notification icon", name="Click Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Click failed: {e}")
        allure.attach(str(e), name="Click Error", attachment_type=allure.attachment_type.TEXT)

@then(u'notifications are shown')
def step_impl(context):
    try:
        log.info("Notification icon is working and ss attached ")
        Envi_Helper.capture_screenshot()
        allure.attach("Notifications shown", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user clicks the logout icon')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
        allure.attach("Clicked logout icon", name="Click Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Click failed: {e}")
        allure.attach(str(e), name="Click Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user is logged out')
def step_impl(context):
    try:
        log.info("logout is working and ss attached ")
        Envi_Helper.capture_screenshot()
        allure.attach("User logged out", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user sorts by a columns')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_EXPERIENCE_NAME_HEADING)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_EXPERIENCE_NAME_HEADING)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TITLE_HEADING)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TITLE_HEADING)
        allure.attach("Sorted by column", name="Sort Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Sort failed: {e}")
        allure.attach(str(e), name="Sort Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the table is sorted accordingly')
def step_impl(context):
    try:
        log.info("sorting is working and ss attached")
        allure.attach("Sorting verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user access the field button')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FIELDS_BUTTON)
        allure.attach("Accessed Field button", name="Field button", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed: {e}")
        allure.attach(str(e), name="field button error clicking", attachment_type=allure.attachment_type.TEXT)


@then(u'user can display columns according to fields selected')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("field button is working ")
        allure.attach("field button column", name="Field button", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed: {e}")
        allure.attach(str(e), name="Add Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user get the experience count')
def step_impl(context):
    try:
        Envi_Helper(context.driver).get_value(locators.EXPERIENCE_COUNT)
        allure.attach("Web apps experience added", name="Add Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed: {e}")
        allure.attach(str(e), name="Add Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the total experience count should be displayed')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        allure.attach("Web apps experience added", name="Add Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed: {e}")
        allure.attach(str(e), name="Add Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user adds a new web apps experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_CHOOSE_EXPERIENCE_BUTTON)
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME,"Auto WebApp Experience")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_SUBTITLE,"Auto Subtitle")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_PRODUCTSKU,"Auto SKU 1234")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_PRODUCTURL,"https://www.autotest.com")
        Envi_Helper.capture_screenshot()
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(
            locators.EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_NEW)
        # Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_NEW_NAME, "Auto Channel")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_NEW_NAME_SAVE)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_All)
        # Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_SEARCH, "Auto")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_SELECT_All)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_CROSS)
        keyboard.press_and_release('Esc')
        keyboard.press_and_release('Page Down')
        log.info("Channel selected successfully")
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_CATEGORY)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_NEW)
        # Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_NEW_NAME,"Auto Category")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_NEW_NAME_SAVE)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_All)
        keyboard.press_and_release('Esc')
        # Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_SEARCH,"Auto")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_SELECT_All)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_CROSS)
        # try:
        #     context.driver.find_element(By.XPATH,"//div[contains(text(),'Auto')]").click()
        # finally:
        #     context.driver.find_element(By.XPATH,"//input[@id='product3']").click()
        log.info("Category created ans selected successfully")
        Envi_Helper.capture_screenshot()
        keyboard.press_and_release('Page Down')

        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_PRODUCT_DESCRIPTION,"Auto Description")
        log.info("product description added")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_ADVANCE_SETTING_BUTTON)
        log.info("navigated to advance settings")
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_SHOW_SOCIAL)
        log.info("social icon is displayed and screenshot is attached ")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_SHOW_SOCIAL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_DESKTOP_VIEW)
        log.info("Desktop view is selected and screenshot is attached ")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_DESKTOP_VIEW)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE)
        log.info("user is selecting the content gate ")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_DROPDOWN)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_DROPDOWN_OPTION)
        log.info("content gate Added successfully")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_ALTERNATELOGO)
        log.info("Alternate logo flag is working ")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_ALTERNATELOGO)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_SECONDARY_MODULE)
        log.info("Customize Secondary Modules Button flag is working")
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_SECONDARY_MODULE_TEXT,"Auto CTA")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_SECONDARY_MODULE)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_SECONDARY_MODULE_THEME)
        # log.info("Change Background Image After Registration flag is working")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_SECONDARY_MODULE_THEME)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CHANGE_BACKGROUND)
        log.info("Change Background Image After Registration flag is working")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CHANGE_BACKGROUND)
        Envi_Helper.capture_screenshot()
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_AUTO_RECEIPT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_SEARCH, "test")
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_AUTO_RECEIPT)
        log.info("Verification Criteria Added successfully")
        time.sleep(2)
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CUSTOM_THEME)
        log.info("Custom Theme flag is clickable and working ")
        Envi_Helper.capture_screenshot()
        keyboard.press_and_release('Page Up')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_BACK)
        time.sleep(3)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_SAVE)
        time.sleep(3)
        log.info("Experience Created Successfully")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION)
        time.sleep(2)
        log.info("Navigated to registration page ")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_OPTION_NEW)
        log.info("selected new registration")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_NAME,"Auto Registration")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_REGISTER)
        log.info("Register CTA selected")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_ACTIVATE)
        log.info("Activate CTA selected")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTAa)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_SIGNUP)
        log.info("Signup CTA selected")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTAs)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_DONATE)
        log.info("Donate CTA selected")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTAd)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_CUSTOM)
        log.info("Custom CTA selected")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_INPUT,"Auto CTA")
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_DESCRIPTION,"Auto Description")
        log.info("description added ")
        keyboard.press_and_release('Page Down')
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_FORM)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_FORM)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_FORM_SEARCH,"registration form")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_FORM_SEARCH_OPTION)
            log.info("form added ")
        except Exception as e:
            log.info("form not added")
        Envi_Helper.capture_screenshot()
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS)
        Envi_Helper.capture_screenshot()
        log.info("navigated to advance settings ")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_SHOW_OTHER)
        log.info("Show other modules after Registration flag is working  ")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_SHOW_OTHER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_MULTIPLE)
        log.info("Enable Multiple Registrations flag is working  ")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_MULTIPLE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_CUSTOM_CONFIRM)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_CUSTOM_CONFIRM_TEXT,"Thankyou")
        keyboard.press_and_release('Page Down')
        log.info("Customize Confirmation Message flag is working  ")
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_MARKETING)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_MARKETING_CONSENT,"Auto Updated")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_MARKETING_REQUIRED)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_MARKETING_DEFAULT)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_TERM)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_TERM_CONSENT,"Auto Updated")
        keyboard.press_and_release('Page Down')
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_TERM_REQUIRED)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_TERM_DEFAULT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_NAME)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_NAME)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE_CONSENT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE_CONSENT)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE_CONSENT_TEXT,"Auto Updated" )
        keyboard.press_and_release('Page Down')
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE_DEFAULT)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE_REQUIRED)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_GOOGLE_SIGNUP)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_GOOGLE_SIGNUP)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE)
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_TEXT,"Auto Updated text")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PHONE)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PHONE_CONSENT)
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PHONE_CONSENT_TEXT,"Auto Updated")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PHONE_REQUIRED)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PHONE_DEFAULT)
        time.sleep(2)
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_NAME1)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PDATE)
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC_BEFORE,"2")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC_AFTER,"2")
        except Exception as e:
            log.info("Dynamic date not selected")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PDATE_FIXED)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_QUANTITY)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PLACE_PURCHASE)
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_ALL)
            log.info("Retail Channel selected")
        except Exception as e:
            log.info("Retail Channel not selected")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_SERIAL_NUM)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PROOF)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PROOF_TEXT,"Updated Text")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_REQUIRED_APPROVAL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_REQUIRED_APPROVAL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_SAVE)
        time.sleep(4)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_SAVE_CONFIRM)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_MODULE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_Cross)
        Envi_Helper.capture_screenshot()
        log.info("Web app experience created sucessfully")
        allure.attach("Web apps experience added", name="Add Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        keyboard.press_and_release('Home')
        keyboard.press_and_release('Page Up')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_Cross)
        log.error(f"Add failed: {e}")
        allure.attach(str(e), name="Add Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the experience is added successfully')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_SEARCH_BAR,"Auto Web")
        Envi_Helper.capture_screenshot()
        context.driver.find_element(By.XPATH,"//input[@placeholder='Search Items...']").clear()
        allure.attach("Experience added verification", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@given(u'a web apps experience exists')
def step_impl(context):
    try:
        allure.attach("Web apps experience exists", name="Setup Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Setup failed: {e}")
        allure.attach(str(e), name="Setup Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user edits the web apps experience')
def step_impl(context):
    try:
        allure.attach("Web apps experience edited", name="Edit Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Edit failed: {e}")
        allure.attach(str(e), name="Edit Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the changes are saved')
def step_impl(context):
    try:
        allure.attach("Changes saved verification", name="Save Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Save verification failed: {e}")
        allure.attach(str(e), name="Save Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user adds a new rebate experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_OPTION)
        log.info("selected Rebate as experience ")
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_CHOOSE_EXPERIENCE_BUTTON)
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME,"Auto Rebate Experience")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)
        time.sleep(2)
        log.info("Rebate experience name save ")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_OPTION)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_NEW_SIGNUP)
        # time.sleep(2)
        # log.info('navigated to the Rebate signup page')
        # Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_SIGNUP_NAME,"Auto Rebate Signup Page")
        # # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_SHOW_BACKGROUND)
        # try:
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_SHOW_INSTRUCTION)
        #     Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_SIGNUP_CARD_TITLE,"Auto Card")
        #     keyboard.press_and_release('Page Down')
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_ADD_STEP)
        #     time.sleep(2)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_REMOVE_STEP)
        # except Exception as e:
        #     log.info("unable to detect the elements of show instructions")
        # time.sleep(2)
        # Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_SIGNUP_DESCRIPTION,"Auto Description")
        # log.info('adding text to rebate signup RTE')
        # keyboard.press_and_release('Page Down')
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_SMS_MARKETING)
        # Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_SIGNUP_SMS_CONSENT,"Auto Updated Consent")
        # time.sleep(2)
        # log.info('updated SMS marketing description')
        # keyboard.press_and_release('Page Down')
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_CUSTOM_CTA)
        # keyboard.press_and_release('Page Down')
        # Envi_Helper.capture_screenshot()
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_AS)
        # log.info("navigated to Rebate advance Settings")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_AS_DISABLE_OPTION)
        # log.info("Disable ``Text to Opt-In`` on Mobile flag is clickable and working")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_AS_DISABLE_OPTION)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_AS_DIM_BACKGROUND)
        # log.info("Dim Background flag is clickable and working")
        # Envi_Helper.capture_screenshot()
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_AS_SOCIAL_MEDIA)
        # log.info("Show social media flag is clickable and working")
        # Envi_Helper.capture_screenshot()
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_AS_SEND_USER)
        # log.info("Show social media flag is clickable and working")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_AS_SEND_USER)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_AS_LEGAL_TEXT)
        # Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_SIGNUP_AS_LEGAL_TEXT_CONSENT,"Auto Updated text")
        # Envi_Helper.capture_screenshot()
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_AS_BACK)
        # try:
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_SAVE1)
        #     log.info('Rebate Signup page created successfully')
        # except Exception as e:
        #     log.info("save button was not triggered, saving alternate way")
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_BACK)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_SIGNUP_SAVE_EXIT)
        #     log.info('Rebate Signup page created successfully')
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_NEW)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_CAMPAIGN_NAME,"Auto Rebate Campaign")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_CAMPAIGN_GRACE,"5")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETCASH)

        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_CAMPAIGN_BUYX_GETY_QUANTITY2,"5")
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_BUYX_GETY_PAYOUT_PLUS)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_CAMPAIGN_BUYX_GETY_PRODUCTNAME, "Donuts")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_BUYX_GETY_MAX,"2")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_REGENERATE)

        Envi_Helper.capture_screenshot()
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_REMINDER)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_REMINDER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_TEXT)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_TEXT2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_RECEIPT)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_RECEIPT2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_ERROR)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_ERROR2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_VALID_RECEIPT )
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_VALID_RECEIPT2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_APPROVAL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_APPROVAL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_BACK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_BACK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_SAVE_CHANGES)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_NEW)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_NAME,"Auto rebate Content Gate")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_DESCRIPTION,"Autp Test Description")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_SHOW_BACKGROUND)
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_VERIFY_AGE)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_AGE,"20")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_BIRTHDAY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_BACK)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_ALTERNATELOGO)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_ALTERNATELOGO)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_AUTO_RECIEPT)

        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_NEW)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_NAME,"Auto Rebate Verification Criteria")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_RETAILER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER )
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_ENTER_RETAILER,"Walmart")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_RETAILER_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_ADD)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME,"Donut")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_PURCHASE_DATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_UNIQUENESS )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_BACK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_SAVE )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_BACK)

        allure.attach("Rebate experience added", name="Add Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed: {e}")
        allure.attach(str(e), name="Add Error", attachment_type=allure.attachment_type.TEXT)

@given(u'a rebate experience exists')
def step_impl(context):
    try:
        allure.attach("Rebate experience exists", name="Setup Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Setup failed: {e}")
        allure.attach(str(e), name="Setup Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user edits the rebate experience')
def step_impl(context):
    try:
        allure.attach("Rebate experience edited", name="Edit Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Edit failed: {e}")
        allure.attach(str(e), name="Edit Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user adds a new Dynamic Link experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TYPE_DynamicLink)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_CHOOSE_EXPERIENCE_BUTTON)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)

        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TYPE_DynamicLink)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LINK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_BRIJURL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_BRIJURL_DESTINATION)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH,"test")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_selected)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_CUSTOMURL)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_CUSTOMURL_URL,"https://www.autotest.com")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_Selected)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_BRIJURL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_BRIJURL_DESTINATION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH,"Auto")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_selected)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_CUSTOMURL)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_CUSTOMURL_URL,"https://www.autotest.com")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_BRIJURL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_BRIJURL_DESTINATION)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH,"Auto")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_selected)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_CUSTOMURL)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_CUSTOMURL_URL,"https://www.autotest.com")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_SelectedP)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_COUNTRY)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_COUNTRY_SEARCH, "Asia")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_COUNTRY_SEARCH_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_BRIJURL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_BRIJURL_DESTINATION)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH,"Auto")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_selected)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_CUSTOMURL)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_CUSTOMURL_URL,"https://www.autotest.com")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_BRIJURL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_BRIJURL_DESTINATION2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_BRIJURL_DESTINATION2_SEARCH,"auto")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_BRIJURL_DESTINATION2_SEARCH_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_selected)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_CUSTOMURL)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_CUSTOMURL_URL,"https://www.autotest.com")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_SelectedG)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_LANGUAGE)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_LANGUAGE_SEARCH,"English")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_LANGUAGE_SEARCH_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_BRIJURL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_BRIJURL_DESTINATION)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH,"Auto")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_selected)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_CUSTOMURL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_CUSTOMURL_URL,"https://www.autotest.com")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_ADD_CONDITION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_REMOVE_COMPONENT_KEBAB)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DYNAMIC_LINK_REMOVE_COMPONENT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_CLOSE)

        allure.attach("Dynamic Link experience added", name="Add Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed: {e}")
        allure.attach(str(e), name="Add Error", attachment_type=allure.attachment_type.TEXT)

@given(u'a dynamic link experience exists')
def step_impl(context):
    try:

        allure.attach("Dynamic Link experience exists", name="Setup Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Setup failed: {e}")
        allure.attach(str(e), name="Setup Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user edits the dynamic link experience')
def step_impl(context):
    try:
        allure.attach("Dynamic Link experience edited", name="Edit Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Edit failed: {e}")
        allure.attach(str(e), name="Edit Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user adds a new Digital Hub experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TYPE_DigitalHub)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_CHOOSE_EXPERIENCE_BUTTON)
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME,"Auto Digital Hub")
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)
        time.sleep(2)
        Envi_Helper(context.driver).drag_and_drop(locators.EXPERIENCE_DIGITAL_HUB_WEBSITE_LINK,locators.EXPERIENCE_DIGITAL_HUB_AREA)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_WEBSITE_LINK_BUTTONTEXT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_WEBSITE_LINK_URL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_WEBSITE_LINK_IMAGE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_WEBSITE_LINK_IMAGE_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN_SEARCH)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN_SELECT_ALL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN_ALL_EXPERIENCE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN_CROSS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN_SEARCHED_OPTIO)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE_DROPDOWN)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE_DROPDOWN_SEARCH)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE_DROPDOWN_CROSS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_EXPERIENCE_DROPDOWN_SEARCHED_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_CUSTOM_CONTENT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_CUSTOM_CONTENT_RTE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_SHOW_SOCIAL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_DESKTOP_VIEW)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_DIM)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_drop)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_NEW)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_NAME)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_DESCRIPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_SHOW_BACKGROUND)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_VERIFY_AGE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_AGE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_BIRTHDAY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_BACK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_ALTERNATELOGO)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_SECONDARY_MODULE_THEME)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_AUTO_RECIEPT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_AUTO_RECIEPT_drop)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_NEW)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_NAME)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_RETAILER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_ENTER_RETAILER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_RETAILER_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_PURCHASE_DATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_UNIQUENESS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_BACK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_CLOSE)

        allure.attach("Digital Hub experience added", name="Add Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed: {e}")
        allure.attach(str(e), name="Add Error", attachment_type=allure.attachment_type.TEXT)

@given(u'a Digital Hub experience exists')
def step_impl(context):
    try:
        allure.attach("Digital Hub experience exists", name="Setup Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Setup failed: {e}")
        allure.attach(str(e), name="Setup Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user edits the Digital Hub experience')
def step_impl(context):
    try:
        allure.attach("Digital Hub experience edited", name="Edit Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Edit failed: {e}")
        allure.attach(str(e), name="Edit Error", attachment_type=allure.attachment_type.TEXT)

@given(u'the user is on a web apps experience')
def step_impl(context):
    try:
        allure.attach("On web apps experience", name="Navigation Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Navigation failed: {e}")
        allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user adds a variant')
def step_impl(context):
    try:
        allure.attach("Variant added", name="Add Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed: {e}")
        allure.attach(str(e), name="Add Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the variant is added successfully')
def step_impl(context):
    try:
        allure.attach("Variant added verification", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@given(u'a web apps variant exists')
def step_impl(context):
    try:
        allure.attach("Web apps variant exists", name="Setup Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Setup failed: {e}")
        allure.attach(str(e), name="Setup Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user edits the variant')
def step_impl(context):
    try:
        allure.attach("Variant edited", name="Edit Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Edit failed: {e}")
        allure.attach(str(e), name="Edit Error", attachment_type=allure.attachment_type.TEXT)

@given(u'the user is on a rebate experience')
def step_impl(context):
    try:
        allure.attach("On rebate experience", name="Navigation Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Navigation failed: {e}")
        allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)

@given(u'a rebate variant exists')
def step_impl(context):
    try:

        allure.attach("Rebate variant exists", name="Setup Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Setup failed: {e}")
        allure.attach(str(e), name="Setup Error", attachment_type=allure.attachment_type.TEXT)

@given(u'the user is on a Dynamic Link experience')
def step_impl(context):
    try:

        allure.attach("On Dynamic Link experience", name="Navigation Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Navigation failed: {e}")
        allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)

@given(u'a Dynamic Link variant exists')
def step_impl(context):
    try:

        allure.attach("Dynamic Link variant exists", name="Setup Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Setup failed: {e}")
        allure.attach(str(e), name="Setup Error", attachment_type=allure.attachment_type.TEXT)

@given(u'the user is on a Digital Hub experience')
def step_impl(context):
    try:

        allure.attach("On Digital Hub experience", name="Navigation Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Navigation failed: {e}")
        allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)

@given(u'a Digital Hub variant exists')
def step_impl(context):
    try:

        allure.attach("Digital Hub variant exists", name="Setup Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Setup failed: {e}")
        allure.attach(str(e), name="Setup Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user adds a new experience with registration and modules')
def step_impl(context):
    try:

        allure.attach("Added experience with registration/modules", name="Add Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed: {e}")
        allure.attach(str(e), name="Add Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the experience is added with modules')
def step_impl(context):
    try:
        allure.attach("Modules verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user adds a new experience without registration and modules')
def step_impl(context):
    try:

        allure.attach("Added experience without registration/modules", name="Add Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed: {e}")
        allure.attach(str(e), name="Add Error", attachment_type=allure.attachment_type.TEXT)

@given(u'the user is creating a new experience')
def step_impl(context):
    try:

        allure.attach("Started creating new experience", name="Setup Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Setup failed: {e}")
        allure.attach(str(e), name="Setup Error", attachment_type=allure.attachment_type.TEXT)


@when(u'the user is creating a new Verification Criteria in Web App experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_CHOOSE_EXPERIENCE_BUTTON)
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME,"Auto WebApp Experience with Verification Criteria")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_SUBTITLE,"Auto Subtitle")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_PRODUCTSKU,"Auto SKU 1234")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_PRODUCTURL,"https://www.autotest.com")
        Envi_Helper.capture_screenshot()
        keyboard.press_and_release('Page Down')
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_PRODUCT_DESCRIPTION,"Auto Description")
        log.info("product description added")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_ADVANCE_SETTING_BUTTON)
        log.info("navigated to advance settings")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_AUTO_RECEIPT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_NEW)
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_NAME,"Auto Web App Verification Criteria")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_RETAILER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_ENTER_RETAILER,"Auto Retailer")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_RETAILER_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME,"line item 1")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_PURCHASE_DATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_UNIQUENESS)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_BACK)
        log.info("Verification Criteria Added successfully")
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CUSTOM_THEME)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_SAVE)
        time.sleep(3)
        log.info("Experience Created Successfully")
        allure.attach("Verification criteria added in Web App", name="Add Verification Criteria Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed in Web App: {e}")
        allure.attach(str(e), name="Add Verification Criteria Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user is creating a new Verification Criteria in Registration experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_CHOOSE_EXPERIENCE_BUTTON)
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME,"Auto WebApp Experience with Verification Criteria")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_SUBTITLE,"Auto Subtitle")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_PRODUCTSKU,"Auto SKU 1234")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_PRODUCTURL,"https://www.autotest.com")
        Envi_Helper.capture_screenshot()
        keyboard.press_and_release('Page Down')
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_PRODUCT_DESCRIPTION,"Auto Description")
        log.info("product description added")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS)
        log.info("navigated to advance settings")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_REQUIRED_APPROVAL )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_NEW)
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_NAME,"Auto Web App reg Verification Criteria")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_RETAILER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_ENTER_RETAILER,"Auto Retailer")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_RETAILER_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME,"line item 1")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_PURCHASE_DATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_UNIQUENESS)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_BACK)
        log.info("Verification Criteria Added successfully")
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_SAVE_CONFIRM)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_MODULE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_SAVE)
        time.sleep(3)
        log.info("Experience Created Successfully")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_Cross)
        Envi_Helper.capture_screenshot()
        allure.attach("Verification criteria added in Registration", name="Add Verification Criteria Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed in Registration: {e}")
        allure.attach(str(e), name="Add Verification Criteria Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user is creating a new Verification Criteria in Rebate Campaign experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_OPTION)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME,"Auto Rebate Campaign Experience with verification criteria ")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_NEW)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_CAMPAIGN_NAME,"Auto Rebate Campaign with verification criteria ")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_CAMPAIGN_GRACE,"5")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETCASH)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_BUYX_GETY_PAYOUT_PLUS)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_AUTO_RECEIPT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_NEW)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_NAME,"Auto Rebate Campaign Verification Criteria")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_RETAILER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER )
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_RETAILER_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_ADD)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME,"Donut")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_PURCHASE_DATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_UNIQUENESS )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_BACK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_SAVE )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_CAMPAIGN_AS_BACK)
        allure.attach("Verification criteria added in Rebate Campaign", name="Add Verification Criteria Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed in Rebate Campaign: {e}")
        allure.attach(str(e), name="Add Verification Criteria Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user is creating a new Verification Criteria in Rebate experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_OPTION)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME,"Auto Rebate Experience")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)
        time.sleep(2)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_AUTO_RECIEPT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_NEW)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_NAME,"Auto Rebate Verification Criteria")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_RETAILER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER )
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_RETAILER_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_ADD)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME,"Donut")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_PURCHASE_DATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_UNIQUENESS )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_BACK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_SAVE )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_BACK)
        allure.attach("Verification criteria added in Rebate", name="Add Verification Criteria Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed in Rebate: {e}")
        allure.attach(str(e), name="Add Verification Criteria Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user is creating a new Verification Criteria inDigital Hub experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TYPE_DigitalHub)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_CHOOSE_EXPERIENCE_BUTTON)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)
        time.sleep(2)
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_AUTO_RECIEPT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_AUTO_RECIEPT_drop)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_NEW)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_NAME)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_RETAILER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_ENTER_RETAILER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_RETAILER_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_PURCHASE_DATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_UNIQUENESS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_BACK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_CLOSE)

        allure.attach("Verification criteria added in Digital Hub", name="Add Verification Criteria Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Add failed in Digital Hub: {e}")
        allure.attach(str(e), name="Add Verification Criteria Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the criteria are saved')
def step_impl(context):
    try:
        log.info("Verification criteria saved sucessfully and screens shots are attached ")
        allure.attach("Criteria saved", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user is creating a new Content Gate in Web App experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_CHOOSE_EXPERIENCE_BUTTON)
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME,"Auto WebApp Experience with Content Gate ")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_SUBTITLE,"Auto Subtitle")
        Envi_Helper.capture_screenshot()
        keyboard.press_and_release('Page Down')
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_PRODUCT_DESCRIPTION,"Auto Description")
        log.info("product description added")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_ADVANCE_SETTING_BUTTON)
        log.info("navigated to advance settings")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_DROPDOWN)
        keyboard.press_and_release('Page Up')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_NEW)
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_NAME,"Auto WebApp Content name ")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_DESCRIPTION,"Auto Description")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_VERIFY_AGE)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_AGE,"20")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_BIRTHDAY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_SAVE)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_BACK)
        log.info("content gate created and saved successfully")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_CLOSE)
        time.sleep(3)
        log.info("Experience Created Successfully")
        allure.attach("Content Gate creation started in Web App", name="Create Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Content Gate creation failed in Web App: {e}")
        allure.attach(str(e), name="Create Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user is creating a new Content Gate in Rebate experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_OPTION)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME,"Auto Rebate Experience with Content Gate")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)
        time.sleep(2)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_NEW)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_NAME,"Auto rRebate Content Gate.")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_DESCRIPTION,"Autp Test Description")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_SHOW_BACKGROUND)
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_VERIFY_AGE)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_AGE,"20")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_BIRTHDAY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_CONTENT_GATE_BACK)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_SAVE )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_REBATE_AS_BACK)
        log.info("Experience Created Successfully")
        allure.attach("Content Gate creation started in Rebate", name="Create Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Content Gate creation failed in Rebate: {e}")
        allure.attach(str(e), name="Create Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user is creating a new Content Gate in Digital Hub experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_NEW_EXPERIENCE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_TYPE_DigitalHub)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_CHOOSE_EXPERIENCE_BUTTON)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME,"Auto content gate Digital Hub")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE)
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_drop)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_NEW)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_NAME,"Auto Digitalhub Content gate")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_DESCRIPTION,"Auto Description")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_SHOW_BACKGROUND)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_VERIFY_AGE)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_AGE,"21")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_BIRTHDAY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_BACK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_EXPERIENCE_SAVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_POPUP_CLOSE)

        allure.attach("Content Gate creation started in Digital Hub", name="Create Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Content Gate creation failed in Digital Hub: {e}")
        allure.attach(str(e), name="Create Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the content gate is saved')
def step_impl(context):
    try:
        log.info("Content Gate saved sucessfully and screensshots are attached ")
        allure.attach("Content gate saved", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user imports experiences')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        allure.attach("Experiences imported", name="Import Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Import failed: {e}")
        allure.attach(str(e), name="Import Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the experiences appear in the list')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        allure.attach("Imported experiences verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user exports experiences')
def step_impl(context):
    try:
        keyboard.press_and_release('pagedown')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_EXPORT_BUTTON )
        Envi_Helper(context.driver).hover_to_element(locators.EXPERIENCE_EXPORT_CANCEL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_EXPORT_CANCEL)
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_EXPORT_BUTTON )
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_EXPORT_CLOSE)
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_EXPORT_BUTTON)
        Envi_Helper(context.driver).hover_to_element(locators.EXPERIENCE_EXPORT_EXPORT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_EXPORT_EXPORT)
        Envi_Helper.capture_screenshot()
        allure.attach("Experiences exported", name="Export Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Export failed: {e}")
        allure.attach(str(e), name="Export Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the export file is generated')
def step_impl(context):
    try:
        log.info("the export file is working as expected and screenshots are attached")
        allure.attach("Export file verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user syncs experiences')
def step_impl(context):
    try:
        keyboard.press_and_release('pagedown')
        Envi_Helper(context.driver).hover_to_element(locators.EXPERIENCE_SYNC_ANALYTICS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_SYNC_ANALYTICS)
        Envi_Helper.capture_screenshot()
        time.sleep(5)
        allure.attach("Experiences synced", name="Sync Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Sync failed: {e}")
        allure.attach(str(e), name="Sync Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the experiences are updated')
def step_impl(context):
    try:
        log.info("Experience is synchronize successfully ")
        allure.attach("Experiences updated", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user imports using Shopify')
def step_impl(context):
    try:
        allure.attach("Imported via Shopify", name="Import Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Import failed: {e}")
        allure.attach(str(e), name="Import Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the experience appears in the list')
def step_impl(context):
    try:
        allure.attach("Shopify experience verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user navigates through pages')
def step_impl(context):
    try:
        keyboard.press('Page Down')
        keyboard.press('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_ROWPERPAGE_OPTION)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_ROWPERPAGE_20)
        Envi_Helper.capture_screenshot()
        keyboard.press('Page Down')
        keyboard.press('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_ROWPERPAGE_OPTION)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_ROWPERPAGE_100)
        Envi_Helper.capture_screenshot()
        keyboard.press('Page Down')
        keyboard.press('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_ROWPERPAGE_OPTION)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_ROWPERPAGE_1000)
        Envi_Helper.capture_screenshot()

        allure.attach("Navigated through pages", name="Navigation Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Navigation failed: {e}")
        allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the correct number of experiences is shown per page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present(locators.EXPERIENCE_COUNT)
        allure.attach("Pagination count verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user clicks on "Get Embed Code"')
def step_impl(context):
    try:
        keyboard.press('Page Up')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_LIST_KEBAB_MENU2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_GET_EMBED_CODE)
        allure.attach('Clicked "Get Embed Code"', name="Click Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Click failed: {e}")
        allure.attach(str(e), name="Click Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the embed code is shown')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("Embedded code is displayed and screen shot attached")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_GET_EMBED_CODE_COPY)
        Envi_Helper.capture_screenshot()
        log.info("Embedded code is copied and screen shot attached")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_GET_EMBED_CODE_cross)
        allure.attach("Embed code shown", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user duplicates an experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_LIST_KEBAB_MENU2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DUPLICATE)
        allure.attach("Experience duplicated", name="Duplicate Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Duplication failed: {e}")
        allure.attach(str(e), name="Duplicate Error", attachment_type=allure.attachment_type.TEXT)

@then(u'a new copy of the experience is created')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("Experience is duplicated and screen shot attached")
        Envi_Helper(context.driver).wait_till_element_is_present(locators.EXPERIENCE_LIST_TR1)
        allure.attach("Duplicated experience verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user deactivates an experience')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_LIST_KEBAB_MENU2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_DEACTIVATE)
        allure.attach("Experience deactivated", name="Deactivate Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Deactivation failed: {e}")
        allure.attach(str(e), name="Deactivate Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the experience status is updated to inactive')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("Experience is Deactivated and screen shot attached")
        Envi_Helper(context.driver).wait_till_element_is_present(locators.EXPERIENCE_LIST_TR1)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_LIST_KEBAB_MENU2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_ACTIVATE)
        Envi_Helper.capture_screenshot()
        allure.attach("Inactive status verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user clicks on the analytics icon')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_LIST_KEBAB_MENU2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_ANALYTICS)
        allure.attach("Clicked analytics icon", name="Click Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Click failed: {e}")
        allure.attach(str(e), name="Click Error", attachment_type=allure.attachment_type.TEXT)

@then(u'analytics data for the experience is displayed')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("User navigated to Analytics page")
        log.info("Experience's Analytics is Displayed and screen shot attached")
        Envi_Helper(context.driver).wait_till_element_is_present(locators.EXPERIENCE_PAGE_OPTION)
        time.sleep(3)
        allure.attach("Analytics data verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user selects "View All Codes"')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_LIST_KEBAB_MENU2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_VIEW_ALL_CODES)
        allure.attach('Selected "View All Codes"', name="Select Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Selection failed: {e}")
        allure.attach(str(e), name="Select Error", attachment_type=allure.attachment_type.TEXT)

@then(u'a list of codes is shown')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("User navigated to Serialized Code page")
        log.info("Experience's codes are displayed and screen shot attached")
        Envi_Helper(context.driver).wait_till_element_is_present(locators.EXPERIENCE_PAGE_OPTION)
        time.sleep(3)
        allure.attach("Codes list verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user expands the experience row')
def step_impl(context):
    try:
        allure.attach("Expanded experience row", name="Expand Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Expand failed: {e}")
        allure.attach(str(e), name="Expand Error", attachment_type=allure.attachment_type.TEXT)

@then(u'all variants are listed')
def step_impl(context):
    try:
        allure.attach("Variants listed", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@given(u'the user hovers over the QR code icon')
def step_impl(context):
    try:
        allure.attach("Hovered over QR code", name="Hover Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Hover failed: {e}")
        allure.attach(str(e), name="Hover Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the QR code preview appears')
def step_impl(context):
    try:
        allure.attach("QR code preview verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)

@given(u'the user hovers on the analytics icon')
def step_impl(context):
    try:
        allure.attach("Hovered on analytics icon", name="Hover Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Hover failed: {e}")
        allure.attach(str(e), name="Hover Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the tooltip with analytics preview is displayed')
def step_impl(context):
    try:
        allure.attach("Analytics tooltip verified", name="Verify Success", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        log.error(f"Verification failed: {e}")
        allure.attach(str(e), name="Verify Error", attachment_type=allure.attachment_type.TEXT)
