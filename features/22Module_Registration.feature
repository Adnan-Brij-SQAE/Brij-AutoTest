@allure.feature.RegistrationModule @story_navigation
Feature: Test Registration Module Page

@allure.feature.RegistrationModule @story_navigation
Scenario: Verify navigation to Registration Module page
  When the user navigates to the Registration Module page

@allure.feature.RegistrationModule @story_ui_elements
Scenario: Verify access to notification button on Registration Module
  Then the user can access the notification button on the Registration Module page

@allure.feature.RegistrationModule @story_ui_elements
Scenario: Verify access to logout button on Registration Module
  Then the user can access the logout button on the Registration Module page

@allure.feature.RegistrationModule @story_ui_elements
Scenario: Verify access to field button on Registration Module
  Then the user can access the field button on the Registration Module page

@allure.feature.RegistrationModule @story_ui_elements
Scenario: Verify show/hide of Configuration name field on Registration Module
  Then the user should be able to show/hide configuration name field

@allure.feature.RegistrationModule @story_ui_elements
Scenario: Verify show/hide of Where used field on Registration Module
  Then the Where used field should be visible when enabled on the Registration Module page

Scenario: Verify all checkbox selection on Registration Module
  Then the user selects the All checkbox on the Registration Module page

@allure.feature.RegistrationModule @story_table_operations
Scenario: Verify table sorting functionality on Registration Module page
  When the user sorts the table on the Registration Module page
  Then the modules should be sorted on the Registration Module page

@allure.feature.RegistrationModule @story_crud_operations
Scenario: Create a new Registration Module
  When the user creates a new Registration Module
  Then the new Registration Module should be displayed in the module list

@allure.feature.RegistrationModule @story_crud_operations
Scenario: Edit an existing Registration Module
  When the user edits an existing Registration Module
  Then the changes should be reflected in the module list

@allure.feature.RegistrationModule @story_crud_operations
Scenario: Duplicate an existing Registration Module
  When the user duplicates an existing Registration Module
  Then the changes should be reflected in the module list

@allure.feature.RegistrationModule @story_crud_operations
Scenario: Delete an unused Registration Module
  When the user deletes an unused Registration Module
  Then the deleted Registration Module should be removed from the module list

  @allure.feature.RegistrationModule @story_crud_operations
  Scenario: Delete multiple Registration Modules
    When the user selects more than one Registration Module and deletes them
    Then the deleted Registration Module should be removed from the module list

@allure.feature.RegistrationModule @story_search_functionality
Scenario: Verify search feature for Registration Modules
  When the user uses the search feature to find a Registration Module
  Then only matching Registration Modules should be displayed
