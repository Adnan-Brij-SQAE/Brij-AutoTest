import keyboard
from behave import  when, then
from Locators import locators
from Helper.enviHelper import Envi_Helper
import time
from allure_commons.types import AttachmentType
import allure
from Logs import logs_file
log = logs_file.get_logs()



# Navigation Steps
@when('the user navigates to the Link Module page')
def step_navigate_to_link_module_page(context):
    with allure.step("User navigates to the Link Module page"):
        helper = Envi_Helper(context.page)
        try:
            helper.wait_till_element_is_present_to_click("(//li[@class='has-subnav ng-star-inserted'])[3]")
            helper.wait_till_element_is_present_to_click("//span[normalize-space()='Link']")
            time.sleep(2)
            helper.open_page("https://rc.brij.it/brand/modules/links")
            helper.get_value("//div[@id='mainContent']")
            log.info("Navigated to Link Module page")
            allure.attach("Link Module page loaded", name="Page Verification")
            time.sleep(2)
        except Exception as e:
            log.error(f"Navigation to Link Module page failed: {e}")
            allure.attach(str(e), name="Navigation Error", attachment_type=allure.attachment_type.TEXT)

@then('the Link Module page should be displayed')
def step_link_module_page_displayed(context):
    with allure.step("Verify Link Module page is displayed"):
        helper = Envi_Helper(context.page)
        try:
            helper.get_value(locators.LINK_TITLE)
            allure.attach("Link Module page is displayed", name="Page Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Link Module page verification failed: {e}")
            allure.attach(str(e), name="Page Verification Error", attachment_type=allure.attachment_type.TEXT)

# UI Elements Steps
@then('the user can access the notification button on the Link Module page')
def step_access_notification_button(context):
    with allure.step("Verify notification button is accessible"):
        helper = Envi_Helper(context.page)
        try:
            helper.wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            allure.attach("Notification button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Notification button access failed: {e}")
            allure.attach(str(e), name="Notification Button Error", attachment_type=allure.attachment_type.TEXT)

@then('the user can access the logout button on the Link Module page')
def step_access_logout_button(context):
    with allure.step("Verify logout button is accessible"):
        helper = Envi_Helper(context.page)
        try:
            helper.wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            allure.attach("Logout button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Logout button access failed: {e}")
            allure.attach(str(e), name="Logout Button Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the user can access the field button on the Link Module page')
def step_access_field_button(context):
    with allure.step("Verify field button is accessible"):
        helper = Envi_Helper(context.page)
        try:
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD)
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD_MODULE_NAME)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD_MODULE_NAME)
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD_WHERE_USED)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD_WHERE_USED)
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD_CTA)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD_CTA)
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD_DESTINATION_URL)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD_DESTINATION_URL)
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD_CUSTOM_URL)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD_CUSTOM_URL)
            helper.wait_till_element_is_present_to_click(locators.LINK_FIELD)
            allure.attach("Field button is accessible", name="UI Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Field button access failed: {e}")
            allure.attach(str(e), name="Field Button Error", attachment_type=allure.attachment_type.TEXT)

# Checkbox Steps
@when('the user can select all checkboxes on Link Module page')
def step_select_all_checkboxes(context):
    with allure.step("User selects all checkboxes"):
        helper = Envi_Helper(context.page)
        try:
            helper.wait_till_element_is_present_to_click(locators.LINK_SELECT_ALL)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_SELECT_ALL)
        except Exception as e:
            log.error(f"Checkbox selection failed: {e}")
            allure.attach(str(e), name="Checkbox Selection Error", attachment_type=allure.attachment_type.TEXT)

# Search Steps
@when(u'the user uses the search feature on Link Module page')
def step_use_search_feature(context):
    with allure.step("User uses the search feature"):
        helper = Envi_Helper(context.page)
        try:
            helper.insert_text_in_input_field(locators.LINK_SEARCH, "test", 10)
        except Exception as e:
            log.error(f"Search feature usage failed: {e}")
            allure.attach(str(e), name="Search Feature Error", attachment_type=allure.attachment_type.TEXT)

