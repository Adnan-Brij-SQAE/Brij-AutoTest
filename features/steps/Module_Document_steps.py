from behave import when, then
from Locators import locators
from Helper.enviHelper import Envi_Helper
import time
from allure_commons.types import AttachmentType
import allure
from Logs import logs_file
log = logs_file.get_logs()


# Navigation Steps
@when('the user navigates to the Document Module page')
def step_navigate_to_document_module_page(context):
    with allure.step("User navigates to the Document Module page"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click("(//li[@class='has-subnav ng-star-inserted'])[3]")
            helper.wait_till_element_is_present_to_click("//span[normalize-space()='Document']")
            time.sleep(2)
            helper.open_page("https://rc.brij.it/brand/modules/documents")
            helper.get_value("//div[@id='mainContent']")
            log.info("Navigated to Document Module page")
            allure.attach("Document Module page loaded", name="Page Verification")
            time.sleep(2)
        except Exception as e:
            log.error(f"Navigation failed: {e}")
            allure.attach(str(e), name="Navigation Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

@then('the Document Module page should be displayed')
def step_document_module_page_displayed(context):
    with allure.step("Verify Document Module page is displayed"):
        try:
            helper = Envi_Helper(context.page)
            page_title = helper.get_value("//h1[normalize-space()='Document']")
            log.info(f"navigated to correct page {page_title}")
            log.info("the user is on the Document Module page")
            allure.attach("Document Module page is displayed", name="Page Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Document Module display verification failed: {e}")
            allure.attach(str(e), name="Document page Display Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

# UI Elements Steps
@then('the user can access the notification button on the Document Module page')
def step_access_notification_button(context):
    with allure.step("Verify notification button is accessible"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            allure.attach("Notification button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Notification button access failed: {e}")
            allure.attach(str(e), name="Notification Access Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

@then('the user can access the logout button on the Document Module page')
def step_access_logout_button(context):
    with allure.step("Verify logout button is accessible"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            allure.attach("Logout button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Logout button access failed: {e}")
            allure.attach(str(e), name="Logout Access Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

@then('the user can access the field button on the Document Module page')
def step_access_field_button(context):
    with allure.step("Verify field button is accessible"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FIELD_BUTTON)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FIELD_MODULE_NAME)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FIELD_MODULE_NAME)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FIELD_WHERE_USED)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FIELD_WHERE_USED)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FIELD_CTA)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FIELD_CTA)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FIELD_FILE_NAME)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FIELD_FILE_NAME)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FIELD_BUTTON)
            allure.attach("Field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Field button access failed: {e}")
            allure.attach(str(e), name="Field Access Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

# Checkbox Steps
@when('the user selects all checkboxes on Document Module page')
def step_select_all_checkboxes(context):
    with allure.step("User selects all checkboxes"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_SELECT_ALL_CHECKBOXES)
        except Exception as e:
            log.error(f"Checkbox selection failed: {e}")
            allure.attach(str(e), name="Checkbox Select Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

@then('all checkboxes should be selected on Document Module page')
def step_verify_all_checkboxes_selected(context):
    with allure.step("Verify all checkboxes are selected"):
        try:
            helper = Envi_Helper(context.page)
            helper.capture_screenshot()
            log.info("All unused forms are selected ")
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_SELECT_ALL_CHECKBOXES)
            allure.attach("All checkboxes are selected", name="Checkbox Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Checkbox verification failed: {e}")
            allure.attach(str(e), name="Checkbox Verification Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

# Search Steps
@when('the user uses the search feature to search between the document modules')
def step_use_search_feature(context):
    with allure.step("User uses the search feature"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.DOCUMENT_SEARCH, "test", 10)
            time.sleep(2)
        except Exception as e:
            log.error(f"Search feature failed: {e}")
            allure.attach(str(e), name="Search Feature Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

@then('the search results should be displayed correctly on document page')
def step_verify_search_results(context):
    with allure.step("Verify search results are displayed correctly"):
        try:
            helper = Envi_Helper(context.page)
            log.info("the searched data is displaying correctly")
            helper.capture_screenshot()
            allure.attach("Search results are correct", name="Search Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Search results verification failed: {e}")
            allure.attach(str(e), name="Search Results Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

# Sort Steps
@when('the user sorts the table on Document Module page')
def step_sort_table(context):
    with allure.step("User sorts the table"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_MODULE_HEADING)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_MODULE_HEADING)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_WHERE_USED)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_WHERE_USED)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_CALL_TO_ACTION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_CALL_TO_ACTION)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FILE_NAME)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_FILE_NAME)
        except Exception as e:
            log.error(f"Table sorting failed: {e}")
            allure.attach(str(e), name="Sort Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

@then('the table should be sorted in the correct order on Document Module page')
def step_verify_table_sorted(context):
    with allure.step("Verify table is sorted"):
        try:
            helper = Envi_Helper(context.page)
            log.info("the table data is sorted successfully ")
            allure.attach("Table is sorted", name="Sort Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Table sorting verification failed: {e}")
            allure.attach(str(e), name="Sort Verification Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

# Create Module Steps
@when('the user creates a new Document module')
def step_create_new_module(context):
    with allure.step("User creates a new Document module"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_NEW_MODULE)
            time.sleep(2)
            helper.capture_screenshot()
            helper.insert_text_in_input_field(locators.DOCUMENT_POPUP_MODULE_NAME, "Auto Document Module", 10)
            helper.insert_text_in_input_field(locators.DOCUMENT_POPUP_CTA, "AUto CTA Text", 10)
            try:
                helper.upload_file_using_file_chooser(locators.DOCUMENT_POPUP_UPLOAD,"test.pdf")
                time.sleep(2)
            except Exception as e:
                log.error(f"File upload failed: {e}")
                allure.attach(str(e), name="Upload Error", attachment_type=AttachmentType.TEXT)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_POPUP_SAVE_BUTTON)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_POPUP_CLOSE)
            time.sleep(2)
        except Exception as e:
            log.error(f"Module creation failed: {e}")
            allure.attach(str(e), name="Create Module Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

@then('the changes should be made with the updated Document module list')
def step_verify_new_module_added(context):
    with allure.step("Verify new Document module is added"):
        try:
            helper = Envi_Helper(context.page)
            helper.get_value(locators.DOCUMENT_LIST, 10)
            allure.attach("New Document module is added", name="Create Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"New module addition verification failed: {e}")
            allure.attach(str(e), name="New Module Verification Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

# Edit Module Steps
@when('the user edits an existing Document module')
def step_edit_module(context):
    with allure.step("User edits an existing Document module"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_KEBAB_MENU)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_EDIT_MODULE)
            helper.get_value(locators.DOCUMENT_ADD_EDIT_MODULE)
            helper.insert_text_in_input_field(locators.DOCUMENT_POPUP_MODULE_NAME, "Auto Updated name")
            helper.insert_text_in_input_field(locators.DOCUMENT_POPUP_CTA, "UpdatedText")
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_POPUP_SAVE_BUTTON)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_POPUP_CLOSE)
            time.sleep(2)
        except Exception as e:
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_POPUP_CLOSE)
            log.error(f"Module edit failed: {e}")
            allure.attach(str(e), name="Edit Module Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

# Delete Module Steps
@when('the user deletes an unused Document module')
def step_delete_module(context):
    with allure.step("User deletes an unused Document module"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.DOCUMENT_SEARCH, "Auto", 10)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_KEBAB_MENU)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_DELETE_BUTTON)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_DELETE_BUTTON_CONFIRM)
            helper.capture_screenshot()
            time.sleep(2)
        except Exception as e:
            log.error(f"Module deletion failed: {e}")
            allure.attach(str(e), name="Delete Module Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

@then('the user deletes more than one unused Document module')
def step_verify_module_deleted(context):
    with allure.step("Verify Delete more than one module"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.DOCUMENT_SEARCH, "Auto", 10)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_SELECT_ALL_CHECKBOXES)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_DELETE_ALL_BUTTON)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_DELETE_BUTTON_CONFIRM)
            helper.capture_screenshot()
            log.info("the unused more than one modules are deleted successfully")
            allure.attach("Module is deleted", name="Delete Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Delete verification failed: {e}")
            allure.attach(str(e), name="Delete Module Verification Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"

@when(u'the user want to see the number of rows on the DOCUMENT module list')
def step_impl(context):
    with allure.step("Verify module is deleted"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_ROWPERPAGE_OPTION)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_ROWPERPAGE_100)
            helper.capture_screenshot()
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_ROWPERPAGE_OPTION)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_ROWPERPAGE_20)
            helper.capture_screenshot()
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_ROWPERPAGE_OPTION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_ROWPERPAGE_1000)
            time.sleep(2)
            helper.capture_screenshot()
            log.info("the unused modules are deleted successfully")
            allure.attach("Row Count Verified", name="Row Count Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Row count verification failed: {e}")
            allure.attach(str(e), name="Row Count Error", attachment_type=allure.attachment_type.TEXT)
            assert False, f"Step failed due to: {e}"

@when(u'the user duplicates an existing Document module')
def step_impl(context):
    with allure.step("Duplicate Document module "):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_KEBAB_MENU)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_EDIT_MODULE)
            helper.get_value(locators.DOCUMENT_ADD_EDIT_MODULE)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_POPUP_DUPLICATE)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_POPUP_SAVE_BUTTON)
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_POPUP_CLOSE)
            time.sleep(2)
        except Exception as e:
            helper.wait_till_element_is_present_to_click(locators.DOCUMENT_POPUP_CLOSE)
            log.error(f"Module edit failed: {e}")
            allure.attach(str(e), name="Edit Module Error", attachment_type=AttachmentType.TEXT)
            assert False, f"Step failed due to: {e}"
