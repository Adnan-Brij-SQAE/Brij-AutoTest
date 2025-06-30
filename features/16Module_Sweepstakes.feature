Feature: Test SweepStakes Module Page


  @allure.feature.SweepStakesModule @navigation
  Scenario: Verify navigation to the SweepStakes Module page
    When the user navigates to the SweepStakes Module page
    Then the SweepStakes Module page should be displayed

  @allure.feature.SweepStakesModule @ui-elements
  Scenario: Verify the notification button on the SweepStakes Module page
    Then the user can access the notification button on the SweepStakes Module page

  @allure.feature.SweepStakesModule @ui-elements
  Scenario: Verify the logout button on the SweepStakes Module page
    Then the user can access the logout button on the SweepStakes Module page

  @allure.feature.SweepStakesModule @ui-elements
  Scenario: Verify the Fields button on the SweepStakes Module page
    When the user can access the Fields button on the SweepStakes Module page
    Then the user can access the SweepStakes Name field on the SweepStakes Module page
    Then the user can access the Where Used field on the SweepStakes Module page
    Then the user can access the SweepStakes Campaign Dates field on the SweepStakes Module page
    Then the user can access the Call to Action field on the SweepStakes Module page


  @allure.feature.SweepStakesModule @checkboxes
  Scenario: Verify checkbox functionality on the SweepStakes Module page
    When the user selects all checkboxes on the SweepStakes Module page
    Then all checkboxes should be selected on the SweepStakes Module page


  @allure.feature.SWEEPSTAKESModule @pagination
  Scenario: Verify pagination functionality on the SWEEPSTAKES
    When the user want to see the number of rows on the SWEEPSTAKES module list
    Then the module list should be updated on SWEEPSTAKES page

  @allure.feature.SweepStakesModule @sort
  Scenario: Verify sorting functionality on the SweepStakes Module page
    When the user sorts the table on the SweepStakes Module page
    Then the table should be sorted in the correct order on the SweepStakes Module page

  @allure.feature.SweepStakesModule @create-module
  Scenario: Verify creation of a new SweepStakes module
    When the user creates a new SweepStakes module
    Then the new SweepStakes module should be added to the module list

  @allure.feature.SweepStakesModule @duplicate-module
  Scenario: Verify duplication of an existing SweepStakes module
    When the user duplicates an existing SweepStakes module
    Then the changes should be saved and reflected in the SweepStakes module list

  @allure.feature.SweepStakesModule @edit-module
  Scenario: Verify editing of an existing SweepStakes module
    When the user edits an existing SweepStakes module
    Then the changes should be saved and reflected in the SweepStakes module list

  @allure.feature.SweepStakesModule @delete-module
  Scenario: Verify deletion of an unused SweepStakes module
    When the user deletes an unused SweepStakes module
    When the user deletes more than one unused SweepStakes module

  @allure.feature.SweepStakesModule @search
  Scenario: Verify search functionality on the SweepStakes Module page
    When the user uses the search feature to search between the SweepStakes modules
    Then the search results should be displayed correctly on the SweepStakes Module page