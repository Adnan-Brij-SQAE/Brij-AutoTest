Feature: Test Rebate Signup page

@allure.feature.RebateSignupPage @rebate_signup_module @allure.severity:blocker
Scenario: Navigate to Rebate Signup Page Module
  When the user navigate to the Rebate Signup Page Module page
#
@allure.feature.RebateSignupPage @notification @allure.severity:normal
Scenario: Access Notification Button on Rebate Signup Page Module page
  Then the user can access the notification button on Rebate Signup Page Module page

@allure.feature.RebateSignupPage @logout @allure.severity:normal
Scenario: Access Logout Button on Rebate Signup Page Module page
  Then the user can access the logout button on Rebate Signup Page Module page

@allure.feature.RebateSignupPage @field @allure.severity:normal
Scenario: Access Field Button on Rebate Signup Page Module page
  Then the user can access the field button on Rebate Signup Page Module page

@allure.feature.RebateSignupPage @AllCheckboxes @allure.severity:normal
Scenario: Select All Checkbox on Rebate Signup Page Module page
  Then the user can select All checkbox on Rebate Signup Page Module page

@allure.feature.RebateSignupPage @Sorting @allure.severity:normal
Scenario: Sort Table on Rebate Signup Page Module page
  Then the user can sort the table on Rebate Signup Page Module page

@allure.feature.RebateSignupPage @pagination @allure.severity:normal
  Scenario: Verify pagination functionality on the Rebate signup Page
    Then the user want to see the number of rows on Rebate Signup Page

@allure.feature.RebateSignupPage @AddModule @allure.severity:critical
Scenario: Create New Rebate Signup Module
  When the user create new Rebate Signup module
  Then the new rebate signup page should appear in list

@allure.feature.RebateSignupPage @EditModule @allure.severity:critical
Scenario: Edit Existing Rebate Signup Module
  Then the user can edit the previous Rebate Signup module

@allure.feature.RebateSignupPage @Duplicate @allure.severity:normal
Scenario: Test functionality duplicate Rebate Signup Page
  Then the user can create duplicate Rebate Signup page

@allure.feature.RebateSignupPage @Delete @allure.severity:critical
Scenario: Delete Rebate Signup Module
  Then the user can delete the unused Rebate Signup module
  Then the user can delete more than one unused Rebate Signup module

@allure.feature.RebateSignupPage @Search @allure.severity:critical
Scenario: Use Search Feature on Rebate Signup Page Module page
  Then the user can search between Rebate Signup Module