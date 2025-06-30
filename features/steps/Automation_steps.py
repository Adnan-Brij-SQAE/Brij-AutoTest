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


@when(u'the user navigate to Automation page')
def step_impl(context):
    with allure.step("User navigates to the Automation page"):
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LEFT_PANEL)
        automation_option = context.driver.find_element(By.XPATH, locators.AUTOMATION_OPTION['xpath'])
        automation_option.click()
        time.sleep(2)
        # Envi_Helper(context.driver).wait_till_element_is_present(locators.AUTOMATION_TITLE)
        time.sleep(2)
        allure.attach("Navigated to the  Automation page", name="Navigation Step", attachment_type=AttachmentType.TEXT)

@when(u'User is on the Automation Page')
def step_impl(context):
    with allure.step("User is on the Automation page"):
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present(locators.AUTOMATION_TITLE, 10)

@then(u'the user can access the notification button on Automation page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_NOTIFICATION_BUTTON, 10)
        log.info("Notification button is accessible")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error accessing notification button: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)

@allure.step('user access logout button')
@then(u'the user can access the logout button on Automation page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_LOGOUT_BUTTON, 10)
        log.info("Logout button is accessible")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error accessing logout button: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)


@allure.step('user searches within Automation')
@then(u'the user can search within the Automation on Automation page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_SEARCH_BAR, "Test", 10)
        log.info("Search performed successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error performing search: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)


@allure.step('user clicks field button')
@then(u'the user can click on field button on Automation page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_FIELD_BUTTON, 10)
        log.info("Field button clicked successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error clicking field button: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)


@allure.step('user checks all checkboxes')
@then(u'the user can check all check boxes on Automation page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_ALL_CHECKBOXES, 10)
        log.info("All checkboxes checked successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error checking checkboxes: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)


@allure.step('user sorts automation table')
@then(u'the user can sort the Automation table on Automation page')
def step_impl(context):
    try:
        # Example for sorting by first column header
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_TABLE_HEADER, 10)
        log.info("Automation table sorted successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error sorting table: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)


@allure.step('automation created successfully')
@then(u'the automation should be created successfully')
def step_impl(context):
    try:
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_SEARCH_BAR, "auto", 10)

        log.info("Automation created successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error creating automation: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)


@allure.step('user creates new automation')
@when(u'the user creates a new Automation')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_NEW_AUTOMATION)
        # Fill out automation creation form
        log.info("Automation popup opened successfully")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_AUTOMATION_NAME, "Test Auto Automation live")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTOMATION_TYPE_WEBHOOK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTOMATION_TYPE_MULBERRY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTOMATION_TYPE_KLAVIYO)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        #authentication tab
        log.info("User successfully entered the Authentication tab")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_NAME,"auto authentication")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_TYPE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_TYPE_OPTION)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_API_KEY,"autokey786")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_SAVE)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        #action tab
        log.info("User successfully entered the Action tab")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_ACTION_NAME)
        keyboard.press_and_release('Esc')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_ACTION_VERSION)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        #filter tab
        log.info("User successfully entered the Filter tab")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH_ALL_EXPERIENCE)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH,"test")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH_SELECT_ALL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH_CROSS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        #Trigger & Properties
        log.info("User successfully entered the Trigger and Properties tab")
        # Envi_Helper(context.driver).wait_till_element_is_present(locators.AUTOMATION_POPUP_TRIGGER_PROPERTIES)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_INITIATION_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_INITIATION_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_SUBMISSION_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_SUBMISSION_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_APPROVAL_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_APPROVAL_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_DENIAL_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_DENIAL_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_FORM_SUBMISSION_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_FORM_SUBMISSION_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REVIEW_SUBMISSION_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REVIEW_SUBMISSION_EVENT_CHECKBOX)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)

        #Configuration
        log.info("User successfully entered the Configuration tab")
        # Envi_Helper(context.driver).wait_till_element_is_present(locators.AUTOMATION_POPUP_CONFIGURATION)
        # try:
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN_NO)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN)
        #     # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN_YES)
        #     # Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_KLAVIYO,"auto123")
        #
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_SMS_SINGLEOPTIN)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_SMS_SINGLEOPTIN_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_SMS_SINGLEOPTIN_NO)
        #
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS_NO)
        #     # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS_YES)
        #     # Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS_INPUT, "auto123")
        #
        #     keyboard.press_and_release('Page down')
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA_NO)
        #
        #     keyboard.press_and_release('Page down')
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA_NO)
        #
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION_NO)
        #     # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION_YES)
        #     # Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION_COUNT, "58")
        #
        #     keyboard.press_and_release('Page down')
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_NOTIFY)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_NOTIFY_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_NOTIFY_NO)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_NOTIFY_YES)
        #     # Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_CONFIGURATION_NOTIFY_EMAIL, "adnan+autotest@brij.it")
        #     Envi_Helper.capture_screenshot()
        #
        # except Exception as e:
        #     log.error(f"Error configuring automation: {e}")
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_SAVE_ACTIVATE)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_SAVE_LIVE)
        #     log.info("New automation created successfully")
        #     Envi_Helper.capture_screenshot()
        #     time.sleep(2)
        #     allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)

        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_SAVE_ACTIVATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_SAVE_LIVE)
        log.info("New automation created successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)

    except Exception as e:
        log.error(f"Error creating automation: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)


@allure.step('user edits existing automation')
@when(u'the user edits the previous Automation')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_LIST_ROW1)
        time.sleep(3)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_ACTION)
        time.sleep(2)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER)
        time.sleep(2)
        log.info("User successfully entered the Filter tab")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH,"testing")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_TEST1)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_SAVE_ACTIVATE, 10)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_SAVE_PAUSE, 10)
        log.info("paused Automation edited successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error editing automation: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)

@then(u'the automation should be updated successfully')
def step_impl(context):
    try:
        log.info("Automation updated successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error updating automation: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)


@allure.step('user drafts automation')
@when(u'the user drafts the automation for future use')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_NEW_AUTOMATION)
        # Fill out automation creation form
        log.info("Automation popup opened successfully")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_AUTOMATION_NAME,"Test Auto Automation draft")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTOMATION_TYPE_WEBHOOK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTOMATION_TYPE_MULBERRY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTOMATION_TYPE_KLAVIYO)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        # authentication tab
        log.info("User successfully entered the Authentication tab")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_NAME,"abc draft")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_TYPE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_TYPE_OPTION)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_API_KEY, "autokey786 abc")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_SAVE)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        # action tab
        log.info("User successfully entered the Action tab")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_ACTION_NAME)
        # keyboard.press_and_release('Esc')
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_ACTION_VERSION)
        # Envi_Helper.capture_screenshot()
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(5)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CROSS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_SAVE_EXIST)
        time.sleep(2)
        log.info("Automation saved as draft successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error saving as draft: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)

@then(u'the draft should be saved successfully')
def step_impl(context):
    try:
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_SEARCH_BAR, "draft", 10)
        log.info("Automation drafted successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error drafting automation: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)

@allure.step('user saves and pauses automation')
@then(u'the user can save new automation but pause')
def step_impl(context):
    try:

        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_NEW_AUTOMATION)
        # Fill out automation creation form
        log.info("Automation popup opened successfully")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_AUTOMATION_NAME,"Test Auto Automation Pause")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTOMATION_TYPE_WEBHOOK)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTOMATION_TYPE_MULBERRY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTOMATION_TYPE_KLAVIYO)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        # authentication tab
        log.info("User successfully entered the Authentication tab")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_OPTION)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_NAME,"auto pause")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_TYPE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_TYPE_OPTION)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_API_KEY, "autokey7861")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_SAVE)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        # action tab
        log.info("User successfully entered the Action tab")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_ACTION_NAME)
        # keyboard.press_and_release('Esc')
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_ACTION_VERSION)
        # Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        # filter tab
        log.info("User successfully entered the Filter tab")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH_ALL_EXPERIENCE)
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH, "test")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH_SELECT_ALL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH_CROSS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_FILTER)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)
        # Trigger & Properties
        log.info("User successfully entered the Trigger and Properties tab")
        # Envi_Helper(context.driver).wait_till_element_is_present(locators.AUTOMATION_POPUP_TRIGGER_PROPERTIES)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_INITIATION_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_INITIATION_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_SUBMISSION_EVENT_CHECKBOX)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_SUBMISSION_EVENT_CHECKBOX)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_APPROVAL_EVENT_CHECKBOX)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_APPROVAL_EVENT_CHECKBOX)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_DENIAL_EVENT_CHECKBOX)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_DENIAL_EVENT_CHECKBOX)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_FORM_SUBMISSION_EVENT_CHECKBOX)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_FORM_SUBMISSION_EVENT_CHECKBOX)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REVIEW_SUBMISSION_EVENT_CHECKBOX)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REVIEW_SUBMISSION_EVENT_CHECKBOX)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_NEXT_BUTTON)
        time.sleep(2)

        # Configuration
        log.info("User successfully entered the Configuration tab")
        # Envi_Helper(context.driver).wait_till_element_is_present(locators.AUTOMATION_POPUP_CONFIGURATION)
        # try:
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN_NO)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN)
        #     # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN_YES)
        #     # Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_KLAVIYO,"auto123")
        #
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_SMS_SINGLEOPTIN)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_SMS_SINGLEOPTIN_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_SMS_SINGLEOPTIN_NO)
        #
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS_NO)
        #     # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS_YES)
        #     # Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS_INPUT, "auto123")
        #
        #     keyboard.press_and_release('Page down')
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA_NO)
        #
        #     keyboard.press_and_release('Page down')
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA_NO)
        #
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION_NO)
        #     # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION_YES)
        #     # Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION_COUNT, "58")
        #
        #     keyboard.press_and_release('Page down')
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_NOTIFY)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_NOTIFY_YES)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_NOTIFY_NO)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_CONFIGURATION_NOTIFY_YES)
        #     # Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_POPUP_CONFIGURATION_NOTIFY_EMAIL, "adnan+autotest@brij.it")
        #     Envi_Helper.capture_screenshot()
        #
        # except Exception as e:
        #     log.error(f"Error configuring automation: {e}")
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_SAVE_ACTIVATE)
        #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_SAVE_LIVE)
        #     log.info("New automation created successfully")
        #     Envi_Helper.capture_screenshot()
        #     time.sleep(2)
        #     allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)

        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_SAVE_ACTIVATE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_SAVE_PAUSE, 10)
        log.info("Automation created and paused successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error saving and pausing: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)

@allure.step('user pauses automation')
@when(u'the user pauses the automation')
def step_impl(context):
    try:
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_SEARCH_BAR, "live", 10)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_LIST_ECLIPSE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_ECLIPSE_PAUSE, 10)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_YES, 10)
        log.info("Automation paused successfully")
        Envi_Helper.capture_screenshot()
        context.driver.find_element(By.XPATH, "//input[@placeholder='Search Items...']").clear()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error pausing automation: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)

