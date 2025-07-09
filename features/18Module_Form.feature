Feature: Test Form Module Page

  @allure.feature.FormModule @navigation @severity.blocker
  Scenario: Verify navigation to the Form Module page
    When the user navigates to the Form Module page
    Then the Form Module page should be displayed

  @allure.feature.FormModule @notification @severity.critical
  Scenario: Verify notification button on the Form Module page
    Then the user can access the notification button on the Form Module page

  @allure.feature.FormModule @logout @severity.critical
  Scenario: Verify logout button on the Form Module page
    Then the user can access the logout button on the Form Module page

  @allure.feature.FormModule @field-button @severity.critical
  Scenario: Verify field button on the Form Module page
    Then the user can access the field button on the Form Module page
    And the user should select Module Name option on the field button on the Form Module page
    And the user should select the Where Used option on the field button on the Form Module page
    And the user should select the Call to Action option on the field button on the Form Module page

  @allure.feature.FormModule @checkboxes @severity.normal
  Scenario: Verify checkbox functionality on the Form Module page
    When the user selects all checkboxes on the Form Module page
    Then all checkboxes should be selected on the Form Module page

  @allure.feature.FormModule @sort @severity.normal
  Scenario: Verify sorting functionality on the Form Module page
    When the user sorts the table on the Form Module page
    Then the changes should be saved and reflected in the Form module list

  @allure.feature.FormModule @create-module @severity.blocker
  Scenario: Verify creation of a new Form module
    When the user creates a new Form module
    Then the changes should be saved and reflected in the Form module list

  @allure.feature.FormModule @create-module @severity.blocker
  Scenario: Verify creation of a new Form module
    When the user creates a new Form module with properties and validation
    Then the changes should be saved and reflected in the Form module list
#
  @allure.feature.FormModule @duplicate-module @severity.critical
  Scenario: Verify duplicating of an existing Form module
    When the user duplicates an existing Form module
    Then the changes should be saved and reflected in the Form module list

  @allure.feature.FormModule @edit-module @severity.critical
  Scenario: Verify editing of an existing Form module
    When the user edits an existing Form module
    Then the changes should be saved and reflected in the Form module list

  @allure.feature.FormModule @pagination @severity.normal
  Scenario: Verify pagination functionality on the Form Module
    When the user wants to see the number of rows on the Form Module list
    Then the module list should be updated on Form Module page

  @allure.feature.FormModule @delete-module @severity.critical
  Scenario: Verify deletion of an unused Form module
    When the user deletes an unused Form module
    Then the user deletes more than one unused Form module

  @allure.feature.FormModule @search @severity.normal
  Scenario: Verify search functionality on the Form Module page
    When the user uses the search feature to search between the Form modules
    Then the search results should be displayed correctly on the Form Module page

