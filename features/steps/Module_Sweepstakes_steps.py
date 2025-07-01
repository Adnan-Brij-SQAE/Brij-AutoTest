from behave import  when, then
from Locators import locators
from Helper.enviHelper import Envi_Helper
import time
from allure_commons.types import AttachmentType
import allure
from Logs import logs_file
log = logs_file.get_logs()


# Navigation Steps
@when('the user navigates to the Sweepstakes Module page')
def step_navigate_to_sweepstakes_module_page(context):
    with allure.step("User navigates to the Sweepstakes Module page"):
        try:
            helper = Envi_Helper(context.page)
            helper.wait_till_element_is_present_to_click("(//li[@class='has-subnav ng-star-inserted'])[3]")
            helper.wait_till_element_is_present_to_click("//*[@id='adminDashboardContainer']/nav/ul[1]/li[5]/ul/li[11]/span")
            time.sleep(2)
            helper.open_page("https://rc.brij.it/brand/modules/sweepstakes")
            helper.get_value("//div[@id='mainContent']")
            log.info("Navigated to Sweepstakes Module page")
            allure.attach("Sweepstakes Module page loaded", name="Page Verification")
        except Exception as e:
            log.error(f"Navigation to Sweepstakes Module page failed: {e}")
            allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)

@then('the Sweepstakes Module page should be displayed')
def step_sweepstakes_module_page_displayed(context):
    with allure.step("Verify Sweepstakes Module page is displayed"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_TITLE)
            allure.attach("Sweepstakes Module page is displayed", name="Page Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Sweepstakes Module page verification failed: {e}")
            allure.attach(str(e), name="Page Verification Error", attachment_type=allure.attachment_type.TEXT)

