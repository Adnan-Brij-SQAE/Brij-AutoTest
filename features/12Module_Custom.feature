Feature: Test Custom Module Page

  @allure.feature.CustomModule @navigation
  Scenario: Verify navigation to the Custom Module page
    When the user navigates to the Custom Module page
    Then the Custom Module page should be displayed

  @allure.feature.CustomModule @notification
  Scenario: Verify the notification button on the Custom Module page
    Then the user should see the notification button on the Custom Module page

  @allure.feature.CustomModule @logout
  Scenario: Verify the logout button on the Custom Module page
    Then the user should see the logout button on the Custom Module page

  @allure.feature.CustomModule @field_button
  Scenario: Verify the field button options on the Custom Module page
    Then the user should see the field button on the Custom Module page
    And the user should see the Module Name option on the field button
    And the user should see the Where Used option on the field button
    And the user should see the Call to Action option on the field button

  @allure.feature.CustomModule @checkboxes
  Scenario: Verify checkbox selection functionality on the Custom Module page
    When the user selects all checkboxes on the Custom Module page
    Then all checkboxes should be selected on the Custom Module page

  @allure.feature.CustomModule @create_module
  Scenario: Verify creating a new Custom module
    When the user creates a new Custom module
    Then the new Custom module should appear in the module list

  @allure.feature.CustomModule @duplicate_module
  Scenario: Verify duplicating an existing Custom module
    When the user duplicates an existing Custom module
    Then the changes should be made with the updated custom module

  @allure.feature.CustomModule @edit_module
  Scenario: Verify editing an existing Custom module
    When the user edits an existing Custom module
    Then the changes should be made with the updated custom module

  @allure.feature.CustomModule @sort
  Scenario: Verify sorting functionality on the Custom Module page
    When the user sorts the table data
    Then the table data should be sorted correctly

  @allure.feature.CustomModule @pagination
  Scenario: Verify pagination functionality on the Custom Module page
    When the user changes the number of rows displayed on the module list
    Then the module list should update to reflect the selected number of rows

  @allure.feature.CustomModule @delete_module
  Scenario: Verify deletion of unused Custom modules
    When the user deletes unused Custom modules
    Then the user deletes more than one unused Custom module

  @allure.feature.CustomModule @search
  Scenario: Verify search functionality on the Custom Module page
    When the user searches for a Custom module
    Then the search results should display the matching Custom modules


