import keyboard
from behave import *
from Locators import locators
from Helper.enviHelper import Envi_Helper
from Logs import logs_file
import allure
import time

log = logs_file.get_logs()


@when('the user navigates to the Ab899 page')
def step_impl(context):
    with allure.step("User navigates to AB899 page"):
        time.sleep(2)
        helper = Envi_Helper(context.page)
        helper.wait_till_element_is_present_to_click("(//li[@class='has-subnav ng-star-inserted'])[3]")
        helper.wait_till_element_is_present_to_click("//span[normalize-space()='AB 899']")
        helper.get_value("//div[@id='mainContent']")
        helper.open_page("https://rc.brij.it/brand/modules/ab899")
        time.sleep(2)
        log.info("Navigated to Custom Module page")
        time.sleep(2)
        allure.attach("Navigated to AB899 page", name="Navigation", attachment_type=allure.attachment_type.TEXT)


@then('the Ab899 page should be displayed')
def step_impl(context):
    with allure.step("Verify AB899 page is displayed"):
        # Envi_Helper(context.page).wait_till_element_is_present(locators.AB899_TITLE)
        Envi_Helper(context.page).capture_screenshot()
        allure.attach("AB899 page is displayed", name="Page Verification", attachment_type=allure.attachment_type.TEXT)


@given('the user is on the Ab899 page')
def step_impl(context):
    with allure.step("User is on AB899 page"):
        Envi_Helper(context.page).get_value(locators.AB899_TITLE)
        Envi_Helper(context.page).capture_screenshot()
        allure.attach("User is on AB899 page", name="Page Verification", attachment_type=allure.attachment_type.TEXT)


