Feature: Test Document Module Page
  As a user
  I want to interact with the Document Module page
  So that I can manage Document modules effectively

  @allure.feature.DocumentModule @navigation
  Scenario: Verify navigation to the Document Module page
    When the user navigates to the Document Module page
    Then the Document Module page should be displayed

  @allure.feature.DocumentModule @notification-button
  Scenario: Verify notification button on the Document Module page
    Then the user can access the notification button on the Document Module page

  @allure.feature.DocumentModule @logout-button
  Scenario: Verify logout button on the Document Module page
    Then the user can access the logout button on the Document Module page

  @allure.feature.DocumentModule @field-button
  Scenario: Verify field button on the Document Module page
    Then the user can access the field button on the Document Module page

  @allure.feature.DocumentModule @checkboxes
  Scenario: Verify checkbox functionality on the Document Module page
    When the user selects all checkboxes on Document Module page
    Then all checkboxes should be selected on Document Module page

  @allure.feature.DocumentModule @create-module
  Scenario: Verify creation of a new Document module
    When the user creates a new Document module
    Then the changes should be made with the updated Document module list

  @allure.feature.DocumentModule @duplicate_module
  Scenario: Verify duplicating an existing Document module
    When the user duplicates an existing Document module
    Then the changes should be made with the updated Document module list

  @allure.feature.DocumentModule @edit-module
  Scenario: Verify editing of an existing Document module
    When the user edits an existing Document module
    Then the changes should be made with the updated Document module list

   @allure.feature.DocumentModule @sort
  Scenario: Verify sorting functionality on the Document Module page
    When the user sorts the table on Document Module page
    Then the table should be sorted in the correct order on Document Module page

  @allure.feature.DOCUMENTModule @pagination
  Scenario: Verify pagination functionality on the DOCUMENT
    When the user want to see the number of rows on the DOCUMENT module list
    Then the changes should be made with the updated Document module list

  @allure.feature.DocumentModule @delete-module
  Scenario: Verify deletion of an unused Document module
    When the user deletes an unused Document module
    Then the user deletes more than one unused Document module

      @allure.feature.DocumentModule @search
  Scenario: Verify search functionality on the Document Module page
    When the user uses the search feature to search between the document modules
    Then the search results should be displayed correctly on document page