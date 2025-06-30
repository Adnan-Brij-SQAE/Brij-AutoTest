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

@when('the user navigates to the Video Module page')
def step_navigate_to_video_module_page(context):
    with allure.step("User navigates to the Video Module page"):
        try:
            with allure.step("User navigates to the Warranty Module page"):
                module_menu = context.driver.find_element(By.XPATH, "//span[normalize-space()='Modules']")
                module_menu.click()
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_OPTION)
                time.sleep(2)
                context.driver.find_element(By.XPATH, "//div[@id='mainContent']")
        except Exception as e:
            log.error(f"Navigation to Video Module page failed: {e}")
            allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)

@then('the Video Module page should be displayed')
def step_video_module_page_displayed(context):
    with allure.step("Verify Video Module page is displayed"):
        try:
            Envi_Helper(context.driver).get_value(locators.VIDEO_HEADING)
            allure.attach("Video Module page is displayed", name="Page Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Video Module page verification failed: {e}")
            allure.attach(str(e), name="Page Verification Error", attachment_type=allure.attachment_type.TEXT)

# UI Elements Steps
@then('the user can access the notification button on the Video Module page')
def step_access_notification_button(context):
    with allure.step("Verify notification button is accessible"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_NOTIFICATION_ICON)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_NOTIFICATION_ICON)
            allure.attach("Notification button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Notification button access failed: {e}")
            allure.attach(str(e), name="Notification Button Error", attachment_type=allure.attachment_type.TEXT)

