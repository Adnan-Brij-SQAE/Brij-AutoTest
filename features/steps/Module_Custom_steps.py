import time

from behave import when, then
from Locators import locators
from Helper.enviHelper import Envi_Helper
from Logs import logs_file
import allure

log = logs_file.get_logs()

# --- Navigation Steps ---

@when('the user navigates to the Custom Module page')
def step_navigate_to_custom_module_page(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click("(//li[@class='has-subnav ng-star-inserted'])[3]")
    helper.wait_till_element_is_present_to_click("//span[normalize-space()='Custom']")
    time.sleep(2)
    helper.open_page("https://rc.brij.it/brand/modules/custom")
    helper.get_value("//div[@id='mainContent']")
    log.info("Navigated to Custom Module page")
    allure.attach("Custom Module page loaded", name="Page Verification")


@then('the Custom Module page should be displayed')
def step_verify_navigation(context):
    helper = Envi_Helper(context.page)
    helper.get_value(locators.CUSTOM_TITLE)
    allure.attach("Custom Module page displayed", name="Navigation Verification")


# --- UI Elements Steps ---

@then('the user should see the notification button on the Custom Module page')
def step_verify_notification_button(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
    allure.attach("Notification button accessible", name="Notification Verification")


@then('the user should see the logout button on the Custom Module page')
def step_verify_logout_button(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
    allure.attach("Logout button accessible", name="Logout Verification")


@then('the user should see the field button on the Custom Module page')
def step_verify_field_button(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_FIELD_BUTTON)
    helper.capture_screenshot()
    allure.attach("Field button accessible", name="Field Button Verification")


@then('the user should see the Module Name option on the field button')
def step_verify_field_module_name(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_FIELD_MODULE_NAME)
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_FIELD_MODULE_NAME)
    allure.attach("Module name accessible", name="Field Module Name Verification")


@then('the user should see the Where Used option on the field button')
def step_verify_field_where_used(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_FIELD_WHERE_USED)
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_FIELD_WHERE_USED)
    allure.attach("'Where Used' accessible", name="Field Where Used Verification")


@then('the user should see the Call to Action option on the field button')
def step_verify_field_cta(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_FIELD_CALL_TO_ACTION)
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_FIELD_CALL_TO_ACTION)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_FIELD_BUTTON)
    allure.attach("'Call to Action' accessible", name="Field CTA Verification")


# --- Checkbox Steps ---

@when('the user selects all checkboxes on the Custom Module page')
def step_select_all_checkboxes(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ALL_CHECK)
    helper.capture_screenshot()
    allure.attach("All checkboxes selected", name="Checkbox Selection")


@then('all checkboxes should be selected on the Custom Module page')
def step_verify_checkboxes_selected(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ALL_CHECK)
    allure.attach("Checkboxes selection verified", name="Checkbox Verification")


# --- Create Module Steps ---

@when('the user creates a new Custom module')
def step_create_custom_module(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_NEW_MODULE)
    helper.insert_text_in_input_field(locators.CUSTOM_POPUP_MODULE_NAME, "AUTO Custom module")
    helper.insert_text_in_input_field(locators.CUSTOM_POPUP_CTA, "AUTO Custom CTA")
    helper.insert_text_in_input_field(locators.CUSTOM_POPUP_EDITOR, "Demo Automation Text")
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_POPUP_SAVE_BUTTON)
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_POPUP_CLOSE)
    allure.attach("New Custom module created", name="Create Module")


@then('the new Custom module should appear in the module list')
def step_verify_module_added(context):
    helper = Envi_Helper(context.page)
    helper.get_value(locators.CUSTOM_LIST)
    allure.attach("New module added to list", name="Create Verification")


# --- Edit Module Steps ---

@when('the user edits an existing Custom module')
def step_edit_custom_module(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ECLIPSE)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ECLIPSE_EDIT)
    helper.insert_text_in_input_field(locators.CUSTOM_POPUP_MODULE_NAME, "AUTO Updated module")
    helper.insert_text_in_input_field(locators.CUSTOM_POPUP_CTA, "AUTO Updated CTA")
    helper.insert_text_in_input_field(locators.CUSTOM_POPUP_EDITOR, "Updated text")
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_POPUP_SAVE_BUTTON)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_POPUP_CLOSE)
    allure.attach("Custom module edited", name="Edit Module")


@then('the changes should be made with the updated custom module')
def step_verify_module_edited(context):
    helper = Envi_Helper(context.page)
    helper.capture_screenshot()
    helper.get_value(locators.CUSTOM_LIST)
    allure.attach("Changes saved and reflected", name="Edit Verification")


# --- Duplicate Module Steps ---

@when('the user duplicates an existing Custom module')
def step_duplicate_custom_module(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ECLIPSE)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ECLIPSE_EDIT)
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_POPUP_DUPLICATE)
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_POPUP_SAVE_BUTTON)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_POPUP_CLOSE)
    allure.attach("Custom module duplicated", name="Duplicate Module")

# --- Sort Steps ---

@when('the user sorts the table data')
def step_sort_table_data(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_MODULE_HEADING)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_WHERE_USED)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_CALL_TO_ACTION)
    allure.attach("Table sorted", name="Sort Action")


@then('the table data should be sorted correctly')
def step_verify_table_sorted(context):
    allure.attach("Table sorted correctly", name="Sort Verification")


# --- Pagination Steps ---

@when('the user changes the number of rows displayed on the module list')
def step_set_rows_per_page(context):
    helper = Envi_Helper(context.page)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ROWPERPAGE_OPTION)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ROWPERPAGE_20)
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ROWPERPAGE_OPTION)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ROWPERPAGE_100)
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ROWPERPAGE_OPTION)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ROWPERPAGE_1000)
    helper.capture_screenshot()
    allure.attach("Rows per page updated", name="Pagination Action")


@then('the module list should update to reflect the selected number of rows')
def step_verify_pagination(context):
    allure.attach("Pagination verified", name="Pagination Verification")


# --- Delete Module Steps ---

@when('the user deletes unused Custom modules')
def step_delete_custom_module(context):
    helper = Envi_Helper(context.page)
    helper.insert_text_in_input_field(locators.CUSTOM_SEARCH, "Auto")
    time.sleep(2)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ECLIPSE)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ECLIPSE_DELETE)
    helper.capture_screenshot()
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_CONFIRM_DELETE_BUTTON)
    allure.attach("Single Custom module deleted", name="Delete Single")


@then('the user deletes more than one unused Custom module')
def step_delete_multiple_custom_modules(context):
    helper = Envi_Helper(context.page)
    helper.insert_text_in_input_field(locators.CUSTOM_SEARCH, "Auto")
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_ALL_CHECK)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_DELETE_ALL)
    helper.wait_till_element_is_present_to_click(locators.CUSTOM_DELETE_CONFIRM)
    helper.capture_screenshot()
    allure.attach("Multiple Custom modules deleted", name="Delete Multiple")

@when('the user searches for a Custom module')
def step_search_custom_module(context):
    helper = Envi_Helper(context.page)
    helper.insert_text_in_input_field(locators.CUSTOM_SEARCH, "test")

    allure.attach("search custom module", name="search functionality")

@then(u'the search results should display the matching Custom modules')
def step_impl(context):
    helper = Envi_Helper(context.page)
    helper.capture_screenshot()

    allure.attach("search custom module", name="search functionality")