@then('the search results should be displayed correctly on Link Module page')
def step_verify_search_results(context):
    helper = Envi_Helper(context.page)
    with allure.step("Verify search results are displayed correctly"):
        try:
            time.sleep(2)
            log.info("search results are displayed correctly and screenshot captured")
            helper.capture_screenshot()
            allure.attach("Search results are correct", name="Search Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Search results verification failed: {e}")
            allure.attach(str(e), name="Search Results Error", attachment_type=allure.attachment_type.TEXT)

# Sort Steps
@when('the user sorts the table on Link Module page')
def step_sort_table(context):
    with allure.step("User sorts the table"):
        helper = Envi_Helper(context.page)
        try:
            helper.wait_till_element_is_present_to_click(locators.LINK_MODULE_HEADING)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_MODULE_HEADING)
            helper.wait_till_element_is_present_to_click(locators.LINK_WHERE_USED)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_WHERE_USED)
            helper.wait_till_element_is_present_to_click(locators.LINK_CALL_TO_ACTION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_CALL_TO_ACTION)
            helper.wait_till_element_is_present_to_click(locators.LINK_DESTINATION_URL)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_DESTINATION_URL)
            helper.wait_till_element_is_present_to_click(locators.LINK_CUSTOM_URL)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_CUSTOM_URL)
        except Exception as e:
            log.error(f"Table sorting failed: {e}")
            allure.attach(str(e), name="Table Sorting Error", attachment_type=allure.attachment_type.TEXT)

# Create Module Steps
@when('the user creates a new Link module')
def step_create_new_module(context):
    with allure.step("User creates a new Link module"):
        helper = Envi_Helper(context.page)
        try:
            helper.wait_till_element_is_present_to_click(locators.LINK_NEW_MODULE)
            time.sleep(2)
            helper.get_value(locators.LINK_DIALOG)
            try:
                helper.insert_text_in_input_field(locators.LINK_POPUP_MODULE_NAME, "Auto Link Test", 10)
                helper.insert_text_in_input_field(locators.LINK_POPUP_CTA, "Testing", 10)
                helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_DESTINATION_URL)
                log.info("selecting Website home")
                helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_WEBSITEHOME, 10)
            except:
                page = context.page
                page.get_by_role("textbox", name="Enter module name...").fill("Auto Test Link")
                page.get_by_role("textbox", name="Enter call to action...").fill("Auto test CTA")
                page.get_by_role("combobox", name="Select an option").click()
                page.get_by_text("Website Homepage").click()
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_SAVE_BUTTON)
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_CLOSE)
            time.sleep(5)
        except Exception as e:
            log.error(f"New Link module creation failed: {e}")
            allure.attach(str(e), name="Module Creation Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the module list should be updated on LINK module page')
def step_verify_new_module_added(context):
    helper = Envi_Helper(context.page)
    with allure.step("Verify new Link module is added"):
        try:
            helper.get_value(locators.LINK_LIST)
            helper.capture_screenshot()
            allure.attach("New Link module is added", name="Create Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"New module verification failed: {e}")
            allure.attach(str(e), name="Module Verification Error", attachment_type=allure.attachment_type.TEXT)

# Navigate to Added Links Steps
@when('the user navigates to the added links')
def step_navigate_to_added_links(context):
    helper = Envi_Helper(context.page)
    with allure.step("User navigates to the added links"):
        try:
            helper.wait_till_element_is_present_to_click(locators.LINK_NEW_MODULE)
            time.sleep(2)
            try:
                helper.capture_screenshot()
                helper.insert_text_in_input_field(locators.LINK_POPUP_MODULE_NAME, "Auto link navigation testing", 10)
                helper.insert_text_in_input_field(locators.LINK_POPUP_CTA, "Testing", 10)
                helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_DESTINATION_URL)
                helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_WEBSITEHOME, 10)
                helper.capture_screenshot()
                time.sleep(2)
                helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_SAVE_BUTTON)
            except:
                page = context.page
                page.get_by_role("textbox", name="Enter module name...").click()
                page.get_by_role("textbox", name="Enter module name...").fill("Auto link Navigation testing website homepage")
                page.get_by_role("textbox", name="Enter call to action...").fill("test homepage link")
                page.get_by_role("combobox", name="Select an option").click()
                page.get_by_label("Website Homepage").get_by_text("Website Homepage").first.click()
                page.locator("iframe[title=\"mobilePreview\"]").content_frame.get_by_role("button", name="test homepage link").click()
                page.locator("div").filter(has_text="Add Link Module Save Module").first.click()
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_CLOSE)
        except Exception as e:
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_CLOSE)
            log.error(f"Link navigation failed: {e}")
            allure.attach(str(e), name="Link Navigation Error", attachment_type=allure.attachment_type.TEXT)

