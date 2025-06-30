Feature: Customer Registration page
  @customer_page
  @allure.feature.CustomerRegistration @navigation
  Scenario: test customer page
    When the user navigate to Customer Registration page

  @allure.feature.CustomerExperienceDropdown @customer_page  @allure.severity:high
  Scenario: Test Experience Dropdown on Customer page
    When User is on the Customer Page
    Then the user can access Experience dropdown on Customer page
    And the data should be filtered accordingly

  @allure.feature.CustomerVariantDropdown @customer_page  @allure.severity:high
  Scenario: Test Variant Dropdown on Customer page
    When User is on the Customer Page
    Then the user can access Variant dropdown on Customer page
    And the data should be filtered accordingly

  @allure.feature.CustomerStatusDropdown @customer_page  @allure.severity:high
  Scenario: Test Registration Status Dropdown on Customer page
    When User is on the Customer Page
    Then the user can access registration status dropdown on Customer page
    And the data should be filtered accordingly

  @allure.feature.CustomerSourceDropdown @customer_page  @allure.severity:high
  Scenario: Test Customer Source Dropdown on Customer page
    When User is on the Customer Page
    Then the user can access customer source dropdown on Customer page
    And the data should be filtered accordingly

  @allure.feature.CustomerRegistration @ui-elements
  Scenario: Verify page elements of Customer Registration
    When User is on the Customer Page
    Then the user should access the notification button on Customer page
    And the user should access the logout button dropdown on Customer page
    And the user should get the customer count on Customer page

  @story:Search @severity:critical
  @allure.feature.CustomerRegistration @search
  Scenario: Search functionality on Customer Registration page
    Then the user can search within the customer on Customer page

 @allure.feature.CustomerRegistration @table-elements
  Scenario: Verify table elements of Customer Registration
    Then the user can click on field button on Customer page
#    And the user can check all check boxes on Customer page

 @allure.feature.CustomerRegistration @table-sorting
  Scenario: Verify sorting functionality on the Customer page
    When the user can sort the customer table on Customer page
    Then the table should be sorted in the correct order on Customer page


  @allure.feature.CustomerRegistration @customer-popup
  Scenario: Verify Customer Popup
    Then open customer popup on Customer page
    And user can expand the customer registrations on Customer page
    And user can open registration popup on Customer page

  @allure.feature.CustomerRegistration @export
  Scenario: Verify Export, and google sheet view  of Customer Registration
    Then user can export the customer registrations on Customer page
    And user can reset the google sheet on Customer page
#    And user can view the customer registrations in google sheet on Customer page

  @allure.feature.CustomerRegistration @registration-page
  Scenario: Verify page elements of  Registration
    Then user can use switcher to switch to Registration page
    And the user should get the Registration count on Registration page

  @allure.feature.CustomerRegistration @registration-search
  Scenario: Search functionality on Registration page
    Then the user can search within the Registration on Registration page

  @allure.feature.CustomerRegistration @registration-table
  Scenario: Verify table elements of Registration
    Then the user can click on field button on Registration page
#    And the user can check all check boxes on Registration page

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

  @allure.feature.CustomerRegistration @registration-export
  Scenario: Verify Export, and google sheet view  of  Registration
    Then user can export the Registration registrations on Registration page
    And user can reset the google sheet on Registration page
#    And user can view the Registration registrations in google sheet on Registration page
#
#
#
#####
#####
#####
#####
#####
#  #Feature: Customer Registration page
##  @customer_page
##  Scenario: test customer page
##
##    When the user navigate to Customer Registration page
##    Then the user should access the notification button on Customer page
##    And the user should access the logout button dropdown on Customer page
##    And the user should get the customer count on Customer page
##    And the user can search within the customer on Customer page
##    And the user can click on field button on Customer page
##    And the user can check all check boxes on Customer page
##    And the user can sort the customer table on Customer page
##    And open customer popup on Customer page
##    And user can expand the customer registrations on Customer page
##    And user can open registration popup on Customer page
##    And user can export the customer registrations on Customer page
##    And user can reset the google sheet on Customer page
##    And user can view the customer registrations in google sheet on Customer page
##    And user can use switcher to switch to Registration page
##    And the user should get the Registration count on Registration page
##    And the user can search within the Registration on Registration page
##    And the user can click on field button on Registration page
##    And the user can check all check boxes on Registration page
##    And the user can sort the Registration table on Registration page
##    And the user can open Registration popup on Registration page
##    And the user can edit registration on registration page
##    And the user can archive registration on registration page
##    And user can export the Registration registrations on Registration page
##    And user can reset the google sheet on Registration page
##    And user can view the Registration registrations in google sheet on Registration page
##
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
######
###  Scenario: Accessing page elements
###    Given User is on the customer registration page
###    Then USER should see the customer registration table
###    And USER should see the total number of customers
###
###  Scenario: Using dropdown filters
###    Given User is on the customer registration page
###    When USER select "Active, Onboarding, Demo" from the Brand Status dropdown
###    And USER select "All Brands" from the Brands dropdown
###    And USER select "All Registration Statuses" from the Registration Status dropdown
###    And USER select "All Customer Sources" from the Customer Source dropdown
###    Then the customer registration table should be filtered accordingly
###
###  Scenario: Searching for a customer
###    Given User is on the customer registration page
###    When USER enter "sush" in the search bar
###    Then the customer registration table should display results matching "sush"
###
###  Scenario: Opening customer popup
###    Given User is on the customer registration page
###    When USER click on a customer name
###    Then a customer details popup should open
###
###  Scenario: Opening registration popup
###    Given User is on the customer registration page
###    When USER click on a registration entry
###    Then a registration details popup should open
###
###  Scenario: Using the switcher
###    Given User is on the customer registration page
###    When USER click on the switcher button
###    Then the view should toggle between different modes
###
###  Scenario: Exporting data
###    Given User is on the customer registration page
###    When USER click on the export button
###    Then the customer registration data should be exported
