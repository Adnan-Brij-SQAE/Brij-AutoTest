Feature: Analytics Rebate Dashboard
  @analytics_rebates

 @allure.feature.Navigate @rebate_page @allure.severity:critical
Scenario: Test Navigation to Analytics Rebate page
  When the user is on the Analytics Rebate page


 @allure.feature.Dropdowns @rebate_page @allure.severity:critical
Scenario: Test Experience Dropdown on Analytics Rebate page
  When  the user can access Experience dropdown on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page

@allure.feature.Dropdowns @rebate_page @allure.severity:critical
Scenario: Test Variant Dropdown on Analytics Rebate page
  When the user can access Variant dropdown on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page

@allure.feature.PageElements @rebate_page @allure.severity:normal
Scenario: Test Notification Button on Analytics Rebate page
  Then the user can access the notification button on Analytics Rebate page

@allure.feature.PageElements @rebate_page @allure.severity:normal
Scenario: Test Logout Dropdown on Analytics Rebate page
  Then the user can access the logout button dropdown on Analytics Rebate page

@allure.feature.DateRangeFilters @rebate_page @allure.severity:normal
Scenario: Test Date Range Filter Button on Analytics Rebate page
  When the user can select the date range filter button on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page


@allure.feature.PageElements @rebate_page @allure.severity:normal
Scenario: Test Export Option on Analytics Rebate page
  When the user can Export the data on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page


@allure.feature.TimeFilters @rebate_page @allure.severity:high
Scenario: Test Today Filter on Analytics Rebate page
  When the user clicks the Today filter button on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page


@allure.feature.TimeFilters @rebate_page @allure.severity:high
Scenario: Test This Week Filter on Analytics Rebate page
  When the user clicks the This Week filter button on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page


@allure.feature.TimeFilters @rebate_page @allure.severity:high
Scenario: Test This Month Filter on Analytics Rebate page
  When the user clicks the This Month filter button on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page


@allure.feature.TimeFilters @rebate_page @allure.severity:high
Scenario: Test This Year Filter on Analytics Rebate page
  When the user clicks the This Year filter button on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page

@allure.feature.DateRangeFilters @rebate_page @allure.severity:high
Scenario: Test Custom Date Range Filter on Analytics Rebate page
  When the user clicks date range filter button on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page

@allure.feature.MetricFilters @rebate_page @allure.severity:high
Scenario: Test Payout Metric Filter on Analytics Rebate page
  When the user clicks the Payout filter button on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page

@allure.feature.MetricFilters @rebate_page @allure.severity:high
Scenario: Test Approvals Metric Filter on Analytics Rebate page
  When the user clicks the APPROVALS filter button on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page

@allure.feature.MetricFilters @rebate_page @allure.severity:high
Scenario: Test Submission Metric Filter on Analytics Rebate page
  When the user clicks the Submission filter button on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page

@allure.feature.MetricFilters @rebate_page @allure.severity:high
Scenario: Test Initiations Metric Filter on Analytics Rebate page
  When the user clicks the Initiations filter button on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page

@allure.feature.MetricFilters @rebate_page @allure.severity:high
Scenario: Test Scan/Clicks Metric Filter on Analytics Rebate page
  When the user clicks the Scan/Clicks filter button on Analytics Rebate page
  Then the data should be displayed accordingly on rebate analytics page











##Feature: Analytics Rebate Dashboard
##  @analytics_rebates
##  Scenario: Test Analytics Rebate page
##    When the user is on the Analytics Rebate page
##    Then the user can access Experience dropdown on Analytics Rebate page
##    And the user can access Variant dropdown on Analytics Rebate page
##    And the user can access the notification button on Analytics Rebate page
##    And the user can access the logout button dropdown on Analytics Rebate page
##    And the user can select the date range filter button on Analytics Rebate page
##    And the user can Export the data on Analytics Rebate page
##    And the user clicks the Today filter button on Analytics Rebate page
##    And the user clicks the This Week filter button on Analytics Rebate page
##    And the user clicks the This Month filter button on Analytics Rebate page
##    And the user clicks the This Year filter button on Analytics Rebate page
##    And the user clicks the Payout filter button on Analytics Rebate page
##    And the user clicks the APPROVALS filter button  on Analytics Rebate page
##    And the user clicks the Submission filter button on Analytics Rebate page
##    And the user clicks the Initiations filter button on Analytics Rebate page
##    And the user clicks the Scan/Clicks filter button on Analytics Rebate page
#
#

#
#
#
#
#
#####from behave import *
#####
#####Feature: Customer Registration Management
#####
#####  Scenario: Accessing page elements
#####    Given The user is on the customer registration page
#####    Then THE USER should see the customer registration table
#####    And THE USER should see the total number of customers
#####
#####  Scenario: Using dropdown filters
#####    Given The user is on the customer registration page
#####    When THE USER select "Active, Onboarding, Demo" from the Brand Status dropdown
#####    And THE USER select "All Brands" from the Brands dropdown
#####    And THE USER select "All Registration Statuses" from the Registration Status dropdown
#####    And THE USER select "All Customer Sources" from the Customer Source dropdown
#####    Then the customer registration table should be filtered accordingly
#####
#####  Scenario: Searching for a customer
#####    Given The user is on the customer registration page
#####    When THE USER enter "sush" in the search bar
#####    Then the customer registration table should display results matching "sush"
#####
#####  Scenario: Opening customer popup
#####    Given The user is on the customer registration page
#####    When THE USER click on a customer name
#####    Then a customer details popup should open
#####
#####  Scenario: Opening registration popup
#####    Given The user is on the customer registration page
#####    When THE USER click on a registration entry
#####    Then a registration details popup should open
#####
#####  Scenario: Using the switcher
#####    Given The user is on the customer registration page
#####    When THE USER click on the switcher button
#####    Then the view should toggle between different modes
#####
#####  Scenario: Exporting data
#####    Given The user is on the customer registration page
#####    When THE USER click on the export button
#####    Then the customer registration data should be exported
