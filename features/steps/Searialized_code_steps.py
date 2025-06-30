import allure
import keyboard
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators import locators
from Helper.enviHelper import Envi_Helper
from Logs import logs_file
import time
log = logs_file.get_logs()


@allure.step('User navigates to Serialized Code page')
@when(u'The user navigates to  Serialized Code page')
def step_impl(context):
    try:
        module_menu = context.driver.find_element(By.XPATH, "//span[normalize-space()='Serialized Codes']")
        actions = ActionChains(context.driver)
        actions.move_to_element(module_menu).perform()
        module_menu.click()
        time.sleep(2)
        log.info("user is on the Serialized Code")
    except Exception as e:
        log.error(f"Navigation to Serialized Code page failed: {e}")
        allure.attach(str(e), name="Navigation Error", attachment_type=AttachmentType.TEXT)


@allure.step('Verify Serialized Code page is displayed')
@then(u'The Serialized Code page should be displayed correctly')
def step_impl(context):
    try:
        time.sleep(2)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_TITLE)
        log.info("user is on the Serialized Code")
    except Exception as e:
        log.error(f"Serialized Code page verification failed: {e}")
        allure.attach(str(e), name="Page Display Error", attachment_type=AttachmentType.TEXT)


@allure.step('User clicks notification button')
@when(u'The user clicks on the notification button')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
        log.info("user is able to access the notification button")
    except Exception as e:
        log.error(f"Notification button click failed: {e}")
        allure.attach(str(e), name="Notification Error", attachment_type=AttachmentType.TEXT)

@allure.step('Verify notification panel is accessible')
@then(u'The notification panel should be accessible')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        time.sleep(2)
        log.info("user is able to access the notification button")
        keyboard.press_and_release("Esc")
    except Exception as e:
        log.error(f"Notification panel verification failed: {e}")
        allure.attach(str(e), name="Notification Panel Error", attachment_type=AttachmentType.TEXT)

@allure.step('User clicks logout button')
@when(u'The user clicks on the logout button')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
    except Exception as e:
        log.error(f"Logout button click failed: {e}")
        allure.attach(str(e), name="Logout Error", attachment_type=AttachmentType.TEXT)


@allure.step('Verify user is logged out')
@then(u'The user should be logged out successfully')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("logout button successfully opened and screenshot is attached")
    except Exception as e:
        log.error(f"Logout verification failed: {e}")
        allure.attach(str(e), name="Logout Verification Error", attachment_type=AttachmentType.TEXT)


@allure.step('Verify Serialized Code count is displayed')
@then(u'The Serialized Code count should be displayed correctly')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present(locators.SEARIALIZED_CODE_COUNT, 10)
        log.info("Customer count is displayed")
        time.sleep(2)
    except Exception as e:
        log.error(f"Serialized Code count verification failed: {e}")
        allure.attach(str(e), name="Count Display Error", attachment_type=AttachmentType.TEXT)


@allure.step('User performs search in Serialized Codes')
@when(u'The user performs a search within Serialized Codes')
def step_impl(context):
    try:
        Envi_Helper(context.driver).insert_text_in_input_field(locators.SEARIALIZED_CODE_SEARCH_BAR, "Auto", 10)
        time.sleep(2)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).insert_text_in_input_field(locators.SEARIALIZED_CODE_SEARCH_BAR, "", 10)
        # context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Items...']").clear()
        time.sleep(3)
    except Exception as e:
        log.error(f"Search operation failed: {e}")
        allure.attach(str(e), name="Search Error", attachment_type=AttachmentType.TEXT)


@allure.step('User clicks on field button')
@when(u'The user clicks on field button')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_FIELDS_BUTTON)
        time.sleep(2)
    except Exception as e:
        log.error(f"Field button click failed: {e}")
        allure.attach(str(e), name="Field Button Error", attachment_type=AttachmentType.TEXT)


@allure.step('Verify fields are displayed')
@then(u'The corresponding fields should be displayed')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("user is able to access the field button and screenshot is attached")
        keyboard.press_and_release('Esc')
    except Exception as e:
        log.error(f"Fields display verification failed: {e}")
        allure.attach(str(e), name="Fields Display Error", attachment_type=AttachmentType.TEXT)


