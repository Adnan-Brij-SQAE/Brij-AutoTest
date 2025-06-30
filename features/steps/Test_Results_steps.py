import pyautogui
import keyboard
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators import locators
from Helper.enviHelper import Envi_Helper
from Logs import logs_file
import allure
import time
log = logs_file.get_logs()



file1 = "C:/Users/Vqode/Desktop/csv_file.xlsx"
file2 = "C:/Users/Vqode/Desktop/excel_file.xlsx"
test_file = "D:/Vqode/Brij/TestData/testfile.pdf"


@given(u'the user is logged into the Brij platform')
def step_impl(context):
    with allure.step("the user is logged into the Brij platform"):
        try:
            log.info("The user is t Brij Platform ")
        except Exception as e:
            log.error(f" is logged into the Brij platform failed: {e}")
            allure.attach(str(e), name=" logged into the Brij platform Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user navigates to the Test Result page')
def step_impl(context):
    with allure.step("the user navigates to the Test Result page"):
            module_menu = context.driver.find_element(By.XPATH, "//li[@class='has-subnav orders ng-star-inserted']")
            actions = ActionChains(context.driver)
            actions.move_to_element(module_menu).perform()
            module_menu.click()
            time.sleep(2)

@then(u'the Test Result page should be displayed')
def step_impl(context):
    with allure.step("the Test Result page should be displayed"):
        try:
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present(locators.TEST_RESULT_TITLE)
        except Exception as e:
            log.error(f"the Test Result page should be displayed failed: {e}")
            allure.attach(str(e), name="the Test Result page display Error", attachment_type=allure.attachment_type.TEXT)

@when('the user is on test result page')
def step_impl(context):
    with allure.step("Navigate to test result page"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present(locators.TEST_RESULT_TITLE)
            time.sleep(2)
        except Exception as e:
            log.error(f"the Test Result page should be displayed failed: {e}")
            allure.attach(str(e), name="the Test Result page should be displayed Error", attachment_type=allure.attachment_type.TEXT)

@then('the user should be able to access the notification button')
def step_impl(context):
    with allure.step("the user should be able to access the notification button"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON)
            Envi_Helper.capture_screenshot()
            time.sleep(2)
        except Exception as e:
            log.error(f" access the notification button failed: {e}")
            allure.attach(str(e), name="access the notification button Error", attachment_type=allure.attachment_type.TEXT)

@then('the user should be able to access the logout button dropdown')
def step_impl(context):
    with allure.step("the user should be able to access the logout button dropdown"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            Envi_Helper.capture_screenshot()
            # Envi_Helper(context.driver).wait_till_element_is_present(locators.)
            context.driver.find_element(By.XPATH, "//app-brand-main[@class='ng-star-inserted']")
        except Exception as e:
            log.error(f" access the logout button dropdown failed: {e}")
            allure.attach(str(e), name=" access the logout button dropdown Error", attachment_type=allure.attachment_type.TEXT)

@then('the user should be able to see the Test Result count displayed')
def step_impl(context):
    with allure.step("the user should be able to see the Test Result count displayed"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present(locators.TEST_RESULT_COUNT)
            Envi_Helper.capture_screenshot()
            time.sleep(2)
        except Exception as e:
            log.error(f" Test Result count displayed failed: {e}")
            allure.attach(str(e), name="Test Result count displayed Error", attachment_type=allure.attachment_type.TEXT)
@when(u'the user applies Testing Panel filters on the page')
def step_impl(context):
    with allure.step("the user applies filters on the page"):
        try:
            log.info("Testing Panel filter testing ")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_PANEL_FILTER)
            try:
                log.info("searching Heavy Metal in Testing Panel")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_TEST_PANEL_FILTER_SEARCH, "Heavy Metals")
                Envi_Helper.capture_screenshot()
                log.info("searching is working")
            except Exception as e:
                log.error("search is not working")
                log.error(f" element is failed to be located: {e}")
            time.sleep(2)
            try:
                # Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_PANEL_FILTER)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_PANEL_FILTER_HEAVY)
                time.sleep(2)
                Envi_Helper.capture_screenshot()
                log.info("user is able to filter the table with heavy metals ")
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_PANEL_FILTER_HEAVY)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_PANEL_FILTER_PESTICIDES)
                time.sleep(2)
                Envi_Helper.capture_screenshot()
                log.info("user is able to filter the table with Pesticides")
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_PANEL_FILTER_PESTICIDES)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_PANEL_FILTER_PLASTICISER)
                time.sleep(2)
                Envi_Helper.capture_screenshot()
                log.info("user is able to filter the table with Plasticisers")
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_PANEL_FILTER_PLASTICISER)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            time.sleep(2)
        except Exception as e:
            log.error(f"applies filters on the page failed: {e}")
            allure.attach(str(e), name=" applies filters on the page Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user applies Lab filters on the page')
def step_impl(context):
    with allure.step("the user applies Lab filters on the page"):
        try:
            log.info("Test Lab filter testing ")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_LAB_FILTER)
            try:
                log.info("searching test in Test lab filter")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_TEST_PANEL_FILTER_SEARCH, "test")
                Envi_Helper.capture_screenshot()
                log.info("searching is working")
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_LAB_FILTER_OPTION,  10)
                log.info("user is able to filter the table with selected lab")
                Envi_Helper.capture_screenshot()
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_LAB_FILTER_OPTION)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.EXPERIENCE_FILTER_SEARCH_CROSS)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            time.sleep(2)
        except Exception as e:
            log.error(f"applies filters on the page failed: {e}")
            allure.attach(str(e), name=" applies lab filters on the page Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the Test Results should be filtered accordingly')
def step_impl(context):
    with allure.step("the Test Results should be filtered accordingly"):
        try:
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"the Test Results should be filtered accordingly failed: {e}")
            allure.attach(str(e), name="the Test Results should be filtered accordingly Error", attachment_type=allure.attachment_type.TEXT)
