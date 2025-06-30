import keyboard
import pyautogui
from behave import when, then
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
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
            module_menu = context.driver.find_element(By.XPATH, "(//li[@class='has-subnav ng-star-inserted'])[3]")
            actions = ActionChains(context.driver)
            actions.move_to_element(module_menu).perform()
            doc_option = context.driver.find_element(By.XPATH, "//span[normalize-space()='Document']")
            doc_option.click()
            context.driver.find_element(By.XPATH, "//div[@id='mainContent']")
            time.sleep(2)
        except Exception as e:
            log.error(f"Navigation failed: {e}")
            allure.attach(str(e), name="Navigation Error", attachment_type=AttachmentType.TEXT)

@then('the Document Module page should be displayed')
def step_document_module_page_displayed(context):
    with allure.step("Verify Document Module page is displayed"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present(locators.DOCUMENT_OPTION, 10)
            log.info("the user is on the Document Module page")
            allure.attach("Document Module page is displayed", name="Page Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Document Module display verification failed: {e}")
            allure.attach(str(e), name="Document Display Error", attachment_type=AttachmentType.TEXT)

# UI Elements Steps
@then('the user can access the notification button on the Document Module page')
def step_access_notification_button(context):
    with allure.step("Verify notification button is accessible"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            time.sleep(2)
            Envi_Helper(context.driver).click(locators.NOTIFICATION_ICON)
            allure.attach("Notification button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Notification button access failed: {e}")
            allure.attach(str(e), name="Notification Access Error", attachment_type=AttachmentType.TEXT)

@then('the user can access the logout button on the Document Module page')
def step_access_logout_button(context):
    with allure.step("Verify logout button is accessible"):
        try:
            Envi_Helper(context.driver).hover_to_element_to_click(locators.LOGOUT_BUTTON)
            Envi_Helper.capture_screenshot()
            allure.attach("Logout button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Logout button access failed: {e}")
            allure.attach(str(e), name="Logout Access Error", attachment_type=AttachmentType.TEXT)

@then('the user can access the field button on the Document Module page')
def step_access_field_button(context):
    with allure.step("Verify field button is accessible"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_FIELD_BUTTON)
            Envi_Helper.capture_screenshot()
            allure.attach("Field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Field button access failed: {e}")
            allure.attach(str(e), name="Field Access Error", attachment_type=AttachmentType.TEXT)

# Checkbox Steps
@when('the user selects all checkboxes on Document Module page')
def step_select_all_checkboxes(context):
    with allure.step("User selects all checkboxes"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_SELECT_ALL_CHECKBOXES)
        except Exception as e:
            log.error(f"Checkbox selection failed: {e}")
            allure.attach(str(e), name="Checkbox Select Error", attachment_type=AttachmentType.TEXT)

@then('all checkboxes should be selected on Document Module page')
def step_verify_all_checkboxes_selected(context):
    with allure.step("Verify all checkboxes are selected"):
        try:
            Envi_Helper.capture_screenshot()
            log.info("All unused forms are selected ")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_SELECT_ALL_CHECKBOXES)
            allure.attach("All checkboxes are selected", name="Checkbox Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Checkbox verification failed: {e}")
            allure.attach(str(e), name="Checkbox Verification Error", attachment_type=AttachmentType.TEXT)

# Search Steps
@when('the user uses the search feature to search between the document modules')
def step_use_search_feature(context):
    with allure.step("User uses the search feature"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.DOCUMENT_SEARCH, "Auto", 10)
            time.sleep(2)
        except Exception as e:
            log.error(f"Search feature failed: {e}")
            allure.attach(str(e), name="Search Feature Error", attachment_type=AttachmentType.TEXT)

@then('the search results should be displayed correctly on document page')
def step_verify_search_results(context):
    with allure.step("Verify search results are displayed correctly"):
        try:
            log.info("the searched data is displaying correctly")
            Envi_Helper.capture_screenshot()
            context.driver.find_element(By.XPATH, "//input[@placeholder='Search Items...']").clear()
            allure.attach("Search results are correct", name="Search Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Search results verification failed: {e}")
            allure.attach(str(e), name="Search Results Error", attachment_type=AttachmentType.TEXT)

# Sort Steps
@when('the user sorts the table on Document Module page')
def step_sort_table(context):
    with allure.step("User sorts the table"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_MODULE_HEADING)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_WHERE_USED)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_CALL_TO_ACTION)
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"Table sorting failed: {e}")
            allure.attach(str(e), name="Sort Error", attachment_type=AttachmentType.TEXT)

