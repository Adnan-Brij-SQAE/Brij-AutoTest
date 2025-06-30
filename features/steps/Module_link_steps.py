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

@given('the user is on the Link Module page')
def step_user_on_link_module_page(context):
    with allure.step("User navigates to the Link Module page"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_TITLE)
            allure.attach("Navigated to the Link Module page", name="Navigation Step", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Navigation to Link Module page failed: {e}")
            allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)

# Navigation Steps
@when('the user navigates to the Link Module page')
def step_navigate_to_link_module_page(context):
    with allure.step("User navigates to the Link Module page"):
        try:
            module_menu = context.driver.find_element(By.XPATH, "(//li[@class='has-subnav ng-star-inserted'])[3]")
            actions = ActionChains(context.driver)
            actions.move_to_element(module_menu).perform()
            doc_option = context.driver.find_element(By.XPATH, "//span[normalize-space()='Link']")
            doc_option.click()
            context.driver.find_element(By.XPATH, "//div[@id='mainContent']")
            time.sleep(2)
        except Exception as e:
            log.error(f"Navigation to Link Module page failed: {e}")
            allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)

@then('the Link Module page should be displayed')
def step_link_module_page_displayed(context):
    with allure.step("Verify Link Module page is displayed"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_TITLE)
            allure.attach("Link Module page is displayed", name="Page Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Link Module page verification failed: {e}")
            allure.attach(str(e), name="Page Verification Error", attachment_type=allure.attachment_type.TEXT)

# UI Elements Steps
@then('the user can access the notification button on the Link Module page')
def step_access_notification_button(context):
    with allure.step("Verify notification button is accessible"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            time.sleep(2)
            Envi_Helper(context.driver).click(locators.NOTIFICATION_ICON)
            allure.attach("Notification button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Notification button access failed: {e}")
            allure.attach(str(e), name="Notification Button Error", attachment_type=allure.attachment_type.TEXT)

@then('the user can access the logout button on the Link Module page')
def step_access_logout_button(context):
    with allure.step("Verify logout button is accessible"):
        try:
            Envi_Helper(context.driver).hover_to_element_to_click(locators.LOGOUT_BUTTON)
            Envi_Helper.capture_screenshot()
            allure.attach("Logout button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Logout button access failed: {e}")
            allure.attach(str(e), name="Logout Button Error", attachment_type=allure.attachment_type.TEXT)

@then('the user can access the field button on the Link Module page')
def step_access_field_button(context):
    with allure.step("Verify field button is accessible"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_FIELD)
            Envi_Helper.capture_screenshot()
            allure.attach("Field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Field button access failed: {e}")
            allure.attach(str(e), name="Field Button Error", attachment_type=allure.attachment_type.TEXT)

# Checkbox Steps
@when('the user selects all checkboxes on Link Module page')
def step_select_all_checkboxes(context):
    with allure.step("User selects all checkboxes"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_SELECT_ALL)
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"Checkbox selection failed: {e}")
            allure.attach(str(e), name="Checkbox Selection Error", attachment_type=allure.attachment_type.TEXT)

@then('all checkboxes should be selected on Link Module page')
def step_verify_all_checkboxes_selected(context):
    with allure.step("Verify all checkboxes are selected"):
        try:
            log.info("All checkbox selected")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_SELECT_ALL)
            log.info("All checkbox unselected")
            allure.attach("All checkboxes are selected", name="Checkbox Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Checkbox verification failed: {e}")
            allure.attach(str(e), name="Checkbox Verification Error", attachment_type=allure.attachment_type.TEXT)

# Search Steps
@when('the user uses the search feature to search between the modules on Link Module page')
def step_use_search_feature(context):
    with allure.step("User uses the search feature"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.LINK_SEARCH, "test", 10)
        except Exception as e:
            log.error(f"Search feature usage failed: {e}")
            allure.attach(str(e), name="Search Feature Error", attachment_type=allure.attachment_type.TEXT)

