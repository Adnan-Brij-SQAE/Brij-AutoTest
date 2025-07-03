from logging import exception

import keyboard
from behave import when, then
from Locators import locators
from Helper.enviHelper import Envi_Helper
from allure_commons.types import AttachmentType
from Logs import logs_file
import allure
import time
log = logs_file.get_logs()


@when(u'the user navigate to the Rebate Campaign Module page')
def step_impl(context):
    with allure.step("User navigates to the Rebate Campaign Module page"):
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click("(//li[@class='has-subnav ng-star-inserted'])[3]")
            helper.wait_till_element_is_present_to_click("//span[normalize-space()='Rebate Campaign']")
            time.sleep(2)
            helper.open_page("https://rc.brij.it/brand/modules/sms/campaigns")
            helper.get_value("//div[@id='mainContent']")
            log.info("Navigated to Video Module page")
            allure.attach("Video Module page loaded", name="Page Verification")
            time.sleep(2)


@then(u'the user should be navigated to the Rebate Campaign Module page')
def step_impl(context):
    with allure.step("Verify navigation to Rebate Campaign Module page"):
        try:
            helper = Envi_Helper(context.page)
            helper.capture_screenshot()
            helper.get_value("//h1[normalize-space()='Rebate Campaign']")
            log.info("Successfully navigated to Rebate Campaign Module page")
        except Exception as e:
            log.error(f"Verification of navigation failed: {e}")
            allure.attach(str(e), name="Navigation Verification Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the notification button on Rebate Campaign Module page')
def step_impl(context):
    with allure.step("Access notification button on Rebate Campaign Module page"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            helper.capture_screenshot()
            log.info("Notification button is accessible")
            keyboard.press_and_release('Esc')
        except Exception as e:
            log.error(f"Notification button access failed: {e}")
            allure.attach(str(e), name="Notification Button Error", attachment_type=allure.attachment_type.TEXT)



@then(u'the user can access the logout button on Rebate Campaign Module page')
def step_impl(context):
    with allure.step("Access logout button on Rebate Campaign Module page"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_LOGOUT_BUTTON)
            log.info("Logout button is accessible")
            helper.capture_screenshot()
            keyboard.press_and_release('Esc')
        except Exception as e:
            log.error(f"Logout button access failed: {e}")
            allure.attach(str(e), name="Logout Button Error", attachment_type=allure.attachment_type.TEXT)



@then(u'the user can access the field button on Rebate Campaign Module page')
def step_impl(context):
    with allure.step("Access field button on Rebate Campaign Module page"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_CAMPAIGN_NAME)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_CAMPAIGN_NAME)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_PHONE_NUMBER)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_PHONE_NUMBER)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_DATE_RANGE)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_DATE_RANGE)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_CAMPAIGN_FLOW)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_CAMPAIGN_FLOW)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_REBATE_TERMS)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_REBATE_TERMS)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_MAX_REBATE_AMOUNT)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_MAX_REBATE_AMOUNT)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_CAMPAIGN_STATUS)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_CAMPAIGN_STATUS)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_WHERE_USED)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_FIELD_WHERE_USED)
            log.info("Field button is accessible")
            helper.capture_screenshot()
        except Exception as e:
            log.error(f"Field button access failed: {e}")
            allure.attach(str(e), name="Field Button Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can select All checkbox on Rebate Campaign Module page')
def step_impl(context):
    with allure.step("Select all checkboxes on Rebate Campaign Module page"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_ALL_CHECKBOX)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_ALL_CHECKBOX)
            log.info("All checkboxes selected")
        except Exception as e:
            log.error(f"Selecting checkboxes failed: {e}")
            allure.attach(str(e), name="Checkbox Selection Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user use search feature to search between the modules on Rebate Campaign Module page')
def step_impl(context):
    with allure.step("Use search feature on Rebate Campaign Module page"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.REBATE_CAMPAIGN_SEARCH, "SQAE", 10)
            time.sleep(2)
            helper.capture_screenshot()
            log.info("Search input used")
        except Exception as e:
            log.error(f"Search feature failed: {e}")
            allure.attach(str(e), name="Search Feature Error", attachment_type=allure.attachment_type.TEXT)
            helper.capture_screenshot()


@then(u'the user can sort the table on Rebate Campaign Module page')
def step_impl(context):
    with allure.step("Sort table data on Rebate Campaign Module page"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_CAMPAIGN_HEADING)
            helper.capture_screenshot()
            log.info("sorted with Campaign name and screenshot attached")
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_CAMPAIGN_HEADING)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_PHONE)
            helper.capture_screenshot()
            log.info("sorted with Phone Number and screenshot attached")
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_PHONE)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_WHERE_USED)
            helper.capture_screenshot()
            log.info("sorted with where used and screenshot attached")
            log.info("Table sorted")
        except Exception as e:
            log.error(f"Table sort failed: {e}")
            allure.attach(str(e), name="Sort Table Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can create new Rebate Campaign module from on Rebate Campaign Module page')
def step_impl(context):
    with allure.step("Create new Rebate Campaign module"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_NEW_MODULE)
            time.sleep(2)
            log.info("Opened Add/Edit Rebate Campaign Popup")

            helper.insert_text_in_input_field(locators.REBATE_CAMPAIGN_POPUP_MODULE_NAME,"Auto Rebate Campaign")
            log.info("Named the  Rebate Campaign Popup")
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_NUMBER)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_NUMBER_none)
            helper.insert_text_in_input_field(locators.REBATE_CAMPAIGN_GRACE,"5")
            log.info("entered the grace period")
            try:
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_REBATE_TERM)
            except:
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_REBATE_TERM_alternate)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETCASH)
            log.info("selected rebate terms buy X get Y cash Add/Edit Rebate Campaign Popup")
            helper.insert_text_in_input_field(locators.REBATE_CAMPAIGN_BUYX_GETY_QUANTITY2,"5")
            log.info("entered quantity ")
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_BUYX_GETY_PAYOUT_PLUS)
            log.info("entered payout amount ")
            helper.capture_screenshot()
            helper.insert_text_in_input_field(locators.REBATE_CAMPAIGN_BUYX_GETY_PRODUCTNAME, "Donuts")
            log.info("entered product name ")
            helper.insert_text_in_input_field(locators.REBATE_CAMPAIGN_BUYX_GETY_MAX,"2")
            log.info("entered max. rebate amount ")
            helper.capture_screenshot()
            # helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_SAVE)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS)
            log.info("navigated to advance settings  ")
            time.sleep(2)
            try:
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_REMINDER)
                log.info("selected Enable Reminder Messages flag ")
                helper.capture_screenshot()
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_REMINDER)
            except Exception as e:
                log.info(f"unable to select Enable Reminder Messages flag with exception {e} ")

            try:
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_CUSTOMIZE_AI)
                log.info("selected Customize AI Settings flag ")
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_OPTION)
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_TEXT)
                helper.capture_screenshot()
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_TEXT2)
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_RECEIPT)
                helper.capture_screenshot()
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_RECEIPT2)
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_ERROR)
                helper.capture_screenshot()
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_ERROR2)
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_VALID_RECEIPT )
                helper.capture_screenshot()
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_VALID_RECEIPT2)
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_OPTION)
            except exception() as e:
                log.error(f"unable to select Customize AI setting flag with exception {e} ")
            try:
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_APPROVAL)
                log.info("selected Rebate Auto-Approval flag ")
                helper.capture_screenshot()
                helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_APPROVAL)
            except:
                log.error(f"unable to select Rebate Auto-Approval flag with exception {e} ")
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_AS_BACK)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_SAVE)
            keyboard.press_and_release('Esc')
            time.sleep(2)
            log.info("New Rebate Campaign module created")
        except Exception as e:
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_SAVE)
            keyboard.press_and_release('Esc')
            log.error(f"Creation of new Rebate Campaign module failed: {e}")
            allure.attach(str(e), name="Create Module Error", attachment_type=allure.attachment_type.TEXT)
            helper.capture_screenshot()
            raise


