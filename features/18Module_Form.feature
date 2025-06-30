Feature: Test Form Module Page

  @allure.feature.FormModule @navigation
  Scenario: Verify navigation to the Form Module page
    When the user navigates to the Form Module page
    Then the Form Module page should be displayed

  @allure.feature.FormModule @ui-elements
  Scenario: Verify UI elements on the Form Module page
    Then the user can access the notification button on the Form Module page
    And the user can access the logout button on the Form Module page
    And the user can access the field button on the Form Module page

  @allure.feature.FormModule @create-module
  Scenario: Verify creation of a new Form module
    When the user creates a new Form module
    Then the new Form module should be added to the module list

  @allure.feature.FormModule @checkboxes
  Scenario: Verify checkbox functionality on the Form Module page
    When the user selects all checkboxes on the Form Module page
    Then all checkboxes should be selected on the Form Module page

  @allure.feature.FormModule @search
  Scenario: Verify search functionality on the Form Module page
    When the user uses the search feature to search between the Form modules
    Then the search results should be displayed correctly on the Form Module page

  @allure.feature.FormModule @sort
  Scenario: Verify sorting functionality on the Form Module page
    When the user sorts the table on the Form Module page
    Then the table should be sorted in the correct order on the Form Module page


  @allure.feature.FormModule @edit-module
  Scenario: Verify editing of an existing Form module
    When the user edits an existing Form module
    Then the changes should be saved and reflected in the Form module list

  @allure.feature.FormModule @delete-module
  Scenario: Verify deletion of an unused Form module
    When the user deletes an unused Form module
    Then the module should be removed from the Form module list

  @allure.feature.FORMModule @pagination
  Scenario: Verify pagination functionality on the FORM
    When the user want to see the number of rows on the FORM module list
    Then the module list should be updated on FORM page
#
#
#
##Feature: Test Form Module page
##  Scenario: Form Module page testing
##    When the user should be navigated to the Form Module page
##    Then the user can access the notification button on Form Module page
##    And the user can access the logout button on Form Module page
##    And the user can access the field button on Form Module page
##    And the user can select All checkbox on Form Module page
##    And the user use search feature to search between the modules on Form Module page
##    And the user can sort the table on Form Module page
##    And the user can create new Form module from on Form Module page
##    And the user can edit the previous Form module on Form Module page
##    And the user can delete the unused Form module on Form Module pahge