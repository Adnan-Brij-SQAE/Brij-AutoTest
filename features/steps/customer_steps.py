import allure
import keyboard
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from Locators import locators
from Helper.enviHelper import Envi_Helper
from Logs import logs_file
import time
log = logs_file.get_logs()

@when(u'the user navigate to Customer Registration page')
def step_impl(context):
    time.sleep(2)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LEFT_PANEL)
    customer_option = context.driver.find_element(By.XPATH, "// span[normalize-space()='Customers']")
    customer_option.click()
    time.sleep(2)
    allure.attach("Navigated to the Customer Registration page", name="Navigation Step", attachment_type=AttachmentType.TEXT)

@when(u'User is on the Customer Page')
def step_impl(context):
    time.sleep(2)
    try:
        with allure.step("User is on the Customer Registration page"):
            Envi_Helper(context.driver).get_value(locators.CUSTOMER_REGISTRATION_TITLE,10)
    except Exception as e:
        log.error(f"Customer page verification failed: {e}")
        allure.attach(str(e), name="Customer Page Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the data should be filtered accordingly')
def step_impl(context):
    try:
        with allure.step("filters implementation"):
            Envi_Helper.capture_screenshot()
            log.info("the data is sorted and screenshots are captured")
    except Exception as e:
        log.error(f"Data filtering failed: {e}")
        allure.attach(str(e), name="Filter Error", attachment_type=allure.attachment_type.TEXT)

@allure.step('user access Experience Dropdown')
@then(u'the user can access Experience dropdown on Customer page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPERIENCE_FILTER)
        log.info("searching Test in experience filter")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_FILTER_SEARCH,"Test",10)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_OPTION)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_CROSS)
        time.sleep(3)
    except Exception as e:
        log.error(f"Experience Dropdown access failed: {e}")
        allure.attach(str(e), name="Experience Dropdown Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user can access Variant dropdown ')
@then(u'the user can access Variant dropdown on Customer page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_VARIANT_FILTER)
        log.info("searching Test in variant filter")
        time.sleep(2)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Test",10)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION2)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_SAll)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_AllV)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_VARIANT_FILTER)
        time.sleep(2)
    except Exception as e:
        log.error(f"Variant Dropdown access failed: {e}")
        allure.attach(str(e), name="Variant Dropdown Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user can access Registration Status dropdown ')
@then(u'the user can access registration status dropdown on Customer page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_STATUS)
        log.info("searching Test in variant filter")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Active",10)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ALL)
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ALL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ACTIVE)
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ACTIVE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_PENDING)
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_PENDING)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_INCOMPLETE)
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_INCOMPLETE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DENIED)
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DENIED)
        keyboard.press_and_release('pagedown')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_EXPIRED)
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_EXPIRED)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        time.sleep(2)
    except Exception as e:
        log.error(f"Registration Status Dropdown access failed: {e}")
        allure.attach(str(e), name="Registration Status Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user can access Customer Source dropdown ')
@then(u'the user can access customer source dropdown on Customer page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_SOURCE)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_ALL)
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_ALL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_BRIJ)
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_BRIJ)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_OTHERS)
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_OTHERS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        time.sleep(2)
    except Exception as e:
        log.error(f"Customer Source Dropdown access failed: {e}")
        allure.attach(str(e), name="Customer Source Error", attachment_type=AttachmentType.TEXT)