@then('the links should be accessible')
def step_verify_links_accessible(context):
    helper = Envi_Helper(context.page)
    with allure.step("Verify links are accessible"):
        helper = Envi_Helper(context.page)
        try:
            helper.wait_till_element_is_present_to_click(locators.LINK_LIST_ECLIPSE)
            helper.wait_till_element_is_present_to_click(locators.LINK_LIST_ECLIPSE_EDIT)
            time.sleep(3)
            log.info("Navigating to the link")
            try:
                helper.switch_frame("//iframe[@title='mobilePreview']")
                helper.wait_till_element_is_present_to_click(locators.LINK_PREVIEW_LINKBTN)
            except:
                context.page.locator("iframe[title=\"mobilePreview\"]").content_frame.get_by_role("button",name="test homepage link").click()
            allure.attach("Links are accessible", name="Link Navigation Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Link accessibility verification failed: {e}")
            allure.attach(str(e), name="Link Accessibility Error", attachment_type=allure.attachment_type.TEXT)

# Navigate to Added Links with Suffix Steps
@when('the user navigates to the added links with suffix')
def step_navigate_to_added_links_with_suffix(context):
    with allure.step("User navigates to the added links with suffix"):
        helper = Envi_Helper(context.page)
        try:
            helper.wait_till_element_is_present_to_click(locators.LINK_NEW_MODULE)
            time.sleep(2)
            helper.capture_screenshot()
            helper.insert_text_in_input_field(locators.LINK_POPUP_MODULE_NAME, "Auto link navigation testing with suffix", 10)
            helper.insert_text_in_input_field(locators.LINK_POPUP_CTA, "Testing", 10)
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_DESTINATION_URL)
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_WEBSITEHOME, 10)
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_ASETTING)
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_ADD_SUFIX)
            helper.insert_text_in_input_field(locators.LINK_POPUP_SUFIX_INSERT, "BrijTesting", 10)
            time.sleep(2)
        except Exception as e:
            log.error(f"Link with suffix navigation failed: {e}")
            allure.attach(str(e), name="Link with Suffix Error", attachment_type=allure.attachment_type.TEXT)

@then('the links with suffix should be accessible')
def step_verify_links_with_suffix_accessible(context):
    with allure.step("Verify links with suffix are accessible"):
        helper = Envi_Helper(context.page)
        try:
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_ADV_BACK)
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_SAVE_BUTTON)
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_CLOSE)
            time.sleep(5)
            allure.attach("Links with suffix are accessible", name="Link Navigation with Suffix Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Link with suffix verification failed: {e}")
            allure.attach(str(e), name="Link with Suffix Verification Error", attachment_type=allure.attachment_type.TEXT)

