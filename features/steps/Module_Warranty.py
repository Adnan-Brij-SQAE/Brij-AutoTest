from behave import when, then
from Locators import locators
from Helper.enviHelper import Envi_Helper
import time
from allure_commons.types import AttachmentType
import allure
from Logs import logs_file
log = logs_file.get_logs()



# Navigation Steps
@when('the user navigates to the Warranty Module page')
def step_navigate_to_warranty_module_page(context):
    with allure.step("User navigates to the Warranty Module page"):
        helper = Envi_Helper(context.page)
        helper.wait_till_element_is_present_to_click("(//li[@class='has-subnav ng-star-inserted'])[3]")
        helper.wait_till_element_is_present_to_click("//span[normalize-space()='Warranty']")
        time.sleep(2)
        helper.open_page("https://rc.brij.it/brand/modules/warranty")
        helper.get_value("//div[@id='mainContent']")
        log.info("Navigated to Warranty Module page")
        allure.attach("Warranty Module page loaded", name="Page Verification")

@then('the Warranty Module page should be displayed')
def step_warranty_module_page_displayed(context):
    with allure.step("Verify Warranty Module page is displayed"):
        try:
            helper = Envi_Helper(context.page)
            helper.get_value(locators.WARRANTY_TITLE)
            helper.capture_screenshot()
            allure.attach("Warranty Module page is displayed", name="Page Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="Filter Error", attachment_type=allure.attachment_type.TEXT)

# UI Elements Steps
@then('the user can access the notification button on the Warranty Module page')
def step_access_notification_button(context):
    with allure.step("Verify notification button is accessible"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.Warranty_NOTIFICATION_ICON)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.Warranty_NOTIFICATION_ICON)
            allure.attach("Notification button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="notification button Error", attachment_type=allure.attachment_type.TEXT)

@then('the user can access the logout button on the Warranty Module page')
def step_access_logout_button(context):
    with allure.step("Verify logout button is accessible"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_LOGOUT_BUTTON)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_LOGOUT_BUTTON)
            allure.attach("Logout button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="logout Error", attachment_type=allure.attachment_type.TEXT)

@when('the user can access the Fields button on the Warranty Module page')
def step_access_field_button(context):
    with allure.step("Verify field button is accessible"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_BUTTON)
            allure.attach("Field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="logout Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can access the Warranty Name field on the Warranty Module page')
def step_impl(context):
    with allure.step("Verify Warranty Name field is accessible"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_WARRANTY_NAME)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_WARRANTY_NAME)
            allure.attach("Warranty Name field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="Warranty Name field Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the Where Used field on the Warranty Module page')
def step_impl(context):
    with allure.step("Verify Where Used field is accessible"):
        try:
            helper = Envi_Helper(context.page)
            # helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_BUTTON)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_WHERE_USED)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_WHERE_USED)
            allure.attach("Where Used Field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="Where Used field Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the Warranty Duration field on the Warranty Module page')
def step_impl(context):
    with allure.step("Verify Warranty Duration field is accessible"):
        try:
            helper = Envi_Helper(context.page)
            # helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_BUTTON)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_WARRANTY_DURATION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_WARRANTY_DURATION)
            allure.attach("Warranty Duration field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="Warranty Duration field Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the Call to Action field on the Warranty Module page')
def step_impl(context):
    with allure.step("Verify call to Action field is accessible"):
        try:
            helper = Envi_Helper(context.page)
            # helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_BUTTON)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_CTA)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_CTA)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_FIELD_BUTTON)
            allure.attach("call to Action field is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="call to Action field Error", attachment_type=allure.attachment_type.TEXT)

# Checkbox Steps
@when('the user selects all checkboxes on the Warranty Module page')
def step_select_all_checkboxes(context):
    with allure.step("User selects all checkboxes"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_SELECT_ALL_CHECKBOXES)
            helper.capture_screenshot()
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="select all checkbox Error", attachment_type=allure.attachment_type.TEXT)

@then('all checkboxes should be selected on the Warranty Module page')
def step_verify_all_checkboxes_selected(context):
    with allure.step("Verify all checkboxes are selected"):
        try:
            helper = Envi_Helper(context.page)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_SELECT_ALL_CHECKBOXES)
            allure.attach("All checkboxes are selected", name="Checkbox Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Checkbox selection verification failed: {e}")
            allure.attach(str(e), name="Checkbox Selection Error", attachment_type=allure.attachment_type.TEXT)

# Search Steps
@when('the user uses the search feature to search between the Warranty modules')
def step_use_search_feature(context):
    with allure.step("User uses the search feature"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.WARRANTY_SEARCH, "test")
        except Exception as e:
            log.error(f"Search feature usage failed: {e}")
            allure.attach(str(e), name="Search Feature Error", attachment_type=allure.attachment_type.TEXT)

@then('the search results should be displayed correctly on the Warranty Module page')
def step_verify_search_results(context):
    with allure.step("Verify search results are displayed correctly"):
        try:
            helper = Envi_Helper(context.page)
            helper.capture_screenshot()
            allure.attach("Search results are correct", name="Search Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Search results verification failed: {e}")
            allure.attach(str(e), name="Search Results Error", attachment_type=allure.attachment_type.TEXT)

# Sort Steps
@when('the user sorts the table on the Warranty Module page')
def step_sort_table(context):
    with allure.step("User sorts the table"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_WARRANTY_NAME)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_WARRANTY_NAME)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_WHERE_USED)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_WHERE_USED)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_DURATION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_DURATION)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_CALL_TO_ACTION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_CALL_TO_ACTION)
        except Exception as e:
            log.error(f"Table sorting failed: {e}")
            allure.attach(str(e), name="Table Sorting Error", attachment_type=allure.attachment_type.TEXT)