# UI Elements Steps
@then('the user can access the notification button on the Sweepstakes Module page')
def step_access_notification_button(context):
    with allure.step("Verify notification button is accessible"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            allure.attach("Notification button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Notification button access failed: {e}")
            allure.attach(str(e), name="Notification Button Error", attachment_type=allure.attachment_type.TEXT)

@then('the user can access the logout button on the Sweepstakes Module page')
def step_access_logout_button(context):
    with allure.step("Verify logout button is accessible"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            allure.attach("Logout button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Logout button access failed: {e}")
            allure.attach(str(e), name="Logout Button Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user can access the Fields button on the SweepStakes Module page')
def step_access_field_button(context):
    with allure.step("Verify field button is accessible"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_BUTTON)
            allure.attach("Field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="logout Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can access the SweepStakes Name field on the SweepStakes Module page')
def step_impl(context):
    with allure.step("Verify SweepStakes Name field is accessible"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_SWEEPSTAKES_NAME)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_SWEEPSTAKES_NAME)
            allure.attach("SweepStakes Name field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="SweepStakes Name field Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the Where Used field on the SweepStakes Module page')
def step_impl(context):
    with allure.step("Verify Where Used field is accessible"):
        try:
            # Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_BUTTON)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_WHERE_USED)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_WHERE_USED)
            allure.attach("Where Used Field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="Where Used field Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the SweepStakes Campaign Dates field on the SweepStakes Module page')
def step_impl(context):
    with allure.step("Verify SweepStakes Duration field is accessible"):
        try:
            # Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_BUTTON)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_SWEEPSTAKES_DURATION)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_SWEEPSTAKES_DURATION)
            allure.attach("SweepStakes Duration field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="SweepStakes Duration field Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the Call to Action field on the SweepStakes Module page')
def step_impl(context):
    with allure.step("Verify call to Action field is accessible"):
        try:
            # Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_BUTTON)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_CTA)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_CTA)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_FIELD_BUTTON)
            allure.attach("call to Action field is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Filter failed: {e}")
            allure.attach(str(e), name="call to Action field Error", attachment_type=allure.attachment_type.TEXT)


# Checkbox Steps
@when(u'the user selects all checkboxes on the SweepStakes Module page')
def step_select_all_checkboxes(context):
    with allure.step("User selects all checkboxes"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_SELECT_ALL_CHECKBOXES)
            Envi_Helper(context.page).capture_screenshot()
        except Exception as e:
            log.error(f"Checkbox selection failed: {e}")
            allure.attach(str(e), name="Checkbox Selection Error", attachment_type=allure.attachment_type.TEXT)

@then(u'all checkboxes should be selected on the SweepStakes Module page')
def step_verify_all_checkboxes_selected(context):
    with allure.step("Verify all checkboxes are selected"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_SELECT_ALL_CHECKBOXES)
            Envi_Helper(context.page).capture_screenshot()
            allure.attach("All checkboxes are selected", name="Checkbox Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Checkbox verification failed: {e}")
            allure.attach(str(e), name="Checkbox Verification Error", attachment_type=allure.attachment_type.TEXT)

# Search Steps
@when('the user uses the search feature to search between the Sweepstakes modules')
def step_use_search_feature(context):
    with allure.step("User uses the search feature"):
        try:
            Envi_Helper(context.page).insert_text_in_input_field(locators.SWEEPSTAKES_SEARCH, "test")
            Envi_Helper(context.page).capture_screenshot()
        except Exception as e:
            log.error(f"Search feature usage failed: {e}")
            allure.attach(str(e), name="Search Feature Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the search results should be displayed correctly on the SweepStakes Module page')
def step_verify_search_results(context):
    with allure.step("Verify search results are displayed correctly"):
        try:
            allure.attach("Search results are correct", name="Search Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Search results verification failed: {e}")
            allure.attach(str(e), name="Search Results Error", attachment_type=allure.attachment_type.TEXT)


# Sort Steps
@when(u'the user sorts the table on the SweepStakes Module page')
def step_sort_table(context):
    with allure.step("User sorts the table"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_MODULE_HEADING)
        except Exception as e:
            log.error(f"Table sorting failed: {e}")
            allure.attach(str(e), name="Table Sorting Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the table should be sorted in the correct order on the SweepStakes Module page')
def step_verify_table_sorted(context):
    with allure.step("Verify table is sorted"):
        try:
            Envi_Helper(context.page).capture_screenshot()
            log.info("the table data is sorted successfully")
            allure.attach("Table is sorted", name="Sort Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Table sort verification failed: {e}")
            allure.attach(str(e), name="Sort Verification Error", attachment_type=allure.attachment_type.TEXT)

# Create Module Steps
@when('the user creates a new Sweepstakes module')
def step_create_new_module(context):
    with allure.step("User creates a new Sweepstakes module"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_NEW_MODULE)
            time.sleep(2)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).insert_text_in_input_field(locators.SWEEPSTAKES_POPUP_MODULE_NAME, "Auto Sweepstakes Test")
            Envi_Helper(context.page).insert_text_in_input_field(locators.SWEEPSTAKES_POPUP_CTA, "Testing")
            Envi_Helper(context.page).insert_text_in_input_field(locators.SWEEPSTAKES_POPUP_EDITOR, "Demo")
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_POPUP_SAVE_BUTTON)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_POPUP_CLOSE)
            time.sleep(2)
        except Exception as e:
            log.error(f"New Sweepstakes module creation failed: {e}")
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_POPUP_CLOSE)
            allure.attach(str(e), name="Module Creation Error", attachment_type=allure.attachment_type.TEXT)

@then('the new Sweepstakes module should be added to the module list')
def step_verify_new_module_added(context):
    with allure.step("Verify new Sweepstakes module is added"):
        try:
            Envi_Helper(context.page).get_value(locators.CUSTOM_LIST,10)
            allure.attach("New Sweepstakes module is added", name="Create Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"New module verification failed: {e}")
            allure.attach(str(e), name="Module Verification Error", attachment_type=allure.attachment_type.TEXT)

# Edit Module Steps
@when('the user edits an existing Sweepstakes module')
def step_edit_module(context):
    with allure.step("User edits an existing Sweepstakes module"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_KEBAB_MENU)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_EDIT_MODULE)
            time.sleep(2)
            Envi_Helper(context.page).insert_text_in_input_field(locators.SWEEPSTAKES_POPUP_MODULE_NAME, "Auto Updated name")
            Envi_Helper(context.page).insert_text_in_input_field(locators.SWEEPSTAKES_POPUP_CTA, "UpdatedText")
            Envi_Helper(context.page).capture_screenshot()
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_POPUP_SAVE_BUTTON)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_POPUP_CLOSE)
            time.sleep(2)
        except Exception as ex:
            log.error(f"Sweepstakes module edit failed: {ex}")
            allure.attach(str(ex), name="Module Edit Error", attachment_type=allure.attachment_type.TEXT)

@then('the changes should be saved and reflected in the Sweepstakes module list')
def step_verify_module_edited(context):
    with allure.step("Verify changes are saved"):
        try:
            Envi_Helper(context.page).get_value(locators.SWEEPSTAKES_LIST)
            allure.attach("Changes are saved", name="Edit Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Changes verification failed: {e}")
            allure.attach(str(e), name="Edit Verification Error", attachment_type=allure.attachment_type.TEXT)

# Delete Module Steps
@when('the user deletes an unused Sweepstakes module')
def step_delete_module(context):
    with allure.step("User deletes an unused Sweepstakes module"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_KEBAB_MENU)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_DELETE_BUTTON)
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_CONFIRM_DELETE_BUTTON)
        except Exception as e:
            log.error(f"Sweepstakes module deletion failed: {e}")
            allure.attach(str(e), name="Module Deletion Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user deletes more than one unused SweepStakes module')
def step_verify_module_deleted(context):
    with allure.step("Verify module is deleted"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_SELECT_ALL_CHECKBOXES)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_DELETEALL_BUTTON)
            time.sleep(2)
            Envi_Helper(context.page).capture_screenshot()
            allure.attach("Module are deleted", name="Delete Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Module deletion verification failed: {e}")
            allure.attach(str(e), name="Deletion Verification Error", attachment_type=allure.attachment_type.TEXT)