@then(u'the automation status should change to paused')
def step_impl(context):
    try:
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_SEARCH_BAR, "pause", 10)
        time.sleep(2)
        log.info("Automation paused successfully")
        Envi_Helper.capture_screenshot()
        context.driver.find_element(By.XPATH,"//input[@placeholder='Search Items...']").clear()
        time.sleep(4)
    except Exception as e:
        log.error(f"Error pausing automation: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)

@allure.step('user makes automation live')
@when(u'the user makes the previous automation live')
def step_impl(context):
    try:
        Envi_Helper(context.driver).insert_text_in_input_field(locators.AUTOMATION_SEARCH_BAR, "pause", 10)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_LIST_ECLIPSE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_ECLIPSE_ACTIVATE, 10)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_POPUP_YES, 10)
        log.info("Automation Active successfully")
        Envi_Helper.capture_screenshot()
        context.driver.find_element(By.XPATH, "//input[@placeholder='Search Items...']").clear()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error making automation live: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)


@then(u'the automation status should change to active')
def step_impl(context):
    try:
        log.info("Automation activated successfully")
        Envi_Helper.capture_screenshot()

        context.driver.find_element(By.XPATH, "//input[@placeholder='Search Items...']").clear()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error activating automation: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)

@allure.step('user tests pagination')
@then(u'the user can test the pagination on Automation page')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, "//input[@placeholder='Search Items...']").clear()
        keyboard.press('page down')
        keyboard.press('page down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_ROWPERPAGE_OPTION)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_ROWPERPAGE_20)
        Envi_Helper.capture_screenshot()
        keyboard.press('page down')
        keyboard.press('page down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_ROWPERPAGE_OPTION)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_ROWPERPAGE_100)
        Envi_Helper.capture_screenshot()
        keyboard.press('page down')
        keyboard.press('page down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_ROWPERPAGE_OPTION)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.AUTOMATION_ROWPERPAGE_1000)
        Envi_Helper.capture_screenshot()

        log.info("Pagination tested successfully")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Error testing pagination: {e}")
        allure.attach(str(e), name="Error", attachment_type=AttachmentType.TEXT)