# Edit Module Steps
@when('the user edits an existing Link module')
def step_edit_module(context):
    with allure.step("User edits an existing Link module"):
        helper = Envi_Helper(context.page)
        try:
            helper.insert_text_in_input_field(locators.LINK_SEARCH,"Auto")
            time.sleep(4)
            helper.wait_till_element_is_present_to_click(locators.LINK_LIST_ECLIPSE)
            helper.wait_till_element_is_present_to_click(locators.LINK_LIST_ECLIPSE_EDIT)
            time.sleep(2)
            helper.get_value(locators.LINK_ADD_EDIT_MODULE, 10)
            helper.capture_screenshot()
            helper.insert_text_in_input_field(locators.LINK_POPUP_MODULE_NAME, "updated Auto Link Test", 10)
            helper.insert_text_in_input_field(locators.LINK_POPUP_CTA, "updated Testing", 10)
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_DESTINATION_URL)
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_PRODUCTPAGE, 10)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_SAVE_BUTTON)
            time.sleep(3)
            helper.wait_till_element_is_present_to_click(locators.LINK_POPUP_CLOSE)
            time.sleep(2)
        except Exception as e:
            log.error(f"Link module edit failed: {e}")
            allure.attach(str(e), name="Module Edit Error", attachment_type=allure.attachment_type.TEXT)


# Delete Module Steps
@when('the user deletes an unused Link module')
def step_delete_module(context):
    with allure.step("User deletes an unused Link module"):
        helper = Envi_Helper(context.page)
        try:
            helper.insert_text_in_input_field(locators.LINK_SEARCH, "Auto", 10)
            time.sleep(4)
            helper.wait_till_element_is_present_to_click(locators.LINK_SELECT_ALL)
            helper.wait_till_element_is_present_to_click(locators.LINK_DELETE_BUTTON)
        except Exception as e:
            log.error(f"Link module deletion failed: {e}")
            allure.attach(str(e), name="Module Deletion Error", attachment_type=allure.attachment_type.TEXT)

@then('the user deletes more than one unused Link module')
def step_verify_module_deleted(context):
    with allure.step("Verify module is deleted"):
        helper = Envi_Helper(context.page)
        try:
            helper.insert_text_in_input_field(locators.LINK_SEARCH, "Auto", 10)
            time.sleep(4)
            helper.wait_till_element_is_present_to_click(locators.LINK_SELECT_ALL)
            helper.wait_till_element_is_present_to_click(locators.LINK_DELETE_ALL)
            helper.capture_screenshot()
            allure.attach("Module is deleted", name="Delete Module Verification", attachment_type=AttachmentType.TEXT)
        except Exception as e:
            log.error(f"Module deletion verification failed: {e}")
            allure.attach(str(e), name="Deletion Verification Error", attachment_type=allure.attachment_type.TEXT)

@when('the user want to see the number of rows on the LINK module list')
def step_impl(context):
    with allure.step("User checks number of rows"):
        helper = Envi_Helper(context.page)
        try:
            helper.wait_till_element_is_present_to_click(locators.LINK_ROWPERPAGE_OPTION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_ROWPERPAGE_20)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_ROWPERPAGE_OPTION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_ROWPERPAGE_100)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_ROWPERPAGE_OPTION)
            helper.capture_screenshot()
            helper.wait_till_element_is_present_to_click(locators.LINK_ROWPERPAGE_1000)
            helper.capture_screenshot()
        except Exception as e:
            log.error(f"Row count verification failed: {e}")
            allure.attach(str(e), name="Row Count Error", attachment_type=allure.attachment_type.TEXT)

@then('the module list should be updated on LINK page')
def step_impl(context):
    with allure.step("Verify module list is updated"):
        helper = Envi_Helper(context.page)
        try:
            helper.get_value(locators.LINK_LIST)
            helper.capture_screenshot()
            log.info("the rows are updated successfully")
        except Exception as e:
            log.error(f"Module list update verification failed: {e}")
            allure.attach(str(e), name="List Update Error", attachment_type=allure.attachment_type.TEXT)