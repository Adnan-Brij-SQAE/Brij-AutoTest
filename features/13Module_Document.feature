Feature: Test Document Module Page
  As a user
  I want to interact with the Document Module page
  So that I can manage Document modules effectively

  @allure.feature.DocumentModule @navigation
  Scenario: Verify navigation to the Document Module page
    When the user navigates to the Document Module page
    Then the Document Module page should be displayed

  @allure.feature.DocumentModule @ui-elements
  Scenario: Verify UI elements on the Document Module page
    Then the user can access the notification button on the Document Module page
    And the user can access the logout button on the Document Module page
    And the user can access the field button on the Document Module page

  @allure.feature.DocumentModule @checkboxes
  Scenario: Verify checkbox functionality on the Document Module page
    When the user selects all checkboxes on Document Module page
    Then all checkboxes should be selected on Document Module page

  @allure.feature.DocumentModule @sort
  Scenario: Verify sorting functionality on the Document Module page
    When the user sorts the table on Document Module page
    Then the table should be sorted in the correct order on Document Module page

  @allure.feature.DocumentModule @create-module
  Scenario: Verify creation of a new Document module
    When the user creates a new Document module
    Then the new Document module should be added to the module list

  @allure.feature.DocumentModule @edit-module
  Scenario: Verify editing of an existing Document module
    When the user edits an existing Document module
    Then the changes should be saved and reflected in the module list on Document Module page

  @allure.feature.DocumentModule @search
  Scenario: Verify search functionality on the Document Module page
    When the user uses the search feature to search between the document modules
    Then the search results should be displayed correctly on document page

  @allure.feature.DocumentModule @delete-module
  Scenario: Verify deletion of an unused Document module
    When the user deletes an unused Document module
    Then the module should be removed from the module list on Document Module page


  @allure.feature.DOCUMENTModule @pagination
  Scenario: Verify pagination functionality on the DOCUMENT
    When the user want to see the number of rows on the DOCUMENT module list
    Then the module list should be updated on DOCUMENT page
#
#
#
#
#
##
##Feature: Test Document Module page
##  Scenario: Document Module page testing
##    When the user navigate to the Document Module page
##    Then the user can access the field button on Document Module page
##    And the user can select All checkbox on Document Module page
##    And the user use search feature to search between the modules on Document Module page
##    And the user can sort the table on Document Module page
##    And the user can create new document module from on Document Module page
##    And the user can edit the previous document module on Document Module page
##    And the user can access the notification button on Document Module page
##    And the user can access the logout button on Document Module page
##    And the user can delete the unused document module on Document Module page