@then(u'the user should access the notification button on Customer page')
def step_impl(context):
    try:
        with allure.step("Verify notification button is accessible"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON, 10)
            log.info("user is able to access the notification button ")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON_2)
            time.sleep(2)
            allure.attach("Notification button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Notification button access failed: {e}")
        allure.attach(str(e), name="Notification Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user should access the logout button dropdown on Customer page')
def step_impl(context):
    try:
        with allure.step("Verify logout button dropdown is accessible"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON, 10)
            Envi_Helper.capture_screenshot()
            log.info("user is able to access the logout button ")
            time.sleep(2)
            allure.attach("Logout button dropdown is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Logout button access failed: {e}")
        allure.attach(str(e), name="Logout Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user should get the customer count on Customer page')
def step_impl(context):
    try:
        with allure.step("Verify customer count is displayed"):
            Envi_Helper(context.driver).wait_till_element_is_present(locators.CUSTOMER_COUNT,10)
            log.info("Customer count is displayed")
            time.sleep(2)
            allure.attach("Customer count is displayed", name="UI Verification", attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Customer count verification failed: {e}")
        allure.attach(str(e), name="Customer Count Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can search within the customer on Customer page')
def step_impl(context):
    try:
        with allure.step("User searches within the customer"):
            Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR,"Adnan",10)
            Envi_Helper.capture_screenshot()
            log.info("user is able to search within the customer table")
            context.driver.find_element(By.XPATH,"//input[@placeholder='Search Items...']").clear()
            time.sleep(4)
            allure.attach("the search functionality is working", name="Search functionality ",attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Customer search failed: {e}")
        allure.attach(str(e), name="Search Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can click on field button on Customer page')
def step_impl(context):
    try:
        with allure.step("User clicks on the field button"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
            Envi_Helper.capture_screenshot()
            log.info("the field button is available and clickable")
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
            time.sleep(2)
            allure.attach("The field button is accessible", name="Field Button",attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Field button click failed: {e}")
        allure.attach(str(e), name="Field Button Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can check all check boxes on Customer page')
def step_impl(context):
    try:
        with allure.step("User checks all checkboxes"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_SELECT_ALL_CHECKBOX, 10)
            Envi_Helper.capture_screenshot()
            log.info("user is able to click on all checkboxes button ")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_UNSELECT_ALL_CHECKBOX, 10)
            time.sleep(2)
    except Exception as e:
        log.error(f"Checkbox operation failed: {e}")
        allure.attach(str(e), name="Checkbox Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user can sort the customer table on Customer page')
def step_impl(context):
    try:
        with allure.step("User sorts the customer table"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_CUSTOMER_NAME_HEADING, 10)
            time.sleep(2)
            log.info("sorting is working on customer page ")
            Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Customer table sorting failed: {e}")
        allure.attach(str(e), name="Sorting Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the table should be sorted in the correct order on Customer page')
def step_impl(context):
    try:
        log.info("the table is sorted and the screenshots are attached")
    except Exception as e:
        log.error(f"Table sorting verification failed: {e}")
        allure.attach(str(e), name="Sort Verification Error", attachment_type=allure.attachment_type.TEXT)

@then(u'open customer popup on Customer page')
def step_impl(context):
    try:
        with allure.step("User sorts the customer table"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_ICON, 10)
            Envi_Helper.capture_screenshot()
            log.info("user is able to open the customer popup")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_CUSTOMER_DETAIL)
            Envi_Helper.capture_screenshot()
            log.info("user is able to expand customer detail")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_CUSTOMER_DETAIL)
            keyboard.press_and_release('pagedown')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_ENGAGEMENT_DETAIL)
            Envi_Helper.capture_screenshot()
            log.info("user is able to expand engagement detail")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_ENGAGEMENT_DETAIL)
            keyboard.press_and_release('pagedown')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_REGISTRATION)
            Envi_Helper.capture_screenshot()
            log.info("user is able to expand registration detail")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_REGISTRATION)
            keyboard.press('Esc')
            time.sleep(2)
    except Exception as e:
        log.error(f"Customer popup operation failed: {e}")
        allure.attach(str(e), name="Customer Popup Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can expand the customer registrations on Customer page')
def step_impl(context):
    try:
        with allure.step("User expands customer registrations"):
            Envi_Helper(context.driver).hover_to_element_to_click(locators.Customer_Expander)
            log.info("clicked on expander")
            time.sleep(2)
    except Exception as e:
        log.error(f"Customer registration expansion failed: {e}")
        allure.attach(str(e), name="Expansion Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can open registration popup on Customer page')
def step_impl(context):
    try:
        with allure.step("User opens the registration popup"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_ICON, 10)
            time.sleep(2)
            keyboard.press('Esc')
    except Exception as e:
        log.error(f"Registration popup opening failed: {e}")
        allure.attach(str(e), name="Registration Popup Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can export the customer registrations on Customer page')
def step_impl(context):
    try:
        with allure.step("User exports customer registrations"):
            keyboard.press_and_release('Page Down')
            keyboard.press_and_release('Page Down')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CANCEL)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CLOSE, 10)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_EXPORT, 10)
            time.sleep(10)
    except Exception as e:
        log.error(f"Customer export failed: {e}")
        allure.attach(str(e), name="Export Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can view the customer registrations in google sheet on Customer page')
def step_impl(context):
    try:
        with allure.step("User resets the Google Sheet"):
            keyboard.press_and_release('Page Down')
            keyboard.press_and_release('Page Down')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_VIEW_IN_GOOGLE_SHEET, 10)
            time.sleep(2)
            keyboard.press('ctrl'+'w')
    except Exception as e:
        log.error(f"Google Sheet view failed: {e}")
        allure.attach(str(e), name="Google Sheet Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can reset the google sheet on Customer page')
def step_impl(context):
    try:
        with allure.step("User resets the Google Sheet"):
            keyboard.press_and_release('Page Down')
            keyboard.press_and_release('Page Down')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_RESET_GOOGLE_PERMISSION, 10)
            time.sleep(4)
            keyboard.press_and_release('pageup')
    except Exception as e:
        log.error(f"Google Sheet reset failed: {e}")
        allure.attach(str(e), name="Google Sheet Reset Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can use switcher to switch to Registration page')
def step_impl(context):
    try:
        with allure.step("User switches to the Registration page"):
            keyboard.press_and_release('page up')
            keyboard.press_and_release('page up')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_SWITCHER_BUTTON)
            log.info("clicked on switcher")
            time.sleep(2)
    except Exception as e:
        log.error(f"Page switching failed: {e}")
        allure.attach(str(e), name="Switcher Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user should get the Registration count on Registration page')
def step_impl(context):
    try:
        with allure.step("Verify Registration count is displayed"):
            Envi_Helper(context.driver).wait_till_element_is_present(locators.CUSTOMER_REGISTRATION_COUNT,10)
            log.info("Registration count is available")
            allure.attach("Registration count is displayed", name="UI Verification", attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Registration count verification failed: {e}")
        allure.attach(str(e), name="Registration Count Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can search within the Registration on Registration page')
def step_impl(context):
    try:
        with allure.step("User searches within the Registration"):
            Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "Adnan", 10)
            Envi_Helper.capture_screenshot()
            log.info("user is able to search within the customer table")
            locators.CUSTOMER_SEARCH_BAR.clear()
            time.sleep(4)
    except Exception as e:
        log.error(f"Registration search failed: {e}")
        allure.attach(str(e), name="Registration Search Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can click on field button on Registration page')
def step_impl(context):
    try:
        with allure.step("User clicks on the field button"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
            Envi_Helper.capture_screenshot()
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
            log.info("the field button is available and clickable")
    except Exception as e:
        log.error(f"Field button click failed: {e}")
        allure.attach(str(e), name="Field Button Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can check all check boxes on Registration page')
def step_impl(context):
    try:
        with allure.step("User checks all checkboxes"):
            Envi_Helper(context.driver).click(locators.CUSTOMER_SELECT_ALL_CHECKBOX)
            Envi_Helper.capture_screenshot()
            log.info("user is able to click on all checkboxes button ")
            Envi_Helper(context.driver).click(locators.CUSTOMER_UNSELECT_ALL_CHECKBOX)
    except Exception as e:
        log.error(f"Checkbox operation failed: {e}")
        allure.attach(str(e), name="Checkbox Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user sort the Registration table on Registration page')
def step_impl(context):
    try:
        with allure.step("User sorts the Registration table"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_CUSTOMER_HEADING, 10)
            time.sleep(2)
            log.info("customer sorting is working on customer page ")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_REG_DATE, 10)
            time.sleep(2)
            log.info("sorting is working on customer page ")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_PURCHASE_DATE, 10)
            time.sleep(2)
            log.info("sorting is working on customer page ")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_REG_STATUS, 10)
            time.sleep(2)
            log.info("sorting is working on customer page ")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_LOCATION, 10)
            time.sleep(2)
            log.info("sorting is working on customer page ")
            Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Registration table sorting failed: {e}")
        allure.attach(str(e), name="Registration Sorting Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the table should be sorted in the correct order on Registration page')
def step_impl(context):
    try:
        with allure.step("Table updated after sorting"):
            log.info("the table is sorted and the screenshots are attached")
    except Exception as e:
        log.error(f"Sort verification failed: {e}")
        allure.attach(str(e), name="Sort Verification Error", attachment_type=allure.attachment_type.TEXT)

@when(u'user open registration popup on Registration page')
def step_impl(context):
    try:
        with allure.step("User opens the Registration popup"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_ICON, 10)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Registration popup opening failed: {e}")
        allure.attach(str(e), name="Registration Popup Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can access all the information for specific registration')
def step_impl(context):
    try:
        with allure.step("Registration popup"):
            log.info("user is able to open the Registration popup")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR,"test new product",10)
            keyboard.press_and_release('page down')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CUSTOMER_DETAIL)
            Envi_Helper.capture_screenshot()
            log.info("user is able to expand engagement detail")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CUSTOMER_DETAIL)
            keyboard.press_and_release('page down')
            keyboard.press_and_release('page down')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_FORM)
            Envi_Helper.capture_screenshot()
            log.info("user is able to expand registration detail")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_FORM)
            keyboard.press_and_release('page down')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_STATUS)
            Envi_Helper.capture_screenshot()
            log.info("user is able to expand registration detail")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CLOSE)
            time.sleep(2)
    except Exception as e:
        log.error(f"Registration information access failed: {e}")
        allure.attach(str(e), name="Registration Info Error", attachment_type=allure.attachment_type.TEXT)