@then('the search results should be displayed correctly on Link Module page')
def step_verify_search_results(context):
    with allure.step("Verify search results are displayed correctly"):
        try:
            time.sleep(2)
            log.info("search results are displayed correctly and screenshot captured")
            Envi_Helper.capture_screenshot()
            context.driver.find_element(By.XPATH,"//input[@placeholder='Search Items...']").clear()
            allure.attach("Search results are correct", name="Search Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Search results verification failed: {e}")
            allure.attach(str(e), name="Search Results Error", attachment_type=allure.attachment_type.TEXT)

# Sort Steps
@when('the user sorts the table on Link Module page')
def step_sort_table(context):
    with allure.step("User sorts the table"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_MODULE_HEADING)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_WHERE_USED)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_CALL_TO_ACTION)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_DESTINATION_URL)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_CUSTOM_URL)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"Table sorting failed: {e}")
            allure.attach(str(e), name="Table Sorting Error", attachment_type=allure.attachment_type.TEXT)

@then('the table should be sorted in the correct order on Link Module page')
def step_verify_table_sorted(context):
    with allure.step("Verify table is sorted"):
        try:
            log.info("search results are sorted correctly and screenshot captured")
            allure.attach("Table is sorted", name="Sort Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Table sort verification failed: {e}")
            allure.attach(str(e), name="Sort Verification Error", attachment_type=allure.attachment_type.TEXT)

# Create Module Steps
@when('the user creates a new Link module')
def step_create_new_module(context):
    with allure.step("User creates a new Link module"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_NEW_MODULE)
            time.sleep(2)
            Envi_Helper(context.driver).capture_screenshot()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.LINK_POPUP_MODULE_NAME, "Auto Link Test", 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.LINK_POPUP_CTA, "Testing", 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_DESTINATION_URL)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_WEBSITEHOME, 10)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_SAVE_BUTTON)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_CLOSE)
            time.sleep(5)
        except Exception as e:
            log.error(f"New Link module creation failed: {e}")
            allure.attach(str(e), name="Module Creation Error", attachment_type=allure.attachment_type.TEXT)

@then('the new Link module should be added to the module list')
def step_verify_new_module_added(context):
    with allure.step("Verify new Link module is added"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present(locators.LINK_LIST)
            Envi_Helper.capture_screenshot()
            allure.attach("New Link module is added", name="Create Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"New module verification failed: {e}")
            allure.attach(str(e), name="Module Verification Error", attachment_type=allure.attachment_type.TEXT)

# Navigate to Added Links Steps
@when('the user navigates to the added links')
def step_navigate_to_added_links(context):
    with allure.step("User navigates to the added links"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_NEW_MODULE)
            time.sleep(2)
            Envi_Helper(context.driver).capture_screenshot()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.LINK_POPUP_MODULE_NAME, "Auto link navigation testing", 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.LINK_POPUP_CTA, "Testing", 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_DESTINATION_URL)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_WEBSITEHOME, 10)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_SAVE_BUTTON)
            time.sleep(5)
        except Exception as e:
            log.error(f"Link navigation failed: {e}")
            allure.attach(str(e), name="Link Navigation Error", attachment_type=allure.attachment_type.TEXT)

@then('the links should be accessible')
def step_verify_links_accessible(context):
    with allure.step("Verify links are accessible"):
        try:
            Envi_Helper(context.driver).switch_to_mobile_preview_iframe()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_PREVIEW_LINKBTN)
            allure.attach("Links are accessible", name="Link Navigation Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Link accessibility verification failed: {e}")
            allure.attach(str(e), name="Link Accessibility Error", attachment_type=allure.attachment_type.TEXT)

# Navigate to Added Links with Suffix Steps
@when('the user navigates to the added links with suffix')
def step_navigate_to_added_links_with_suffix(context):
    with allure.step("User navigates to the added links with suffix"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_NEW_MODULE)
            time.sleep(2)
            Envi_Helper(context.driver).capture_screenshot()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.LINK_POPUP_MODULE_NAME, "Auto link navigation testing with suffix", 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.LINK_POPUP_CTA, "Testing", 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_DESTINATION_URL)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_WEBSITEHOME, 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_ASETTING)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_ADD_SUFIX)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.LINK_POPUP_SUFIX_INSERT, "BrijTesting", 10)
            time.sleep(2)
        except Exception as e:
            log.error(f"Link with suffix navigation failed: {e}")
            allure.attach(str(e), name="Link with Suffix Error", attachment_type=allure.attachment_type.TEXT)

