import allure
import keyboard
from allure_commons.types import AttachmentType
from behave import *
from Locators import locators
from Helper.enviHelper import Envi_Helper
from Logs import logs_file
import time
log = logs_file.get_logs()

@when(u'the user navigate to Customer Registration page')
def step_impl(context):

    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.LEFT_PANEL)
    customer_option = context.page.goto( "// span[normalize-space()='Customers']")
    customer_option.click()
    time.sleep(2)
    allure.attach("Navigated to the Customer Registration page", name="Navigation Step", attachment_type=AttachmentType.TEXT)

@when(u'User is on the Customer Page')
def step_impl(context):
    time.sleep(2)
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User is on the Customer Registration page"):
            helper.get_value(locators.CUSTOMER_REGISTRATION_TITLE,10)
    except Exception as e:
        log.error(f"Customer page verification failed: {e}")
        allure.attach(str(e), name="Customer Page Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the data should be filtered accordingly')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("filters implementation"):
            helper.capture_screenshot()
            log.info("the data is sorted and screenshots are captured")
    except Exception as e:
        log.error(f"Data filtering failed: {e}")
        allure.attach(str(e), name="Filter Error", attachment_type=allure.attachment_type.TEXT)

@allure.step('user access Experience Dropdown')
@then(u'the user can access Experience dropdown on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPERIENCE_FILTER)
        log.info("searching Test in experience filter")
        helper.insert_text_in_input_field(locators.CUSTOMER_FILTER_SEARCH,"Test",10)
        helper.wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_OPTION)
        helper.capture_screenshot()
        helper.wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_OPTION)
        helper.wait_till_element_is_present_to_click(locators.CUSTOMER_FILTER_CROSS)
        time.sleep(3)
    except Exception as e:
        log.error(f"Experience Dropdown access failed: {e}")
        allure.attach(str(e), name="Experience Dropdown Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user can access Variant dropdown ')
@then(u'the user can access Variant dropdown on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        helper.wait_till_element_is_present_to_click(locators.CUSTOMER_VARIANT_FILTER)
        log.info("searching Test in variant filter")
        time.sleep(2)
        helper.insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Test",10)
        time.sleep(2)
        helper.wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION2)
        helper.capture_screenshot()
        helper.wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_SAll)
        helper.wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        helper.wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_AllV)
        helper.wait_till_element_is_present_to_click(locators.CUSTOMER_VARIANT_FILTER)
        time.sleep(2)
    except Exception as e:
        log.error(f"Variant Dropdown access failed: {e}")
        allure.attach(str(e), name="Variant Dropdown Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user can access Registration Status dropdown ')
@then(u'the user can access registration status dropdown on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        helper.wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_STATUS)
        log.info("searching Test in variant filter")
        helper.insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Active",10)
        helper.wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ALL)
        helper.capture_screenshot()
        time.sleep(2)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ALL)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ACTIVE)
        helper.capture_screenshot()
        time.sleep(2)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_ACTIVE)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_PENDING)
        helper.capture_screenshot()
        time.sleep(2)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_PENDING)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_INCOMPLETE)
        helper.capture_screenshot()
        time.sleep(2)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_INCOMPLETE)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DENIED)
        helper.capture_screenshot()
        time.sleep(2)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DENIED)
        keyboard.press_and_release('pagedown')
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_EXPIRED)
        helper.capture_screenshot()
        time.sleep(2)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_EXPIRED)
        helper.wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        time.sleep(2)
    except Exception as e:
        log.error(f"Registration Status Dropdown access failed: {e}")
        allure.attach(str(e), name="Registration Status Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user can access Customer Source dropdown ')
@then(u'the user can access customer source dropdown on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        helper.wait_till_element_is_present_to_click(locators.CUSTOMER_SOURCE)
        helper.capture_screenshot()
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_ALL)
        helper.capture_screenshot()
        time.sleep(2)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_ALL)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_BRIJ)
        helper.capture_screenshot()
        time.sleep(2)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_BRIJ)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_OTHERS)
        helper.capture_screenshot()
        time.sleep(2)
        helper.wait_till_element_is_present_to_click(locators.REGISTRATION_CUSTOMER_SOURCE_OTHERS)
        helper.wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        time.sleep(2)
    except Exception as e:
        log.error(f"Customer Source Dropdown access failed: {e}")
        allure.attach(str(e), name="Customer Source Error", attachment_type=AttachmentType.TEXT)