@when(u'the user sorts the Test Results table')
def step_impl(context):
    with allure.step("the user sorts the Test Results table"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_LOT_NO)
            time.sleep(1)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_DATE)
            time.sleep(1)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_EXPIRATION_DATE)
            time.sleep(1)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_TEST_ID)
            time.sleep(1)
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f" sorts the Test Results table failed: {e}")
            allure.attach(str(e), name=" sorts the Test Results table Error", attachment_type=allure.attachment_type.TEXT)
@then(u'the Test Results should be sorted in the correct order')
def step_impl(context):
    with allure.step("the Test Results should be sorted in the correct order"):
        try:

            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"the Test Results should be sorted in the correct order failed: {e}")
            allure.attach(str(e), name="the Test Results should be sorted in the correct order Error", attachment_type=allure.attachment_type.TEXT)
@when(u'the user clicks on the field button')
def step_impl(context):
    with allure.step("the user clicks on the field button"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_FIELDS_BUTTON)
        except Exception as e:
            log.error(f" clicks on the field button failed: {e}")
            allure.attach(str(e), name="clicks on the field button Error", attachment_type=allure.attachment_type.TEXT)
@then(u'the corresponding action should be performed')
def step_impl(context):
    with allure.step("the corresponding action should be performed"):
        try:
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).hover_to_element_to_click(locators.TEST_RESULT_FIELDS_BUTTON)
        except Exception as e:
            log.error(f"the corresponding action should be performed failed: {e}")
            allure.attach(str(e), name="the corresponding action should be performed Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user checks all checkboxes')
def step_impl(context):
    with allure.step("the user checks all checkboxes"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_SELECT_ALL_CHECKBOX)
        except Exception as e:
            log.error(f" checks all checkboxes failed: {e}")
            allure.attach(str(e), name="checks all checkboxes Error", attachment_type=allure.attachment_type.TEXT)
@then(u'all checkboxes should be selected on test result page')
def step_impl(context):
    with allure.step("all checkboxes should be selected on test result page"):
        try:
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_SELECT_ALL_CHECKBOX)
        except Exception as e:
            log.error(f"all checkboxes should be selected failed: {e}")
            allure.attach(str(e), name="all checkboxes should be selected  Error", attachment_type=allure.attachment_type.TEXT)