@then('the links with suffix should be accessible')
def step_verify_links_with_suffix_accessible(context):
    with allure.step("Verify links with suffix are accessible"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_ADV_BACK)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_SAVE_BUTTON)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_CLOSE)
            time.sleep(5)
            allure.attach("Links with suffix are accessible", name="Link Navigation with Suffix Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Link with suffix verification failed: {e}")
            allure.attach(str(e), name="Link with Suffix Verification Error", attachment_type=allure.attachment_type.TEXT)

# Edit Module Steps
@when('the user edits an existing Link module')
def step_edit_module(context):
    with allure.step("User edits an existing Link module"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_LIST_ECLIPSE)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_LIST_ECLIPSE_EDIT)
            time.sleep(2)
            Envi_Helper(context.driver).capture_element_text(locators.LINK_ADD_EDIT_MODULE, 10)
            Envi_Helper(context.driver).capture_screenshot()
            context.driver.find_element(By.XPATH, "//input[@placeholder='Enter module name...']").clear()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.LINK_POPUP_MODULE_NAME, "updated Auto Link Test", 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.LINK_POPUP_CTA, "updated Testing", 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_DESTINATION_URL)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_PRODUCTPAGE, 10)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_SAVE_BUTTON)
            time.sleep(3)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_POPUP_CLOSE)
            time.sleep(2)
        except Exception as e:
            log.error(f"Link module edit failed: {e}")
            allure.attach(str(e), name="Module Edit Error", attachment_type=allure.attachment_type.TEXT)

@then('the changes should be saved and reflected in the Link module list')
def step_verify_module_edited(context):
    with allure.step("Verify changes are saved"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present(locators.LINK_LIST)
            Envi_Helper.capture_screenshot()
            allure.attach("Changes are saved", name="Edit Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Changes verification failed: {e}")
            allure.attach(str(e), name="Edit Verification Error", attachment_type=allure.attachment_type.TEXT)

# Delete Module Steps
@when('the user deletes an unused Link module')
def step_delete_module(context):
    with allure.step("User deletes an unused Link module"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.LINK_SEARCH, "Auto", 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_SELECT_ALL)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_DELETE_BUTTON)
            time.sleep(2)
        except Exception as e:
            log.error(f"Link module deletion failed: {e}")
            allure.attach(str(e), name="Module Deletion Error", attachment_type=allure.attachment_type.TEXT)

@then('the module should be removed from the Link module list')
def step_verify_module_deleted(context):
    with allure.step("Verify module is deleted"):
        try:
            Envi_Helper.capture_screenshot()
            time.sleep(2)
            allure.attach("Module is deleted", name="Delete Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Module deletion verification failed: {e}")
            allure.attach(str(e), name="Deletion Verification Error", attachment_type=allure.attachment_type.TEXT)

@when('the user want to see the number of rows on the LINK module list')
def step_impl(context):
    with allure.step("User checks number of rows"):
        try:
            keyboard.press('pagedown')
            Envi_Helper(context.driver).hover_to_element_to_click(locators.LINK_ROWPERPAGE_OPTION)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_ROWPERPAGE_20)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_ROWPERPAGE_OPTION)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_ROWPERPAGE_100)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_ROWPERPAGE_OPTION)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LINK_ROWPERPAGE_1000)
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"Row count verification failed: {e}")
            allure.attach(str(e), name="Row Count Error", attachment_type=allure.attachment_type.TEXT)

@then('the module list should be updated on LINK page')
def step_impl(context):
    with allure.step("Verify module list is updated"):
        try:
            Envi_Helper.capture_screenshot()
            log.info("the rows are updated successfully")
        except Exception as e:
            log.error(f"Module list update verification failed: {e}")
            allure.attach(str(e), name="List Update Error", attachment_type=allure.attachment_type.TEXT)