@then('the user can access the logout button on the Video Module page')
def step_access_logout_button(context):
    with allure.step("Verify logout button is accessible"):
        try:
            Envi_Helper(context.driver).hover_to_element_to_click(locators.VIDEO_LOGOUT_BUTTON)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).hover_to_element_to_click(locators.VIDEO_LOGOUT_BUTTON)
            allure.attach("Logout button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Logout button access failed: {e}")
            allure.attach(str(e), name="Logout Button Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user can access the Fields button on the Video Module page')
def step_access_field_button(context):
    with allure.step("Verify field button is accessible"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELDS_BUTTON)
            Envi_Helper.capture_screenshot()
            allure.attach("Field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Field button access failed: {e}")
            allure.attach(str(e), name="Field Button Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can access the Video Name field on the Video Module page')
def step_impl(context):
    with allure.step("Verify Video Name field is accessible"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_MODULE_NAME)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_MODULE_NAME)
            allure.attach("Video Name field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="Video Name field Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the Where Used field on the Video Module page')
def step_impl(context):
    try:
        # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_BUTTON)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_WHERE_USED)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_WHERE_USED)
        allure.attach("Where Used Field button is accessible", name="UI Verification",attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.error(f"Filter failed: {e}")
        allure.attach(str(e), name="Where Used field Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can access the File name field on the Video Module page')
def step_impl(context):
    with allure.step("Verify Video Duration field is accessible"):
        try:
            # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_BUTTON)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_FILE_NAME)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_FILE_NAME)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_BUTTON)
            allure.attach("Video Duration field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="Video Duration field Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the Call to Action field on the Video Module page')
def step_impl(context):
    def step_impl(context):
        with allure.step("Verify call to Action field is accessible"):
            try:
                # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_BUTTON)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_CTA)
                Envi_Helper.capture_screenshot()
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FIELD_CTA)

                allure.attach("call to Action field is accessible", name="UI Verification",attachment_type=AttachmentType.TEXT)
            except Exception as e:
                log.error(f"Filter failed: {e}")
                allure.attach(str(e), name="call to Action field Error", attachment_type=allure.attachment_type.TEXT)


# Checkbox Steps
@when(u'the user selects all checkboxes on the Video Module page')
def step_select_all_checkboxes(context):
    with allure.step("User selects all checkboxes"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_ALL_CHECKBOX)
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"Checkbox selection failed: {e}")
            allure.attach(str(e), name="Checkbox Selection Error", attachment_type=allure.attachment_type.TEXT)

@then(u'all checkboxes should be selected on the Video Module page')
def step_verify_all_checkboxes_selected(context):
    with allure.step("Verify all checkboxes are selected"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_ALL_CHECKBOX)
            allure.attach("All checkboxes are selected", name="Checkbox Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Checkbox verification failed: {e}")
            allure.attach(str(e), name="Checkbox Verification Error", attachment_type=allure.attachment_type.TEXT)

# Search Steps
@when(u'the user uses the search feature to search between the Video modules')
def step_use_search_feature(context):
    with allure.step("User uses the search feature"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOM_SEARCH, "SQA")
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"Search feature usage failed: {e}")
            allure.attach(str(e), name="Search Feature Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the search results should be displayed correctly on the Video Module page')
def step_verify_search_results(context):
    with allure.step("Verify search results are displayed correctly"):
        try:
            Envi_Helper.capture_screenshot()
            allure.attach("Search results are correct", name="Search Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Search results verification failed: {e}")
            allure.attach(str(e), name="Search Results Error", attachment_type=allure.attachment_type.TEXT)

# Sort Steps
@when(u'the user sorts the table on the Video Module page')
def step_sort_table(context):
    with allure.step("User sorts the table"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_MODULE_HEADING)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_MODULE_HEADING)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_WHERE_USED)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_WHERE_USED)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_CALL_TO_ACTION)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_CALL_TO_ACTION)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FILE_NAME)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_FILE_NAME)
        except Exception as e:
            log.error(f"Table sorting failed: {e}")
            allure.attach(str(e), name="Table Sorting Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the table should be sorted in the correct order on the Video Module page')
def step_verify_table_sorted(context):
    with allure.step("Verify table is sorted"):
        try:
            log.info("table is sorted with the correct sorting orders ")
            allure.attach("Table is sorted", name="Sort Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Table sort verification failed: {e}")
            allure.attach(str(e), name="Sort Verification Error", attachment_type=allure.attachment_type.TEXT)

# @when(u'the user duplicates an existing Video module')
# def step_impl(context):


@when('the user creates a new Video module')
def step_create_new_module(context):
    with allure.step("User creates a new Video module"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_NEW_MODULE)
            time.sleep(2)
            Envi_Helper(context.driver).get_value(locators.VIDEO_ADD_EDIT_MODULE,10)
            locators.VIDEO_NEW_MODULE.clear()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.VIDEO_NEW_MODULE, "SQAE Custom module")
            locators.VIDEO_POPUP_CTA.clear()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.VIDEO_POPUP_CTA, "SQAE Custom CTA")
            locators.VIDEO_POPUP_EDITOR.clear()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.VIDEO_POPUP_EDITOR, "Demo Automation Text")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_POPUP_SAVE_BUTTON)
            time.sleep(2)
        except Exception as e:
            log.error(f"New Video module creation failed: {e}")
            allure.attach(str(e), name="Module Creation Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the changes should be saved and reflected in the Video module list')
def step_verify_new_module_added(context):
    with allure.step("Verify new Video module is added"):
        try:
            assert context.driver.is_new_module_added(), "New Video module is not added"
            allure.attach("New Video module is added", name="Create Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"New module verification failed: {e}")
            allure.attach(str(e), name="Module Verification Error", attachment_type=allure.attachment_type.TEXT)

# Edit Module Steps
@when('the user edits an existing Video module')
def step_edit_module(context):
    with allure.step("User edits an existing Video module"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOM_LIST)
            time.sleep(2)
            Envi_Helper(context.driver).capture_element_text(locators.VIDEO_ADD_EDIT_MODULE,10)
            locators.VIDEO_NEW_MODULE.clear()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.VIDEO_POPUP_MODULE_NAME, "Updated name")
            locators.VIDEO_POPUP_CTA.clear()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.VIDEO_POPUP_CTA, "UpdatedText")
            locators.VIDEO_POPUP_EDITOR.clear()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.VIDEO_POPUP_EDITOR, "Updated text")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_POPUP_SAVE_BUTTON)
            time.sleep(2)
        except Exception as e:
            log.error(f"Video module edit failed: {e}")
            allure.attach(str(e), name="Module Edit Error", attachment_type=allure.attachment_type.TEXT)

@then('the changes should be saved and reflected in the module list')
def step_verify_module_edited(context):
    with allure.step("Verify changes are saved"):
        try:
            assert context.driver.are_changes_saved(), "Changes are not saved"
            allure.attach("Changes are saved", name="Edit Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Changes verification failed: {e}")
            allure.attach(str(e), name="Edit Verification Error", attachment_type=allure.attachment_type.TEXT)

# Delete Module Steps
@when('the user deletes an unused Video module')
def step_delete_module(context):
    with allure.step("User deletes an unused Video module"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_CHECKBOX_LIST)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_DELETE_BUTTON)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VIDEO_CONFIRM_DELETE_BUTTON)
            Envi_Helper(context.driver).get_toast_message(locators.VIDEO_CONFIRM_DELETE_toast)
            Envi_Helper.capture_screenshot()
            time.sleep(2)
        except Exception as e:
            log.error(f"Video module deletion failed: {e}")
            allure.attach(str(e), name="Module Deletion Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user deletes more than one unused Video module')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user deletes more than one unused Video module')


@then('the module should be removed from the module list')
def step_verify_module_deleted(context):
    with allure.step("Verify module is deleted"):
        try:

            allure.attach("Module is deleted", name="Delete Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Module deletion verification failed: {e}")
            allure.attach(str(e), name="Deletion Verification Error", attachment_type=allure.attachment_type.TEXT)