@when(u'the user creates a new Test Result')
def step_impl(context):
    with allure.step("the user creates a new Test Result"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_NEW_TEST)
            time.sleep(2)
            try:
                Envi_Helper.capture_screenshot()
                log.info('The user is on the Add test result popup')
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTING_PANEL)
                Envi_Helper.capture_screenshot()
                time.sleep(2)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_HEAVY_METAL)
                Envi_Helper.capture_screenshot()
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PESTICIDES)
                Envi_Helper.capture_screenshot()
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PLASTICISERS)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTING_PANEL)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            ###CREATE TEST LAB ###
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTLAB)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_NEWLAB)
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_NEWLAB_NAME, "Auto test lab")
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_NEWLAB_SAVE)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            time.sleep(2)
                ###add lot number etc ###
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_APPLY_ALL_LOT)
                log.info("selected All lot no.")
                Envi_Helper.capture_screenshot()
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_APPLY_ALL_LOT)
                log.info("unselected All lot no.")
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
                time.sleep(2)
            try:
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_LOT_NO, "test lot 001")
                log.info("enetered lot no.")
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
                time.sleep(2)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_TESTID, "")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_SAMPLE_ID, "AUTO001")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_ORDER_ID, "AUTO001")
            # Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_EXPIRYDATE, "12 February 2025")
            time.sleep(2)
            ### ADD Test Product ###
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PRODUCT)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_NEW_PRODUCT)
                time.sleep(2)
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_PRODUCTNAME, "Auto test product 12 digit")
                random_number = Envi_Helper.add_random_number_12()
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_UPC, random_number)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PRODUCT_SAVE)
                time.sleep(2)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            # context.driver.find_element(By.XPATH, "//div[@class='whole-container ng-untouched ng-pristine ng-invalid']")
            keyboard.press('Tab')
            # Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_ARSENIC, "10")
            try:
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_CADMIUM, "10")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_LEAD, "10")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_MERCURY, "10")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_PESTICIDE, "10")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_GLYPHOSATE, "10")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_BPA, "10")
                # Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_BPS, "10")
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TEST_RESULT_UPLOAD)
                upload_button = context.driver.find_element(By.XPATH,"//div[@class='csv-upload-container']")
                ActionChains(context.driver).move_to_element(upload_button).click().perform()
                time.sleep(2)
                pyautogui.write("desktop")
                pyautogui.press("Enter")
                time.sleep(1)
                pyautogui.write("testfile.pdf")
                pyautogui.press("Enter")
                # Envi_Helper(context.driver).upload_file(locators.TEST_RESULT_POPUP_TEST_RESULT_UPLOAD,test_file)
                time.sleep(7)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
                Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_SAVE)
            time.sleep(4)
        except Exception as e:
            log.error(f" creates a new Test Result failed: {e}")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_SAVE)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_CROSS_ICON)
            allure.attach(str(e), name="creates a new Test Result Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the new Test Result should be added to the list')
def step_impl(context):
    with allure.step("the new Test Result should be added to the list"):
        try:
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"the new Test Result should be added to the list failed: {e}")
            allure.attach(str(e), name="the new Test Result should be added to the list Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user edits an existing Test Result')
def step_impl(context):
    with allure.step("the user edits an existing Test Result"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_KEBAB_MENU)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_EDIT)
            time.sleep(2)
            Envi_Helper(context.driver).capture_screenshot()
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTING_PANEL)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_ALL_PANEL)
                log.info("selected All testing panel")
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_HEAVY_METAL)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PESTICIDES)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PLASTICISERS)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_HEAVY_METAL)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTING_PANEL)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            time.sleep(2)
            ###select lab###
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTLAB_1)
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_LAB_SEARCH, "test")
                time.sleep(2)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTLAB_SLAB)
                time.sleep(2)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            ###add lot number etc ###

            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_APPLY_ALL_LOT)
                Envi_Helper.capture_screenshot()
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            try:
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_TESTID, "")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_SAMPLE_ID, "updated AUTO001")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_ORDER_ID, "updated AUTO001")
                time.sleep(2)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            ###SELECT TEST PRODUCT###
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PRODUCT_selected)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(
                    locators.TEST_RESULT_POPUP_NEW_PRODUCT)
                time.sleep(2)
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_PRODUCTNAME,"Auto test product 14 digit")
                random_number = Envi_Helper.add_random_number_14()
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_UPC, random_number)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PRODUCT_SAVE)
                time.sleep(2)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            time.sleep(2)
            ###update elements
            keyboard.press('pagedown')
            try:
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_ARSENIC, "10")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_CADMIUM, "10")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_LEAD, "10")
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_MERCURY, "10")
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            keyboard.press('pagedown')
            # try:
            #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TEST_RESULT_UPLOAD)
            #     upload_button = context.driver.find_element(By.XPATH, "//div[@class='csv-upload-container']")
            #     ActionChains(context.driver).move_to_element(upload_button).click().perform()
            #     time.sleep(2)
            #     pyautogui.write("desktop")
            #     pyautogui.press("enter")
            #     time.sleep(1)
            #     pyautogui.write("testfile.pdf")
            #     pyautogui.press("enter")
            #     # Envi_Helper(context.driver).upload_file(locators.TEST_RESULT_POPUP_TEST_RESULT_UPLOAD,test_file)
            #     time.sleep(10)
            # except Exception as e:
            #     log.error(f" element is failed to be located: {e}")
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_SAVE)
            time.sleep(4)
        except Exception as e:
            log.error(f" edits an existing Test Result failed: {e}")
            allure.attach(str(e), name=" edits an existing Test Result Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the changes should be saved and reflected in the list')
def step_impl(context):
    with allure.step("the changes should be saved and reflected in the list"):
        try:
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"the changes should be saved  failed: {e}")
            allure.attach(str(e), name="the changes should be saved and reflected in the list Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user creates, updates, or deletes a lab')
def step_impl(context):
    with allure.step("the user creates, updates, or deletes a lab"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_KEBAB_MENU)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_EDIT)
            time.sleep(2)
            Envi_Helper(context.driver).capture_screenshot()
            ###select lab###
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTLAB_SLAB)
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_LAB_SEARCH, "test")
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTLAB_SLAB)
                time.sleep(2)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")

                #edit lab
                try:
                    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTLAB_edit)
                    Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_TESTLAB_name, "Updated test lab")
                    time.sleep(2)
                    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTLAB_SLAB)
                    time.sleep(2)
                except Exception as e:
                    log.error(f" element is failed to be located: {e}")
                #delete lab
                try:
                    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_TESTLAB_edit)
                    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_LAB_NAME_DELETE)
                    time.sleep(2)
                    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_LAB_NAME_DELETE_CONFIRM)
                    time.sleep(2)
                except Exception as e:
                    log.error(f" element is failed to be located: {e}")

        except Exception as e:
            log.error(f"the lab details should be updated accordingly failed: {e}")
            allure.attach(str(e), name="the lab details should be updated accordingly Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the lab details should be updated accordingly')
def step_impl(context):
    with allure.step("the lab details should be updated accordingly"):
        try:
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"the lab details should be updated accordingly failed: {e}")
            allure.attach(str(e), name="the lab details should be updated accordingly Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user creates, updates, or deletes a UPC Result')
def step_impl(context):
    with allure.step("the user creates, updates, or deletes a UPC Result"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_NEW_TEST)
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            ### ADD Test Product ###
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PRODUCT)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_NEW_PRODUCT)
                time.sleep(2)
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_PRODUCTNAME,"Auto new test product")
                random_number = Envi_Helper.add_random_number_13()
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_UPC, random_number)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PRODUCT_SAVE)
                time.sleep(5)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            ### EDIT TEST PRODUCT###
            try:
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PRODUCT1)
                # Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_SEARCH_PRODUCT,"test")
                Envi_Helper(context.driver).hover_to_element(locators.TEST_RESULT_POPUP_SELECT_PRODUCT)
                Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_EDIT_PRODUCT)
                time.sleep(2)
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_PRODUCTNAME, "updated UPC")
                random_number = Envi_Helper.add_random_number_14()
                Envi_Helper(context.driver).insert_text_in_input_field(locators.TEST_RESULT_POPUP_UPC, random_number)
            except Exception as e:
                log.error(f" element is failed to be located: {e}")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_PRODUCT_SAVE)
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_CROSS_ICON)
        except Exception as e:
            log.error(f" creates, updates, or deletes a UPC Result failed: {e}")
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_POPUP_CROSS_ICON)
            allure.attach(str(e), name=" creates, updates, or deletes a UPC Result Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the UPC Result details should be updated accordingly')
def step_impl(context):
    with allure.step("the UPC Result details should be updated accordingly"):
        try:
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"the UPC Result details should be updated accordingly failed: {e}")
            allure.attach(str(e), name="the UPC Result details should be updated accordingly Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user exports the Test Result')
def step_impl(context):
    with allure.step("the user exports the Test Result"):
        try:
            keyboard.press_and_release('pagedown')
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_EXPORT)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_EXPORT_CONFIRM)
            Envi_Helper.capture_screenshot()
            time.sleep(2)
        except Exception as e:
            log.error(f" exports the Test Result failed: {e}")
            allure.attach(str(e), name=" exports the Test Result Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the Test Result data should be downloaded successfully')
def step_impl(context):
    with allure.step("the Test Result data should be downloaded successfully"):
        try:
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"the Test Result data should be downloaded successfully failed: {e}")
            allure.attach(str(e), name="the Test Result data should be downloaded successfully Error", attachment_type=allure.attachment_type.TEXT)