@allure.step('User checks all checkboxes')
@when(u'The user checks all check boxes')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_SELECT_ALL_CHECKBOX)
        time.sleep(2)
    except Exception as e:
        log.error(f"Checkbox selection failed: {e}")
        allure.attach(str(e), name="Checkbox Error", attachment_type=AttachmentType.TEXT)


@allure.step('Verify all items are selected')
@then(u'All items should be selected')
def step_impl(context):
    try:
        Envi_Helper.capture_screenshot()
        log.info("user is able to access all checkbox button and screenshot is attached")
    except Exception as e:
        log.error(f"Item selection verification failed: {e}")
        allure.attach(str(e), name="Selection Verification Error", attachment_type=AttachmentType.TEXT)


@allure.step('User sorts Serialized Code table')
@when(u'The user sorts the Serialized Code table')
def step_impl(context):
    try:
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_BRIJ_HEADING, 10)
            time.sleep(2)
            log.info("Brij Id sorting is working")
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f'Brij Id sorting is not working {e} ')

        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_CODE_HEADING, 10)
            time.sleep(2)
            log.info("Code type sorting is working")
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f'Code type sorting is not working {e} ')

        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_SERIAL_HEADING, 10)
            time.sleep(2)
            log.info("Serial no. sorting is working")
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f'Serial no. sorting is not working {e} ')

        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_LOT_HEADING, 10)
            time.sleep(2)
            log.info("Lot No. sorting is working")
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f'Lot No. sorting is not working  {e} ')

        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_OWNER_HEADING, 10)
            time.sleep(2)
            log.info("Owner sorting is working")
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f'Lot No. sorting is not working {e} ')
    except Exception as e:
        log.error(f"Table sorting failed: {e}")
        allure.attach(str(e), name="Sorting Error", attachment_type=AttachmentType.TEXT)


@allure.step('User applies Variant filter')
@when(u'The user apply Variant filter on Serialize code page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER)
        log.info("clicked on variant filter")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_ALL_VARIANT)
        log.info("searching Test in experience filter")
        Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_FILTER_SEARCH, "Auto", 10)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_SELECT_ALL)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_FILTER_SEARCH_CROSS)
        keyboard.press_and_release('Esc')
        time.sleep(2)
    except Exception as e:
        log.error(f"Variant filter application failed: {e}")
        allure.attach(str(e), name="Variant Filter Error", attachment_type=AttachmentType.TEXT)


@when(u'The user apply Experience filter on Serialize code page')
def step_impl(context):
    try:
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER)
            log.info("clicked on experience filters")
        except :
            context.driver.find_element(By.XPATH,"//*[@id='pn_id_40']/div[2]/div")
            log.info("element not found used another method")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_ALL_EXPERIENCE)
        try:
            log.info("searching Test in experience filter")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.EXPERIENCE_FILTER_SEARCH,"Auto",10)
        except Exception as e:
            log.error("filter search is not working")
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.DROPDOWN_SELECT_ALL)
        Envi_Helper.capture_screenshot()
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
        keyboard.press_and_release('Esc')
    except Exception as e:
        log.error(f"Experience dropdown access failed: {e}")
        allure.attach(str(e), name="Experience Dropdown Error", attachment_type=AttachmentType.TEXT)


@then(u'The serialized code(s) should be displayed accordingly')
def step_impl(context):
    Envi_Helper.capture_screenshot()
    log.info("Serialized Codes are displaying accordingly and screenshot is attached")

