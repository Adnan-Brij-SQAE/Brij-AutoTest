Feature: Test Video Module Page


  @allure.feature.VideoModule @navigation
  Scenario: Verify navigation to the Video Module page
    When the user navigates to the Video Module page
    Then the Video Module page should be displayed

  @allure.feature.VideoModule @ui-elements
  Scenario: Verify the notification button on the Video Module page
    Then the user can access the notification button on the Video Module page

  @allure.feature.VideoModule @ui-elements
  Scenario: Verify the logout button on the Video Module page
    Then the user can access the logout button on the Video Module page

#  @allure.feature.VideoModule @ui-elements
#  Scenario: Verify the Fields button on the Video Module page
#    When the user can access the Fields button on the Video Module page
#    Then the user can access the Video Name field on the Video Module page
#    Then the user can access the Where Used field on the Video Module page
#    Then the user can access the Call to Action field on the Video Module page
#    Then the user can access the File name field on the Video Module page



  @allure.feature.VideoModule @create-module
  Scenario: Verify creation of a new Video module
    When the user creates a new Video module
    Then the changes should be saved and reflected in the Video module list

  @allure.feature.VideoModule @duplicate-module
  Scenario: Verify duplication of an existing Video module
    When the user duplicates an existing Video module
    Then the changes should be saved and reflected in the Video module list

  @allure.feature.VideoModule @edit-module
  Scenario: Verify editing of an existing Video module
    When the user edits an existing Video module
    Then the changes should be saved and reflected in the Video module list

  @allure.feature.VideoModule @checkboxes
  Scenario: Verify checkbox functionality on the Video Module page
    When the user selects all checkboxes on the Video Module page
    Then all checkboxes should be selected on the Video Module page

  @allure.feature.WARRANTYModule @pagination
  Scenario: Verify pagination functionality on the WARRANTY
    When the user want to see the number of rows on the WARRANTY module list
    Then the module list should be updated on WARRANTY page

  @allure.feature.VideoModule @delete-module
  Scenario: Verify deletion of an unused Video module
    When the user deletes an unused Video module
    When the user deletes more than one unused Video module

  @allure.feature.VideoModule @sort
  Scenario: Verify sorting functionality on the Video Module page
    When the user sorts the table on the Video Module page
    Then the table should be sorted in the correct order on the Video Module page

  @allure.feature.VideoModule @search
  Scenario: Verify search functionality on the Video Module page
    When the user uses the search feature to search between the Video modules
    Then the search results should be displayed correctly on the Video Module page




























#  @allure.feature.VideoModule @navigation
#  Scenario: Verify navigation to the Video Module page
#    Given the user is logged into the platform
#    When the user navigates to the Video Module page
#    Then the Video Module page should be displayed
#
#  @allure.feature.VideoModule @ui-elements
#  Scenario: Verify UI elements on the Video Module page
#    Given the user is on the Video Module page
#    Then the user can access the notification button on the Video Module page
#    And the user can access the logout button on the Video Module page
#    And the user can access the field button on the Video Module page
#
#  @allure.feature.VideoModule @checkboxes
#  Scenario: Verify checkbox functionality on the Video Module page
#    Given the user is on the Video Module page
#    When the user selects all checkboxes on video module
#    Then all checkboxes should be selected on video module
#
#  @allure.feature.VideoModule @search
#  Scenario: Verify search functionality on the Video Module page
#    Given the user is on the Video Module page
#    When the user uses the search feature to search between the modules
#    Then the search results should be displayed correctly
#
#  @allure.feature.VideoModule @sort
#  Scenario: Verify sorting functionality on the Video Module page
#    Given the user is on the Video Module page
#    When the user sorts the table
#    Then the table should be sorted in the correct order
#
#  @allure.feature.VideoModule @create-module
#  Scenario: Verify creation of a new Video module
#    Given the user is on the Video Module page
#    When the user creates a new Video module
#    Then the new Video module should be added to the module list
#
#  @allure.feature.VideoModule @edit-module
#  Scenario: Verify editing of an existing Video module
#    Given the user is on the Video Module page
#    When the user edits an existing Video module
#    Then the changes should be saved and reflected in the module list
#
#  @allure.feature.VideoModule @delete-module
#  Scenario: Verify deletion of an unused Video module
#    Given the user is on the Video Module page
#    When the user deletes an unused Video module
#    Then the module should be removed from the module list

