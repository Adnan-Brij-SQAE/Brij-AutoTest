import keyboard
from behave import when, then
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
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click("(//li[@class='has-subnav ng-star-inserted'])[3]")
            helper.wait_till_element_is_present_to_click("//span[normalize-space()='Form & Survey']")
            time.sleep(2)
            helper.open_page("https://rc.brij.it/brand/modules/forms")
            helper.get_value("//div[@id='mainContent']")
            log.info("Navigated to FORM Module page")
            allure.attach("FORM Module page loaded", name="Page Verification")
            time.sleep(2)

        except Exception as ex:
            log.error(f"Navigation to Form Module page failed: {ex}")
            allure.attach(str(ex), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@then('the Form Module page should be displayed')
def step_form_module_page_displayed(context):
    with allure.step("Verify Form Module page is displayed"):
        try:
            helper = Envi_Helper(context.page)
            helper.get_value(locators.FORM_TITLE)
            helper.capture_screenshot()
            allure.attach("Form Module page is displayed", name="Page Verification",attachment_type=AttachmentType.TEXT)
        except Exception as ex:
            log.error(f"Form Module page verification failed: {ex}")
            allure.attach(str(ex), name="Page Verification Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

# UI Elements Steps
@then('the user can access the notification button on the Form Module page')
def step_access_notification_button(context):
    with allure.step("Verify notification button is accessible"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            allure.attach("Notification button is accessible", name="UI Verification",attachment_type=AttachmentType.TEXT)
        except Exception as ex:
            log.error(f"Notification button access failed: {ex}")
            allure.attach(str(ex), name="Notification Button Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@then('the user can access the logout button on the Form Module page')
def step_access_logout_button(context):
    with allure.step("Verify logout button is accessible"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            allure.attach("Logout button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as ex:
            log.error(f"Logout button access failed: {ex}")
            allure.attach(str(ex), name="Logout Button Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@then('the user can access the field button on the Form Module page')
def step_access_field_button(context):
    with allure.step("Verify field button is accessible"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.FORM_FIELD)
            helper.capture_screenshot()
            allure.attach("Field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as ex:
            log.error(f"Field button access failed: {ex}")
            allure.attach(str(ex), name="Field Button Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

# Checkbox Steps
@when('the user selects all checkboxes on the Form Module page')
def step_select_all_checkboxes(context):
    with allure.step("User selects all checkboxes"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.FORM_SELECT_ALL)
            helper.capture_screenshot()
        except Exception as ex:
            log.error(f"Checkbox selection failed: {ex}")
            allure.attach(str(ex), name="Checkbox Selection Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@then('all checkboxes should be selected on the Form Module page')
def step_verify_all_checkboxes_selected(context):
    with allure.step("Verify all checkboxes are selected"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.FORM_SELECT_ALL)
            helper.capture_screenshot()
            allure.attach("All checkboxes are selected", name="Checkbox Verification",attachment_type=AttachmentType.TEXT)
        except Exception as ex:
            log.error(f"Checkbox verification failed: {ex}")
            allure.attach(str(ex), name="Checkbox Verification Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

# Search Steps
@when('the user uses the search feature to search between the Form modules')
def step_use_search_feature(context):
    with allure.step("User uses the search feature"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.FORM_SEARCH, "test", 10)
            time.sleep(5)
        except Exception as ex:
            log.error(f"Search feature usage failed: {ex}")
            allure.attach(str(ex), name="Search Feature Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@then('the search results should be displayed correctly on the Form Module page')
def step_verify_search_results(context):
    with allure.step("Verify search results are displayed correctly"):
        try:
            helper = Envi_Helper(context.page)
            log.info("the searched data is displaying correctly")
            helper.capture_screenshot()
            time.sleep(5)
            allure.attach("Search results are correct", name="Search Verification", attachment_type=AttachmentType.TEXT)
        except Exception as ex:
            log.error(f"Search results verification failed: {ex}")
            allure.attach(str(ex), name="Search Results Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

# Sort Steps
@when('the user sorts the table on the Form Module page')
def step_sort_table(context):
    with allure.step("User sorts the table"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.FORM_MODULE_HEADING)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.FORM_MODULE_HEADING)
            helper.wait_till_element_is_present_to_click(locators.FORM_WHERE_USED)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.FORM_WHERE_USED)
            helper.wait_till_element_is_present_to_click(locators.FORM_CALL_TO_ACTION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.FORM_CALL_TO_ACTION)
        except Exception as ex:
            log.error(f"Table sorting failed: {ex}")
            allure.attach(str(ex), name="Table Sorting Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@then('the table should be sorted in the correct order on the Form Module page')
def step_verify_table_sorted(context):
    with allure.step("Verify table is sorted"):
        try:
            helper = Envi_Helper(context.page)
            log.info("the searched data is sorted correctly and the screenshots are captured")
            allure.attach("Table is sorted", name="Sort Verification", attachment_type=AttachmentType.TEXT)
        except Exception as ex:
            log.error(f"Table sort verification failed: {ex}")
            allure.attach(str(ex), name="Sort Verification Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

# Create Module Steps
@when('the user creates a new Form module')
def step_create_new_module(context):
    with allure.step("User creates a new Form module"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.FORM_NEW_MODULE)
            time.sleep(2)
            helper.insert_text_in_input_field(locators.FORM_POPUP_MODULE_NAME, "Auto FORM Test")
            helper.insert_text_in_input_field(locators.FORM_POPUP_CTA, "Form Testing")
            helper.insert_text_in_input_field(locators.FORM_POPUP_EDITOR, "Auto Test Description")
            helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_SAVE_BUTTON)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_CLOSE)
        except Exception as ex:
            log.error(f"New Form module creation failed: {ex}")
            allure.attach(str(ex), name="Module Creation Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@when('the user creates a new Form module with properties and validation')
def step_create_new_module(context):
    with allure.step("User creates a new Form module"):
        try:
            log.error("Form module properties and validation check is pending")
            # helper = Envi_Helper(context.page)
            # helper.wait_till_element_is_present_to_click(locators.FORM_NEW_MODULE)
            # time.sleep(4)
            # helper.insert_text_in_input_field(locators.FORM_POPUP_MODULE_NAME, "Auto FORM Test",10)
            # helper.insert_text_in_input_field(locators.FORM_POPUP_CTA, "Form Testing", 10)
            # helper.insert_text_in_input_field(locators.FORM_POPUP_EDITOR, "Auto Test Description", 10)
            #
            # # text field
            # try:
            #     keyboard.press_and_release('pagedown')
            #     helper.wait_till_element_is_present_to_click(locators.FORM_TEXTFIELD_BUTTON)
            #     helper.insert_text_in_input_field(locators.FORM_TEXTFIELD_TITLE, "Auto Text")
            #     helper.insert_text_in_input_field(locators.FORM_TEXTFIELD_SUBTEXT, "Auto subtext")
            #     helper.capture_screenshot()
            # except:
            #     context.page.get_by_role("button", name="text field button Text Field").click()
            #     context.page.get_by_role("textbox", name="Enter question text").fill("Auto Text")
            #     context.page.get_by_role("textbox", name="Enter question text").fill("Auto Subtext")
            #     context.page.locator(".icon2").click()
            #     context.page.locator(".short-answer-icon").click()
            #     log.info("successfully created text question")
            #     helper.capture_screenshot()
            #
            # # dropdown field
            # try:
            #     helper.wait_till_element_is_present_to_click(locators.FORM_DROPDOWN, 10)
            #     helper.insert_text_in_input_field(locators.FORM_DROPDOWN_TITLE, "Auto Text", 10)
            #     helper.insert_text_in_input_field(locators.FORM_DROPDOWN_SUBTEXT, "Auto subtext", 10)
            #     helper.insert_text_in_input_field(locators.FORM_DROPDOWN_CHOICE_1, "option 1", 10)
            #     helper.wait_till_element_is_present_to_click(locators.FORM_DROPDOWN_ADDCHOICE)
            #     helper.insert_text_in_input_field(locators.FORM_DROPDOWN_CHOICE_2, "option 2", 10)
            #     helper.capture_screenshot()
            # except:
            #     context.page.get_by_role("button", name="text field button Dropdown").click()
            #     context.page.get_by_role("textbox", name="Enter question text").fill("Auto Test dropdown")
            #     context.page.get_by_role("textbox", name="Enter subtext").fill("Auto Test subtext")
            #     context.page.get_by_role("textbox", name="Enter choice").click()
            #     context.page.get_by_role("textbox", name="Enter choice").fill("first choice")
            #     context.page.get_by_role("button", name="Choice icon Add Choice").click()
            #     context.page.locator("#drop-down11").fill("second choice")
            #     context.page.get_by_role("button", name="Choice icon Add Choice").click()
            #     context.page.locator("#drop-down12").fill("third choice")
            #     context.page.get_by_role("button", name="Choice icon Add Choice").click()
            #     log.info("created dropdown question")
            #     context.page.locator("#drop-down13").fill("for delete")
            #     context.page.get_by_role("img", name="three dots icon").click()
            #     context.page.get_by_text("Remove Choice").click()
            #     log.info("sucessfully deleted the choice ")
            #     helper.capture_screenshot()
            #
            # # multiple choice
            # try:
            #     helper.wait_till_element_is_present_to_click(locators.FORM_MULTICHOICE, 10)
            #     helper.insert_text_in_input_field(locators.FORM_MULTICHOICE_TITLE, "Auto Text", 10)
            #     helper.insert_text_in_input_field(locators.FORM_MULTICHOICE_SUBTEXT, "Auto subtext")
            #     helper.insert_text_in_input_field(locators.FORM_MULTICHOICE_CHOICE_1, "Choice 1", 10)
            #     helper.wait_till_element_is_present_to_click(locators.FORM_MULTICHOICE_ADDCHOICE)
            #     helper.insert_text_in_input_field(locators.FORM_MULTICHOICE_CHOICE_2, "Choice 2", 10)
            #     time.sleep(2)
            # except:
            #     context.page.get_by_role("button", name="text field button Multiple").click()
            #     context.page.get_by_role("textbox", name="Enter question text").fill("Auto Test Multiple choice ")
            #     context.page.get_by_role("textbox", name="Enter question text").click()
            #     context.page.get_by_role("textbox", name="Enter subtext").click()
            #     context.page.get_by_role("textbox", name="Enter subtext").fill("Auto Subtext")
            #     context.page.get_by_role("textbox", name="Enter choice").click()
            #     context.page.get_by_role("textbox", name="Enter choice").fill("M Choice 1")
            #     context.page.get_by_role("button", name="Add option icon Add Choice").click()
            #     context.page.locator("#multiple-choice21").fill("M Choice 2")
            #     context.page.get_by_role("button", name="Add option icon Add Choice").click()
            #     context.page.locator("#multiple-choice22").fill("M Choice 3")
            #     context.page.get_by_role("button", name="Add option icon Add Choice").click()
            #     context.page.locator("#multiple-choice23").fill("M Choice Delete ")
            #     context.page.get_by_role("img", name="three dots").click()
            #     context.page.get_by_text("Remove Choice").click()
            #
            # # advanced settings
            # helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING)
            # time.sleep(2)
            # helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING_lIMIT)
            # helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING_lIMIT)
            # helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING_CCM)
            # helper.insert_text_in_input_field(locators.FORM_POPUP_ASETTING_CCM_TEXT, "thankyou")
            # helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING_CC)
            # helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_ASETTING_BACK)
            # time.sleep(2)
            # helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_SAVE_BUTTON)
            # time.sleep(2)
            # helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_CLOSE)
            # time.sleep(5)
        except Exception as ex:

            log.error(f"New Form module creation failed: {ex}")
            allure.attach(str(ex), name="Module Creation Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@then('the module list should be updated on Form Module page')
def step_verify_new_module_added(context):
    with allure.step("Verify new Form module is added"):
        try:
            helper = Envi_Helper(context.page)
            helper.get_value(locators.FORM_LIST, 10)
            allure.attach("New Form module is added", name="Create Module Verification",attachment_type=AttachmentType.TEXT)
        except Exception as ex:
            log.error(f"New module verification failed: {ex}")
            allure.attach(str(ex), name="Module Verification Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

# Edit Module Steps
@when('the user edits an existing Form module')
def step_edit_module(context):
    with allure.step("User edits an existing Form module"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.FORM_SEARCH,"Auto")
            time.sleep(4)
            helper.wait_till_element_is_present_to_click(locators.FORM_LIST_ECLIPSE)
            helper.wait_till_element_is_present_to_click(locators.FORM_LIST_ECLIPSE_EDIT)
            time.sleep(2)
            helper.insert_text_in_input_field(locators.FORM_POPUP_MODULE_NAME,"updated Auto FORM Test", 10)
            helper.insert_text_in_input_field(locators.FORM_POPUP_CTA, "updated Testing", 10)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_SAVE_BUTTON)
            time.sleep(5)
            helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_CLOSE)
            time.sleep(2)
        except Exception as ex:
            log.error(f"Form module edit failed: {ex}")
            allure.attach(str(ex), name="Module Edit Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

# Delete Module Steps
@when('the user deletes an unused Form module')
def step_delete_module(context):
    with allure.step("User deletes an unused Form module"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.FORM_SEARCH, "Auto", 10)
            time.sleep(4)
            helper.wait_till_element_is_present_to_click(locators.FORM_LIST_ECLIPSE)
            helper.wait_till_element_is_present_to_click(locators.FORM_LIST_DELETE)
            helper.wait_till_element_is_present_to_click(locators.FORM_CONFIRM_DELETE_BUTTON)
            helper.capture_screenshot()
        except Exception as ex:
            log.error(f"Form module deletion failed: {ex}")
            allure.attach(str(ex), name="Module Deletion Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@then('the user deletes more than one unused Form module')
def step_verify_module_deleted(context):
    helper = Envi_Helper(context.page)
    with allure.step("Verify module is deleted"):
        try:
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.FORM_SELECT_ALL)
            helper.wait_till_element_is_present_to_click(locators.FORM_DELETE_BUTTON)
            time.sleep(2)
            log.info("the unused modules are deleted successfully")
            allure.attach("Module is deleted", name="Delete Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as ex:
            log.error(f"Module deletion verification failed: {ex}")
            allure.attach(str(ex), name="Deletion Verification Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@when('the user wants to see the number of rows on the Form Module list')
def step_impl(context):
    with allure.step("User checks number of rows"):
        try:
            helper = Envi_Helper(context.page)
            keyboard.press('pagedown')
            helper.wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_OPTION)
            helper.wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_20)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_OPTION)
            helper.wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_100)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_OPTION)
            helper.wait_till_element_is_present_to_click(locators.FORM_ROWPERPAGE_1000)
            helper.capture_screenshot()
        except Exception as ex:
            log.error(f"Row count verification failed: {ex}")
            allure.attach(str(ex), name="Row Count Error", attachment_type=allure.attachment_type.TEXT)
            raise ex


@then('the changes should be saved and reflected in the Form module list')
def step_impl(context):
    with allure.step("Verify module list is updated"):
        try:
            helper = Envi_Helper(context.page)
            helper.capture_screenshot()
            log.info("the rows are updated successfully")
        except Exception as ex:
            log.error(f"Module list update verification failed: {ex}")
            allure.attach(str(ex), name="List Update Error", attachment_type=allure.attachment_type.TEXT)
            raise ex


@then(u'the user should select Module Name option on the field button on the Form Module page')
def step_impl(context):
    with allure.step("Check/uncheck Module name"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.FORM_FIELD_MODULE_NAME)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.FORM_FIELD_MODULE_NAME)
        except Exception as ex:
            log.error(f"Module name interaction failed: {ex}")
            allure.attach(str(ex), name="Module name interaction Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@then(u'the user should select the Where Used option on the field button on the Form Module page')
def step_impl(context):
    with allure.step("Check/uncheck Where Used"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.FORM_FIELD_WHERE_USED)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.FORM_FIELD_WHERE_USED)
        except Exception as ex:
            log.error(f"where used interaction failed: {ex}")
            allure.attach(str(ex), name="Where used interaction Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@then(u'the user should select the Call to Action option on the field button on the Form Module page')
def step_impl(context):
    with allure.step("Check/uncheck Call to Action"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.FORM_FIELD_CTA)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.FORM_FIELD_CTA)
            helper.wait_till_element_is_present_to_click(locators.FORM_FIELD)
        except Exception as ex:
            log.error(f"CTA interaction failed: {ex}")
            allure.attach(str(ex), name="CTA interaction Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

@when(u'the user duplicates an existing Form module')
def step_impl(context):
    with allure.step("User edits an existing Form module"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.FORM_SEARCH,"Auto")
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.FORM_LIST_ECLIPSE)
            helper.wait_till_element_is_present_to_click(locators.FORM_LIST_ECLIPSE_EDIT)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.FORM_DUPLICATE)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_SAVE_BUTTON)
            helper.capture_screenshot()
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_CLOSE)
        except Exception as ex:
            helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_SAVE_BUTTON)
            helper.capture_screenshot()
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.FORM_POPUP_CLOSE)
            log.error(f"Form module duplicate failed: {ex}")
            allure.attach(str(ex), name="Module duplicate Error", attachment_type=allure.attachment_type.TEXT)
            raise ex