@when(u'the user downloads the template sheet')
def step_impl(context):
    with allure.step("the user downloads the template sheet"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_IMPORT_BTN)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_DOWNLOAD_TEMPLATE)
            Envi_Helper.capture_screenshot()
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_IMPORT_CROSS)
            time.sleep(2)
        except Exception as e:
            log.error(f" downloads the template sheet failed: {e}")
            allure.attach(str(e), name=" downloads the template sheet Error", attachment_type=allure.attachment_type.TEXT)
@then(u'the template sheet should be downloaded successfully')
def step_impl(context):
    with allure.step("the template sheet should be downloaded successfully"):
        try:
            Envi_Helper.capture_screenshot()
        except Exception as e:
            log.error(f"the template sheet should be downloaded successfully failed: {e}")
            allure.attach(str(e), name="the template sheet should be downloaded successfully Error", attachment_type=allure.attachment_type.TEXT)
@when(u'the user imports data into the Test Result page')
def step_impl(context):
    with allure.step("the user imports data into the Test Result page"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_IMPORT_BTN)
            upload_button = context.driver.find_element(By.XPATH, "//span[@class='upload-text']")
            ActionChains(context.driver).move_to_element(upload_button).click().perform()
            time.sleep(2)
            pyautogui.write("desktop")
            pyautogui.press("enter")
            pyautogui.write("csv_file")
            pyautogui.press("enter")
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_IMPORT_SHEET)
            time.sleep(5)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_UPDATE_FILE)
            time.sleep(3)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_IMPORT_BTN)
            upload_button = context.driver.find_element(By.XPATH, "//span[@class='upload-text']")
            ActionChains(context.driver).move_to_element(upload_button).click().perform()
            time.sleep(2)
            pyautogui.write("excel_file")
            pyautogui.press("enter")
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_IMPORT_SHEET)
            time.sleep(5)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.TEST_RESULT_UPDATE_FILE)
            time.sleep(3)
        except Exception as e:
            log.error(f" imports data into the Test Result page failed: {e}")
            allure.attach(str(e), name="t imports data into the Test Result page Error", attachment_type=allure.attachment_type.TEXT)

@then(u'the imported data should be reflected in the Test Results')
def step_impl(context):
    with allure.step("the user navigates to the Test Result page"):
        Envi_Helper.capture_screenshot()