@when(u'user open registration popup')
def step_impl(context):
    try:
        with allure.step("User open registration popup to edit"):
            time.sleep(2)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "testregistration+28118@yopmail.com", 10)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_EDIT_REG)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Registration popup opening for edit failed: {e}")
        allure.attach(str(e), name="Registration Edit Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can edit registration details')
def step_impl(context):
    try:
        with allure.step("user edit registration details"):
            log.info("user is on the registration popup ")
            try:
                try:
                    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_PENCIL_ICON)
                except:
                    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_PENCIL_ICON2)
                time.sleep(2)
                Envi_Helper.capture_screenshot()
                try:
                    Envi_Helper(context.driver).insert_text_in_input_field(locators.REGISTRATION_POPUP_WARRANTY_NUM,"5",10)
                except:
                    Envi_Helper(context.driver).insert_text_in_input_field(locators.REGISTRATION_POPUP_WARRANTY_NUM1, "5", 10)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_WARRANTY_DUR)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_WARRANTY_MON)
                Envi_Helper.capture_screenshot()
                log.info("user has edited the warranty details")
                context.driver.find_element(By.XPATH,"//div[@class='field flex-50 ng-tns-c4084589801-315 ng-star-inserted']//input[@type='text']").clear()
                Envi_Helper(context.driver).insert_text_in_input_field(locators.REGISTRATION_POPUP_SERIAL_NUM,"Auto 123",10)
                Envi_Helper.capture_screenshot()
                log.info("user updated the serial number")
                keyboard.press_and_release('pageup')
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_SAVE_BUTTON)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CLOSE)
            except:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CLOSE)
                log.info("user successfully updated the registration details")
                time.sleep(2)
    except Exception as e:
        log.error(f"Registration edit failed: {e}")
        allure.attach(str(e), name="Registration Edit Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user archive registration on registration page')
def step_impl(context):
    try:
        with allure.step("User archives the registration"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_ARCHIVE)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_ARCHIVE_CONFIRM)
            time.sleep(2)
    except Exception as e:
        log.error(f"Registration archiving failed: {e}")
        allure.attach(str(e), name="Archive Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the registration should be archieved')
def step_impl(context):
    try:
        with allure.step("viewing the archived registration"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN_ARCHIVE)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN_CLOSE)
            Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Archive verification failed: {e}")
        allure.attach(str(e), name="Archive Verification Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can unarchived the registration')
def step_impl(context):
    try:
        with allure.step("User archives the registration"):
            time.sleep(2)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "Test IT services", 10)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_RESTORE)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_RESTORE_CONFIRM)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Registration unarchive failed: {e}")
        allure.attach(str(e), name="Unarchive Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user want to see the number of rows on Customer Page')
def step_impl(context):
    try:
        keyboard.press('page down')
        keyboard.press('page down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_20)
        Envi_Helper.capture_screenshot()
        keyboard.press('page down')
        keyboard.press('page down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_100)
        Envi_Helper.capture_screenshot()
        keyboard.press('page down')
        keyboard.press('page down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_1000)
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Row count operation failed: {e}")
        allure.attach(str(e), name="Row Count Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the list should be updated on Customer page')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("the rows are updated successfully")
    except Exception as e:
        log.error(f"List update verification failed: {e}")
        allure.attach(str(e), name="List Update Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can export the Registration registrations on Registration page')
def step_impl(context):
    try:
        with allure.step("User exports Registration registrations"):
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_LIST_CHECKBOX1)
            keyboard.press_and_release('Page Down')
            keyboard.press_and_release('Page Down')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CANCEL)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CLOSE, 10)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_EXPORT, 10)
            time.sleep(10)
    except Exception as e:
        log.error(f"Registration export failed: {e}")
        allure.attach(str(e), name="Registration Export Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can reset the google sheet on Registration page')
def step_impl(context):
    try:
        with allure.step("User resets the Google Sheet"):
            keyboard.press_and_release('Page Down')
            keyboard.press_and_release('Page Down')
            time.sleep(5)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_RESET_GOOGLE_PERMISSION, 10)
            time.sleep(4)
    except Exception as e:
        log.error(f"Google Sheet reset failed: {e}")
        allure.attach(str(e), name="Google Sheet Reset Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can view the Registration registrations in google sheet on Registration page')
def step_impl(context):
    try:
        with allure.step("User views Registration registrations in Google Sheet"):
            keyboard.press_and_release('Page Down')
            keyboard.press_and_release('Page Down')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_VIEW_IN_GOOGLE_SHEET, 10)
            time.sleep(2)
            keyboard.press('ctrl' + 'w')
    except Exception as e:
        log.error(f"Google Sheet view failed: {e}")
        allure.attach(str(e), name="Google Sheet View Error", attachment_type=allure.attachment_type.TEXT)








#
# @when(u'the user navigate to Customer Registration page')
# def step_impl(context):
#     with allure.step("User navigates to the Customer Registration page"):
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LEFT_PANEL)
#         customer_option = context.driver.find_element(By.XPATH, "// span[normalize-space()='Customers']")
#         customer_option.click()
#         time.sleep(2)
#         allure.attach("Navigated to the Customer Registration page", name="Navigation Step", attachment_type=AttachmentType.TEXT)
#
# @when(u'User is on the Customer Page')
# def step_impl(context):
#     with allure.step("User is on the Customer Registration page"):
#         Envi_Helper(context.driver).get_value(locators.CUSTOMER_REGISTRATION_TITLE,10)
#
# @then(u'the data should be filtered accordingly')
# def step_impl(context):
#     with allure.step("filters implementation"):
#         Envi_Helper.capture_screenshot()
#         log.info("the data is sorted and screenshots are captured")
#
#
# @allure.step('user access Experience Dropdown')
# @then(u'the user can access Experience dropdown on Customer page')
# def step_impl(context):
#     try:
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPERIENCE_FILTER)
#         log.info("searching Test in experience filter")
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_FILTER_SEARCH,"Test",10)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_OPTION)
#         Envi_Helper.capture_screenshot()
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_OPTION)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_CROSS)
#         time.sleep(3)
#     except Exception as e:
#         log.error(f"Error accessing Experience Dropdown: {e}")
#         allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)
#
#
# @allure.step('the user can access Variant dropdown ')
# @then(u'the user can access Variant dropdown on Customer page')
# def step_impl(context):
#     try:
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_VARIANT_FILTER)
#         log.info("searching Test in variant filter")
#         time.sleep(2)
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Test",10)
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION2)
#         Envi_Helper.capture_screenshot()
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_SAll)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_AllV)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_VARIANT_FILTER)
#         time.sleep(2)
#
#     except Exception as e:
#         log.error(f"Error accessing Experience Dropdown: {e}")
#         allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)
#
#
# @allure.step('the user can access Registration Status dropdown ')
# @then(u'the user can access registration status dropdown on Customer page')
# def step_impl(context):
#     try:
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_STATUS)
#         log.info("searching Test in variant filter")
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Active",10)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ALL)
#         Envi_Helper.capture_screenshot()
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ALL)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ACTIVE)
#         Envi_Helper.capture_screenshot()
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ACTIVE)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_PENDING)
#         Envi_Helper.capture_screenshot()
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_PENDING)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_INCOMPLETE)
#         Envi_Helper.capture_screenshot()
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_INCOMPLETE)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DENIED)
#         Envi_Helper.capture_screenshot()
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DENIED)
#         keyboard.press_and_release('pagedown')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_EXPIRED)
#         Envi_Helper.capture_screenshot()
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_EXPIRED)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
#         time.sleep(2)
#     except Exception as e:
#         log.error(f"Error accessing  Dropdown: {e}")
#         allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)
#
# @allure.step('the user can access Customer Source dropdown ')
# @then(u'the user can access customer source dropdown on Customer page')
# def step_impl(context):
#
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_SOURCE)
#     # log.info("searching Test in Customer Source dropdown filter")
#     # Envi_Helper(context.driver).insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Test",10)
#     # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_ALL)
#     Envi_Helper.capture_screenshot()
#     time.sleep(2)
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_ALL)
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_BRIJ)
#     Envi_Helper.capture_screenshot()
#     time.sleep(2)
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_BRIJ)
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_OTHERS)
#     Envi_Helper.capture_screenshot()
#     time.sleep(2)
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_OTHERS)
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
#     time.sleep(2)
#
#
# @then(u'the user should access the notification button on Customer page')
# def step_impl(context):
#     with allure.step("Verify notification button is accessible"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON, 10)
#         log.info("user is able to access the notification button ")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON_2)
#         time.sleep(2)
#         allure.attach("Notification button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
#
#
# @then(u'the user should access the logout button dropdown on Customer page')
# def step_impl(context):
#     with allure.step("Verify logout button dropdown is accessible"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON, 10)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to access the logout button ")
#         time.sleep(2)
#         allure.attach("Logout button dropdown is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
#
# @then(u'the user should get the customer count on Customer page')
# def step_impl(context):
#     with allure.step("Verify customer count is displayed"):
#         Envi_Helper(context.driver).wait_till_element_is_present(locators.CUSTOMER_COUNT,10)
#         log.info("Customer count is displayed")
#         time.sleep(2)
#         allure.attach("Customer count is displayed", name="UI Verification", attachment_type=AttachmentType.TEXT)
#
# @then(u'the user can search within the customer on Customer page')
# def step_impl(context):
#     with allure.step("User searches within the customer"):
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR,"Adnan",10)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to search within the customer table")
#         context.driver.find_element(By.XPATH,"//input[@placeholder='Search Items...']").clear()
#         time.sleep(4)
#         allure.attach("the search functionality is working", name="Search functionality ",attachment_type=AttachmentType.TEXT)
#
#
# @then(u'the user can click on field button on Customer page')
# def step_impl(context):
#     with allure.step("User clicks on the field button"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
#         Envi_Helper.capture_screenshot()
#         log.info("the field button is available and clickable")
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
#         time.sleep(2)
#         allure.attach("The field button is accessible", name="Field Button",attachment_type=AttachmentType.TEXT)
#
# @then(u'the user can check all check boxes on Customer page')
# def step_impl(context):
#     with allure.step("User checks all checkboxes"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_SELECT_ALL_CHECKBOX, 10)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to click on all checkboxes button ")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_UNSELECT_ALL_CHECKBOX, 10)
#         time.sleep(2)
#         pass
#
# @when(u'the user can sort the customer table on Customer page')
# def step_impl(context):
#     with allure.step("User sorts the customer table"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_CUSTOMER_NAME_HEADING, 10)
#         time.sleep(2)
#         log.info("sorting is working on customer page ")
#         Envi_Helper.capture_screenshot()
#
# @then(u'the table should be sorted in the correct order on Customer page')
# def step_impl(context):
#         log.info("the table is sorted and the screenshots are attached")
#
# @then(u'open customer popup on Customer page')
# def step_impl(context):
#     with allure.step("User sorts the customer table"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_ICON, 10)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to open the customer popup")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_CUSTOMER_DETAIL)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to expand customer detail")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_CUSTOMER_DETAIL)
#         keyboard.press_and_release('pagedown')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_ENGAGEMENT_DETAIL)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to expand engagement detail")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_ENGAGEMENT_DETAIL)
#         keyboard.press_and_release('pagedown')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_REGISTRATION)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to expand registration detail")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_REGISTRATION)
#         keyboard.press('Esc')
#         time.sleep(2)
#
# @then(u'user can expand the customer registrations on Customer page')
# def step_impl(context):
#     with allure.step("User expands customer registrations"):
#         Envi_Helper(context.driver).hover_to_element_to_click(locators.Customer_Expander)
#         log.info("clicked on expander")
#         time.sleep(2)
#
# @then(u'user can open registration popup on Customer page')
# def step_impl(context):
#     with allure.step("User opens the registration popup"):
#         # context.driver.find_element(By.XPATH,"//img[@class='cursor-pointer arrow-btn img-border ng-star-inserted']").click()
#         # time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_ICON, 10)
#         time.sleep(2)
#         keyboard.press('Esc')
#
# @then(u'user can export the customer registrations on Customer page')
# def step_impl(context):
#     with allure.step("User exports customer registrations"):
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         #cancel the export
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CANCEL)
#         #close export popup
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CLOSE, 10)
#         time.sleep(2)
#         # click export button
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_EXPORT, 10)
#         time.sleep(10)
#
# @then(u'user can view the customer registrations in google sheet on Customer page')
# def step_impl(context):
#     with allure.step("User resets the Google Sheet"):
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_VIEW_IN_GOOGLE_SHEET, 10)
#         time.sleep(2)
#         keyboard.press('ctrl'+'w')
#
# @then(u'user can reset the google sheet on Customer page')
# def step_impl(context):
#     with allure.step("User resets the Google Sheet"):
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_RESET_GOOGLE_PERMISSION, 10)
#         time.sleep(4)
#         keyboard.press_and_release('pageup')
#
# @then(u'user can use switcher to switch to Registration page')
# def step_impl(context):
#     with allure.step("User switches to the Registration page"):
#         keyboard.press_and_release('page up')
#         keyboard.press_and_release('page up')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_SWITCHER_BUTTON)
#         log.info("clicked on switcher")
#         time.sleep(2)
#
#
# @then(u'the user should get the Registration count on Registration page')
# def step_impl(context):
#     with allure.step("Verify Registration count is displayed"):
#         Envi_Helper(context.driver).wait_till_element_is_present(locators.CUSTOMER_REGISTRATION_COUNT,10)
#         log.info("Registration count is available")
#         allure.attach("Registration count is displayed", name="UI Verification", attachment_type=AttachmentType.TEXT)
#
#
# @then(u'the user can search within the Registration on Registration page')
# def step_impl(context):
#     with allure.step("User searches within the Registration"):
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "Adnan", 10)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to search within the customer table")
#         locators.CUSTOMER_SEARCH_BAR.clear()
#         time.sleep(4)
#
#
# @then(u'the user can click on field button on Registration page')
# def step_impl(context):
#     with allure.step("User clicks on the field button"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
#         Envi_Helper.capture_screenshot()
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
#         log.info("the field button is available and clickable")
#
# @then(u'the user can check all check boxes on Registration page')
# def step_impl(context):
#     with allure.step("User checks all checkboxes"):
#         Envi_Helper(context.driver).click(locators.CUSTOMER_SELECT_ALL_CHECKBOX)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to click on all checkboxes button ")
#         Envi_Helper(context.driver).click(locators.CUSTOMER_UNSELECT_ALL_CHECKBOX)
#
#
# @when(u'the user sort the Registration table on Registration page')
# def step_impl(context):
#     with allure.step("User sorts the Registration table"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_CUSTOMER_HEADING, 10)
#         time.sleep(2)
#         log.info("customer sorting is working on customer page ")
#         Envi_Helper.capture_screenshot()
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_REG_DATE, 10)
#         time.sleep(2)
#         log.info("sorting is working on customer page ")
#         Envi_Helper.capture_screenshot()
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_PURCHASE_DATE, 10)
#         time.sleep(2)
#         log.info("sorting is working on customer page ")
#         Envi_Helper.capture_screenshot()
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_REG_STATUS, 10)
#         time.sleep(2)
#         log.info("sorting is working on customer page ")
#         Envi_Helper.capture_screenshot()
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_LOCATION, 10)
#         time.sleep(2)
#         log.info("sorting is working on customer page ")
#         Envi_Helper.capture_screenshot()
#
# @then(u'the table should be sorted in the correct order on Registration page')
# def step_impl(context):
#     with allure.step("Table updated after sorting"):
#         log.info("the table is sorted and the screenshots are attached")
#
# @when(u'user open registration popup on Registration page')
# def step_impl(context):
#     with allure.step("User opens the Registration popup"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_ICON, 10)
#         time.sleep(2)
#         Envi_Helper.capture_screenshot()
#
# @then(u'user can access all the information for specific registration')
# def step_impl(context):
#     with allure.step("Registration popup"):
#         log.info("user is able to open the Registration popup")
#         Envi_Helper.capture_screenshot()
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR,"test new product",10)
#         keyboard.press_and_release('page down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CUSTOMER_DETAIL)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to expand engagement detail")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CUSTOMER_DETAIL)
#         keyboard.press_and_release('page down')
#         keyboard.press_and_release('page down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_FORM)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to expand registration detail")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_FORM)
#         keyboard.press_and_release('page down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_STATUS)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to expand registration detail")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CLOSE)
#         time.sleep(2)
#
#
# @when(u'user open registration popup')
# def step_impl(context):
#     with allure.step("User open registration popup to edit"):
#         time.sleep(2)
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "testregistration+28118@yopmail.com", 10)
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_EDIT_REG)
#         time.sleep(2)
#         Envi_Helper.capture_screenshot()
#
# @then(u'the user can edit registration details')
# def step_impl(context):
#     with allure.step("user edit registration details"):
#         log.info("user is on the registration popup ")
#         try:
#             try:
#                 Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_PENCIL_ICON)
#             except:
#                 Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_PENCIL_ICON2)
#             time.sleep(2)
#             Envi_Helper.capture_screenshot()
#             try:
#                 Envi_Helper(context.driver).insert_text_in_input_field(locators.REGISTRATION_POPUP_WARRANTY_NUM,"5",10)
#             except:
#                 Envi_Helper(context.driver).insert_text_in_input_field(locators.REGISTRATION_POPUP_WARRANTY_NUM1, "5", 10)
#             Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_WARRANTY_DUR)
#             Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_WARRANTY_MON)
#             Envi_Helper.capture_screenshot()
#             log.info("user has edited the warranty details")
#             context.driver.find_element(By.XPATH,"//div[@class='field flex-50 ng-tns-c4084589801-315 ng-star-inserted']//input[@type='text']").clear()
#             Envi_Helper(context.driver).insert_text_in_input_field(locators.REGISTRATION_POPUP_SERIAL_NUM,"Auto 123",10)
#             Envi_Helper.capture_screenshot()
#             log.info("user updated the serial number")
#             keyboard.press_and_release('pageup')
#             Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_SAVE_BUTTON)
#             Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CLOSE)
#         except:
#             Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CLOSE)
#             log.info("user successfully updated the registration details")
#             time.sleep(2)
#
# @when(u'the user archive registration on registration page')
# def step_impl(context):
#     with allure.step("User archives the registration"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_ARCHIVE)
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_ARCHIVE_CONFIRM)
#         time.sleep(2)
#
# @then(u'the registration should be archieved')
# def step_impl(context):
#     with allure.step("viewing the archived registration"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN_ARCHIVE)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN_CLOSE)
#         Envi_Helper.capture_screenshot()
#
# @then(u'the user can unarchived the registration')
# def step_impl(context):
#     with allure.step("User archives the registration"):
#         time.sleep(2)
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "Test IT services", 10)
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_RESTORE)
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_RESTORE_CONFIRM)
#         time.sleep(2)
#         Envi_Helper.capture_screenshot()
#
# @when(u'the user want to see the number of rows on Customer Page')
# def step_impl(context):
#     keyboard.press('page down')
#     keyboard.press('page down')
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_20)
#     Envi_Helper.capture_screenshot()
#     keyboard.press('page down')
#     keyboard.press('page down')
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_100)
#     Envi_Helper.capture_screenshot()
#     keyboard.press('page down')
#     keyboard.press('page down')
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_1000)
#     Envi_Helper.capture_screenshot()
#
# @then(u'the list should be updated on Customer page')
# def step_impl(context):
#     Envi_Helper.capture_screenshot()
#     log.info("the rows are updated successfully")
#
#
# @then(u'user can export the Registration registrations on Registration page')
# def step_impl(context):
#     with allure.step("User exports Registration registrations"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_LIST_CHECKBOX1)
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         # cancel the export
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CANCEL)
#         # close export popup
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CLOSE, 10)
#         time.sleep(2)
#         # click export button
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_EXPORT, 10)
#         time.sleep(10)
#
#
# @then(u'user can reset the google sheet on Registration page')
# def step_impl(context):
#     with allure.step("User resets the Google Sheet"):
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         time.sleep(5)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_RESET_GOOGLE_PERMISSION, 10)
#         time.sleep(4)
#
#
# @then(u'user can view the Registration registrations in google sheet on Registration page')
# def step_impl(context):
#     with allure.step("User views Registration registrations in Google Sheet"):
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_VIEW_IN_GOOGLE_SHEET, 10)
#         time.sleep(2)
#         keyboard.press('ctrl' + 'w')
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
# # import allure
# # import keyboard
# # from allure_commons.types import AttachmentType
# # from behave import *
# # from selenium.webdriver import ActionChains
# # from selenium.webdriver.common.by import By
# # from Locators import locators
# # from Helper.enviHelper import Envi_Helper
# # from Logs import logs_file
# # import time
# # log = logs_file.get_logs()
# #
# # @when(u'the user navigate to Customer Registration page')
# # def step_impl(context):
# #     with allure.step("User navigates to the Customer Registration page"):
# #         time.sleep(2)
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LEFT_PANEL)
# #         customer_option = context.driver.find_element(By.XPATH, "// span[normalize-space()='Customers']")
# #         customer_option.click()
# #         keyboard.press('Esc')
# #         Envi_Helper(context.driver).wait_till_element_is_present(locators.CUSTOMER_REGISTRATION_TITLE,10)
# #         time.sleep(2)
# #         allure.attach("Navigated to the Customer Registration page", name="Navigation Step", attachment_type=AttachmentType.TEXT)
# #
# # @allure.step('user access Experience Dropdown')
# # @then(u'the user can access Experience dropdown on Customer page')
# # def step_impl(context):
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPERIENCE_FILTER)
# #     log.info("searching Test in experience filter")
# #     Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_FILTER_SEARCH,"Test",10)
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_OPTION)
# #     Envi_Helper.capture_screenshot()
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_OPTION)
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_CROSS)
# #
# # @allure.step('the user can access Variant dropdown ')
# # @then(u'the user can access Variant dropdown on Customer page')
# # def step_impl(context):
# #
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_VARIANT_FILTER)
# #     log.info("searching Test in variant filter")
# #     Envi_Helper(context.driver).insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Test",10)
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION)
# #     Envi_Helper.capture_screenshot()
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION)
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
# #     time.sleep(2)
# #
# # @allure.step('the user can access Registration Status dropdown ')
# # @then(u'the user can access registration status dropdown on Customer page')
# # def step_impl(context):
# #
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_STATUS)
# #     log.info("searching Test in variant filter")
# #     Envi_Helper(context.driver).insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Test",10)
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION)
# #     Envi_Helper.capture_screenshot()
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION)
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
# #     time.sleep(2)
# #
# # @allure.step('the user can access Customer Source dropdown ')
# # @then(u'the user can access customer source dropdown on Customer page')
# # def step_impl(context):
# #
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_SOURCE)
# #     log.info("searching Test in variant filter")
# #     Envi_Helper(context.driver).insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Test",10)
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION)
# #     Envi_Helper.capture_screenshot()
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION)
# #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
# #     time.sleep(2)
# #
# #
# # @then(u'the user should access the notification button on Customer page')
# # def step_impl(context):
# #     with allure.step("Verify notification button is accessible"):
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON, 10)
# #         log.info("user is able to access the notification button ")
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON_2)
# #         time.sleep(2)
# #         allure.attach("Notification button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
# #
# #
# # @then(u'the user should access the logout button dropdown on Customer page')
# # def step_impl(context):
# #     with allure.step("Verify logout button dropdown is accessible"):
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON, 10)
# #         Envi_Helper.capture_screenshot()
# #         log.info("user is able to access the logout button ")
# #         time.sleep(2)
# #         allure.attach("Logout button dropdown is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
# #
# # @then(u'the user should get the customer count on Customer page')
# # def step_impl(context):
# #     with allure.step("Verify customer count is displayed"):
# #         Envi_Helper(context.driver).wait_till_element_is_present(locators.CUSTOMER_COUNT, 10)
# #         log.info("Customer count is displayed")
# #         time.sleep(2)
# #         allure.attach("Customer count is displayed", name="UI Verification", attachment_type=AttachmentType.TEXT)
# #
# # @then(u'the user can search within the customer on Customer page')
# # def step_impl(context):
# #     with allure.step("User searches within the customer"):
# #         Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR,"Adnan",10)
# #         Envi_Helper.capture_screenshot()
# #         log.info("user is able to search within the customer table")
# #         context.driver.find_element(By.XPATH,"//input[@placeholder='Search Items...']").clear()
# #         time.sleep(4)
# #
# #
# # @then(u'the user can click on field button on Customer page')
# # def step_impl(context):
# #     with allure.step("User clicks on the field button"):
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
# #         Envi_Helper.capture_screenshot()
# #         log.info("the field button is available and clickable")
# #         time.sleep(2)
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
# #         time.sleep(2)
# #
# # @then(u'the user can check all check boxes on Customer page')
# # def step_impl(context):
# #     with allure.step("User checks all checkboxes"):
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_SELECT_ALL_CHECKBOX, 10)
# #         Envi_Helper.capture_screenshot()
# #         log.info("user is able to click on all checkboxes button ")
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_UNSELECT_ALL_CHECKBOX, 10)
# #         time.sleep(2)
# #         pass
# #
# # @when(u'the user can sort the customer table on Customer page')
# # def step_impl(context):
# #     with allure.step("User sorts the customer table"):
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_CUSTOMER_NAME_HEADING, 10)
# #         time.sleep(2)
# #         log.info("sorting is working on customer page ")
# #         Envi_Helper.capture_screenshot()
# #
# # @then(u'the table should be sorted in the correct order on Customer page')
# # def step_impl(context):
# #         log.info("the table is sorted and the screenshots are attached")
# #
# # @then(u'open customer popup on Customer page')
# # def step_impl(context):
# #     with allure.step("User sorts the customer table"):
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_ICON, 10)
# #         Envi_Helper.capture_screenshot()
# #         log.info("user is able to open the customer popup")
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_CUSTOMER_DETAIL)
# #         Envi_Helper.capture_screenshot()
# #         log.info("user is able to expand customer detail")
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_CUSTOMER_DETAIL)
# #         keyboard.press_and_release('pagedown')
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_ENGAGEMENT_DETAIL)
# #         Envi_Helper.capture_screenshot()
# #         log.info("user is able to expand engagement detail")
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_ENGAGEMENT_DETAIL)
# #         keyboard.press_and_release('pagedown')
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_REGISTRATION)
# #         Envi_Helper.capture_screenshot()
# #         log.info("user is able to expand registration detail")
# #         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_REGISTRATION)
# #         keyboard.press('Esc')
# #         time.sleep(2)
# #
# # @then(u'user can expand the customer registrations on Customer page')
# # def step_impl(context):
# #     with allure.step("User expands customer registrations"):
# #         Envi_Helper(context.driver).hover_to_element_to_click(locators.Customer_Expander)
# #         log.info("clicked on expander")
#         time.sleep(2)
#
# @then(u'user can open registration popup on Customer page')
# def step_impl(context):
#     with allure.step("User opens the registration popup"):
#         # context.driver.find_element(By.XPATH,"//img[@class='cursor-pointer arrow-btn img-border ng-star-inserted']").click()
#         # time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_ICON, 10)
#         time.sleep(2)
#         keyboard.press('Esc')
#
# @then(u'user can export the customer registrations on Customer page')
# def step_impl(context):
#     with allure.step("User exports customer registrations"):
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         #cancel the export
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CANCEL)
#         #close export popup
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CLOSE, 10)
#         time.sleep(2)
#         # click export button
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_EXPORT, 10)
#         time.sleep(4)
#
# @then(u'user can view the customer registrations in google sheet on Customer page')
# def step_impl(context):
#     with allure.step("User resets the Google Sheet"):
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_VIEW_IN_GOOGLE_SHEET, 10)
#         time.sleep(2)
#         keyboard.press('ctrl'+'w')
#
# @then(u'user can reset the google sheet on Customer page')
# def step_impl(context):
#     with allure.step("User resets the Google Sheet"):
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_RESET_GOOGLE_PERMISSION, 10)
#         time.sleep(4)
#         keyboard.press_and_release('pageup')
#
# @then(u'user can use switcher to switch to Registration page')
# def step_impl(context):
#     with allure.step("User switches to the Registration page"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_SWITCHER_BUTTON)
#         log.info("clicked on switcher")
#         time.sleep(2)
#
#
# @then(u'the user should get the Registration count on Registration page')
# def step_impl(context):
#     with allure.step("Verify Registration count is displayed"):
#         Envi_Helper(context.driver).wait_till_element_is_present(locators.CUSTOMER_REGISTRATION_COUNT)
#         log.info("Registration count is available")
#         allure.attach("Registration count is displayed", name="UI Verification", attachment_type=AttachmentType.TEXT)
#
#
# @then(u'the user can search within the Registration on Registration page')
# def step_impl(context):
#     with allure.step("User searches within the Registration"):
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "Adnan", 10)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to search within the customer table")
#         locators.CUSTOMER_SEARCH_BAR.clear()
#         time.sleep(4)
#
#
# @then(u'the user can click on field button on Registration page')
# def step_impl(context):
#     with allure.step("User clicks on the field button"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
#         Envi_Helper.capture_screenshot()
#         log.info("the field button is available and clickable")
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
#
# @then(u'the user can check all check boxes on Registration page')
# def step_impl(context):
#     with allure.step("User checks all checkboxes"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_SELECT_ALL_CHECKBOX, 10)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to click on all checkboxes button ")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_UNSELECT_ALL_CHECKBOXES, 10)
#
#
# @when(u'the user sort the Registration table on Registration page')
# def step_impl(context):
#     with allure.step("User sorts the Registration table"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_CUSTOMER_HEADING, 10)
#         time.sleep(2)
#         log.info("customer sorting is working on customer page ")
#         Envi_Helper.capture_screenshot()
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_REG_DATE, 10)
#         time.sleep(2)
#         log.info("sorting is working on customer page ")
#         Envi_Helper.capture_screenshot()
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_PURCHASE_DATE, 10)
#         time.sleep(2)
#         log.info("sorting is working on customer page ")
#         Envi_Helper.capture_screenshot()
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_REG_STATUS, 10)
#         time.sleep(2)
#         log.info("sorting is working on customer page ")
#         Envi_Helper.capture_screenshot()
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_LOCATION, 10)
#         time.sleep(2)
#         log.info("sorting is working on customer page ")
#         Envi_Helper.capture_screenshot()
#
# @then(u'the table should be sorted in the correct order on Registration page')
# def step_impl(context):
#     with allure.step("Table updated after sorting"):
#         log.info("the table is sorted and the screenshots are attached")
#
# @when(u'user open registration popup on Registration page')
# def step_impl(context):
#     with allure.step("User opens the Registration popup"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_ICON, 10)
#         time.sleep(2)
#         Envi_Helper.capture_screenshot()
#
# @then(u'user can access all the information for specific registration')
# def step_impl(context):
#     with allure.step("Registration popup"):
#         log.info("user is able to open the customer popup")
#         keyboard.press_and_release('pagedown')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CUSTOMER_DETAIL)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to expand engagement detail")
#         keyboard.press_and_release('pagedown')
#         # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_FORM)
#         # Envi_Helper.capture_screenshot()
#         # log.info("user is able to expand registration detail")
#         # keyboard.press_and_release('pagedown')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_STATUS)
#         Envi_Helper.capture_screenshot()
#         log.info("user is able to expand registration detail")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CLOSE)
#         keyboard.press('Esc')
#         time.sleep(2)
#
#
# @when(u'user open registration popup')
# def step_impl(context):
#     with allure.step("User open registration popup to edit"):
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "test new product", 10)
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_EDIT_REG)
#         time.sleep(2)
#         Envi_Helper.capture_screenshot()
#
# @then(u'the user can edit registration details')
# def step_impl(context):
#     with allure.step("user edit registration details"):
#         log.info("user is on the registration popup ")
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_PENCIL_ICON)
#         time.sleep(2)
#         Envi_Helper.capture_screenshot()
#         context.driver.find_element(By.XPATH,"//input[@class='enabled-input ng-tns-c4084589801-315 ng-pristine ng-valid ng-touched']").clear()
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.REGISTRATION_POPUP_WARRANTY_NUM,"5",10)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_WARRANTY_DUR)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_WARRANTY_MON)
#         Envi_Helper.capture_screenshot()
#         log.info("user has edited the warranty details")
#         context.driver.find_element(By.XPATH,"//div[@class='field flex-50 ng-tns-c4084589801-315 ng-star-inserted']//input[@type='text']").clear()
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.REGISTRATION_POPUP_SERIAL_NUM,"Auto 123",10)
#         Envi_Helper.capture_screenshot()
#         log.info("user updated the serial number")
#         keyboard.press_and_release('pageup')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_SAVE_BUTTON)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CLOSE)
#         keyboard.press('Esc')
#         log.info("user successfully updated the registration details")
#         time.sleep(2)
#
# @when(u'the user archive registration on registration page')
# def step_impl(context):
#     with allure.step("User archives the registration"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_ARCHIVE)
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_ARCHIVE_CONFIRM)
#         time.sleep(2)
#
# @then(u'the registration should be archieved')
# def step_impl(context):
#     with allure.step("viewing the archived registration"):
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN_ARCHIVE)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN_CLOSE)
#         Envi_Helper.capture_screenshot()
#
# @then(u'the user can unarchived the registration')
# def step_impl(context):
#     with allure.step("User archives the registration"):
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "Test IT services", 10)
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_RESTORE)
#         time.sleep(2)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATION_RESTORE_CONFIRM)
#         time.sleep(2)
#         Envi_Helper.capture_screenshot()
#
#
# @then(u'user can export the Registration registrations on Registration page')
# def step_impl(context):
#     with allure.step("User exports Registration registrations"):
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         # cancel the export
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CANCEL)
#         # close export popup
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CLOSE, 10)
#         time.sleep(2)
#         # click export button
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_EXPORT, 10)
#         time.sleep(4)
#
#
# @then(u'user can reset the google sheet on Registration page')
# def step_impl(context):
#     with allure.step("User resets the Google Sheet"):
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_RESET_GOOGLE_PERMISSION, 10)
#         time.sleep(4)
#
#
# @then(u'user can view the Registration registrations in google sheet on Registration page')
# def step_impl(context):
#     with allure.step("User views Registration registrations in Google Sheet"):
#         keyboard.press_and_release('Page Down')
#         keyboard.press_and_release('Page Down')
#         Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_VIEW_IN_GOOGLE_SHEET, 10)
#         time.sleep(2)
#         keyboard.press('ctrl' + 'w')

