Feature: Test Link Module Page
  As a user
  I want to interact with the Link Module page
  So that I can manage Link modules effectively

  @allure.feature.LinkModule @navigation
  Scenario: Verify navigation to the Link Module page
    When the user navigates to the Link Module page
    Then the Link Module page should be displayed
#
#  @allure.feature.LinkModule @ui-elements @notification
#  Scenario: Verify Notification button on the Link Module page
#    Then the user can access the notification button on the Link Module page
#
#  @allure.feature.LinkModule @ui-elements @logout
#  Scenario: Verify Logout button on the Link Module page
#    Then the user can access the logout button on the Link Module page
#
#  @allure.feature.LinkModule @ui-elements @field
#  Scenario: Verify Field button on the Link Module page
#    Then the user can access the field button on the Link Module page
#
#
#  @allure.feature.LinkModule @checkboxes
#  Scenario: Verify checkbox functionality on the Link Module page
#    Then the user can select all checkboxes on Link Module page
#
#
#  @allure.feature.LinkModule @sort
#  Scenario: Verify sorting functionality on the Link Module page
#    When the user sorts the table on Link Module page
#    Then the module list should be updated on LINK module page

#  @allure.feature.LinkModule @create-module
#  Scenario: Verify creation of a new Link module
#    When the user creates a new Link module
#    Then the module list should be updated on LINK module page
#
#  @allure.feature.LinkModule @duplicate-module
#  Scenario: Verify duplicating of an existing Link module
#    When the user duplicates an existing Link module
#    Then the module list should be updated on LINK module page
#
#  @allure.feature.LinkModule @edit-module
#  Scenario: Verify editing of an existing Link module
#    When the user edits an existing Link module
#    Then the module list should be updated on LINK module page

  @allure.feature.LinkModule @navigate-links
  Scenario: Verify navigation to added links
    When the user navigates to the added links
    Then the links should be accessible

  @allure.feature.LinkModule @navigate-links-suffix
  Scenario: Verify navigation to added links with suffix
    When the user navigates to the added links with suffix
    Then the links should be accessible

  @allure.feature.LinkModule @delete-module
  Scenario: Verify deletion of an unused Link module
    When the user deletes an unused Link module
    Then the user deletes more than one unused Link module

  @allure.feature.LINKModule @pagination
  Scenario: Verify pagination functionality on the LINK
    When the user want to see the number of rows on the LINK module list
    Then the module list should be updated on LINK module page

  @allure.feature.LinkModule @search
  Scenario: Verify search functionality on the Link Module page
    When the user uses the search feature on Link Module page
    Then the search results should be displayed correctly on Link Module page
#