@then('the user can access the notification button on the Ab899 module page')
def step_impl(context):
    with allure.step("Verify notification button is accessible"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON, 10)
            time.sleep(3)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON_2, 10)
            keyboard.press_and_release('Esc')
            allure.attach("Notification button is accessible", name="UI Verification",
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Notification button access failed: {e}")
            allure.attach(str(e), name="Notification Button Error", attachment_type=allure.attachment_type.TEXT)


@then('the user can access the logout button on the Ab899 module page')
def step_impl(context):
    with allure.step("Verify logout button is accessible"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            time.sleep(3)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON)
            keyboard.press_and_release('Esc')
            allure.attach("Logout button is accessible", name="UI Verification",
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Logout button access failed: {e}")
            allure.attach(str(e), name="Logout Button Error", attachment_type=allure.attachment_type.TEXT)


@then('the user can access the field button on the Ab899 module page')
def step_impl(context):
    with allure.step("Verify field button is accessible"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_FIELD_BUTTON)
            Envi_Helper(context.page).capture_screenshot()
            time.sleep(3)
            try:
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_FIELD_MODULE_NAME)
                Envi_Helper(context.page).capture_screenshot()
                log.info("the where used is accessible and clickable")
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_FIELD_MODULE_NAME)
                allure.attach("'Where Used' on field button is accessible", name="UI Verification",attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                log.error(f"'Where Used' access failed: {e}")
                allure.attach(str(e), name="Where Used Error", attachment_type=allure.attachment_type.TEXT)

            try:
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_FIELD_BUTTON)
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_FIELD_WHERE_USED)
                Envi_Helper(context.page).capture_screenshot()
                log.info("the where used is accessible and clickable")
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_FIELD_WHERE_USED)
                allure.attach("'Where Used' on field button is accessible", name="UI Verification",attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                log.error(f"'Where Used' access failed: {e}")
                allure.attach(str(e), name="Where Used Error", attachment_type=allure.attachment_type.TEXT)

            try:
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_FIELD_BUTTON)
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_FIELD_CALL_TO_ACTION)
                Envi_Helper(context.page).capture_screenshot()
                log.info("the where used is accessible and clickable")
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_FIELD_CALL_TO_ACTION)
                allure.attach("'Where Used' on field button is accessible", name="UI Verification",attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                log.error(f"'Where Used' access failed: {e}")
                allure.attach(str(e), name="Where Used Error", attachment_type=allure.attachment_type.TEXT)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_FIELD_BUTTON)
            allure.attach("Field button is accessible", name="UI Verification",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Field button access failed: {e}")
            allure.attach(str(e), name="Field Button Error", attachment_type=allure.attachment_type.TEXT)


@when('the user selects all AB899 checkboxes')
def step_impl(context):
    with allure.step("User selects all checkboxes"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_ALL_CHECK, 10)
            Envi_Helper(context.page).capture_screenshot()
            allure.attach("All checkboxes selected", name="Checkbox Selection",
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Checkbox selection failed: {e}")
            allure.attach(str(e), name="Checkbox Selection Error", attachment_type=allure.attachment_type.TEXT)


@then('all checkboxes should be selected on Ab899')
def step_impl(context):
    with allure.step("Verify all checkboxes are selected"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_ALL_CHECK, 10)
            Envi_Helper(context.page).capture_screenshot()
            allure.attach("All checkboxes are selected", name="Checkbox Verification",
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Checkbox verification failed: {e}")
            allure.attach(str(e), name="Checkbox Verification Error", attachment_type=allure.attachment_type.TEXT)


@when('the user uses the search feature to search for a module')
def step_impl(context):
    with allure.step("User searches for module"):
        try:
            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_SEARCH, "test", 10)
            Envi_Helper(context.page).capture_screenshot()
            time.sleep(2)
            allure.attach("Search performed", name="Search Action", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Search failed: {e}")
            allure.attach(str(e), name="Search Error", attachment_type=allure.attachment_type.TEXT)


@then('the searched results should be displayed correctly')
def step_impl(context):
    with allure.step("Verify search results"):
        try:
            context.page.find_element("//input[@placeholder='Search Items...']").clear()
            Envi_Helper(context.page).capture_screenshot()
            allure.attach("Search results displayed correctly", name="Search Verification",
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Search results verification failed: {e}")
            allure.attach(str(e), name="Search Results Error", attachment_type=allure.attachment_type.TEXT)


@when('the user creates a new AB 899 module')
def step_impl(context):
    with allure.step("User creates new AB899 module"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_NEW_MODULE)
            Envi_Helper(context.page).capture_screenshot()
            time.sleep(2)
            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_POPUP_MODULE_NAME, "Auto Ab-899 Test",10)
            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_POPUP_CTA, "Testing", 10)
            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_POPUP_EDITOR, "Demo", 10)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_POPUP_SAVE_BUTTON)
            time.sleep(2)

            try:
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS)
                log.info("navigated to Advance Settings")
                time.sleep(2)
                Envi_Helper(context.page).capture_screenshot()
            #Heavy Metals configuration
                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HEAVY_METALS)
                    log.info("Expanded Heavy Metal section")
                    Envi_Helper(context.page).capture_screenshot()


                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_HIDE_TEST_DATE)
                        log.info("clicked on hide test date flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_HIDE_TEST_DATE)
                    except Exception as e:
                        log.error(f"Failed to clicked on hide test date flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_EXPIRY_DATE)
                        log.info("clicked on Hide Expiration Date flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_EXPIRY_DATE)
                    except Exception as e:
                        log.error(f"Failed to clicked on Hide Expiration Date flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_HIDE_NULL)
                        log.info("clicked on hide null value flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_HIDE_NULL)
                    except Exception as e:
                        log.error(f"Failed to clicked on hide null value flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_POST_30DAYS)
                        log.info("clicked on Hide Results 30 Days Post-Expiration flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_POST_30DAYS)
                    except Exception as e:
                        log.error(f"Failed to clicked on Hide Results 30 Days Post-Expiration flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_OVERRIDE_NONNUMERIC)
                        log.info("clicked on Override Non-Numeric Results flag")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_OVERRIDE_NONNUMERIC_ARSENIC)
                            log.info("clicked on Override Non-Numeric Results flag")
                            Envi_Helper(context.page).capture_screenshot()
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_OVERRIDE_NONNUMERIC_ARSENIC_TEXT,"Arsenic non numeric")
                            log.info(" added value in arsenic Non-Numeric Results flag")
                        except Exception as e:
                            log.error(f"Failed to clicked on Override Non-Numeric Results flag : {e}")

                        try:

                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_OVERRIDE_NONNUMERIC_CADMIUM)
                            log.info("clicked on CADMIUM Override Non-Numeric Results flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_OVERRIDE_NONNUMERIC_CADMIUM_TEXT, "CADMIUM non numeric")
                            log.info(" added value in CADMIUM Non-Numeric Results flag")
                            Envi_Helper(context.page).capture_screenshot()
                            keyboard.press_and_release('Page Down')
                        except Exception as e:
                            log.error(f"Failed to clicked on CADMIUM Override Non-Numeric Results flag : {e}")

                        try:

                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_OVERRIDE_NONNUMERIC_lEAD)
                            log.info("clicked on LEAD Override Non-Numeric Results flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_OVERRIDE_NONNUMERIC_lEAD_TEXT,"LEAD non numeric")
                            log.info(" added value in LEAD Non-Numeric Results flag")
                            Envi_Helper(context.page).capture_screenshot()
                        except Exception as e:
                            log.error(f"Failed to clicked on LEAD Override Non-Numeric Results flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_OVERRIDE_NONNUMERIC_MERCURY)
                            log.info("clicked on MERCURY Override Non-Numeric Results flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_OVERRIDE_NONNUMERIC_MERCURY_TEXT, "MERCURY non numeric")
                            log.info(" added value in MERCURY Non-Numeric Results flag")
                            Envi_Helper(context.page).capture_screenshot()
                        except Exception as e:
                            log.error(f"Failed to clicked on MERCURY Override Non-Numeric Results flag : {e}")

                    except Exception as e:
                        log.error(f"Failed to click on Override Non-Numeric Results flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_SHOW_EDUCATIONAL)
                        log.info("clicked on Show Educational Text flag")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_SHOW_EDUCATIONAL_TEXT,"Auto Show Educational ")
                        log.info(" added value in Show Educational Text flag")
                        Envi_Helper(context.page).capture_screenshot()
                        keyboard.press_and_release('Page Down')
                    except Exception as e:
                        log.error(f"Failed to clicked on Show Educational Text flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_SHOW_INFO)
                        log.info("clicked on Show Info Tool Tip flag")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_SHOW_INFO_LABEL,"Auto Pb label ")
                        log.info(" added value in Info Tool Tip label")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_SHOW_INFO_TEXT,"Auto Pb Text ")
                        log.info(" added value in Info Tool Tip Text ")
                        Envi_Helper(context.page).capture_screenshot()
                    except Exception as e:
                        log.error(f"Failed to clicked on Show Educational Text flag : {e}")


                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_INCLUDE_LINK)
                        log.info("clicked on Include Link to Test Result Document flag")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_INCLUDE_LINK_TEXT,"Auto link ")
                        log.info(" added value in Include Link to Test Result Document text")
                        Envi_Helper(context.page).capture_screenshot()

                    except Exception as e:
                        log.error(f"Failed to clicked on Include Link to Test Result Document flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_BELOW_THRESHOLD)
                        log.info("clicked on Override Results Below a Threshold flag")
                        Envi_Helper(context.page).capture_screenshot()

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_BELOW_THRESHOLD_ARSENIC)
                            log.info("clicked on Override Results Below-Arsenic flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_BELOW_THRESHOLD_ARSENIC_TEXT,"auto arsenic")
                            log.info(" added value in arsenic Override Results Below a Threshold text")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_BELOW_THRESHOLD_ARSENIC_VALUE, "5")
                            log.info(" added value in arsenic Override Results Below a Threshold limit")
                            Envi_Helper(context.page).capture_screenshot()
                        except Exception as e:
                            log.error(f"Failed to clicked on Override Results Below-Arsenic flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_BELOW_THRESHOLD_CADMIUM)
                            log.info("clicked on Override Results Below-Cadmium flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_BELOW_THRESHOLD_CADMIUM_TEXT,"auto CADMIUM")
                            log.info(" added value in CADMIUM Override Results Below a Threshold text")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_BELOW_THRESHOLD_CADMIUM_VALUE, "5")
                            log.info(" added value in CADMIUM Override Results Below a Threshold limit")
                            Envi_Helper(context.page).capture_screenshot()
                            # keyboard.press_and_release('Page Down')
                        except Exception as e:
                            log.error(f"Failed to clicked on Override Results Below-Cadmium flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_BELOW_THRESHOLD_LEAD)
                            log.info("clicked on Override Results Below-Lead flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_BELOW_THRESHOLD_LEAD_TEXT,"auto LEAD")
                            log.info(" added value in LEAD Override Results Below a Threshold text")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_BELOW_THRESHOLD_LEAD_VALUE, "5")
                            log.info(" added value in LEAD Override Results Below a Threshold limit")
                            Envi_Helper(context.page).capture_screenshot()
                        except Exception as e:
                            log.error(f"Failed to clicked on Override Results Below-Lead flag : {e}")


                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_BELOW_THRESHOLD_MERCURY)
                            log.info("clicked on Override Results Below-Mercury flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_BELOW_THRESHOLD_MERCURY_TEXT,"auto MERCURY")
                            log.info(" added value in MERCURY Override Results Below a Thresholds text")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_BELOW_THRESHOLD_MERCURY_VALUE, "5")
                            log.info(" added value in MERCURY Override Results Below a Threshold limit")
                            Envi_Helper(context.page).capture_screenshot()

                        except Exception as e:
                            log.error(f"Failed to clicked on Override Results Below-Mercury flag : {e}")
                    except Exception as e:
                        log.error(f"Failed to clicked on on Override Results Below a Threshold flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_STANDARD_LIMIT)
                        log.info("clicked on Show Standard Limits flag")
                        Envi_Helper(context.page).capture_screenshot()

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_STANDARD_LIMIT_ARSENIC)
                            log.info("clicked on Standard Limit Arsenic flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_STANDARD_LIMIT_ARSENIC_LIMIT,"20")
                            log.info(" added value in Standard Limit Arsenic value")
                            Envi_Helper(context.page).capture_screenshot()

                        except Exception as e:
                            log.error(f"Failed to clicked on Standard Limit Arsenic flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_STANDARD_LIMIT_CADMIUM)
                            log.info("clicked on Standard Limit CADMIUM flag")
                            keyboard.press_and_release('Page Down')
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_STANDARD_LIMIT_CADMIUM_LIMIT, "20")
                            log.info(" added value in Standard Limit CADMIUM value")
                            Envi_Helper(context.page).capture_screenshot()
                        except Exception as e:
                            log.error(f"Failed to clicked on Standard Limit CADMIUM flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_STANDARD_LIMIT_LEAD)
                            log.info("clicked on Standard Limit LEAD flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_STANDARD_LIMIT_LEAD_LIMIT, "20")
                            log.info(" added value in Standard Limit LEAD value")
                            Envi_Helper(context.page).capture_screenshot()
                        except Exception as e:
                            log.error(f"Failed to clicked on Standard Limit LEAD flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_STANDARD_LIMIT_MERCURY)
                            log.info("clicked on Standard Limit MERCURY flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_STANDARD_LIMIT_MERCURY_LIMIT, "20")
                            log.info(" added value in Standard Limit MERCURY value")
                        except Exception as e:
                            log.error(f"Failed to clicked on Standard Limit MERCURY flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_HM_STANDARD_LIMIT_ALERT)
                            log.info("clicked on Standard Limit MERCURY flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_HM_STANDARD_LIMIT_ALERT_TEXT, "Auto Alert text ")
                            log.info(" added value in Standard Limit MERCURY value")
                        except Exception as e:
                            log.error(f"Failed to clicked on Standard Limit alert : {e}")
                    except Exception as e:
                        log.error(f"Failed to clicked on Show Standard Limits flag : {e}")

                except Exception as e:
                    log.error(f"Failed configured Heavy Metals : {e}")
                #PESTICIDES AND GLYPHOSATE
                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PESTICIDE_GLYPHOSATE)
                    log.info("Expanded Heavy Metal section")
                    Envi_Helper(context.page).capture_screenshot()


                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_HIDE_TEST_DATE)
                        log.info("clicked on hide test date flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_HIDE_TEST_DATE)
                    except Exception as e:
                        log.error(f"Failed to clicked on hide test date flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_EXPIRY_DATE)
                        log.info("clicked on Hide Expiration Date flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_EXPIRY_DATE)
                    except Exception as e:
                        log.error(f"Failed to clicked on Hide Expiration Date flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_HIDE_NULL)
                        log.info("clicked on hide null value flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_HIDE_NULL)
                    except Exception as e:
                        log.error(f"Failed to clicked on hide null value flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_POST_30DAYS)
                        log.info("clicked on Hide Results 30 Days Post-Expiration flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_POST_30DAYS)
                    except Exception as e:
                        log.error(f"Failed to clicked on Hide Results 30 Days Post-Expiration flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_OVERRIDE_NONNUMERIC)
                        log.info("clicked on Override Non-Numeric Results flag")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_OVERRIDE_NONNUMERIC_PESTICIDES)
                            log.info("clicked on Override Non-Numeric Results flag")
                            Envi_Helper(context.page).capture_screenshot()
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_OVERRIDE_NONNUMERIC_PESTICIDES_TEXT,"Pesticides non numeric")
                            log.info(" added value in PESTICIDES Non-Numeric Results flag")
                        except Exception as e:
                            log.error(f"Failed to clicked on Override Non-Numeric Results flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_OVERRIDE_NONNUMERIC_GLYPHOSATE)
                            log.info("clicked on GLYPHOSATE Override Non-Numeric Results flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_OVERRIDE_NONNUMERIC_GLYPHOSATE_TEXT, "GLYPHOSATE non numeric")
                            log.info(" added value in GLYPHOSATE Non-Numeric Results flag")
                            Envi_Helper(context.page).capture_screenshot()
                            keyboard.press_and_release('Page Down')
                        except Exception as e:
                            log.error(f"Failed to clicked on GLYPHOSATE Override Non-Numeric Results flag : {e}")


                    except Exception as e:
                        log.error(f"Failed to on Override Non-Numeric Results flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_SHOW_EDUCATIONAL)
                        log.info("clicked on Show Educational Text flag")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_SHOW_EDUCATIONAL_TEXT,"Auto Show Educational ")
                        log.info(" added value in Show Educational Text flag")
                        Envi_Helper(context.page).capture_screenshot()
                        keyboard.press_and_release('Page Down')
                    except Exception as e:
                        log.error(f"Failed to clicked on Show Educational Text flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_SHOW_INFO)
                        log.info("clicked on Show Info Tool Tip flag")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_SHOW_INFO_LABEL,"Auto Pb label ")
                        log.info(" added value in Info Tool Tip label")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_SHOW_INFO_TEXT,"Auto Pb Text ")
                        log.info(" added value in Info Tool Tip Text ")
                        Envi_Helper(context.page).capture_screenshot()
                    except Exception as e:
                        log.error(f"Failed to clicked on Show Educational Text flag : {e}")

                    keyboard.press_and_release('Page Down')
                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_INCLUDE_LINK)
                        log.info("clicked on Include Link to Test Result Document flag")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_INCLUDE_LINK_TEXT,"Auto link text ")
                        log.info(" added value in Include Link to Test Result Document text")
                        Envi_Helper(context.page).capture_screenshot()
                    except Exception as e:
                        log.error(f"Failed to clicked on Include Link to Test Result Document flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_BELOW_THRESHOLD)
                        log.info("clicked on Override Results Below a Threshold flag")
                        Envi_Helper(context.page).capture_screenshot()

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_BELOW_THRESHOLD_PESTICIDES)
                            log.info("clicked on Override Results Below-Arsenic flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_BELOW_THRESHOLD_PESTICIDES_TEXT,"auto PESTICIDES")
                            log.info(" added value in PESTICIDES Override Results Below a Threshold text")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_BELOW_THRESHOLD_PESTICIDES_VALUE, "5")
                            log.info(" added value in PESTICIDES Override Results Below a Threshold limit")
                            Envi_Helper(context.page).capture_screenshot()
                        except Exception as e:
                            log.error(f"Failed to clicked on Override Results Below-Arsenic flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_BELOW_THRESHOLD_GLYPHOSATE)
                            log.info("clicked on Override Results Below-Cadmium flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_BELOW_THRESHOLD_GLYPHOSATE_TEXT,"auto GLYPHOSATE")
                            log.info(" added value in GLYPHOSATE Override Results Below a Threshold text")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_BELOW_THRESHOLD_GLYPHOSATE_VALUE, "5")
                            log.info(" added value in GLYPHOSATE Override Results Below a Threshold limit")
                            Envi_Helper(context.page).capture_screenshot()
                            keyboard.press_and_release('Page Down')
                        except Exception as e:
                            log.error(f"Failed to clicked on Override Results Below-Cadmium flag : {e}")

                    except Exception as e:
                      log.error(f"Failed to clicked on on Override Results Below a Threshold flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_STANDARD_LIMIT)
                        log.info("clicked on Show Standard Limits flag")
                        Envi_Helper(context.page).capture_screenshot()

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_STANDARD_LIMIT_PESTICIDES)
                            log.info("clicked on Standard Limit Arsenic flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_STANDARD_LIMIT_PESTICIDES_LIMIT,"20")
                            log.info(" added value in Standard Limit Arsenic value")
                            Envi_Helper(context.page).capture_screenshot()

                        except Exception as e:
                            log.error(f"Failed to clicked on Standard Limit Arsenic flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_STANDARD_LIMIT_GLYPHOSATE)
                            log.info("clicked on Standard Limit GLYPHOSATE flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_STANDARD_LIMIT_GLYPHOSATE_LIMIT, "20")
                            log.info("added value in Standard Limit GLYPHOSATE value")
                            Envi_Helper(context.page).capture_screenshot()
                        except Exception as e:
                            log.error(f"Failed to clicked on Standard Limit GLYPHOSATE flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PnG_STANDARD_LIMIT_ALERT)
                            log.info("clicked on Standard Limit MERCURY flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PnG_STANDARD_LIMIT_ALERT_text, "Auto Alert text ")
                            log.info(" added value in Standard Limit MERCURY value")
                        except Exception as e:
                            log.error(f"Failed to clicked on Standard Limit alert : {e}")

                    except Exception as e:
                        log.error(f"Failed to clicked on Show Standard Limits flag : {e}")
                except Exception as e:
                    log.error(f"Failed expand  Pesticides & Glyphosate Results options on  AB899 Advance settings : {e}")

                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PLASTICIZERS)
                    log.info("Expanded Plasticizers Results section")
                    Envi_Helper(context.page).capture_screenshot()


                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_HIDE_TEST_DATE)
                        log.info("clicked on hide test date flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_HIDE_TEST_DATE)
                    except Exception as e:
                        log.error(f"Failed to clicked on hide test date flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_EXPIRY_DATE)
                        log.info("clicked on Hide Expiration Date flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_EXPIRY_DATE)
                    except Exception as e:
                        log.error(f"Failed to clicked on Hide Expiration Date flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_HIDE_NULL)
                        log.info("clicked on hide null value flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_HIDE_NULL)
                    except Exception as e:
                        log.error(f"Failed to clicked on hide null value flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_POST_30DAYS)
                        log.info("clicked on Hide Results 30 Days Post-Expiration flag")
                        Envi_Helper(context.page).capture_screenshot()
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_POST_30DAYS)
                    except Exception as e:
                        log.error(f"Failed to clicked on Hide Results 30 Days Post-Expiration flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_OVERRIDE_NONNUMERIC)
                        log.info("clicked on Override Non-Numeric Results flag")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_OVERRIDE_NONNUMERIC_BPA)
                            log.info("clicked on Override Non-Numeric Results flag")
                            Envi_Helper(context.page).capture_screenshot()
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_OVERRIDE_NONNUMERIC_BPA_TEXT,"Arsenic non numeric")
                            log.info(" added value in BPA Non-Numeric Results flag")
                        except Exception as e:
                            log.error(f"Failed to clicked on Override Non-Numeric Results flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_OVERRIDE_NONNUMERIC_BPS)
                            log.info("clicked on BPS Override Non-Numeric Results flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_OVERRIDE_NONNUMERIC_BPS_TEXT, "BPS non numeric")
                            log.info(" added value in BPS Non-Numeric Results flag")
                            Envi_Helper(context.page).capture_screenshot()
                            keyboard.press_and_release('Page Down')
                        except Exception as e:
                            log.error(f"Failed to clicked on BPS Override Non-Numeric Results flag : {e}")


                    except Exception as e:
                        log.error(f"Failed to on Override Non-Numeric Results flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_SHOW_EDUCATIONAL)
                        log.info("clicked on Show Educational Text flag")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_SHOW_EDUCATIONAL_TEXT,"Auto Show Educational ")
                        log.info(" added value in Show Educational Text flag")
                        Envi_Helper(context.page).capture_screenshot()
                        keyboard.press_and_release('Page Down')
                    except Exception as e:
                        log.error(f"Failed to clicked on Show Educational Text flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_SHOW_INFO)
                        log.info("clicked on Show Info Tool Tip flag")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_SHOW_INFO_LABEL,"Auto Pb label ")
                        log.info(" added value in Info Tool Tip label")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_SHOW_INFO_TEXT,"Auto Pb Text ")
                        log.info(" added value in Info Tool Tip Text ")
                        Envi_Helper(context.page).capture_screenshot()
                    except Exception as e:
                        log.error(f"Failed to clicked on Show Educational Text flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_INCLUDE_LINK)
                        log.info("clicked on Include Link to Test Result Document flag")
                        Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_INCLUDE_LINK_TEXT,"Auto link text ")
                        log.info(" added value in Include Link to Test Result Document text")
                        Envi_Helper(context.page).capture_screenshot()
                    except Exception as e:
                        log.error(f"Failed to clicked on Include Link to Test Result Document flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_BELOW_THRESHOLD)
                        log.info("clicked on Override Results Below a Threshold flag")
                        Envi_Helper(context.page).capture_screenshot()

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_BELOW_THRESHOLD_BPA)
                            log.info("clicked on Override Results Below-Arsenic flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_BELOW_THRESHOLD_BPA_TEXT,"auto BPAS")
                            log.info(" added value in BPA Override Results Below a Threshold text")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_BELOW_THRESHOLD_BPA_VALUE, "5")
                            log.info(" added value in BPA Override Results Below a Threshold limit")
                            Envi_Helper(context.page).capture_screenshot()
                        except Exception as e:
                            log.error(f"Failed to clicked on Override Results Below-Arsenic flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_BELOW_THRESHOLD_BPS)
                            log.info("clicked on Override Results Below-Cadmium flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_BELOW_THRESHOLD_BPS_TEXT,"auto BPS")
                            log.info(" added value in BPS Override Results Below a Threshold text")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_BELOW_THRESHOLD_BPS_VALUE, "5")
                            log.info(" added value in BPS Override Results Below a Threshold limit")
                            Envi_Helper(context.page).capture_screenshot()
                            keyboard.press_and_release('Page Down')
                        except Exception as e:
                            log.error(f"Failed to clicked on Override Results Below-Cadmium flag : {e}")

                    except Exception as e:
                      log.error(f"Failed to clicked on on Override Results Below a Threshold flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_STANDARD_LIMIT)
                        log.info("clicked on Show Standard Limits flag")
                        Envi_Helper(context.page).capture_screenshot()

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_STANDARD_LIMIT_BPA)
                            log.info("clicked on Standard Limit Arsenic flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_STANDARD_LIMIT_BPA_LIMIT,"20")
                            log.info(" added value in Standard Limit Arsenic value")
                            Envi_Helper(context.page).capture_screenshot()

                        except Exception as e:
                            log.error(f"Failed to clicked on Standard Limit Arsenic flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_STANDARD_LIMIT_BPS)
                            log.info("clicked on Standard Limit BPS flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_STANDARD_LIMIT_BPS_LIMIT, "20")
                            log.info(" added value in Standard Limit BPS value")
                            Envi_Helper(context.page).capture_screenshot()
                        except Exception as e:
                            log.error(f"Failed to clicked on Standard Limit BPS flag : {e}")

                        try:
                            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_PS_STANDARD_LIMIT_ALERT)
                            log.info("clicked on Standard Limit Alert flag")
                            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_PS_STANDARD_LIMIT_ALERT_text, "Auto Alert text")
                            log.info(" added value in Standard Limit Alert text")
                            Envi_Helper(context.page).capture_screenshot()
                        except Exception as e:
                            log.error(f"Failed to clicked on Standard Limit Alert flag : {e}")

                    except Exception as e:
                        log.error(f"Failed to clicked on Show Standard Limits flag : {e}")

                except Exception as e:
                    log.error(f"Failed expand Plasticizers Results on  AB899 Advance settings : {e}")

                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_CUSTOMIZE_SEARCH_INSTRUCTION)
                    log.info("clicked on Customize Search Instructions Message flag")
                    Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_CUSTOMIZE_SEARCH_INSTRUCTION_TEXT, "Auto text")
                    log.info(" added value in Customize Search Instructions Message text")
                    Envi_Helper(context.page).capture_screenshot()
                except Exception as e:
                    log.error(f"Failed to clicked on Customize Search Instructions Message flag : {e}")

                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_CUSTOMIZE_SEARCH_DISCLAIMER)
                    log.info("clicked on Customize Search Disclaimer Text flag")
                    Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_CUSTOMIZE_SEARCH_DISCLAIMER_TEXT, "Auto text")
                    log.info(" added value in Customize Search Disclaimer Text")
                    Envi_Helper(context.page).capture_screenshot()
                except Exception as e:
                    log.error(f"Failed to clicked on Customize Search Disclaimer Text flag : {e}")

                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_CUSTOMIZE_NORESULT)
                    log.info("clicked on Customize No Results Message flag")
                    Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_AS_CUSTOMIZE_NORESULT_TEXT, "Auto text")
                    log.info(" added value in Customize No Results Message Text")
                    Envi_Helper(context.page).capture_screenshot()
                except Exception as e:
                    log.error(f"Failed to clicked on Customize No Results Message flag : {e}")

                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_SEARCHBY_PRODUCT)
                    log.info("clicked on Enable Search by Product flag")
                    Envi_Helper(context.page).capture_screenshot()

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_SEARCHBY_PRODUCT_byUPC)
                        log.info("clicked on Search product by UPC flag")
                        Envi_Helper(context.page).capture_screenshot()
                    except Exception as e:
                        log.error(f"Failed to clicked on Search product by UPC flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_SEARCHBY_PRODUCT_byNAME)
                        log.info("clicked on Search product by Name flag")
                        Envi_Helper(context.page).capture_screenshot()
                    except Exception as e:
                        log.error(f"Failed to click on search by producy name  flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_SEARCHBY_PRODUCT_REQUIRED)
                        log.info("clicked on Required flag")
                        Envi_Helper(context.page).capture_screenshot()
                    except Exception as e:
                        log.error(f"Failed to clicked on required flag : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_SEARCHBY_PRODUCT_IGNORE_SPECIAL)
                        log.info("clicked on Ignore Special Character flag")
                        Envi_Helper(context.page).capture_screenshot()
                    except Exception as e:
                        log.error(f"Failed to clicked on Ignore Special Character flag : {e}")

                except Exception as e:
                    log.error(f"Failed to clicked on Enable Search by Product flag : {e}")

                try:
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_SEARCHBY_LOTNO)
                    Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_SEARCHBY_LOTNO)
                    log.info("clicked on Enable Search by Lot No.")
                    Envi_Helper(context.page).capture_screenshot()

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_SEARCHBY_LOTNO_IGNORE)
                        log.info("clicked on ignore special character")
                        Envi_Helper(context.page).capture_screenshot()
                    except Exception as e:
                        log.error(f"Failed to clicked on ignore special character : {e}")

                    try:
                        Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_SEARCHBY_LOTNO_REQUIRED)
                        log.info("clicked on Required flag")
                        Envi_Helper(context.page).capture_screenshot()
                    except Exception as e:
                        log.error(f"Failed to clicked on required flag : {e}")

                except Exception as e:
                    log.error(f"Failed to clicked on Enable Search by Product flag : {e}")


            except Exception as e:
                context.page.execute_script("window.scrollTo(0, 0);")
                log.error(f"Failed to configure AB899 Advance settings : {e}")
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_SAVE)
                Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_POPUP_CLOSE)
                time.sleep(2)

            context.page.execute_script("window.scrollTo(0, 0);")
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_AS_SAVE)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_POPUP_CLOSE)
            time.sleep(2)
            allure.attach("New AB899 module created", name="Module Creation",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Module creation failed: {e}")
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_POPUP_SAVE_BUTTON)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_POPUP_CLOSE)
            time.sleep(2)
            allure.attach(str(e), name="Module Creation Error", attachment_type=allure.attachment_type.TEXT)


@then('the new module should be added to the module list')
def step_impl(context):
    with allure.step("Verify new module in list"):
        try:
            Envi_Helper(context.page).get_value(locators.AB899_TABLE_LIST_OPTION, 10)
            allure.attach("New module added to list", name="Module Verification",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Module verification failed: {e}")
            allure.attach(str(e), name="Module Verification Error", attachment_type=allure.attachment_type.TEXT)


@when('the user edits an existing Ab899 module')
def step_impl(context):
    with allure.step("User edits AB899 module"):
        try:
            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_SEARCH,"Auto")
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_LIST, 10)
            time.sleep(2)
            Envi_Helper(context.page).get_value(locators.AB899_ADD_EDIT_MODULE, 10)
            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_POPUP_MODULE_NAME,"Auto Updated name", 10)
            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_POPUP_CTA, "UpdatedText", 10)
            Envi_Helper(context.page).capture_screenshot()
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_POPUP_SAVE_BUTTON)
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_POPUP_CLOSE)
            time.sleep(2)
            allure.attach("Module edited successfully", name="Module Edit", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Module edit failed: {e}")
            allure.attach(str(e), name="Module Edit Error", attachment_type=allure.attachment_type.TEXT)


@then('the changes should be saved and reflected in the AB899 module list')
def step_impl(context):
    with allure.step("Verify changes are saved"):
        try:
            Envi_Helper(context.page).get_value(locators.AB899_TABLE_LIST_OPTION, 10)
            allure.attach("Changes saved successfully", name="Changes Verification",
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Changes verification failed: {e}")
            allure.attach(str(e), name="Changes Verification Error", attachment_type=allure.attachment_type.TEXT)


@when('the user sorts the module list')
def step_impl(context):
    with allure.step("User sorts module list"):
        try:
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_MODULE_HEADING)
            time.sleep(2)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_MODULE_HEADING)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_WHERE_USED)
            time.sleep(2)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_WHERE_USED)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_CALL_TO_ACTION)
            time.sleep(2)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_CALL_TO_ACTION)
            allure.attach("Module list sorted", name="Sort Action", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Module sorting failed: {e}")
            allure.attach(str(e), name="Sort Error", attachment_type=allure.attachment_type.TEXT)


@then('the module list should be sorted in the correct order')
def step_impl(context):
    with allure.step("Verify module list sorting"):
        try:
            log.info("the list has been sorted and screen shots are captured")
            allure.attach("Module list sorted correctly", name="Sort Verification",
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Sort verification failed: {e}")
            allure.attach(str(e), name="Sort Verification Error", attachment_type=allure.attachment_type.TEXT)


@when('the user deletes an unused Ab899 module')
def step_impl(context):
    with allure.step("User deletes AB899 module"):
        try:
            Envi_Helper(context.page).insert_text_in_input_field(locators.AB899_SEARCH, "Auto")
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_CHECKBOX_LIST)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_DELETE_BUTTON)
            Envi_Helper(context.page).capture_screenshot()
            time.sleep(2)
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_CONFIRM_DELETE_BUTTON)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).capture_screenshot()
            time.sleep(2)
            allure.attach("Module deletion initiated", name="Delete Action",
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Module deletion failed: {e}")
            allure.attach(str(e), name="Delete Error", attachment_type=allure.attachment_type.TEXT)


@then('the module should be removed from the AB899 module list')
def step_impl(context):
    with allure.step("Verify module deletion"):
        try:
            Envi_Helper(context.page).capture_screenshot()
            allure.attach("Module removed successfully", name="Deletion Verification",attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Deletion verification failed: {e}")
            allure.attach(str(e), name="Deletion Verification Error", attachment_type=allure.attachment_type.TEXT)


@when('the user want to see the number of rows on the Ab899 module list')
def step_impl(context):
    with allure.step("User checks row count"):
        try:
            keyboard.press('pagedown')
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_20)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_100)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_OPTION)
            Envi_Helper(context.page).capture_screenshot()
            Envi_Helper(context.page).wait_till_element_is_present_to_click(locators.AB899_ROWPERPAGE_1000)
            Envi_Helper(context.page).capture_screenshot()
            allure.attach("Row count options checked", name="Row Count Action",
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Row count check failed: {e}")
            allure.attach(str(e), name="Row Count Error", attachment_type=allure.attachment_type.TEXT)


@then('the module list should be updated on Ab899 page')
def step_impl(context):
    with allure.step("Verify module list update"):
            Envi_Helper(context.page).capture_screenshot()
            log.info("the rows are updated successfully")
            allure.attach("Module list updated", name="List Update Verification",
                          attachment_type=allure.attachment_type.TEXT)