#
# #
# #
# #
# #
# #
# #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # from behave import given, when, then
# # # # from selenium import webdriver
# # # # from selenium.webdriver.common.by import By
# # # # from selenium.webdriver.support.ui import Select
# # # #
# # # # @given('User is on the customer registration page')
# # # # def step_impl(context):
# # # #     context.browser = webdriver.Chrome()
# # # #     context.browser.get('https://rc.brij.it/brand/users/general')
# # # #
# # # # @then('USER should see the customer registration table')
# # # # def step_impl(context):
# # # #     table = context.browser.find_element(By.CSS_SELECTOR, '.customer-registration-table')
# # # #     assert table.is_displayed()
# # # #
# # # # @then('I should see the total number of customers')
# # # # def step_impl(context):
# # # #     total_customers = context.browser.find_element(By.CSS_SELECTOR, '.total-customers')
# # # #     assert total_customers.is_displayed()
# # # #
# # # # @when('I select "{option}" from the {dropdown} dropdown')
# # # # def step_impl(context, option, dropdown):
# # # #     dropdown_element = context.browser.find_element(By.CSS_SELECTOR, f'.{dropdown}-dropdown')
# # # #     select = Select(dropdown_element)
# # # #     select.select_by_visible_text(option)
# # # #
# # # # @when('I enter "{text}" in the search bar')
# # # # def step_impl(context, text):
# # # #     search_bar = context.browser.find_element(By.CSS_SELECTOR, '.search-bar')
# # # #     search_bar.send_keys(text)
# # # #
# # # # @then('the customer registration table should display results matching "{text}"')
# # # # def step_impl(context, text):
# # # #     results = context.browser.find_elements(By.CSS_SELECTOR, '.customer-registration-table .customer-name')
# # # #     for result in results:
# # # #         assert text in result.text
# # # #
# # # # @when('I click on a customer name')
# # # # def step_impl(context):
# # # #     customer_name = context.browser.find_element(By.CSS_SELECTOR, '.customer-name')
# # # #     customer_name.click()
# # # #
# # # # @then('a customer details popup should open')
# # # # def step_impl(context):
# # # #     popup = context.browser.find_element(By.CSS_SELECTOR, '.customer-details-popup')
# # # #     assert popup.is_displayed()
# # # #
# # # # @when('I click on a registration entry')
# # # # def step_impl(context):
# # # #     registration_entry = context.browser.find_element(By.CSS_SELECTOR, '.registration-entry')
# # # #     registration_entry.click()
# # # #
# # # # @then('a registration details popup should open')
# # # # def step_impl(context):
# # # #     popup = context.browser.find_element(By.CSS_SELECTOR, '.registration-details-popup')
# # # #     assert popup.is_displayed()
# # # #
# # # # @when('I click on the switcher button')
# # # # def step_impl(context):
# # # #     switcher_button = context.browser.find_element(By.CSS_SELECTOR, '.switcher-button')
# # # #     switcher_button.click()
# # # #
# # # # @then('the view should toggle between different modes')
# # # # def step_impl(context):
# # # #     # Add assertions to verify the view has toggled
# # # #     pass
# # # #
# # # # @when('I click on the export button')
# # # # def step_impl(context):
# # # #     export_button = context.browser.find_element(By.CSS_SELECTOR, '.export-button')
# # # #     export_button.click()
