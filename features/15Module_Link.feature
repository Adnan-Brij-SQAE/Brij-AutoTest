Feature: Test Link Module Page
  As a user
  I want to interact with the Link Module page
  So that I can manage Link modules effectively

  @allure.feature.LinkModule @navigation
  Scenario: Verify navigation to the Link Module page
    When the user navigates to the Link Module page
    Then the Link Module page should be displayed

  @allure.feature.LinkModule @ui-elements
  Scenario: Verify UI elements on the Link Module page
    Then the user can access the notification button on the Link Module page
    And the user can access the logout button on the Link Module page
    And the user can access the field button on the Link Module page

  @allure.feature.LinkModule @checkboxes
  Scenario: Verify checkbox functionality on the Link Module page
    When the user selects all checkboxes on Link Module page
    Then all checkboxes should be selected on Link Module page

  @allure.feature.LinkModule @search
  Scenario: Verify search functionality on the Link Module page
    When the user uses the search feature to search between the modules on Link Module page
    Then the search results should be displayed correctly on Link Module page

  @allure.feature.LinkModule @sort
  Scenario: Verify sorting functionality on the Link Module page
    When the user sorts the table on Link Module page
    Then the table should be sorted in the correct order on Link Module page

  @allure.feature.LinkModule @create-module
  Scenario: Verify creation of a new Link module

    When the user creates a new Link module
    Then the new Link module should be added to the module list

  @allure.feature.LinkModule @navigate-links
  Scenario: Verify navigation to added links
    When the user navigates to the added links
    Then the links should be accessible

  @allure.feature.LinkModule @navigate-links-suffix
  Scenario: Verify navigation to added links with suffix
    When the user navigates to the added links with suffix
    Then the links with suffix should be accessible

  @allure.feature.LinkModule @edit-module
  Scenario: Verify editing of an existing Link module
    When the user edits an existing Link module
    Then the changes should be saved and reflected in the Link module list

  @allure.feature.LinkModule @delete-module
  Scenario: Verify deletion of an unused Link module
    When the user deletes an unused Link module
    Then the module should be removed from the Link module list


  @allure.feature.LINKModule @pagination
  Scenario: Verify pagination functionality on the LINK
    When the user want to see the number of rows on the LINK module list
    Then the module list should be updated on LINK page

#
#
#
#
#
#
#
#
#
#
##Feature: Test Link Module page
##
##  Scenario: Link Module page testing
##    When the user navigate to the Link Module page
##    Then the user can access the field button on Link Module page
##    And the user can access the notification button on Link Module page
##    And the user can access the logout button on Link Module page
##    And the user can access the field button on Link Module page
##    And the user can select All checkbox on Link Module page
##    And the user use search feature to search between the modules on Link Module page
##    And the user can sort the table on Link Module page
##    And the user can create new Link module from on Link Module page
##    And the user can navigate to the added links
##    And the user can navigate to the added links with suffix
##    And the user can edit the previous Link module on Link Module page
##    And the user can delete the unused Link module on Link Module page
