import keyboard
from allure_commons.types import AttachmentType
from behave import *
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Locators import locators
from Helper.enviHelper import Envi_Helper
from Logs import logs_file
import allure
import time
log = logs_file.get_logs()

@allure.step('User is on the Analytics General page')
@when(u'the user is on the Analytics General page')
def step_impl(context):
    try:
        # Envi_Helper(context.driver).wait_till_element_is_present(locators.analytics_general_dashboard,10)
        log.info("user is on the Analytics General page")
        time.sleep(2)
    except Exception as e:
        log.error(f"Navigation to Analytics General page failed: {e}")
        allure.attach(str(e), name="Analytics General Page Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user can access Experience dropdown on Analytics General page')
@when(u'the user can access Experience dropdown on Analytics General page')
def step_impl(context):
    try:
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER)
            log.info("clicked on experience filters")
        except :
            context.driver.find_element(By.XPATH,"//*[@id='pn_id_40']/div[2]/div")
            log.info("element not found used another method")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_ALL_EXPERIENCE)
        try:
            log.info("searching Test in experience filter")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_FILTER_SEARCH,"Auto WebApp Experience",10)
        except Exception as e:
            log.error("filter search is not working")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_SELECT_ALL)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        keyboard.press_and_release('Esc')
    except Exception as e:
        log.error(f"Experience dropdown access failed: {e}")
        allure.attach(str(e), name="Experience Dropdown Error", attachment_type=AttachmentType.TEXT)

@allure.step('Access dropdown ')
@then(u'metric with the selected filters will be shown')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("metrics data updated accordingly and screenshot attached")
    except Exception as e:
        log.error(f"Access dropdown failed: {e}")
        allure.attach(str(e), name="Dropdown Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user can access Variant dropdown ')
@when(u'the user can access Variant dropdown on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER)
        log.info("clicked  on variant filter")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_ALL_VARIANT)
        log.info("searching Test in experience filter")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_FILTER_SEARCH, "Auto", 10)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_SELECT_ALL)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_CROSS)
        keyboard.press_and_release('Esc')
        time.sleep(2)
    except Exception as e:
        log.error(f"Variant dropdown access failed: {e}")
        allure.attach(str(e), name="Variant Dropdown Error", attachment_type=AttachmentType.TEXT)

