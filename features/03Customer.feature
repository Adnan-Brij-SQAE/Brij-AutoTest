Feature: Customer Registration page
  @customer_page
  @allure.feature.CustomerRegistration @navigation
  Scenario: test customer page
    When the user navigate to Customer Registration page

  @allure.feature.CustomerExperienceDropdown @customer_page  @allure.severity:high
  Scenario: Test Experience Dropdown on Customer page
    Then the user can access Experience dropdown on Customer page
    And the data should be filtered accordingly

  @allure.feature.CustomerVariantDropdown @customer_page  @allure.severity:high
  Scenario: Test Variant Dropdown on Customer page
    Then the user can access Variant dropdown on Customer page
    And the data should be filtered accordingly

  @allure.feature.CustomerStatusDropdown @customer_page  @allure.severity:high
  Scenario: Test Registration Status Dropdown on Customer page
    Then the user can access registration status dropdown on Customer page
    And the data should be filtered accordingly

  @allure.feature.CustomerSourceDropdown @customer_page  @allure.severity:high
  Scenario: Test Customer Source Dropdown on Customer page
    Then the user can access customer source dropdown on Customer page
    And the data should be filtered accordingly

  @story:Search @severity:critical
  @allure.feature.CustomerRegistration @search
  Scenario: Search functionality on Customer Registration page
    Then the user can search within the customer on Customer page

  @allure.feature.CustomerRegistration @table-elements @field-button
  Scenario: Verify field button click functionality on Customer Page
    Then the user can click on field button on Customer page

  @allure.feature.CustomerRegistration @table-elements @checkboxes
  Scenario: Verify bulk checkbox selection on Customer Page
    Then the user can check all check boxes on Customer page

  @allure.feature.CustomerRegistration @customer-popup @open-popup
  Scenario: Verify customer popup opening on Customer Page
    Then open customer popup on Customer page

  @allure.feature.CustomerRegistration @customer-popup @expand-registration
  Scenario: Verify registration expansion on Customer Page
   Then user can expand the customer registrations on Customer page

  @allure.feature.CustomerRegistration @customer-popup @registration-popup
  Scenario: Verify registration popup opening on Customer Page
   Then user can open registration popup on Customer page

  @allure.feature.CustomerRegistration @ui-elements @notification
  Scenario: Verify notification button accessibility on Customer Page
    Then the user should access the notification button on Customer page

  @allure.feature.CustomerRegistration @ui-elements @logout-dropdown
  Scenario: Verify logout dropdown accessibility on Customer Page
    Then the user should access the logout button dropdown on Customer page

  @allure.feature.CustomerRegistration @ui-elements @customer-count
  Scenario: Verify customer count display on Customer Page
    Then the user should get the customer count on Customer page

  @allure.feature.CustomerRegistration @export @data-export
  Scenario: Verify export functionality on Customer Page
    Then user can export the customer registrations on Customer page

  @allure.feature.CustomerRegistration @google-sheet @reset-sheet
  Scenario: Verify Google Sheet reset on Customer Page
    Then user can reset the google sheet on Customer page

  @allure.feature.CustomerRegistration @google-sheet @view-data
  Scenario: Verify Google Sheet data view on Customer Page
    Then user can view the customer registrations in google sheet on Customer page

  @allure.feature.CustomerRegistration @table-sorting
  Scenario: Verify sorting functionality on the Customer page
    When the user can sort the customer table on Customer page
    Then the table should be sorted in the correct order on Customer page


  @allure.feature.CustomerRegistration @export
  Scenario: Verify export functionality for Customer Registration data
    Then user can export the customer registrations on Customer page

  @allure.feature.CustomerRegistration @google_sheet
  Scenario: Verify Google Sheet reset for Customer Registration
    Then user can reset the google sheet on Customer page

  @allure.feature.CustomerRegistration @google_sheet
  Scenario: Verify Google Sheet view of Customer Registration data
    Then user can view the customer registrations in google sheet on Customer page

  @allure.feature.CustomerRegistration @registration-page @page-switcher
  Scenario: Verify page switcher functionality on Registration Page
    Then user can use switcher to switch to Registration page

  @allure.feature.CustomerRegistration @registration-page @count-verification
  Scenario: Verify registration count display on Registration Page
    Then the user should get the Registration count on Registration page

  @allure.feature.CustomerRegistration @registration-search
  Scenario: Search functionality on Registration page
    Then the user can search within the Registration on Registration page


  @allure.feature.Registration @table-sorting
  Scenario: Verify sorting functionality on the Registration page
    When the user sort the Registration table on Registration page
    Then the table should be sorted in the correct order on Registration page

  @allure.feature.CustomerRegistration @customer-popup
  Scenario: Verify Registration Popup
    When user open registration popup on Registration page
    Then user can access all the information for specific registration

  @allure.feature.CustomerRegistration @customer-popup
  Scenario: Verify Edit Registration
  When user open registration popup
   Then the user can edit registration details

  @allure.feature.CustomerRegistrationArchived @customer-popup
  Scenario: Verify Customer Popup
  When the user archive registration on registration page
    Then the registration should be archieved
    And the user can unarchived the registration

  @allure.feature.CustomerPage @pagination
  Scenario: Verify pagination functionality on the Customer page
    When the user want to see the number of rows on Customer Page
    Then the list should be updated on Customer page

  @allure.feature.CustomerRegistration @registration-export @export
  Scenario: Verify Export functionality of Registration on Registration Page
    Then user can export the Registration registrations on Registration page

  @allure.feature.CustomerRegistration @registration-export @google-sheet-reset
  Scenario: Verify Google Sheet reset for Registration on Registration Page
    Then user can reset the google sheet on Registration page

  @allure.feature.CustomerRegistration @registration-export @google-sheet-view
  Scenario: Verify Google Sheet view of Registration on Registration Page
    Then user can view the Registration registrations in google sheet on Registration page