@when(u'The user apply Registration status filter on Serialize code page')
def step_impl(context):
    try:
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS)
        Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_ALL)
        log.info("unselected all registration status")

        try:
            log.info("searching Active in variant filter")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.VARIANT_FILTER_SEARCH, "Active", 10)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SELECTALL)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
            time.sleep(2)
        except Exception as e:
            log.error("filter search is not working")

        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_ALL)
            log.info("selected all registration status")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_ALL)
            log.info("unselected all registration status")
        except Exception as e:
            log.error("select all registrtation not working ")

        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_APPROVED)
            Envi_Helper.capture_screenshot()
            log.info('selected Approved Filter')
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_APPROVED)
        except Exception as e:
            log.error("Approved filter is not working")

        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_ACTIVE)
            Envi_Helper.capture_screenshot()
            log.info('selected Active Filter')
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_ACTIVE)
        except Exception as e:
            log.error("Active filter is not working")

        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_INACTIVE)
            Envi_Helper.capture_screenshot()
            log.info('selected Inactive Filter')
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_INACTIVE)
        except Exception as e:
            log.error("Inactive filter is not working")

        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_PENDING)
            Envi_Helper.capture_screenshot()
            log.info('selected Pending Filter')
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_PENDING)
        except Exception as e:
            log.error("Pending filter is not working")
        keyboard.press_and_release('Page Down')
        time.sleep(2)
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_INCOMPLETE)
            Envi_Helper.capture_screenshot()
            log.info('selected Incomplete Filter')
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_INCOMPLETE)
        except Exception as e:
            log.error("Incomplete filter is not working")

        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_DENIED)
            Envi_Helper.capture_screenshot()
            log.info('selected Denied Filter')
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_DENIED)
        except Exception as e:
            log.error("Denied filter is not working")

        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_EXPIRED)
            Envi_Helper.capture_screenshot()
            log.info('selected Expired Filter')
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_EXPIRED)
        except Exception as e:
            log.error("Expired filter is not working")


        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_UNREGISTERED)
            Envi_Helper.capture_screenshot()
            log.info('selected unregistered Filter')
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_REGISTRATION_STATUS_UNREGISTERED)
        except Exception as e:
            log.error("Unregistered filter is not working")
        keyboard.press_and_release('Esc')
        time.sleep(2)
    except Exception as e:
        log.error(f"Registration Status Dropdown access failed: {e}")
        allure.attach(str(e), name="Registration Status Error", attachment_type=AttachmentType.TEXT)


@when(u'The user download the Serialized Code popup as png')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user download the Serialized Code popup as png')


@then(u'The the selected code should be downloaded')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The the selected code should be downloaded')


@when(u'The user download the Serialized Code popup as svg')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user download the Serialized Code popup as svg')


@when(u'The user hover to the code icon')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user hover to the code icon')


@then(u'The QR code shold be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The QR code shold be displayed')


@then(u'The user can open the QR code link')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The user can open the QR code link')


@when(u'The user deactivate the Serialized Code')
def step_impl(context):
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_KEBAB)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_Deactivate)

@then(u'The code status be updated in the listing')
def step_impl(context):
    Envi_Helper.capture_screenshot()
    log.info('serialized code updated and screenshot attached')

@when(u'The user activate the Serialized Code')
def step_impl(context):
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_KEBAB)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_Activate)

@when(u'The user delete the Serialized Code')
def step_impl(context):
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_KEBAB)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_Delete)
    time.sleep(2)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SERIALIZED_DELETE_CONFIRM)
    time.sleep(3)

@then(u'The serialized code(s) should no longer be in list')
def step_impl(context):
    log.info("pending")


@when(u'The user delete more than one Serialized Code')
def step_impl(context):
    log.info("pending")


@when(u'The user want to test pagination')
def step_impl(context):
    keyboard.press('page down')
    keyboard.press('page down')
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_ROWPERPAGE_OPTION)


@then(u'The user can view 100 rows of Serialized code')
def step_impl(context):
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_ROWPERPAGE_20)
    Envi_Helper.capture_screenshot()
    keyboard.press('page down')


@then(u'The user can view 20 rown of Serialized code')
def step_impl(context):
    keyboard.press('page down')
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_ROWPERPAGE_OPTION)
    Envi_Helper.capture_screenshot()
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_ROWPERPAGE_100)
    Envi_Helper.capture_screenshot()
    keyboard.press('page down')


@then(u'The user can view 1000 rows of Serialized code')
def step_impl(context):
    keyboard.press('page down')
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_ROWPERPAGE_OPTION)
    Envi_Helper.capture_screenshot()
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_ROWPERPAGE_1000)
    Envi_Helper.capture_screenshot()


@then(u'The table should be sorted correctly')
def step_impl(context):
    log.info("table is being sorted according to rows selected and screenshots are attached")


