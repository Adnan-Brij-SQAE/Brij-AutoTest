Feature: Test Review Module Page

  @allure.feature.ReviewModule @navigation @severity.blocker
  Scenario: Verify navigation to the Review Module page
    When the user navigates to the Review Module page
    Then the Review Module page should be displayed

  @allure.feature.ReviewModule @notification @severity.critical
  Scenario: Verify notification button on the Review Module page
    Then the user can access the notification button on the Review Module page

  @allure.feature.ReviewModule @logout @severity.critical
  Scenario: Verify logout button on the Review Module page
    Then the user can access the logout button on the Review Module page

  @allure.feature.ReviewModule @field-button @severity.critical
  Scenario: Verify field button on the Review Module page
    Then the user can access the field button on the Review Module page
    And the user should select Module Name option on the field button on the Review Module page
    And the user should select the Where Used option on the field button on the Review Module page
    And the user should select the Call to Action option on the field button on the Review Module page

  @allure.feature.ReviewModule @checkboxes @severity.normal
  Scenario: Verify checkbox functionality on the Review Module page
    When the user selects all checkboxes on the Review Module page
    Then all checkboxes should be selected on the Review Module page

  @allure.feature.ReviewModule @sort @severity.normal
  Scenario: Verify sorting functionality on the Review Module page
    When the user sorts the table on the Review Module page
    Then the changes should be saved and reflected in the Review module list

  @allure.feature.ReviewModule @create-module @severity.blocker
  Scenario: Verify creation of a new Review module
    When the user creates a new Review module
    Then the changes should be saved and reflected in the Review module list

  @allure.feature.ReviewModule @create-module @severity.blocker
  Scenario: Verify creation of a new Review module
    When the user creates a new Review module with properties and validations
    Then the changes should be saved and reflected in the Review module list
#
  @allure.feature.ReviewModule @duplicate-module @severity.critical
  Scenario: Verify duplicating of an existing Review module
    When the user duplicates an existing Review module
    Then the changes should be saved and reflected in the Review module list

  @allure.feature.ReviewModule @edit-module @severity.critical
  Scenario: Verify editing of an existing Review module
    When the user edits an existing Review module
    Then the changes should be saved and reflected in the Review module list

  @allure.feature.ReviewModule @pagination @severity.normal
  Scenario: Verify pagination functionality on the Review Module
    When the user wants to see the number of rows on the Review Module list
    Then the module list should be updated on Review Module page

  @allure.feature.ReviewModule @delete-module @severity.critical
  Scenario: Verify deletion of an unused Review module
    When the user deletes an unused Review module
    Then the user deletes more than one unused Review module

  @allure.feature.ReviewModule @search @severity.normal
  Scenario: Verify search functionality on the Review Module page
    When the user uses the search feature to search between the Review modules
    Then the search results should be displayed correctly on the Review Module page