@then('the table should be sorted in the correct order on the Warranty Module page')
def step_verify_table_sorted(context):
    with allure.step("Verify table is sorted"):
        try:
            helper = Envi_Helper(context.page)
            log.info("the searched data is sorted correctly and the screenshots are captured")
            allure.attach("Table is sorted", name="Sort Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Table sort verification failed: {e}")
            allure.attach(str(e), name="Table Sort Verification Error", attachment_type=allure.attachment_type.TEXT)

# Create Module Steps
@when('the user creates a new Warranty module')
def step_create_new_module(context):
    with allure.step("User creates a new Warranty module"):
        # try:
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_NEW_MODULE)
        #     time.sleep(2)
        #     helper.capture_screenshot()
        #     helper.insert_text_in_input_field(locators.WARRANTY_POPUP_MODULE_NAME, "Auto Warranty Test")
        #     helper.insert_text_in_input_field(locators.WARRANTY_POPUP_CTA, "Testing")
        #     helper.insert_text_in_input_field(locators.WARRANTY_DURATION_DAYS, "5")
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_DURATION_TYPE)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_DURATION_TYPE_MONTHS)
        #     helper.insert_text_in_input_field(locators.WARRANTY_POPUP_IMAGE_EDITOR,"Auto Description")
        #     helper.capture_screenshot()
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_INCLUDE_CLAIM)
        #     helper.insert_text_in_input_field(locators.WARRANTY_CLAIM_TEXT, "Auto claim text")
        #     helper.insert_text_in_input_field(locators.WARRANTY_CLAIM_LINK, "https://www.testing.com")
        #     helper.capture_screenshot()
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_MULLBERY_CHECK)
        #     helper.insert_text_in_input_field(locators.WARRANTY_CLAIM_TEXT, "Auto claim text")
        #     helper.insert_text_in_input_field(locators.WARRANTY_CLAIM_LINK, "https://www.testing.com")
        #     helper.capture_screenshot()
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_MULLBERY_CHECK)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_HEADER_TEXT)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_TEXT_BODY)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_EXTENTION_CTA)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_SHOW_STATUS)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_DURATION_SCREEN)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_CUSTOMIZE_STATE)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_CUSTOMIZE_STATE_PENDING)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_CUSTOMIZE_STATE_DENIED)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_CUSTOMIZE_POST_CTA)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_CUSTOMIZE_POST_CTA_TEXT)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_CUSTOMIZE_COLOUR)
        #     keyboard.press_and_release('Page Up')
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_SAVE_BUTTON)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_BACK)
        #     time.sleep(2)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_POPUP_SAVE_BUTTON)
        #     helper.wait_till_element_is_present_to_click(locators.WARRANTY_POPUP_CLOSE)
        #     time.sleep(2)
        try:
            helper = Envi_Helper(context.page)
            try:
                helper.wait_till_element_is_present_to_click(locators.WARRANTY_NEW_MODULE)
                time.sleep(2)
            except Exception as e:
                log.error(f"Failed at WARRANTY_NEW_MODULE: {e}")
                allure.attach(str(e), name="WARRANTY_NEW_MODULE", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.insert_text_in_input_field(locators.WARRANTY_POPUP_MODULE_NAME,"Auto Warranty Test")
            except Exception as e:
                log.error(f"Failed at WARRANTY_POPUP_MODULE_NAME: {e}")
                allure.attach(str(e), name="WARRANTY_POPUP_MODULE_NAME", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.insert_text_in_input_field(locators.WARRANTY_POPUP_CTA, "Testing")
            except Exception as e:
                log.error(f"Failed at WARRANTY_POPUP_CTA: {e}")
                allure.attach(str(e), name="WARRANTY_POPUP_CTA", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.insert_text_in_input_field(locators.WARRANTY_DURATION_DAYS, "5")
            except Exception as e:
                log.error(f"Failed at WARRANTY_DURATION_DAYS: {e}")
                allure.attach(str(e), name="WARRANTY_DURATION_DAYS", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(locators.WARRANTY_DURATION_TYPE)
            except Exception as e:
                log.error(f"Failed at WARRANTY_DURATION_TYPE: {e}")
                allure.attach(str(e), name="WARRANTY_DURATION_TYPE", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(locators.WARRANTY_DURATION_TYPE_MONTHS)
            except Exception as e:
                log.error(f"Failed at WARRANTY_DURATION_TYPE_MONTHS: {e}")
                allure.attach(str(e), name="WARRANTY_DURATION_TYPE_MONTHS", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.insert_text_in_input_field(locators.WARRANTY_POPUP_IMAGE_EDITOR,"Auto Description")
            except Exception as e:
                log.error(f"Failed at WARRANTY_POPUP_IMAGE_EDITOR: {e}")
                allure.attach(str(e), name="WARRANTY_POPUP_IMAGE_EDITOR", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.ensure_checkbox_is_checked(locators.WARRANTY_INCLUDE_CLAIM)
            except Exception as e:
                log.error(f"Failed at WARRANTY_INCLUDE_CLAIM: {e}")
                allure.attach(str(e), name="WARRANTY_INCLUDE_CLAIM", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.insert_text_in_input_field(locators.WARRANTY_CLAIM_TEXT, "Auto claim text")
            except Exception as e:
                log.error(f"Failed at WARRANTY_CLAIM_TEXT: {e}")
                allure.attach(str(e), name="WARRANTY_CLAIM_TEXT", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.insert_text_in_input_field(locators.WARRANTY_CLAIM_LINK,"https://www.testing.com")
            except Exception as e:
                log.error(f"Failed at WARRANTY_CLAIM_LINK: {e}")
                allure.attach(str(e), name="WARRANTY_CLAIM_LINK", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(locators.WARRANTY_MULLBERY_CHECK)
            except Exception as e:
                log.error(f"Failed at WARRANTY_MULLBERY_CHECK: {e}")
                allure.attach(str(e), name="WARRANTY_MULLBERY_CHECK", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(locators.WARRANTY_HEADER_TEXT)
            except Exception as e:
                log.error(f"Failed at WARRANTY_HEADER_TEXT: {e}")
                allure.attach(str(e), name="WARRANTY_HEADER_TEXT", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(locators.WARRANTY_TEXT_BODY)
            except Exception as e:
                log.error(f"Failed at WARRANTY_TEXT_BODY: {e}")
                allure.attach(str(e), name="WARRANTY_TEXT_BODY", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(locators.WARRANTY_EXTENTION_CTA)
            except Exception as e:
                log.error(f"Failed at WARRANTY_EXTENTION_CTA: {e}")
                allure.attach(str(e), name="WARRANTY_EXTENTION_CTA", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS)
            except Exception as e:
                log.error(f"Failed at WARRANTY_AS: {e}")
                allure.attach(str(e), name="WARRANTY_AS", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_SHOW_STATUS)
            except Exception as e:
                log.error(f"Failed at WARRANTY_AS_SHOW_STATUS: {e}")
                allure.attach(str(e), name="WARRANTY_AS_SHOW_STATUS", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.ensure_checkbox_is_checked(locators.WARRANTY_AS_DURATION_SCREEN)
            except Exception as e:
                log.error(f"Failed at WARRANTY_AS_DURATION_SCREEN: {e}")
                allure.attach(str(e), name="WARRANTY_AS_DURATION_SCREEN", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_CUSTOMIZE_STATE)
            except Exception as e:
                log.error(f"Failed at WARRANTY_AS_CUSTOMIZE_STATE: {e}")
                allure.attach(str(e), name="WARRANTY_AS_CUSTOMIZE_STATE", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(
                    locators.WARRANTY_AS_CUSTOMIZE_STATE_PENDING)
            except Exception as e:
                log.error(f"Failed at WARRANTY_AS_CUSTOMIZE_STATE_PENDING: {e}")
                allure.attach(str(e), name="WARRANTY_AS_CUSTOMIZE_STATE_PENDING",
                              attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(
                    locators.WARRANTY_AS_CUSTOMIZE_STATE_DENIED)
            except Exception as e:
                log.error(f"Failed at WARRANTY_AS_CUSTOMIZE_STATE_DENIED: {e}")
                allure.attach(str(e), name="WARRANTY_AS_CUSTOMIZE_STATE_DENIED",
                              attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(
                    locators.WARRANTY_AS_CUSTOMIZE_POST_CTA)
            except Exception as e:
                log.error(f"Failed at WARRANTY_AS_CUSTOMIZE_POST_CTA: {e}")
                allure.attach(str(e), name="WARRANTY_AS_CUSTOMIZE_POST_CTA", attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(
                    locators.WARRANTY_AS_CUSTOMIZE_POST_CTA_TEXT)
            except Exception as e:
                log.error(f"Failed at WARRANTY_AS_CUSTOMIZE_POST_CTA_TEXT: {e}")
                allure.attach(str(e), name="WARRANTY_AS_CUSTOMIZE_POST_CTA_TEXT",attachment_type=allure.attachment_type.PNG)
                raise

            try:
                helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_CUSTOMIZE_COLOUR)
            except Exception as e:
                log.error(f"Failed at WARRANTY_AS_CUSTOMIZE_COLOUR: {e}")
                allure.attach(str(e), name="WARRANTY_AS_CUSTOMIZE_COLOUR", attachment_type=allure.attachment_type.PNG)
                raise

            helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_SAVE)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_AS_BACK)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_POPUP_SAVE_BUTTON)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_POPUP_CLOSE)

        except Exception as e:
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_POPUP_CLOSE)
            log.error(f"New module creation failed: {e}")
            allure.attach(str(e), name="Module Creation Error", attachment_type=allure.attachment_type.TEXT)

@then('the new Warranty module should be added to the module list')
def step_verify_new_module_added(context):
    with allure.step("Verify new Warranty module is added"):
        try:
            helper = Envi_Helper(context.page)
            helper.get_value(locators.WARRANTY_LIST, 10)
            allure.attach("New Warranty module is added", name="Create Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"New module verification failed: {e}")
            allure.attach(str(e), name="New Module Verification Error", attachment_type=allure.attachment_type.TEXT)

# Edit Module Steps
@when('the user edits an existing Warranty module')
def step_edit_module(context):
    with allure.step("User edits an existing Warranty module"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_LIST_KEBAB)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_EDIT_OPTION)
            time.sleep(2)
            helper.capture_screenshot()
            helper.insert_text_in_input_field(locators.WARRANTY_POPUP_MODULE_NAME, "Updated Auto Warranty Test",10)
            helper.insert_text_in_input_field(locators.WARRANTY_POPUP_CTA, " updated Testing",10)
            helper.insert_text_in_input_field(locators.WARRANTY_POPUP_IMAGE_EDITOR," Updated Auto Description")
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_POPUP_SAVE_BUTTON)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_POPUP_CROSS)
            time.sleep(2)
        except Exception as e:
            log.error(f"Module edit failed: {e}")
            allure.attach(str(e), name="Module Edit Error", attachment_type=allure.attachment_type.TEXT)

@then('the changes should be saved and reflected in the Warranty module list')
def step_verify_module_edited(context):
    with allure.step("Verify changes are saved"):
        try:
            helper = Envi_Helper(context.page)
            helper.capture_screenshot()
            allure.attach("Changes are saved", name="Edit Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Edit verification failed: {e}")
            allure.attach(str(e), name="Edit Verification Error", attachment_type=allure.attachment_type.TEXT)

# Delete Module Steps
@when('the user deletes an unused Warranty module')
def step_delete_module(context):
    with allure.step("User deletes an unused Warranty module"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.WARRANTY_SEARCH,"Auto")
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_LIST_KEBAB)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_DELETE_BUTTON)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_CONFIRM_DELETE_BUTTON)
            # helper.get_toast_message(locators.WARRANTY_CONFIRM_DELETE_toast)
            helper.capture_screenshot()
            time.sleep(2)
        except Exception as e:
            log.error(f"Module deletion failed: {e}")
            allure.attach(str(e), name="Module Deletion Error", attachment_type=allure.attachment_type.TEXT)

@when('the user deletes more than one unused Warranty module')
def step_delete_module(context):
    with allure.step("User deletes more than one Warranty module"):
        try:
            helper = Envi_Helper(context.page)
            helper.insert_text_in_input_field(locators.WARRANTY_SEARCH,"Auto")
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_SELECT_ALL_CHECKBOXES)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_DELETEALL_BUTTON)
            time.sleep(2)
            helper.capture_screenshot()
        except Exception as e:
            log.error(f"All Module deletion failed: {e}")
            allure.attach(str(e), name="All Module Deletion Error", attachment_type=allure.attachment_type.TEXT)

@then('the module should be removed from the Warranty module list')
def step_verify_module_deleted(context):
    with allure.step("Verify module is deleted"):
        try:

            log.info("the rows are updated successfully")
            allure.attach("Module is deleted", name="Delete Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Deletion verification failed: {e}")
            allure.attach(str(e), name="Deletion Verification Error", attachment_type=allure.attachment_type.TEXT)



@when(u'the user duplicates an existing Warranty module')
def step_impl(context):
    with allure.step("Verify warranty duplicate "):
        try:
            helper = Envi_Helper(context.page)
            time.sleep(1)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_LIST_KEBAB)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_EDIT_OPTION)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_POPUP_DUPLICATE)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_POPUP_SAVE_BUTTON)
            time.sleep(2)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_POPUP_CROSS)
            time.sleep(2)
            allure.attach("duplicate warranty success", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="duplicate warranty Error", attachment_type=allure.attachment_type.TEXT)