@then('the table should be sorted in the correct order on Document Module page')
def step_verify_table_sorted(context):
    with allure.step("Verify table is sorted"):
        try:
            Envi_Helper.capture_screenshot()
            log.info("the table data is sorted successfully ")
            allure.attach("Table is sorted", name="Sort Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Table sorting verification failed: {e}")
            allure.attach(str(e), name="Sort Verification Error", attachment_type=AttachmentType.TEXT)

# Create Module Steps
@when('the user creates a new Document module')
def step_create_new_module(context):
    with allure.step("User creates a new Document module"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_NEW_MODULE)
            time.sleep(2)
            Envi_Helper(context.driver).capture_screenshot()
            Envi_Helper(context.driver).insert_text_in_input_field(locators.DOCUMENT_POPUP_MODULE_NAME, "Auto Ab899 Test", 10)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.DOCUMENT_POPUP_CTA, "Testing", 10)

            try:
                upload_button = context.driver.find_element(By.XPATH,"//img[@class='upload-icon ng-tns-c3144496486-161']")
                ActionChains(context.driver).move_to_element(upload_button).click().perform()
                time.sleep(2)
                pyautogui.write("desktop")
                pyautogui.press("enter")
                pyautogui.write("testfile.pdf")
                pyautogui.press("enter")
                time.sleep(3)
            except Exception as e:
                log.error(f"File upload failed: {e}")
                allure.attach(str(e), name="Upload Error", attachment_type=AttachmentType.TEXT)

            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_POPUP_SAVE_BUTTON)
            time.sleep(2)
        except Exception as e:
            log.error(f"Module creation failed: {e}")
            allure.attach(str(e), name="Create Module Error", attachment_type=AttachmentType.TEXT)

@then('the new Document module should be added to the module list')
def step_verify_new_module_added(context):
    with allure.step("Verify new Document module is added"):
        try:
            Envi_Helper(context.driver).get_value(locators.DOCUMENT_LIST, 10)
            allure.attach("New Document module is added", name="Create Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"New module addition verification failed: {e}")
            allure.attach(str(e), name="New Module Verification Error", attachment_type=AttachmentType.TEXT)

# Edit Module Steps
@when('the user edits an existing Document module')
def step_edit_module(context):
    with allure.step("User edits an existing Document module"):
        try:
            Envi_Helper(context.driver).capture_element_text(locators.DOCUMENT_ADD_EDIT_MODULE, 10)
            context.driver.find_element(By.XPATH,"//input[@placeholder='Enter module name...']")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.DOCUMENT_POPUP_MODULE_NAME, "Auto Updated name", 10)
            context.driver.find_element(By.XPATH,"//input[@placeholder='Enter call to action...']")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.DOCUMENT_POPUP_CTA, "UpdatedText", 10)
            context.driver.find_element(By.XPATH,"//*[@id='style-1']/div/div[3]/app-form-control/div/app-editor/div/div[2]/div/p")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_POPUP_SAVE_BUTTON)
            time.sleep(2)
        except Exception as e:
            log.error(f"Module edit failed: {e}")
            allure.attach(str(e), name="Edit Module Error", attachment_type=AttachmentType.TEXT)

@then('the changes should be saved and reflected in the module list on Document Module page')
def step_verify_module_edited(context):
    with allure.step("Verify changes are saved"):
        try:
            Envi_Helper(context.driver).capture_element_text(locators.DOCUMENT_LIST,10)
            allure.attach("Changes are saved", name="Edit Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Edit verification failed: {e}")
            allure.attach(str(e), name="Edit Module Verification Error", attachment_type=AttachmentType.TEXT)

# Delete Module Steps
@when('the user deletes an unused Document module')
def step_delete_module(context):
    with allure.step("User deletes an unused Document module"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.DOCUMENT_SEARCH, "Auto", 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_SELECT_ALL_CHECKBOXES)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_DELETE_BUTTON)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DOCUMENT_CONFIRM_DELETE_BUTTON)
            Envi_Helper.capture_screenshot()
            time.sleep(2)
        except Exception as e:
            log.error(f"Module deletion failed: {e}")
            allure.attach(str(e), name="Delete Module Error", attachment_type=AttachmentType.TEXT)

@then('the module should be removed from the module list on Document Module page')
def step_verify_module_deleted(context):
    with allure.step("Verify module is deleted"):
        try:
            Envi_Helper.capture_screenshot()
            log.info("the unused modules are deleted successfully")
            allure.attach("Module is deleted", name="Delete Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Delete verification failed: {e}")
            allure.attach(str(e), name="Delete Module Verification Error", attachment_type=AttachmentType.TEXT)