@allure.step('Category dropdown on Analytics General page')
@when(u'the user can access Category dropdown on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_FILTER)
        log.info("clicked  on filter")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_FILTER_CATEGORY)
        log.info("clicked  on category filter")
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_CATEGORY)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_ALL_CATEGORY)
        log.info("clicked  on all category")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.CATEGORY_FILTER_SEARCH, "Test", 10)
        log.info("searching category in CATEGORY filter")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_SELECT_ALL)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CATEGORY_FILTER_SEARCH_CROSS)
        keyboard.press_and_release('Esc')
        context.driver.find_element(By.XPATH,"//app-multi-select-group-filter[@class='ng-star-inserted']")
    except Exception as e:
        log.error(f"Category dropdown access failed: {e}")
        allure.attach(str(e), name="Category Dropdown Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user can access notification button on Analytics General page')
@then(u'the user can access notification button on Analytics General page')
def step_impl(context):
    try:

        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
        log.info("notification button is available")
        Envi_Helper.capture_screenshot()
        time.sleep(2)
    except Exception as e:
        log.error(f"Notification button access failed: {e}")
        allure.attach(str(e), name="Notification Button Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user can access logout button dropdown on Analytics General page')
@then(u'the user can access logout button dropdown on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
        log.info("logout button is available")
        Envi_Helper.capture_screenshot()
        keyboard.press_and_release('Esc')
        time.sleep(2)
    except Exception as e:
        log.error(f"Logout button access failed: {e}")
        allure.attach(str(e), name="Logout Button Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user can export the data on Analytics General page')
@then(u'the user can export the data on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.ANALYTICS_GENERAL_EXPORT_3DOT)
        log.info("export button is available")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.ANALYTICS_GENERAL_EXPORT)
        Envi_Helper.capture_screenshot()
        log.info("export button is clicked")
        time.sleep(2)
    except Exception as e:
        log.error(f"Data export failed: {e}")
        allure.attach(str(e), name="Data Export Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user clicks the Day filter button on Analytics General page')
@when(u'the user clicks the Day filter button on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TODAY_FILTER)
        log.info("Day Filter button is clicked")
        log.info("export button is available")
        time.sleep(2)
    except Exception as e:
        log.error(f"Day filter click failed: {e}")
        allure.attach(str(e), name="Day Filter Error", attachment_type=AttachmentType.TEXT)

@allure.step('the data should be displayed accordingly with export')
@then(u'the data should be displayed accordingly with export')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("Screenshot captured")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.ANALYTICS_GENERAL_EXPORT_3DOT)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.ANALYTICS_GENERAL_EXPORT)
        log.info("File is exported according to filter selected")
    except Exception as e:
        log.error(f"Data display verification failed: {e}")
        allure.attach(str(e), name="Data Display Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user clicks the This Week filter button on Analytics General page')
@when(u'the user clicks the This Week filter button on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.THIS_WEEK_FILTER)
        log.info("This Week Filter button is clicked")
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"This Week filter click failed: {e}")
        allure.attach(str(e), name="This Week Filter Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user clicks the This Month filter button on Analytics General page')
@when(u'the user clicks the This Month filter button on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.THIS_MONTH_FILTER)
        log.info("This Week Month button is clicked")
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"This Month filter click failed: {e}")
        allure.attach(str(e), name="This Month Filter Error", attachment_type=AttachmentType.TEXT)

@allure.step('All Time filter button on Analytics General page')
@when(u'the user clicks the All Time filter button on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.THIS_MONTH_FILTER)
        log.info("All Time button is clicked")
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"All Time filter click failed: {e}")
        allure.attach(str(e), name="All Time Filter Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user clicks the This Year filter button on Analytics General page')
@when(u'the user clicks the This Year filter button on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.THIS_YEAR_FILTER)
        log.info("This Year Filter button is clicked")
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"This Year filter click failed: {e}")
        allure.attach(str(e), name="This Year Filter Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user clicks date range filter button on Analytics General page')
@When('the user clicks date range filter button on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).insert_text_in_input_field(locators.ANALYTICS_START_DATE,"01 January 2025")
        log.info("Entered start date")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.ANALYTICS_END_DATE,"12 May 2025")
        log.info("Entered End date")

        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_TODAY)
        # time.sleep(2)
        # Envi_Helper.capture_screenshot()
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_YESTERDAY)
        # time.sleep(2)
        # Envi_Helper.capture_screenshot()
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_LAST7)
        # time.sleep(2)
        # Envi_Helper.capture_screenshot()
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_LAST30)
        # time.sleep(2)
        # Envi_Helper.capture_screenshot()
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_THIS_MONTH)
        # time.sleep(2)
        # Envi_Helper.capture_screenshot()
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE_LAST_MONTH)
        time.sleep(2)
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Date range filter operations failed: {e}")
        allure.attach(str(e), name="Date Range Operations Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user clicks the Scans/Clicks filter button on Analytics General page')
@when(u'the user clicks the Scans/Clicks filter button on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SCANS_CLICKS)
        Envi_Helper.capture_screenshot()
        log.info("Scan button is clicked")
    except Exception as e:
        log.error(f"Scans/Clicks filter click failed: {e}")
        allure.attach(str(e), name="Scans/Clicks Filter Error", attachment_type=AttachmentType.TEXT)

@allure.step('the data should be displayed accordingly')
@then(u'the data should be displayed accordingly')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("Screenshot captured")
    except Exception as e:
        log.error(f"Data display verification failed: {e}")
        allure.attach(str(e), name="Data Display Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user clicks the Registrations filter button on Analytics General page')
@when(u'the user clicks the Registrations filter button on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REGISTRATIONS)
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Registrations filter click failed: {e}")
        allure.attach(str(e), name="Registrations Filter Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user clicks the Engagements filter button on Analytics General page')
@when(u'the user clicks the Engagements filter button on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.ENGAGEMENTS)
        log.info("Engagements button is clicked")
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Engagements filter click failed: {e}")
        allure.attach(str(e), name="Engagements Filter Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user clicks the Website Visits filter button on Analytics General page')
@when(u'the user clicks the Website Visits filter button on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.WEBSITE_VISITS)
        log.info("Website Visits button is clicked")
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Website Visits filter click failed: {e}")
        allure.attach(str(e), name="Website Visits Filter Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user clicks the Revenue filter button on Analytics General page')
@when(u'the user clicks the Revenue filter button on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REVENUE)
        log.info("Revenue button is clicked")
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Revenue filter click failed: {e}")
        allure.attach(str(e), name="Revenue Filter Error", attachment_type=AttachmentType.TEXT)

@allure.step('the user hover to the eye icons on Analytics General page')
@when(u'the user hover to the eye icons on Analytics General page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).hover_to_element(locators.SCANS_CLICKS_EYE)
        log.info("scan eye button test us displayed")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).hover_to_element(locators.REGISTRATIONS_EYE)
        log.info("scan eye button test us displayed")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).hover_to_element(locators.ENGAGEMENTS_EYE)
        log.info("scan eye button test us displayed")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).hover_to_element(locators.WEBSITE_VISITS_EYE)
        log.info("scan eye button test us displayed")
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).hover_to_element(locators.REVENUE_EYE)
        log.info("scan eye button test us displayed")
        Envi_Helper.capture_screenshot()
    except Exception as e:
        log.error(f"Eye icon hover operations failed: {e}")
        allure.attach(str(e), name="Eye Icon Hover Error", attachment_type=AttachmentType.TEXT)


# @When(u'the user is on the Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).wait_till_element_is_present(locators.analytics_general_dashboard,10)
#     log.info("user is on the Analytics General page")
#     time.sleep(2)
#
# @Then('the user can access Experience dropdown on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER)
#     log.info("searching Test in experience filter")
#     Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_FILTER_SEARCH,"Test",10)
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_OPTION)
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_OPTION)
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
#
# @Then('the user can access Variant dropdown on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER)
#     log.info("searching Test in variant filter")
#     Envi_Helper(context.driver).insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH,"Test",10)
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION)
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_OPTION)
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
#     time.sleep(2)
#
# @Then('the user can access notification button on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
#     log.info("notification button is available")
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
#     time.sleep(2)
#
#
# @Then('the user can access logout button dropdown on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
#     log.info("logout button is available")
#     Envi_Helper.capture_screenshot()
#     time.sleep(2)
#
# @Then('the user can select a date range filter button on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DATE_RANGE)
#     time.sleep(2)
#
#
# @Then('the user can export the data on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPORT_BUTTON)
#     Envi_Helper.capture_screenshot()
#     log.info("export button is available")
#     time.sleep(2)
#
#
# @Then(u'the user clicks the Scans/Clicks filter button on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.SCANS_CLICKS)
#     log.info("Scan button is available")
#     Envi_Helper.capture_screenshot()
#
# @Then(u'the user clicks the Registrations filter button on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.REGISTRATIONS)
#     log.info("Registrations button is available")
#     Envi_Helper.capture_screenshot()
#
# @Then(u'the user clicks the Engagements filter button on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.ENGAGEMENTS)
#     log.info("Engagements button is available")
#     Envi_Helper.capture_screenshot()
#
# @Then(u'the user clicks the Website Visits filter button on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.WEBSITE_VISITS)
#     log.info("Website Visits button is available")
#     Envi_Helper.capture_screenshot()
#
# @Then(u'the user clicks the Revenue filter button on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.REVENUE)
#     log.info("Revenue button is available")
#     Envi_Helper.capture_screenshot()
#
# @Then(u'the user clicks the Today filter button on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.TODAY_FILTER)
#     log.info("Today Filter button is available")
#     Envi_Helper.capture_screenshot()
#
# @Then(u'the user clicks the This Week filter button on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.THIS_WEEK_FILTER)
#     log.info("This Week Filter button is available")
#     Envi_Helper.capture_screenshot()
#
# @Then(u'the user clicks the This Month filter button on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.THIS_MONTH_FILTER)
#     log.info("This Month Filter button is available")
#     Envi_Helper.capture_screenshot()
#
# @Then(u'the user clicks the This Year filter button on Analytics General page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.THIS_YEAR_FILTER)
#     time.sleep(2)
#     log.info("This Year Filter button is available")
#     Envi_Helper.capture_screenshot()
#
# # #
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
# #
# #
# #
# #
# #
# #
# #
# #
# #
#
#
# # from behave import *
# # from Locators import locators
# # from Logs import logs_file
# # from Helper.enviHelper import Envi_Helper
# # from TestData import Test_Data
# # import time
# #
# # @Given('The user is on the login page')
# # def step_impl(context):
# #     Envi_Helper(context.driver).open_page(Test_Data.Brij_url)
# #     time.sleep(2)
# #
# #  @when(u'The user entered valid email id "{login_id}" and password "{password}"')
# # def step_impl(context,login_id,password):
# #     Envi_Helper(context.driver).insert_text_in_input_field(locators.USERNAME_INPUT, login_id)
# #     Envi_Helper(context.driver).click(locators.USERNAME_SIGNIN)
# #     time.sleep(2)
# #     Envi_Helper(context.driver).insert_text_in_input_field(locators.PASSWORD_INPUT,password)
# #
# # @when('the user clicks the login button')
# # def step_impl(context):
# #     Envi_Helper(context.driver).click(locators.LOGIN_BUTTON)
# #
# #
# # @then('the user should be redirected to the dashboard page')
# # def step_impl(context):
# #     Envi_Helper(context.driver).wait_till_element_is_present(locators.analytics_general_dashboard,10)
# #
# # @then('the user should see the scans/clicks count')
# # def step_impl(context):
# #     Envi_Helper(context.driver).
# #     assert scans_clicks.isdigit()
# #
# # @then('the user should see the registrations count')
# # def step_impl(context):
# #     registrations = context.driver.find_element(*Locators.REGISTRATIONS).text
# #     assert registrations.isdigit()
# #
# # @then('the user should see the engagements count')
# # def step_impl(context):
# #     engagements = context.driver.find_element(*Locators.ENGAGEMENTS).text
# #     assert engagements.isdigit()
# #
# # @then('the user should see the website visits count')
# # def step_impl(context):
# #     website_visits = context.driver.find_element(*Locators.WEBSITE_VISITS).text
# #     assert website_visits.isdigit()
# #
# # @then('the user should see the revenue amount')
# # def step_impl(context):
# #     revenue = context.driver.find_element(*Locators.REVENUE).text
# #     assert revenue.startswith('$')
# #
# # @then('the user should be able to select a date range')
# # def step_impl(context):
# #     date_range = context.driver.find_element(*Locators.DATE_RANGE)
# #     assert date_range.is_displayed()
# #
# # @then('the user should be able to export the data')
# # def step_impl(context):
# #     export_button = context.driver.find_element(*Locators.EXPORT_BUTTON)
# #     assert export_button.is_displayed()
# #
# # @when('the user clicks the "{filter_button}" filter button')
# # def step_impl(context, filter_button):
# #     context.driver.find_element_by_xpath(f"//button[text()='{filter_button}']").click()
# #
# # @then('the results should be filtered for "{filter_button}"')
# # def step_impl(context, filter_button):
# #     # Add logic to verify the results are correctly filtered for the given time span
# #     filtered_results = context.driver.find_element_by_xpath("//div[@id='filteredResults']").text
# #     assert filtered_results == filter_button
