Feature: Test Ab899 Module page

  @allure.feature.Ab899Module @navigation
  Scenario: Verify navigation to the Ab899 page
    When the user navigates to the Ab899 page
    Then the Ab899 page should be displayed

  @allure.feature.Ab899Module @ui-elements
  Scenario: Verify Notification button on the Ab899 page
    Then the user can access the notification button on the Ab899 module page

  @allure.feature.Ab899Module @ui-elements
  Scenario: Verify Logout Button on the Ab899 page
    And the user can access the logout button on the Ab899 module page

  @allure.feature.Ab899Module @ui-elements
  Scenario: Verify Field Button on the Ab899 page
    And the user can access the field button on the Ab899 module page

  @allure.feature.Ab899Module @checkboxes
  Scenario: Verify checkbox functionality on the Ab899 page
    When the user selects all AB899 checkboxes
    Then all checkboxes should be selected on Ab899

  @allure.feature.Ab899Module @sort
  Scenario: Verify sorting functionality on the Ab899 page
    When the user sorts the module list
    Then the module list should be sorted in the correct order

  @allure.feature.Ab899Module @pagination
  Scenario: Verify pagination functionality on the Ab899 page
    When the user want to see the number of rows on the Ab899 module list
    Then the module list should be updated on Ab899 page

  @allure.feature.Ab899Module @create-module
  Scenario: Verify creation of a new AB 899 module
    When the user creates a new AB 899 module
    Then the new module should be added to the module list

  @allure.feature.Ab899Module @edit-module
  Scenario: Verify editing of an existing Ab899 module
    When the user edits an existing Ab899 module
    Then the changes should be saved and reflected in the AB899 module list

  @allure.feature.Ab899Module @delete-module
  Scenario: Verify deletion of an unused Ab899 module
    When the user deletes an unused Ab899 module
    Then the module should be removed from the AB899 module list

  @allure.feature.Ab899Module @search
  Scenario: Verify search functionality on the Ab899 page
    When the user uses the search feature to search for a module
    Then the searched results should be displayed correctly

