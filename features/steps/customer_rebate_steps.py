import keyboard
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators import locators
from Helper.enviHelper import Envi_Helper
from Logs import logs_file
import time
log = logs_file.get_logs()



@when(u'The user is on the Customer Rebate page')
def step_impl(context):
    analytics_menu = context.driver.find_element(By.XPATH, "//span[normalize-space()='Analytics']")
    actions = ActionChains(context.driver)
    actions.move_to_element(analytics_menu).perform()
    cus_option = context.driver.find_element(By.XPATH, "// span[normalize-space()='Customers']")
    cus_option.click()
    rebate_option = context.driver.find_element(By.XPATH, "//li[@class='has-subnav ng-star-inserted is-active']//li[@class='pl-0 is-not-active']")
    rebate_option.click()
    time.sleep(2)
    Envi_Helper.__enter__(context, 'Esc')
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//h6[normalize-space()='Total Rebates']")
    log.info("user is on the rebate page")

@then(u'the user can access Experience dropdown on Rebate page')
def step_impl(context):
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_EXPERIENCE_FILTER,10)
    Envi_Helper(context.driver).insert_text_in_input_field(locators.REBATE_EXPERIENCE_FILTER_SEARCH,"test",10)
    Envi_Helper.capture_screenshot()
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_EXPERIENCE_FILTER_CLOSE)
    time.sleep(2)

@then(u'the user can access Rebate status dropdown')
def step_impl(context):
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_REBATE_STATUS_FILTER,10)
    Envi_Helper(context.driver).insert_text_in_input_field(locators.REBATE_EXPERIENCE_FILTER_SEARCH,"paid",10)
    Envi_Helper.capture_screenshot()
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_FILTER_PAID)
    Envi_Helper.capture_screenshot()
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_FILTER_PAID)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_EXPERIENCE_FILTER_CLOSE)
    time.sleep(2)

@then(u'the user can search between the rebates')
def step_impl(context):
    Envi_Helper(context.driver).insert_text_in_input_field (locators.REBATE_REBATE_SEARCH_BAR, "sqa",10)
    Envi_Helper.capture_screenshot()
    context.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Items...']").clear()
    time.sleep(3)

@then(u'the user can open rebate popup')
def step_impl(context):
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_ICON)
    Envi_Helper.capture_screenshot()
    log.info("user is able to open the rebate popup")
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_POPUP_CUSTOMER_DETAIL)
    Envi_Helper.capture_screenshot()
    log.info("user is able to expand customer detail")
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_POPUP_CUSTOMER_DETAIL)
    keyboard.press_and_release('pagedown')
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_POPUP_REBATE_DETAIL)
    Envi_Helper.capture_screenshot()
    log.info("user is able to expand Rebate detail")
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_POPUP_REBATE_DETAIL)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_POPUP_RECEIPT_DETAIL)
    keyboard.press_and_release('pagedown')
    Envi_Helper.capture_screenshot()
    log.info("user is able to expand registration detail")
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_POPUP_RECEIPT_DETAIL)
    keyboard.press('Esc')
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_POPUP_CLOSE,10)
    time.sleep(2)

@then(u'the user can export rebates')
def step_impl(context):
    Envi_Helper(context.driver).click(locators.REBATE_EXPORT_BUTTON)
    Envi_Helper.capture_screenshot()
    time.sleep(2)

@then(u'the user can sort the rebate table on Rebate page')
def step_impl(context):
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_CUSTOMER_NAME_HEADING, 10)
    time.sleep(2)
    log.info("customer sorting is working  ")
    Envi_Helper.capture_screenshot()
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_REBATE_DATE_HEADING, 10)
    time.sleep(2)
    log.info("REBATE DATE sorting is working  ")
    Envi_Helper.capture_screenshot()
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_REG_STATUS_HEADING, 10)
    time.sleep(2)
    log.info("REBATE DATE sorting is working  ")
    Envi_Helper.capture_screenshot()

