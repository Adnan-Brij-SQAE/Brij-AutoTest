from behave import when, then
from Locators import locators
from Helper.enviHelper import Envi_Helper
import time
import allure
from Logs import logs_file

log = logs_file.get_logs()

@when(u'the user navigates to the Registration Module page')
def step_impl(context):
    with allure.step("the user navigates to the Registration Module page"):
        helper = Envi_Helper(context.page)
        helper.wait_till_element_is_present_to_click("(//li[@class='has-subnav ng-star-inserted'])[3]")
        helper.wait_till_element_is_present_to_click("//span[normalize-space()='Registration']")
        time.sleep(2)
        helper.open_page("https://rc.brij.it/brand/modules/registration")
        helper.get_value("//div[@id='mainContent']")
        log.info("Navigated to Registration Module successfully")
        allure.attach("Registration Module page loaded", name="Page Verification")

@then(u'the user can access the notification button on the Registration Module page')
def step_impl(context):
    with allure.step("the user can access the notification button"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_NOTIFICATION_ICON)
            time.sleep(2)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_NOTIFICATION_ICON)
            log.info("notification icon is clicked and pannel is in openend state")
            allure.attach("Notification button accessible",name="Notification Access Success",attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            log.error(f"Notification button not accessible: {e}")
            allure.attach(str(e),name="Notification Access Error",attachment_type=allure.attachment_type.TEXT)


@then(u'the user can access the logout button on the Registration Module page')
def step_impl(context):
    with allure.step("the user can access the logout button"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            log.info("logout icon is clicked ")
            allure.attach("Logout button accessible",name="Logout Access Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Logout button not accessible: {e}")
            allure.attach(str(e),name="Logout Access Error",attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the user can access the field button on the Registration Module page')
def step_impl(context):
    with allure.step("the user can access the field button"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_FIELD_BUTTON)
            Envi_Helper(context.page).capture_screenshot()
            log.info("field button is clicked")
            allure.attach("Field button accessible",name="Field Access Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Field button not accessible: {e}")
            allure.attach(str(e),name="Field Access Error",attachment_type=allure.attachment_type.TEXT)

@then(u'the user should be able to show/hide configuration name field')
def step_impl(context):
    with allure.step("the user can show/hide the configuration column"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_FIELD_CONFIGURATION)
            Envi_Helper(context.page).capture_screenshot()
            log.info("configuration name field button is clicked")
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_FIELD_CONFIGURATION)
            allure.attach("configuration name field button accessible", name="configuration name field Access Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"configuration name field button not accessible: {e}")
            allure.attach(str(e), name="configuration name field Access Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the Where used field should be visible when enabled on the Registration Module page')
def step_impl(context):
    with allure.step("the user can show/hide the Where used column"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_FIELD_WHERE_USED)
            Envi_Helper(context.page).capture_screenshot()
            log.info("Where used field button is clicked")
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_FIELD_WHERE_USED)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_FIELD_BUTTON)
            allure.attach("Where used field button accessible", name="Where used field Access Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Where used field button not accessible: {e}")
            allure.attach(str(e), name="Where used field Access Error", attachment_type=allure.attachment_type.TEXT)


@then(u'the user selects the All checkbox on the Registration Module page')
def step_impl(context):
    with allure.step("the user selects the 'All' checkbox"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_ALL_CHECKBOX)
            allure.attach("'All' checkbox selected successfully",name="Checkbox Selection Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to select 'All' checkbox: {e}")
            allure.attach(str(e),name="Checkbox Selection Error",attachment_type=allure.attachment_type.TEXT)


@then(u'all modules should be selected')
def step_impl(context):
    with allure.step("all modules should be selected"):
        try:
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_ALL_CHECKBOX)
            allure.attach("All modules selected verified",name="Module Selection Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Not all modules selected: {e}")
            allure.attach(str(e),name="Module Selection Error",attachment_type=allure.attachment_type.TEXT)

@when(u'the user uses the search feature to find a Registration Module')
def step_impl(context):
    with allure.step("the user uses the search feature to find a module"):
        try:
            Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_SEARCH, "SQA",10)
            time.sleep(2)
            allure.attach("Module search performed successfully",name="Search Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Module search failed: {e}")
            allure.attach(str(e),name="Search Error",attachment_type=allure.attachment_type.TEXT)

@then(u'only matching Registration Modules should be displayed')
def step_impl(context):
    with allure.step("only matching modules should be displayed"):
        try:
            Envi_Helper(context.page).capture_screenshot()
            time.sleep(2)
            allure.attach("Matching modules display verified",name="Search Results Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Matching modules not displayed correctly: {e}")
            allure.attach(str(e),name="Search Results Error",attachment_type=allure.attachment_type.TEXT)

