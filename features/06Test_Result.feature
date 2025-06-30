Feature: Test Result Page

  @allure.feature.TestResultPage @navigation
  Scenario: Verify navigation to the Test Result page
    When the user navigates to the Test Result page

#@allure.feature.TestResultPage @ui-elements @notification-button
#  Scenario: Verify presence of notification button on Test Result page
#    Then the user should be able to access the notification button
#
#  @allure.feature.TestResultPage @ui-elements @logout-dropdown
#  Scenario: Verify presence of logout button dropdown on Test Result page
#    Then the user should be able to access the logout button dropdown
#
#  @allure.feature.TestResultPage @ui-elements @test-result-count
#  Scenario: Verify presence of Test Result count on Test Result page
#    Then the user should be able to see the Test Result count displayed

#  @allure.feature.TestResultPage @filters @TestingPanel
#  Scenario: Verify filter functionality on the Test Result page
#    When the user applies Testing Panel filters on the page
#    Then the Test Results should be filtered accordingly
#
#  @allure.feature.TestResultPage @filters
#  Scenario: Verify filter functionality on the Test Result page
#    When the user applies Lab filters on the page
#    Then the Test Results should be filtered accordingly
#
#  @allure.feature.TestResultPage @sorting
#  Scenario: Verify sorting functionality on the Test Result page
#    When the user sorts the Test Results table
#    Then the Test Results should be sorted in the correct order
#
#  @allure.feature.TestResultPage @buttons
#  Scenario: Verify interaction with buttons on the Test Result page
#    When the user clicks on the field button
#    Then the corresponding action should be performed
#
#  @allure.feature.TestResultPage @checkboxes
#  Scenario: Verify interaction with checkboxes on the Test Result page
#    When the user checks all checkboxes
#    Then all checkboxes should be selected on test result page

#  @allure.feature.TestResultPage @create-test-result
#  Scenario: Verify creation of a new Test Result
#    When the user creates a new Test Result
#    Then the new Test Result should be added to the list
#
#  @allure.feature.TestResultPage @edit-test-result
#  Scenario: Verify editing of an existing Test Result
#    When the user edits an existing Test Result
#    Then the changes should be saved and reflected in the list

  @allure.feature.TestResultPage @lab-management
  Scenario: Verify lab management on the Test Result page
    When the user creates, updates, or deletes a lab
    Then the lab details should be updated accordingly

  @allure.feature.TestResultPage @upc-management
  Scenario: Verify UPC Result management on the Test Result page

    When the user creates, updates, or deletes a UPC Result
    Then the UPC Result details should be updated accordingly

  @allure.feature.TestResultPage @export
  Scenario: Verify export functionality on the Test Result page
    When the user exports the Test Result
    Then the Test Result data should be downloaded successfully

  @allure.feature.TestResultPage @template-download
  Scenario: Verify template sheet download functionality
    When the user downloads the template sheet
    Then the template sheet should be downloaded successfully

  @allure.feature.TestResultPage @import
  Scenario: Verify import functionality on the Test Result page
    When the user imports data into the Test Result page
    Then the imported data should be reflected in the Test Results

























#
#Feature: Test Result  page
#
#  Scenario: test Test Result page
#    Given The user is at brij platform
#    When The user navigates to Test Result page
#    Then the user should access the notification button on Test Result page
#    And the user should access the logout button dropdown on Test Result page
#    And the user should get the Test Result count on Test Result page
#    And the user can use filters on Test Result page
#   And the user can click on field button on Test Result page
#    And the user can check all check boxes on Test Result page
#    And the user can sort the Test Results table on Test Result page
#    And user can create the Test Result on Test Result page
#    And user can edit Test Result on Test Result page
#    And user can Create/update/delete lab on Test Result page
#    And user can Create/update/delete UPC Result page
#    And user can export the Test Result on Test Result page
#    And user can download the template sheet from Test Result on Test Result page
#    And user can import from the test result on Test Result page