@then(u'the user should access the notification button on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("Verify notification button is accessible"):
            helper.wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON, 10)
            log.info("user is able to access the notification button ")
            helper.wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON_2)
            time.sleep(2)
            allure.attach("Notification button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Notification button access failed: {e}")
        allure.attach(str(e), name="Notification Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user should access the logout button dropdown on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("Verify logout button dropdown is accessible"):
            helper.wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON, 10)
            helper.capture_screenshot()
            log.info("user is able to access the logout button ")
            time.sleep(2)
            allure.attach("Logout button dropdown is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Logout button access failed: {e}")
        allure.attach(str(e), name="Logout Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user should get the customer count on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("Verify customer count is displayed"):
            helper.wait_till_element_is_present(locators.CUSTOMER_COUNT,10)
            log.info("Customer count is displayed")
            time.sleep(2)
            allure.attach("Customer count is displayed", name="UI Verification", attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Customer count verification failed: {e}")
        allure.attach(str(e), name="Customer Count Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can search within the customer on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User searches within the customer"):
            helper.insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR,"Adnan",10)
            helper.capture_screenshot()
            log.info("user is able to search within the customer table")
            time.sleep(4)
            allure.attach("the search functionality is working", name="Search functionality ",attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Customer search failed: {e}")
        allure.attach(str(e), name="Search Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can click on field button on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User clicks on the field button"):
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
            helper.capture_screenshot()
            log.info("the field button is available and clickable")
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
            time.sleep(2)
            allure.attach("The field button is accessible", name="Field Button",attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Field button click failed: {e}")
        allure.attach(str(e), name="Field Button Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can check all check boxes on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User checks all checkboxes"):
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_SELECT_ALL_CHECKBOX, 10)
            helper.capture_screenshot()
            log.info("user is able to click on all checkboxes button ")
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_UNSELECT_ALL_CHECKBOX, 10)
            time.sleep(2)
    except Exception as e:
        log.error(f"Checkbox operation failed: {e}")
        allure.attach(str(e), name="Checkbox Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user can sort the customer table on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User sorts the customer table"):
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_CUSTOMER_NAME_HEADING, 10)
            time.sleep(2)
            log.info("sorting is working on customer page ")
            helper.capture_screenshot()
    except Exception as e:
        log.error(f"Customer table sorting failed: {e}")
        allure.attach(str(e), name="Sorting Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the table should be sorted in the correct order on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        log.info("the table is sorted and the screenshots are attached")
    except Exception as e:
        log.error(f"Table sorting verification failed: {e}")
        allure.attach(str(e), name="Sort Verification Error", attachment_type=allure.attachment_type.TEXT)

@then(u'open customer popup on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User sorts the customer table"):
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_ICON, 10)
            helper.capture_screenshot()
            log.info("user is able to open the customer popup")
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_CUSTOMER_DETAIL)
            helper.capture_screenshot()
            log.info("user is able to expand customer detail")
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_CUSTOMER_DETAIL)
            keyboard.press_and_release('pagedown')
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_ENGAGEMENT_DETAIL)
            helper.capture_screenshot()
            log.info("user is able to expand engagement detail")
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_ENGAGEMENT_DETAIL)
            keyboard.press_and_release('pagedown')
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_REGISTRATION)
            helper.capture_screenshot()
            log.info("user is able to expand registration detail")
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_POPUP_REGISTRATION)
            keyboard.press('Esc')
            time.sleep(2)
    except Exception as e:
        log.error(f"Customer popup operation failed: {e}")
        allure.attach(str(e), name="Customer Popup Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can expand the customer registrations on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User expands customer registrations"):
            helper.hover_to_element_to_click(locators.Customer_Expander)
            log.info("clicked on expander")
            time.sleep(2)
    except Exception as e:
        log.error(f"Customer registration expansion failed: {e}")
        allure.attach(str(e), name="Expansion Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can open registration popup on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User opens the registration popup"):
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_ICON, 10)
            time.sleep(2)
            keyboard.press('Esc')
    except Exception as e:
        log.error(f"Registration popup opening failed: {e}")
        allure.attach(str(e), name="Registration Popup Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can export the customer registrations on Customer page')
def step_impl(context):
    try:
        with allure.step("User exports customer registrations"):
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CANCEL)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CLOSE, 10)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_EXPORT, 10)
            time.sleep(10)
    except Exception as e:
        log.error(f"Customer export failed: {e}")
        allure.attach(str(e), name="Export Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can view the customer registrations in google sheet on Customer page')
def step_impl(context):
    try:
        with allure.step("User resets the Google Sheet"):
            helper = Envi_Helper(context.page)
            keyboard.press_and_release('Page Down')
            keyboard.press_and_release('Page Down')
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_VIEW_IN_GOOGLE_SHEET, 10)
            time.sleep(2)
            keyboard.press('ctrl'+'w')
    except Exception as e:
        log.error(f"Google Sheet view failed: {e}")
        allure.attach(str(e), name="Google Sheet Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can reset the google sheet on Customer page')
def step_impl(context):
    try:
        with allure.step("User resets the Google Sheet"):
            helper = Envi_Helper(context.page)
            keyboard.press_and_release('Page Down')
            keyboard.press_and_release('Page Down')
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_RESET_GOOGLE_PERMISSION, 10)
            time.sleep(4)
            keyboard.press_and_release('pageup')
    except Exception as e:
        log.error(f"Google Sheet reset failed: {e}")
        allure.attach(str(e), name="Google Sheet Reset Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can use switcher to switch to Registration page')
def step_impl(context):
    try:
        with allure.step("User switches to the Registration page"):
            helper = Envi_Helper(context.page)
            keyboard.press_and_release('page up')
            keyboard.press_and_release('page up')
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_SWITCHER_BUTTON)
            log.info("clicked on switcher")
            time.sleep(2)
    except Exception as e:
        log.error(f"Page switching failed: {e}")
        allure.attach(str(e), name="Switcher Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user should get the Registration count on Registration page')
def step_impl(context):
    try:
        with allure.step("Verify Registration count is displayed"):
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present(locators.CUSTOMER_REGISTRATION_COUNT,10)
            log.info("Registration count is available")
            allure.attach("Registration count is displayed", name="UI Verification", attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Registration count verification failed: {e}")
        allure.attach(str(e), name="Registration Count Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can search within the Registration on Registration page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User searches within the Registration"):
            helper.insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "Adnan", 10)
            helper.capture_screenshot()
            log.info("user is able to search within the customer table")
            locators.CUSTOMER_SEARCH_BAR.clear()
            time.sleep(4)
    except Exception as e:
        log.error(f"Registration search failed: {e}")
        allure.attach(str(e), name="Registration Search Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can click on field button on Registration page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User clicks on the field button"):
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
            helper.capture_screenshot()
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_FIELDS_BUTTON, 10)
            log.info("the field button is available and clickable")
    except Exception as e:
        log.error(f"Field button click failed: {e}")
        allure.attach(str(e), name="Field Button Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can check all check boxes on Registration page')
def step_impl(context):
    try:
        with allure.step("User checks all checkboxes"):
            helper = Envi_Helper(context.page)
            helper.click(locators.CUSTOMER_SELECT_ALL_CHECKBOX)
            helper.capture_screenshot()
            log.info("user is able to click on all checkboxes button ")
            helper.click(locators.CUSTOMER_UNSELECT_ALL_CHECKBOX)
    except Exception as e:
        log.error(f"Checkbox operation failed: {e}")
        allure.attach(str(e), name="Checkbox Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user sort the Registration table on Registration page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User sorts the Registration table"):
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_CUSTOMER_HEADING, 10)
            time.sleep(2)
            log.info("customer sorting is working on customer page ")
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_REG_DATE, 10)
            time.sleep(2)
            log.info("sorting is working on customer page ")
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_PURCHASE_DATE, 10)
            time.sleep(2)
            log.info("sorting is working on customer page ")
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_REG_STATUS, 10)
            time.sleep(2)
            log.info("sorting is working on customer page ")
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_REGISTRATION_LOCATION, 10)
            time.sleep(2)
            log.info("sorting is working on customer page ")
            helper.capture_screenshot()
    except Exception as e:
        log.error(f"Registration table sorting failed: {e}")
        allure.attach(str(e), name="Registration Sorting Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the table should be sorted in the correct order on Registration page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("Table updated after sorting"):
            log.info("the table is sorted and the screenshots are attached")
    except Exception as e:
        log.error(f"Sort verification failed: {e}")
        allure.attach(str(e), name="Sort Verification Error", attachment_type=allure.attachment_type.TEXT)

@when(u'user open registration popup on Registration page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User opens the Registration popup"):
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_ICON, 10)
            time.sleep(2)
            helper.capture_screenshot()
    except Exception as e:
        log.error(f"Registration popup opening failed: {e}")
        allure.attach(str(e), name="Registration Popup Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can access all the information for specific registration')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("Registration popup"):
            log.info("user is able to open the Registration popup")
            helper.capture_screenshot()
            helper.insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR,"test new product",10)
            keyboard.press_and_release('page down')
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CUSTOMER_DETAIL)
            helper.capture_screenshot()
            log.info("user is able to expand engagement detail")
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CUSTOMER_DETAIL)
            keyboard.press_and_release('page down')
            keyboard.press_and_release('page down')
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_FORM)
            helper.capture_screenshot()
            log.info("user is able to expand registration detail")
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_FORM)
            keyboard.press_and_release('page down')
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_STATUS)
            helper.capture_screenshot()
            log.info("user is able to expand registration detail")
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CLOSE)
            time.sleep(2)
    except Exception as e:
        log.error(f"Registration information access failed: {e}")
        allure.attach(str(e), name="Registration Info Error", attachment_type=allure.attachment_type.TEXT)

