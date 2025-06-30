
# from behave import Given,when,then
# from Locators import locators
# from Logs import logs_file
# from Helper.enviHelper import Envi_Helper
# from TestData import Test_Data
# import time
#
# @Given('user is on the login page')
# def step_impl(context):
#     # context.driver.get('https://staging.brij.it/')
#     Envi_Helper(context.driver).open_page(Test_Data.Brij_url)
#     time.sleep(2)
#
# @when('user input invalid email id "{invalid_login_id}"')
# def step_impl(context,invalid_login_id):
#     Envi_Helper(context.driver).insert_text_in_input_field(locators.USERNAME_INPUT, invalid_login_id)
#
# @when('user entered valid email id "{valid_login_id}"')
# def step_impl(context,valid_login_id):
#         Envi_Helper(context.driver).insert_text_in_input_field(locators.USERNAME_INPUT, valid_login_id)
#         context.driver.clear()
#
# @when('user enter invalid password "{invalid_password}"')
# def step_impl(context,invalid_password,login_id):
#     Envi_Helper(context.driver).insert_text_in_input_field(locators.USERNAME_INPUT, login_id)
#     Envi_Helper(context.driver).click(locators.LOGIN_BUTTON)
#     time.sleep(2)
#     Envi_Helper(context.driver).insert_text_in_input_field(locators.PASSWORD_INPUT,invalid_password)
#
# @when(u'user entered correct email id "<login_id>" and password "<password>"')
# def step_impl(context,login_id,password):
#     Envi_Helper(context.driver).insert_text_in_input_field(locators.USERNAME_INPUT, login_id)
#     Envi_Helper(context.driver).click(locators.USERNAME_SIGNIN)
#     time.sleep(2)
#     Envi_Helper(context.driver).insert_text_in_input_field(locators.PASSWORD_INPUT,password)
#
# @then('user should see an error message')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.LOGIN_BUTTON)
#     time.sleep(2)
#     Envi_Helper(context.driver).get_toast_message(locators.toast_message)
#
# @then('user should navigate to password screen')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.LOGIN_BUTTON)
#     time.sleep(2)
#
# @then ('user should be logged in successfully')
# def step_impl(context):
#     Envi_Helper(context.driver).click(locators.LOGIN_BUTTON)
#     Envi_Helper(context.driver).wait_till_element_is_present(locators.analytics_general_dashboard,10)
#     context.driver.quit()
#