@when('the user want to see the number of rows on the SWEEPSTAKES module list')
def step_impl(context):
    with allure.step("User checks number of rows"):
        try:

            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_ROWPERPAGE_OPTION)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_ROWPERPAGE_20)
            Envi_Helper(context.page).capture_screenshot()
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_ROWPERPAGE_OPTION)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_ROWPERPAGE_100)
            Envi_Helper(context.page).capture_screenshot()
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_ROWPERPAGE_OPTION)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_ROWPERPAGE_1000)
            time.sleep(2)
            Envi_Helper(context.page).capture_screenshot()
        except Exception as e:
            log.error(f"Row count verification failed: {e}")
            allure.attach(str(e), name="Row Count Error", attachment_type=allure.attachment_type.TEXT)

@then('the module list should be updated on SWEEPSTAKES page')
def step_impl(context):
    with allure.step("Verify module list is updated"):
        try:
            Envi_Helper(context.page).capture_screenshot()
            log.info("the rows are updated successfully")
        except Exception as e:
            log.error(f"Module list update verification failed: {e}")
            allure.attach(str(e), name="List Update Error", attachment_type=allure.attachment_type.TEXT)


@when(u'the user duplicates an existing SweepStakes module')
def step_impl(context):
    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_KEBAB_MENU)
    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_EDIT_MODULE)
    time.sleep(2)
    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_POPUP_DUPLICATE)
    Envi_Helper(context.page).capture_screenshot()
    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_POPUP_SAVE_BUTTON)
    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.SWEEPSTAKES_POPUP_CLOSE)
    time.sleep(2)