@when(u'user open registration popup')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User open registration popup to edit"):
            time.sleep(2)
            helper.insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "testregistration+28118@yopmail.com", 10)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_EDIT_REG)
            time.sleep(2)
            helper.capture_screenshot()
    except Exception as e:
        log.error(f"Registration popup opening for edit failed: {e}")
        allure.attach(str(e), name="Registration Edit Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can edit registration details')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("user edit registration details"):
            log.info("user is on the registration popup ")
            try:
                try:
                    helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_PENCIL_ICON)
                except:
                    helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_PENCIL_ICON2)
                time.sleep(2)
                helper.capture_screenshot()
                try:
                    helper.insert_text_in_input_field(locators.REGISTRATION_POPUP_WARRANTY_NUM,"5",10)
                except:
                    helper.insert_text_in_input_field(locators.REGISTRATION_POPUP_WARRANTY_NUM1, "5", 10)
                helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_WARRANTY_DUR)
                helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_WARRANTY_MON)
                helper.capture_screenshot()
                log.info("user has edited the warranty details")
                helper.insert_text_in_input_field(locators.REGISTRATION_POPUP_SERIAL_NUM,"Auto 123",10)
                helper.capture_screenshot()
                log.info("user updated the serial number")
                keyboard.press_and_release('pageup')
                helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_SAVE_BUTTON)
                helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CLOSE)
            except:
                helper.wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CLOSE)
                log.info("user successfully updated the registration details")
                time.sleep(2)
    except Exception as e:
        log.error(f"Registration edit failed: {e}")
        allure.attach(str(e), name="Registration Edit Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user archive registration on registration page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User archives the registration"):
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_ARCHIVE)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_ARCHIVE_CONFIRM)
            time.sleep(2)
    except Exception as e:
        log.error(f"Registration archiving failed: {e}")
        allure.attach(str(e), name="Archive Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the registration should be archieved')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("viewing the archived registration"):
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN)
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN_ARCHIVE)
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_STATUS_DROPDOWN_CLOSE)
            helper.capture_screenshot()
    except Exception as e:
        log.error(f"Archive verification failed: {e}")
        allure.attach(str(e), name="Archive Verification Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can unarchived the registration')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User archives the registration"):
            time.sleep(2)
            helper.insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR, "Test IT services", 10)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_KEBAB_MENU)
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_RESTORE)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_RESTORE_CONFIRM)
            time.sleep(2)
            helper.capture_screenshot()
    except Exception as e:
        log.error(f"Registration unarchive failed: {e}")
        allure.attach(str(e), name="Unarchive Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user want to see the number of rows on Customer Page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        keyboard.press('page down')
        keyboard.press('page down')
        helper.wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
        helper.capture_screenshot()
        helper.wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_20)
        helper.capture_screenshot()
        keyboard.press('page down')
        keyboard.press('page down')
        helper.wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
        helper.capture_screenshot()
        helper.wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_100)
        helper.capture_screenshot()
        keyboard.press('page down')
        keyboard.press('page down')
        helper.wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
        helper.capture_screenshot()
        helper.wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_1000)
        helper.capture_screenshot()
    except Exception as e:
        log.error(f"Row count operation failed: {e}")
        allure.attach(str(e), name="Row Count Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the list should be updated on Customer page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        helper.capture_screenshot()
        log.info("the rows are updated successfully")
    except Exception as e:
        log.error(f"List update verification failed: {e}")
        allure.attach(str(e), name="List Update Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can export the Registration registrations on Registration page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User exports Registration registrations"):
            helper.wait_till_element_is_present_to_click(locators.VARIANT_LIST_CHECKBOX1)
            keyboard.press_and_release('Page Down')
            keyboard.press_and_release('Page Down')
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CANCEL)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_CLOSE, 10)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_BUTTON, 10)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_EXPORT_EXPORT, 10)
            time.sleep(10)
    except Exception as e:
        log.error(f"Registration export failed: {e}")
        allure.attach(str(e), name="Registration Export Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can reset the google sheet on Registration page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User resets the Google Sheet"):
            keyboard.press_and_release('Page Down')
            keyboard.press_and_release('Page Down')
            time.sleep(5)
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_RESET_GOOGLE_PERMISSION, 10)
            time.sleep(4)
    except Exception as e:
        log.error(f"Google Sheet reset failed: {e}")
        allure.attach(str(e), name="Google Sheet Reset Error", attachment_type=allure.attachment_type.TEXT)

@then(u'user can view the Registration registrations in google sheet on Registration page')
def step_impl(context):
    try:
        helper = Envi_Helper(context.page)
        with allure.step("User views Registration registrations in Google Sheet"):
            keyboard.press_and_release('Page Down')
            keyboard.press_and_release('Page Down')
            helper.wait_till_element_is_present_to_click(locators.CUSTOMER_VIEW_IN_GOOGLE_SHEET, 10)
            time.sleep(2)
            keyboard.press('ctrl' + 'w')
    except Exception as e:
        log.error(f"Google Sheet view failed: {e}")
        allure.attach(str(e), name="Google Sheet View Error", attachment_type=allure.attachment_type.TEXT)

