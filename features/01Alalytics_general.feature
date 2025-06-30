Feature: General Analytics page
  @General_Analytics_page

@allure.feature.AnalyticsGeneral @navigation
Scenario: Test navigate to Analytics General page
  When the user is on the Analytics General page

@allure.feature.Dropdowns @analytics_general @allure.severity:critical
Scenario: Test Experience Dropdown on the Analytics General page
  When the user can access Experience dropdown on Analytics General page
  Then metric with the selected filters will be shown

@allure.feature.Dropdowns @analytics_general @allure.severity:critical
Scenario: Test Variant Dropdown on the Analytics General page
  When the user can access Variant dropdown on Analytics General page
  Then metric with the selected filters will be shown

#@allure.feature.Dropdowns @analytics_general @allure.severity:critical
#Scenario: Test Category Dropdown on the Analytics General page
#  When the user can access Category dropdown on Analytics General page
#  Then metric with the selected filters will be shown

@allure.feature.PageElements @analytics_general @allure.severity:normal
Scenario: Test Notification Button on the Analytics General page
  Then the user can access notification button on Analytics General page

@allure.feature.PageElements @analytics_general @allure.severity:normal
Scenario: Test Logout Dropdown on the Analytics General page
  Then the user can access logout button dropdown on Analytics General page

@allure.feature.PageElements @analytics_general @allure.severity:normal
Scenario: Test Export Option on the Analytics General page
  Then the user can export the data on Analytics General page

@allure.feature.DateRangeFilters @analytics_general @allure.severity:high
Scenario: Test Predefined Date Range Filters on the Analytics General page
  When the user clicks the Day filter button on Analytics General page
  And the user clicks the This Week filter button on Analytics General page
  And the user clicks the This Month filter button on Analytics General page
  And the user clicks the This Year filter button on Analytics General page
  And the user clicks the All Time filter button on Analytics General page
  Then the data should be displayed accordingly with export

#@allure.feature.DateRangeFilters @analytics_general @allure.severity:high
#Scenario: Test Custom Date Range Filters on the Analytics General page
#  When the user clicks date range filter button on Analytics General page
#  Then the data should be displayed accordingly with export

@allure.feature.MetricFilters @analytics_general @allure.severity:high
Scenario: Test Scans/Clicks Metric Filter on the Analytics General page
  When the user clicks the Scans/Clicks filter button on Analytics General page
  Then the data should be displayed accordingly

@allure.feature.MetricFilters @analytics_general @allure.severity:high
Scenario: Test Registrations Metric Filter on the Analytics General page
  When the user clicks the Registrations filter button on Analytics General page
  Then the data should be displayed accordingly

@allure.feature.MetricFilters @analytics_general @allure.severity:high
Scenario: Test Engagements Metric Filter on the Analytics General page
  When the user clicks the Engagements filter button on Analytics General page
  Then the data should be displayed accordingly

@allure.feature.MetricFilters @analytics_general @allure.severity:high
Scenario: Test Website Visits Metric Filter on the Analytics General page
  When the user clicks the Website Visits filter button on Analytics General page
  Then the data should be displayed accordingly

@allure.feature.MetricFilters @analytics_general @allure.severity:high
Scenario: Test Revenue Metric Filter on the Analytics General page
  When the user clicks the Revenue filter button on Analytics General page
  Then the data should be displayed accordingly



##  Scenario: User interacts with Analytics General page
##    When the user is on the Analytics General page
##    Then the user can access Experience dropdown on Analytics General page
##    And the user can access Variant dropdown on Analytics General page
##    And the user can access notification button on Analytics General page
##    And the user can access logout button dropdown on Analytics General page
##    And the user can select a date range filter button on Analytics General page
##    And the user can export the data on Analytics General page
##    And the user clicks the Today filter button on Analytics General page
##    And the user clicks the This Week filter button on Analytics General page
##    And the user clicks the This Month filter button on Analytics General page
##    And the user clicks the This Year filter button on Analytics General page
##    And the user clicks the Scans/Clicks filter button on Analytics General page
##    And the user clicks the Registrations filter button on Analytics General page
##    And the user clicks the Engagements filter button on Analytics General page
##    And the user clicks the Website Visits filter button on Analytics General page
##    And the user clicks the Revenue filter button on Analytics General page