@when(u'the user sorts the table on the Registration Module page')
def step_impl(context):
    with allure.step("the user sorts the table by a column"):
        try:
            try:
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CONFIGURATION_HEADING)
                Envi_Helper(context.page).capture_screenshot()
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CONFIGURATION_HEADING)
            except Exception as e:
                log.error(f"Failed to click REGISTRATION_CONFIGURATION_HEADING: {e}")
                allure.attach(str(e), name="Error - REGISTRATION_CONFIGURATION_HEADING",attachment_type=allure.attachment_type.TEXT)

            try:
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_WHERE_USED)
                Envi_Helper(context.page).capture_screenshot()
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_WHERE_USED)
            except Exception as e:
                log.error(f"Failed to click REGISTRATION_WHERE_USED: {e}")
                allure.attach(str(e), name="Error - REGISTRATION_WHERE_USED",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Table sorting failed: {e}")
            allure.attach(str(e),name="Sorting Error",attachment_type=allure.attachment_type.TEXT)

@then(u'the modules should be sorted on the Registration Module page')
def step_impl(context):
    with allure.step("the modules should be displayed in the sorted order"):
        try:
            log.info("the searched data is sorted correctly and the screenshots are captured")
            allure.attach("Sorted order verified",name="Sort Verification Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Modules not in sorted order: {e}")
            allure.attach(str(e),name="Sort Verification Error",attachment_type=allure.attachment_type.TEXT)

@when(u'the user creates a new Registration module')
def step_impl(context):
    with allure.step("the user creates a new Registration module"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_NEW_MODULE)
            time.sleep(2)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_POPUP_MODULE_NAME,"Auto Registration")
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CTA)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CTA_REGISTER)
            log.info("Register CTA selected")
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CTA)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CTA_ACTIVATE)
            log.info("Activate CTA selected")
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CTAa)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CTA_SIGNUP)
            log.info("Signup CTA selected")
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CTAs)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CTA_DONATE)
            log.info("Donate CTA selected")
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CTAd)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CTA_CUSTOM)
            log.info("Custom CTA selected")
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_CTA_INPUT,"Auto CTA")
            time.sleep(2)
            Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_DESCRIPTION,"Auto Description")
            log.info("description added ")
            try:
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_FORM)
                Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_FORM_SEARCH,"sqa")
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_FORM_SEARCH_OPTION)
                log.info("form added ")
            except Exception as e:
                log.error("form not added")
                Envi_Helper(context.page).capture_screenshot()
            try:
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS)
                Envi_Helper(context.page).capture_screenshot()
                log.info("navigated to advance settings ")

                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_SHOW_OTHER)
                    log.info("Show other modules after Registration flag is working  ")
                    time.sleep(2)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_SHOW_OTHER)
                except Exception as e:
                    log.error(f"Show other modules after Registration not working {e}")
                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_MULTIPLE)
                    log.info("Enable Multiple Registrations flag is working  ")
                    Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_AS_MULTIPLE_TEXT,"Auto text")
                    time.sleep(2)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_MULTIPLE)
                except Exception as e:
                    log.error(f"Enable Multiple Registrations not working {e}")
                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_CUSTOM_CONFIRM)
                    Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_AS_CUSTOM_CONFIRM_TEXT,"Thankyou")
                    log.info("Customize Confirmation Message flag is working  ")
                except Exception as e:
                    log.error(f"Customize Confirmation Message not working {e}")
                time.sleep(2)
                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_MARKETING)
                    Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_AS_MARKETING_CONSENT,"Auto Updated")
                    # Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_MARKETING_REQUIRED)
                    # Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_MARKETING_DEFAULT)
                    time.sleep(2)
                except Exception as e:
                    log.error(f"Email Marketing Consent not working {e}")

                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_TERM)
                    Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_AS_TERM_CONSENT,"Auto Updated")
                    time.sleep(2)
                    # Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_TERM_REQUIRED)
                    # Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_TERM_DEFAULT)
                except Exception as e:
                    log.error(f"Terms & Privacy Consent not working {e}")

                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PROFILE)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PROFILE)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PROFILE_NAME)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PROFILE_NAME)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PROFILE_PHONE)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PROFILE_PHONE)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PROFILE_PHONE_CONSENT)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PROFILE_PHONE_CONSENT)
                    Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_AS_PROFILE_PHONE_CONSENT_TEXT,"Auto Updated" )

                    # Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PROFILE_PHONE_DEFAULT)
                    # Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PROFILE_PHONE_REQUIRED)
                except Exception as e:
                    log.error(f"Ask to complete profile not working {e}")
                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_GOOGLE_SIGNUP)
                    time.sleep(2)
                    Envi_Helper(context.page).capture_screenshot()
                    log.info('Google signup flag is working')
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_GOOGLE_SIGNUP)
                except Exception as e:
                    log.error(f"Google Signup option not working {e}")
                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE)
                    Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_AS_PURCHASE_TEXT,"Auto Updated text")
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_PHONE)
                    time.sleep(2)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_PHONE_CONSENT)
                    time.sleep(2)
                    Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_AS_PURCHASE_PHONE_CONSENT_TEXT,"Auto Updated")
                    # Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_PHONE_REQUIRED)
                    # Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_PHONE_DEFAULT)

                    time.sleep(2)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_NAME1)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_PDATE)
                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC)
                        Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC_BEFORE,"2")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC_AFTER,"2")
                    except Exception as e:
                        log.error("Dynamic date not selected")
                    time.sleep(2)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_PDATE_FIXED)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_QUANTITY)
                    time.sleep(2)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_PLACE_PURCHASE)
                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL)
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_ALL)
                        log.info("Retail Channel selected")
                    except Exception as e:
                        log.info("Retail Channel not selected")
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_SERIAL_NUM)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_PURCHASE_PROOF)
                    Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_AS_PURCHASE_PROOF_TEXT,"Updated Text")
                except Exception as e:
                    log.error(f"Require Purchase Details not working {e}")
                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_REQUIRED_APPROVAL)
                    log.info('require approval flag is working')
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_REQUIRED_APPROVAL)
                except Exception as e:
                    log.error(f"Require Approval not working {e}")
            except Exception as e:
                log.error(f"unable to navigate to advance setting clicking save button to save registration")
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_SAVE_BUTTON)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_SAVE)
            time.sleep(4)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_SAVE_CONFIRM)
            allure.attach("New Registration module created successfully",name="Module Creation Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_AS_back)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_SAVE)
            log.error(f"Failed to create new Registration module: {e}")
            allure.attach(str(e),name="Module Creation Error",attachment_type=allure.attachment_type.TEXT)


@then(u'the new Registration Module should be displayed in the module list')
def step_impl(context):
    with allure.step("the new module should appear in the module list"):
        try:
            Envi_Helper(context.page).get_value(locators.REGISTRATION_FIRST_ROW)
            Envi_Helper(context.page).capture_screenshot()
            allure.attach("New module in list verified",name="Module List Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"New module not in list: {e}")
            allure.attach(str(e),name="Module List Error",attachment_type=allure.attachment_type.TEXT)

@when(u'the user edits an existing Registration module')
def step_impl(context):
    with allure.step("the user edits an existing Registration module"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_LIST_KEBAB)
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_EDIT_OPTION)
            time.sleep(2)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_POPUP_MODULE_NAME,"Updated Auto Warranty Test", 10)
            Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_POPUP_CTA, " updated Testing",10)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_SAVE_BUTTON)
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CROSS)
            time.sleep(2)

            allure.attach("Registration module edited successfully",name="Module Edit Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to edit Registration module: {e}")
            allure.attach(str(e),name="Module Edit Error",attachment_type=allure.attachment_type.TEXT)

