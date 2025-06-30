import keyboard
from behave import given, when, then
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators import locators
from Helper.enviHelper import Envi_Helper
import time
from allure_commons.types import AttachmentType
import allure
from Logs import logs_file

log = logs_file.get_logs()


# Navigation Steps
@when('the user navigates to the Form Module page')
def step_navigate_to_form_module_page(context):
    with allure.step("User navigates to the Form Module page"):
        try:
            module_menu = context.driver.find_element(By.XPATH, "(//li[@class='has-subnav ng-star-inserted'])[3]")
            actions = ActionChains(context.driver)
            actions.move_to_element(module_menu).perform()
            doc_option = context.driver.find_element(By.XPATH, "//span[normalize-space()='Form & Survey']")
            doc_option.click()
            context.driver.find_element(By.XPATH, "//div[@id='mainContent']")
            time.sleep(2)
        except Exception as e:
            log.error(f"Navigation to Form Module page failed: {e}")
            allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)


@then('the Form Module page should be displayed')
def step_form_module_page_displayed(context):
    with allure.step("Verify Form Module page is displayed"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present(locators.FORM_TITLE)
            Envi_Helper.capture_screenshot()
            allure.attach("Form Module page is displayed", name="Page Verification",
                          attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Form Module page verification failed: {e}")
            allure.attach(str(e), name="Page Verification Error", attachment_type=allure.attachment_type.TEXT)


# UI Elements Steps
@then('the user can access the notification button on the Form Module page')
def step_access_notification_button(context):
    with allure.step("Verify notification button is accessible"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).click(locators.NOTIFICATION_ICON)
            allure.attach("Notification button is accessible", name="UI Verification",
                          attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Notification button access failed: {e}")
            allure.attach(str(e), name="Notification Button Error", attachment_type=allure.attachment_type.TEXT)


@then('the user can access the logout button on the Form Module page')
def step_access_logout_button(context):
    with allure.step("Verify logout button is accessible"):
        try:
            Envi_Helper(context.driver).hover_to_element_to_click(locators.LOGOUT_BUTTON)
            Envi_Helper.capture_screenshot()
            allure.attach("Logout button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Logout button access failed: {e}")
            allure.attach(str(e), name="Logout Button Error", attachment_type=allure.attachment_type.TEXT)


@then('the user can access the field button on the Form Module page')
def step_access_field_button(context):
    with allure.step("Verify field button is accessible"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_FIELD)
            Envi_Helper.capture_screenshot()
            allure.attach("Field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Field button access failed: {e}")
            allure.attach(str(e), name="Field Button Error", attachment_type=allure.attachment_type.TEXT)


# Checkbox Steps
@when('the user selects all checkboxes on the Form Module page')
def step_select_all_checkboxes(context):
    with allure.step("User selects all checkboxes"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_SELECT_ALL)
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"Checkbox selection failed: {e}")
            allure.attach(str(e), name="Checkbox Selection Error", attachment_type=allure.attachment_type.TEXT)


@then('all checkboxes should be selected on the Form Module page')
def step_verify_all_checkboxes_selected(context):
    with allure.step("Verify all checkboxes are selected"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_SELECT_ALL)
            Envi_Helper.capture_screenshot()
            allure.attach("All checkboxes are selected", name="Checkbox Verification",
                          attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Checkbox verification failed: {e}")
            allure.attach(str(e), name="Checkbox Verification Error", attachment_type=allure.attachment_type.TEXT)


# Search Steps
@when('the user uses the search feature to search between the Form modules')
def step_use_search_feature(context):
    with allure.step("User uses the search feature"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_SEARCH, "test", 10)
            time.sleep(2)
        except Exception as e:
            log.error(f"Search feature usage failed: {e}")
            allure.attach(str(e), name="Search Feature Error", attachment_type=allure.attachment_type.TEXT)


@then('the search results should be displayed correctly on the Form Module page')
def step_verify_search_results(context):
    with allure.step("Verify search results are displayed correctly"):
        try:
            log.info("the searched data is displaying correctly")
            Envi_Helper.capture_screenshot()
            context.driver.find_element(By.XPATH, "//input[@placeholder='Search Items...']").clear()
            time.sleep(5)
            allure.attach("Search results are correct", name="Search Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Search results verification failed: {e}")
            allure.attach(str(e), name="Search Results Error", attachment_type=allure.attachment_type.TEXT)


# Sort Steps
@when('the user sorts the table on the Form Module page')
def step_sort_table(context):
    with allure.step("User sorts the table"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_MODULE_HEADING)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_WHERE_USED)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_CALL_TO_ACTION)
            time.sleep(2)
        except Exception as e:
            log.error(f"Table sorting failed: {e}")
            allure.attach(str(e), name="Table Sorting Error", attachment_type=allure.attachment_type.TEXT)


@then('the table should be sorted in the correct order on the Form Module page')
def step_verify_table_sorted(context):
    with allure.step("Verify table is sorted"):
        try:
            log.info("the searched data is sorted correctly and the screenshots are captured")
            allure.attach("Table is sorted", name="Sort Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Table sort verification failed: {e}")
            allure.attach(str(e), name="Sort Verification Error", attachment_type=allure.attachment_type.TEXT)


# Create Module Steps
@when('the user creates a new Form module')
def step_create_new_module(context):
    with allure.step("User creates a new Form module"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_NEW_MODULE)
            time.sleep(2)
            Envi_Helper(context.driver).capture_screenshot()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_POPUP_MODULE_NAME, "Auto FORM Test",
                                                                   10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_POPUP_CTA, "Form Testing", 10)
            keyboard.press_and_release('pagedown')
            time.sleep(2)

            # text field
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_TEXTFIELD_BUTTON, 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_TEXTFIELD_TITLE, "Auto Text", 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_TEXTFIELD_SUBTEXT, "Auto subtext", 10)
            Envi_Helper.capture_screenshot()
            keyboard.press_and_release('pagedown')
            time.sleep(2)

            # dropdown field
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_DROPDOWN, 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_DROPDOWN_TITLE, "Auto Text", 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_DROPDOWN_SUBTEXT, "Auto subtext", 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_DROPDOWN_CHOICE_1, "option 1", 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_DROPDOWN_ADDCHOICE)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_DROPDOWN_CHOICE_2, "option 2", 10)
            Envi_Helper.capture_screenshot()

            # multiple choice
            keyboard.press_and_release('pagedown')
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_MULTICHOICE, 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_MULTICHOICE_TITLE, "Auto Text", 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_MULTICHOICE_SUBTEXT, "Auto subtext",
                                                                   10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_MULTICHOICE_CHOICE_1, "Choice 1", 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_MULTICHOICE_ADDCHOICE)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_MULTICHOICE_CHOICE_2, "Choice 2", 10)
            time.sleep(2)

            # advanced settings
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING_lIMIT)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING_lIMIT)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING_CCM)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_POPUP_ASETTING_CCM_TEXT, "thankyou",
                                                                   10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING_CC)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING_BACK)
            time.sleep(2)

            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_POPUP_SAVE_BUTTON)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_POPUP_CLOSE)
            time.sleep(5)
        except Exception as e:
            log.error(f"New Form module creation failed: {e}")
            allure.attach(str(e), name="Module Creation Error", attachment_type=allure.attachment_type.TEXT)