@then(u'user can access notification on rebate page')
def step_impl(context):
    Envi_Helper(context.driver).click(locators.NOTIFICATION_ICON)
    log.info("user is able to access the notification button ")
    Envi_Helper.capture_screenshot()
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON_2)
    time.sleep(2)

@then(u'user can logout from rebate page')
def step_impl(context):
    Envi_Helper(context.driver).click(locators.LOGOUT_BUTTON)
    Envi_Helper.capture_screenshot()
    log.info("user is able to access the logout button ")

@then(u'user can edit rebate')
def step_impl(context):
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_LIST_KEBAB_MENU,10)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_LIST_EDIT,10)
    log.info("user is able to edit rebate from popup ")
    time.sleep(2)
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_POPUP_CLOSE, 10)
    time.sleep(2)


@then(u'user can select all rebate')
def step_impl(context):
    Envi_Helper(context.driver).click(locators.REBATE_SELECT_ALL_CHECKBOX)
    time.sleep(2)
    Envi_Helper(context.driver).click(locators.REBATE_SELECT_ALL_CHECKBOX)


@then(u'user can click on field button on Rebate page')
def step_impl(context):
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_FIELDS_BUTTON)
    time.sleep(2)

@then(u'user can switch between the customer view and rebate view')
def step_impl(context):
    Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.REBATE_SWITCHER_BUTTON)
    time.sleep(2)




# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # #
# # # #
# # # # @given(u'The user is on brij platform')
# # # # def step_impl(context):
# # # #      Envi_Helper(context.driver).open_page(Test_Data.Brij_url)
# # # #      time.sleep(2)
# # # #
# # # # @when('The user entered valid email id "{login_id}" and password "{password}"')
# # # # def step_impl(context,login_id,password):
# # # #     Envi_Helper(context.driver).insert_text_in_input_field(locators.USERNAME_INPUT, login_id)
# # # #     Envi_Helper(context.driver).click(locators.USERNAME_SIGNIN)
# # # #     time.sleep(2)
# # # #     Envi_Helper(context.driver).insert_text_in_input_field(locators.PASSWORD_INPUT,password)
# # # #
# # #  # @when(u'the user clicks the login button')
# # # # def step_impl(context):
# # # #     Envi_Helper(context.driver).click(locators.LOGIN_BUTTON)
# # # #     time.sleep(2)
# # # #
# # # # @then(u'The user should logged in and navigate to Customer Registration page')
# # # # def step_impl(context):
# # # #     Envi_Helper(context.driver).wait_till_element_is_present(locators.analytics_general_dashboard)
# # # #     print("on dashboard")
# # # #     time.sleep(5)
# # # #     Envi_Helper(context.driver).hover_to_element_to_click(locators.LEFT_PANEL)
# # # #     time.sleep(2)
# # # #     print("on dashboaroooooooood")
# # # #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_OPTION)
# # # #     print("option clicked")
# # # #     Envi_Helper.__enter__(context,'Esc')
# # # #     Envi_Helper(context.driver).wait_till_element_is_present(locators.CUSTOMER_REGISTRATION_TITLE,10)
# # # #     time.sleep(2)
# # # #
# # # # @then(u'the user should access the notification button')
# # # # def step_impl(context):
# # # #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.NOTIFICATION_ICON, 10)
# # # #     time.sleep(2)
# # # #
# # # #
# # # # @then(u'the user should access the logout button dropdown')
# # # # def step_impl(context):
# # # #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.LOGOUT_BUTTON, 10)
# # # #     time.sleep(2)
# # # #
# # # # @then(u'the user should get the customer count')
# # # # def step_impl(context):
# # # #     Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.CUSTOMER_COUNT, 10)
# # # #     time.sleep(2)
# # # #
# # # #
# # # # @then(u'the user can search within the customer')
# # # # def step_impl(context):
# # # #     Envi_Helper(context.driver).insert_text_in_input_field(locators.CUSTOMER_SEARCH_BAR,"Adnan")
# # # #     time.sleep(4)