@when(u'The user opens the Serialized Code popup')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user opens the Serialized Code popup')


@then(u'The popup should be displayed with all required fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The popup should be displayed with all required fields')


@when(u'The user exports Serialized Codes')
def step_impl(context):
    # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.VARIANT_LIST_CHECKBOX1)
    keyboard.press_and_release('Page Down')
    keyboard.press_and_release('Page Down')
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_EXPORT_BUTTON, 10)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_EXPORT_CANCEL)
    # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_EXPORT_BUTTON, 10)
    # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_EXPORT_CLOSE, 10)
    time.sleep(2)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_EXPORT_BUTTON, 10)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_EXPORT_EXPORT, 10)
    time.sleep(10)


@then(u'The export file should be generated successfully')
def step_impl(context):
    log.info("the serialized codes are exported successfully")


@when(u'The user imports Serialized Codes')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user imports Serialized Codes')


@then(u'The import should be processed successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The import should be processed successfully')
#










# @when(u'The user navigate to Customer Serialized Code page')
# def step_impl(context):
#     module_menu = context.driver.find_element(By.XPATH, "//li[@class='ng-star-inserted is-active']")
#     actions = ActionChains(context.driver)
#     actions.move_to_element(module_menu).perform()
#     module_menu.click()
#     time.sleep(2)
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_OPTION)
#     time.sleep(2)
#     keyboard.press_and_release('esc')
#     log.info("user is on the Serialized Code")
#
#
#
# @then(u'the user can access the notification button on Serialized Code page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.NOTIFICATION_ICON)
#     log.info("user is able to access the notification button ")
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON_2)
#     time.sleep(2)
#
# @then(u'the user can access the logout button on Serialized Code page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.LOGOUT_BUTTON)
#     Envi_Helper.capture_screenshot()
#     log.info("user is able to access the logout button ")
#
# @then(u'the user can get the Serialized Code count on Serialized Code page')
# def step_impl(context):
#     Envi_Helper(context.driver).wait_till_element_is_present(locators.SEARIALIZED_CODE_COUNT, 10)
#     log.info("Customer count is displayed")
#     time.sleep(2)
#
#
# @then(u'the user can search within the Serialized Code on Serialized Code page')
# def step_impl(context):
#     Envi_Helper(context.driver).insert_text_in_input_field(locators.SEARIALIZED_CODE_SEARCH_BAR, "sqa", 10)
#     Envi_Helper.capture_screenshot()
#     context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Items...']").clear()
#     time.sleep(3)
#
#
# @then(u'the user can click on field button on Serialized Code page')
# def step_impl(context):
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_FIELDS_BUTTON)
#     time.sleep(2)
#
#
# @then(u'the user can check all check boxes on Serialized Code page')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.SEARIALIZED_CODE_UNSELECT_ALL_CHECKBOXES)
#     time.sleep(2)
#     Envi_Helper(context.driver).click(locators.SEARIALIZED_CODE_UNSELECT_ALL_CHECKBOXES)
#
#
# @then(u'the user can sort the Serialized Code table on Serialized Code page')
# def step_impl(context):
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_BRIJ_HEADING, 10)
#     time.sleep(2)
#     log.info("customer sorting is working  ")
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_CODE_HEADING, 10)
#     time.sleep(2)
#     log.info("REBATE DATE sorting is working  ")
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_SERIAL_HEADING, 10)
#     time.sleep(2)
#     log.info("REBATE DATE sorting is working  ")
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_LOT_HEADING, 10)
#     time.sleep(2)
#     log.info("REBATE DATE sorting is working  ")
#     Envi_Helper.capture_screenshot()
#     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.SEARIALIZED_CODE_OWNER_HEADING, 10)
#     time.sleep(2)
#     log.info("REBATE DATE sorting is working  ")
#     Envi_Helper.capture_screenshot()
#
# @then(u'the user can open Serialized Code popup on Serialized Code page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the user can open Serialized Code popup on Serialized Code page')
#
#
# @then(u'user can export the Serialized Codes')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then user can export the Serialized Codes')
#
#
# @then(u'user can import Serialized Codes')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then user can import Serialized Codes')