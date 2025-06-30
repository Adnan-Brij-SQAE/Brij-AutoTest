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



@When(u'the user is on the Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LEFT_PANEL)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_OPTION)
        log.info("user is on the Analytics Rebate page")
        time.sleep(2)
    except Exception as e:
        log.error(f"Navigation to Analytics Rebate page failed: {e}")
        allure.attach(str(e), name="Analytics Rebate Page Error", attachment_type=allure.attachment_type.TEXT)

@When('the user can access Experience dropdown on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_EXPERIENCE_FILTER)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_ALL_EXPERIENCE)
        log.info("searching Test in experience filter")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_FILTER_SEARCH,"Test",10)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_SELECT_ALL)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        keyboard.press_and_release('Esc')
    except Exception as e:
        log.error(f"Experience dropdown access failed: {e}")
        allure.attach(str(e), name="Experience Dropdown Error", attachment_type=allure.attachment_type.TEXT)

@When('the user can access Variant dropdown on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER)
        log.info("searching Test in variant filter")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Test",10)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION2)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION2)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        keyboard.press_and_release('Esc')
        time.sleep(2)
    except Exception as e:
        log.error(f"Variant dropdown access failed: {e}")
        allure.attach(str(e), name="Variant Dropdown Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can access the notification button on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
        time.sleep(2)
    except Exception as e:
        log.error(f"Notification button access failed: {e}")
        allure.attach(str(e), name="Notification Button Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can access the logout button dropdown on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
        time.sleep(2)
    except Exception as e:
        log.error(f"Logout button access failed: {e}")
        allure.attach(str(e), name="Logout Button Error", attachment_type=allure.attachment_type.TEXT)

@When(u'the user can select the date range filter button on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        time.sleep(2)
    except Exception as e:
        log.error(f"Date range filter selection failed: {e}")
        allure.attach(str(e), name="Date Range Filter Error", attachment_type=allure.attachment_type.TEXT)

@When(u'the user can Export the data on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPORT_BUTTON)
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Data export failed: {e}")
        allure.attach(str(e), name="Data Export Error", attachment_type=allure.attachment_type.TEXT)

@When(u'the user clicks the Today filter button on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TODAY_FILTER)
        time.sleep(2)
    except Exception as e:
        log.error(f"Today filter click failed: {e}")
        allure.attach(str(e), name="Today Filter Error", attachment_type=allure.attachment_type.TEXT)

@When(u'the user clicks the This Week filter button on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.THIS_WEEK_FILTER)
        time.sleep(2)
    except Exception as e:
        log.error(f"This Week filter click failed: {e}")
        allure.attach(str(e), name="This Week Filter Error", attachment_type=allure.attachment_type.TEXT)

@When(u'the user clicks the This Month filter button on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.THIS_MONTH_FILTER)
        time.sleep(2)
    except Exception as e:
        log.error(f"This Month filter click failed: {e}")
        allure.attach(str(e), name="This Month Filter Error", attachment_type=allure.attachment_type.TEXT)

@When(u'the user clicks the This Year filter button on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.THIS_YEAR_FILTER)
        time.sleep(2)
    except Exception as e:
        log.error(f"This Year filter click failed: {e}")
        allure.attach(str(e), name="This Year Filter Error", attachment_type=allure.attachment_type.TEXT)

@When(u'the user clicks the Payout filter button on Analytics Rebate page')
def step_impl(context):
    try:
        keyboard.press_and_release('Page Down')
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CONVERSION_FUNNEL_PAYOUTS)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CONVERSION_FUNNEL_PAYOUTS)
    except Exception as e:
        log.error(f"Payout filter click failed: {e}")
        allure.attach(str(e), name="Payout Filter Error", attachment_type=allure.attachment_type.TEXT)

@When(u'the user clicks the APPROVALS filter button on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CONVERSION_FUNNEL_APPROVALS)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CONVERSION_FUNNEL_APPROVALS)
    except Exception as e:
        log.error(f"Approvals filter click failed: {e}")
        allure.attach(str(e), name="Approvals Filter Error", attachment_type=allure.attachment_type.TEXT)

@When(u'the user clicks the Submission filter button on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CONVERSION_FUNNEL_SUBMISSIONS)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CONVERSION_FUNNEL_SUBMISSIONS)
    except Exception as e:
        log.error(f"Submission filter click failed: {e}")
        allure.attach(str(e), name="Submission Filter Error", attachment_type=allure.attachment_type.TEXT)

@When(u'the user clicks the Initiations filter button on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CONVERSION_FUNNEL_INITIATIONS)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CONVERSION_FUNNEL_INITIATIONS)
    except Exception as e:
        log.error(f"Initiations filter click failed: {e}")
        allure.attach(str(e), name="Initiations Filter Error", attachment_type=allure.attachment_type.TEXT)

@When(u'the user clicks the Scan/Clicks filter button on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CONVERSION_FUNNEL_SCANS_CLICKS)
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CONVERSION_FUNNEL_SCANS_CLICKS)
        time.sleep(3)
    except Exception as e:
        log.error(f"Scan/Clicks filter click failed: {e}")
        allure.attach(str(e), name="Scan/Clicks Filter Error", attachment_type=allure.attachment_type.TEXT)

@allure.step('the user clicks date range filter button on Analytics Rebate page')
@When('the user clicks date range filter button on Analytics Rebate page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_TODAY)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_YESTERDAY)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_LAST7)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_LAST30)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_THIS_MONTH)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_LAST_MONTH)
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Date range filter operations failed: {e}")
        allure.attach(str(e), name="Date Range Operations Error", attachment_type=allure.attachment_type.TEXT)


@Then(u'the data should be displayed accordingly on rebate analytics page')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("The page data has been updated and screenshot is attached")
    except Exception as e:
        log.error(f"Approvals filter click failed: {e}")
        allure.attach(str(e), name="Approvals Filter Error", attachment_type=allure.attachment_type.TEXT)