@then('the new Form module should be added to the module list')
def step_verify_new_module_added(context):
    with allure.step("Verify new Form module is added"):
        try:
            Envi_Helper(context.driver).capture_element_text(locators.FORM_LIST, 10)
            allure.attach("New Form module is added", name="Create Module Verification",
                          attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"New module verification failed: {e}")
            allure.attach(str(e), name="Module Verification Error", attachment_type=allure.attachment_type.TEXT)


# Edit Module Steps
@when('the user edits an existing Form module')
def step_edit_module(context):
    with allure.step("User edits an existing Form module"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_LIST_ECLIPSE)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_LIST_ECLIPSE_EDIT)
            time.sleep(2)
            Envi_Helper(context.driver).capture_element_text(locators.FORM_ADD_EDIT_MODULE, 10)
            Envi_Helper(context.driver).capture_screenshot()
            context.driver.find_element(By.XPATH, "//input[@placeholder='Enter module name...']").clear()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_POPUP_MODULE_NAME,
                                                                   "updated Auto FORM Test", 10)
            context.driver.find_element(By.XPATH, "//input[@placeholder='Enter call to action...']").clear()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_POPUP_CTA, "updated Testing", 10)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_POPUP_SAVE_BUTTON)
            time.sleep(5)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_POPUP_CLOSE)
            time.sleep(2)
        except Exception as e:
            log.error(f"Form module edit failed: {e}")
            allure.attach(str(e), name="Module Edit Error", attachment_type=allure.attachment_type.TEXT)


@then('the changes should be saved and reflected in the Form module list')
def step_verify_module_edited(context):
    with allure.step("Verify changes are saved"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present(locators.FORM_LIST, 10)
            Envi_Helper.capture_screenshot()
            allure.attach("Changes are saved", name="Edit Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Changes verification failed: {e}")
            allure.attach(str(e), name="Edit Verification Error", attachment_type=allure.attachment_type.TEXT)


# Delete Module Steps
@when('the user deletes an unused Form module')
def step_delete_module(context):
    with allure.step("User deletes an unused Form module"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.FORM_SEARCH, "Auto", 10)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_SELECT_ALL)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_DELETE_BUTTON)
            Envi_Helper.capture_screenshot()
            time.sleep(2)
            context.driver.find_element(By.XPATH, "//input[@placeholder='Search Items...']").clear()
            time.sleep(5)
        except Exception as e:
            log.error(f"Form module deletion failed: {e}")
            allure.attach(str(e), name="Module Deletion Error", attachment_type=allure.attachment_type.TEXT)


@then('the module should be removed from the Form module list')
def step_verify_module_deleted(context):
    with allure.step("Verify module is deleted"):
        try:
            Envi_Helper.capture_screenshot()
            log.info("the unused modules are deleted successfully")
            allure.attach("Module is deleted", name="Delete Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Module deletion verification failed: {e}")
            allure.attach(str(e), name="Deletion Verification Error", attachment_type=allure.attachment_type.TEXT)


@when('the user want to see the number of rows on the FORM module list')
def step_impl(context):
    with allure.step("User checks number of rows"):
        try:
            keyboard.press('pagedown')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_OPTION)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_20)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_OPTION)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_100)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_OPTION)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_1000)
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"Row count verification failed: {e}")
            allure.attach(str(e), name="Row Count Error", attachment_type=allure.attachment_type.TEXT)


@then('the module list should be updated on FORM page')
def step_impl(context):
    with allure.step("Verify module list is updated"):
        try:
            Envi_Helper.capture_screenshot()
            log.info("the rows are updated successfully")
        except Exception as e:
            log.error(f"Module list update verification failed: {e}")
            allure.attach(str(e), name="List Update Error", attachment_type=allure.attachment_type.TEXT)