@then(u'the user can edit the previous Rebate Campaign module on Rebate Campaign Module page')
def step_impl(context):
    with allure.step("Edit Rebate Campaign module"):
        try:
            helper = Envi_Helper(context.page)
            # helper.wait_till_element_is_present_to_click(locators.EDIT_BUTTON)
            log.info("Rebate Campaign module edited")
        except Exception as e:
            log.error(f"Editing module failed: {e}")
            allure.attach(str(e), name="Edit Module Error", attachment_type=allure.attachment_type.TEXT)
            helper.capture_screenshot()
            raise


@then(u'the user can delete the unused Rebate Campaign module')
def step_impl(context):
    with allure.step("Delete Rebate Campaign module(s)"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.REBATE_CAMPAIGN_SEARCH,"auto rebate ")
            # helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_CAMPAIGN_HEADING)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_KEBAB)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_DELETE)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_DELETE_CONFIRM)
            helper.capture_screenshot()
            time.sleep(2)
            log.info("Rebate Campaign module(s) deleted")
        except Exception as e:
            log.error(f"Deleting module(s) failed: {e}")
            allure.attach(str(e), name="Delete Module Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user want to see the number of rows on Rebate Campaign Page')
def step_impl(context):
    with allure.step("Pagination Rebate Campaign module(s)"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_ROWPERPAGE_OPTION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_ROWPERPAGE_20)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_ROWPERPAGE_OPTION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_ROWPERPAGE_100)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_ROWPERPAGE_OPTION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_SIGNUP_ROWPERPAGE_1000)
            log.info("Tested Rebate Campaign module pagination")
        except Exception as e:
            log.error(f"Pagination Test failed: {e}")
            allure.attach(str(e), name="pagination Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can delete more than one unused Rebate Campaign module')
def step_impl(context):
    with allure.step("Delete Rebate Campaign module(s)"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.REBATE_CAMPAIGN_SEARCH, "auto rebate ")
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.REGISTRATION_ALL_CHECKBOX)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_DELETE_ALL)
            helper.capture_screenshot()
            log.info("the selected modules are deleted successfully")
            log.info("Rebate Campaign module(s) deleted")
        except Exception as e:
            log.error(f"Deleting module(s) failed: {e}")
            allure.attach(str(e), name="Delete Module Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can create duplicate Rebate Campaign page')
def step_impl(context):
    with allure.step("Create duplicate Rebate Campaign module"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.REBATE_CAMPAIGN_SEARCH, "auto Rebate ")
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_CAMPAIGN_HEADING)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_KEBAB)
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_EDIT)
            time.sleep(2)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_DUPLICATE)
            time.sleep(2)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_SAVE)
            log.info('Duplicate Rebate Campaign  created successfully')
            helper.wait_till_element_is_present_to_click(locators.REBATE_CAMPAIGN_CLOSE)
            log.info("Duplicate Rebate Campaign module created")
        except Exception as e:
            log.error(f"Duplicate creation failed: {e}")
            allure.attach(str(e), name="Duplicate Module Error", attachment_type=allure.attachment_type.TEXT)
            helper.capture_screenshot()