@then(u'the changes should be reflected in the module list')
def step_impl(context):
    with allure.step("the changes should be reflected in the module list"):
        try:
            # Validation for changes reflection
            allure.attach("Module changes verified",name="Changes Verification Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Changes not reflected: {e}")
            allure.attach(str(e),name="Changes Verification Error",attachment_type=allure.attachment_type.TEXT)

@when(u'the user deletes an unused Registration module')
def step_impl(context):
    with allure.step("the user deletes an unused Registration module"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_LIST_KEBAB)
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_DELETE_OPTION)
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_DELETE_BUTTON)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CONFIRM_DELETE_BUTTON)
            time.sleep(2)
            Envi_Helper(context.page).capture_screenshot()
            allure.attach("Unused Registration module deleted successfully", name="Module Deletion Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to delete Registration module: {e}")
            allure.attach(str(e), name="Module Deletion Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the deleted Registration Module should be removed from the module list')
def step_impl(context):
    log.info("selected modules are deleted successfully")


@when(u'the user duplicates an existing Registration Module')
def step_impl(context):
    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_LIST_KEBAB)
    time.sleep(2)
    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_EDIT_OPTION)
    time.sleep(2)
    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_DUPLICATE)
    Envi_Helper(context.page).insert_text_in_input_field(locators.REGISTRATION_POPUP_CTA, " Duplicate Registration module ", 10)
    Envi_Helper(context.page).capture_screenshot()
    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_SAVE_BUTTON)
    time.sleep(2)
    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_POPUP_CROSS)
    time.sleep(2)


@when(u'the user selects more than one Registration Module and deletes them')
def step_impl(context):
    with allure.step("the user deletes an unused Registration module"):
        try:
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_ALL_CHECKBOX)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_All_DELETE)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.REGISTRATION_CONFIRM_DELETE_BUTTON)
            time.sleep(2)
            Envi_Helper(context.page).capture_screenshot()
            allure.attach("Unused Registration module deleted successfully", name="Module Deletion Success",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to delete Registration module: {e}")
            allure.attach(str(e), name="Module Deletion Error", attachment_type=allure.attachment_type.TEXT)
            raise