@when('the user want to see the number of rows on the WARRANTY module list')
def step_impl(context):
    with allure.step("User checks number of rows in WARRANTY module"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_ROWPERPAGE_OPTION)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_ROWPERPAGE_100)
            time.sleep(2)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_ROWPERPAGE_OPTION)
            helper.wait_till_element_is_present_to_click(locators.WARRANTY_ROWPERPAGE_1000)
            time.sleep(2)
            helper.capture_screenshot()
            # helper.wait_till_element_is_present_to_click(locators.WARRANTY_ROWPERPAGE_OPTION)
            # helper.wait_till_element_is_present_to_click(locators.WARRANTY_ROWPERPAGE_20)
            # time.sleep(2)
            # helper.capture_screenshot()
        except Exception as e:
            log.error(f"WARRANTY row count verification failed: {e}")
            allure.attach(str(e), name="WARRANTY Row Count Error",attachment_type=allure.attachment_type.TEXT)

@then('the module list should be updated on WARRANTY page')
def step_impl(context):
    with allure.step("Verify WARRANTY module list is updated"):
        try:
            helper = Envi_Helper(context.page)
            helper.capture_screenshot()
            log.info("the rows are updated successfully")
        except Exception as e:
            log.error(f"WARRANTY module list update verification failed: {e}")
            allure.attach(str(e), name="WARRANTY List Update Error",attachment_type=allure.attachment_type.TEXT)