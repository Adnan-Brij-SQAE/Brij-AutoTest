Feature: Test Warranty Module Page


  @allure.feature.WarrantyModule @navigation
  Scenario: Verify navigation to the Warranty Module page
    When the user navigates to the Warranty Module page
    Then the Warranty Module page should be displayed

  @allure.feature.WarrantyModule @ui-elements
  Scenario: Verify the notification button on the Warranty Module page
    Then the user can access the notification button on the Warranty Module page

  @allure.feature.WarrantyModule @ui-elements
  Scenario: Verify the logout button on the Warranty Module page
    Then the user can access the logout button on the Warranty Module page

  @allure.feature.WarrantyModule @ui-elements
  Scenario: Verify the Fields button on the Warranty Module page
    When the user can access the Fields button on the Warranty Module page
    Then the user can access the Warranty Name field on the Warranty Module page
    Then the user can access the Where Used field on the Warranty Module page
    Then the user can access the Warranty Duration field on the Warranty Module page
    Then the user can access the Call to Action field on the Warranty Module page

  @allure.feature.WarrantyModule @sort
  Scenario: Verify sorting functionality on the Warranty Module page
    When the user sorts the table on the Warranty Module page
    Then the table should be sorted in the correct order on the Warranty Module page

  @allure.feature.WarrantyModule @create-module
  Scenario: Verify creation of a new Warranty module
    When the user creates a new Warranty module
    Then the new Warranty module should be added to the module list

  @allure.feature.WarrantyModule @duplicate-module
  Scenario: Verify duplication of an existing Warranty module
    When the user duplicates an existing Warranty module
    Then the changes should be saved and reflected in the Warranty module list

  @allure.feature.WarrantyModule @edit-module
  Scenario: Verify editing of an existing Warranty module
    When the user edits an existing Warranty module
    Then the changes should be saved and reflected in the Warranty module list

  @allure.feature.WarrantyModule @checkboxes
  Scenario: Verify checkbox functionality on the Warranty Module page
    When the user selects all checkboxes on the Warranty Module page
    Then all checkboxes should be selected on the Warranty Module page

  @allure.feature.WARRANTYModule @pagination
  Scenario: Verify pagination functionality on the WARRANTY
    When the user want to see the number of rows on the WARRANTY module list
    Then the module list should be updated on WARRANTY page

  @allure.feature.WarrantyModule @delete-module
  Scenario: Verify deletion of an unused Warranty module
    When the user deletes an unused Warranty module
    When the user deletes more than one unused Warranty module

  @allure.feature.WarrantyModule @search
  Scenario: Verify search functionality on the Warranty Module page
    When the user uses the search feature to search between the Warranty modules
    Then the search results should be displayed correctly on the Warranty Module page