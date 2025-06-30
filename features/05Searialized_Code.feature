@SerializedCode
Feature:  Serialized Code Page Functionality

  @allure.feature.SerializedCodeNavigation @SerializedCode
  Scenario: Verify navigation to Serialized Code page
    When The user navigates to  Serialized Code page

  @allure.feature.SerializedCodeExperience @SerializedCode @-Filter
  Scenario: Verify Serialized Code Experience Filters Dropdowns
    When The user apply Experience filter on Serialize code page
    Then The serialized code(s) should be displayed accordingly

  @allure.feature.SerializedCodeVariant @SerializedCode @-Filter
  Scenario: Verify Serialized Code Variant Filters Dropdowns
    When The user apply Variant filter on Serialize code page
    Then The serialized code(s) should be displayed accordingly

  @allure.feature.SerializedCodeRegStatus @SerializedCode @-Filter
  Scenario: Verify Serialized Code Registration status Filters Dropdowns
    When The user apply Registration status filter on Serialize code page
    Then The serialized code(s) should be displayed accordingly

  @allure.feature.SerializedCodeUI @SerializedCode @-popup
  Scenario: Verify notification button functionality
    When The user clicks on the notification button
    Then The notification panel should be accessible

  @allure.feature.SerializedCodeUI @SerializedCode
  Scenario: Verify logout button functionality
    When The user clicks on the logout button
    Then The user should be logged out successfully

  @allure.feature.SerializedCodeNavigation @SerializedCode
  Scenario: Verify field button functionality
     When The user clicks on field button
    Then The corresponding fields should be displayed

  @allure.feature.SerializedCodeSorting @SerializedCode
  Scenario: Verify table sorting functionality
    When The user sorts the Serialized Code table
    Then The table should be sorted correctly


  @allure.feature.SerializedCodePopup @SerializedCode @-Pagination
  Scenario: Verify Serialized Code Dropdown Filters
    When The user want to test pagination
    Then The user can view 100 rows of Serialized code
    Then The user can view 20 rown of Serialized code
    Then The user can view 1000 rows of Serialized code

  @allure.feature.SerializedCodeDeactivate @SerializedCode @-deactivate
  Scenario: Verify Serialized Code Deactivate
    When The user deactivate the Serialized Code
    Then The code status be updated in the listing

  @allure.feature.SerializedCodeActivate @SerializedCode @-activate
  Scenario: Verify Serialized Code Activate
    When The user activate the Serialized Code
    Then The code status be updated in the listing

  @allure.feature.SerializedCodeDelete @SerializedCode @-Delete
  Scenario: Verify Serialized Code Delete individual
    When The user delete the Serialized Code
    Then The serialized code(s) should no longer be in list

#  @allure.feature.SerializedCodeDeleteAll @SerializedCode @-Deleteall
#  Scenario: Verify Serialized Code Delete more than one
#    When The user delete more than one Serialized Code
#    Then The serialized code(s) should no longer be in list

  @allure.feature.SerializedCodeExport @SerializedCode @export
  Scenario: Verify export functionality
    When The user exports Serialized Codes
    Then The export file should be generated successfully


  @allure.feature.SerializedCodeImport @SerializedCode
  Scenario: Verify import functionality
    When The user imports Serialized Codes
    Then The import should be processed successfully

   @allure.feature.SerializedCodeScan @SerializedCode @-Codescan
  Scenario: Verify Serialized Code Scan
    When The user hover to the code icon
    Then The QR code shold be displayed
    Then The user can open the QR code link

  @allure.feature.SerializedCodeDownload @SerializedCode @-downloadPNG
  Scenario: Verify Serialized Code download as png
    When The user download the Serialized Code popup as png
    Then The the selected code should be downloaded

  @allure.feature.SerializedCodeDownload @SerializedCode @-downloadSVG
  Scenario: Verify Serialized Code download as SVG
    When The user download the Serialized Code popup as svg
    Then The the selected code should be downloaded


  @allure.feature.SerializedCodeSearch @SerializedCode
  Scenario: Verify search functionality
    When The user performs a search within Serialized Codes
#    Then The search results should be displayed correctly









#Feature: Customer Serialized Code page
#  @Serialized_Code
#  Scenario: test Serialized Code page
#    When The user navigate to Customer Serialized Code page
#    Then the user can access the notification button on Serialized Code page
#    And the user can access the logout button on Serialized Code page
#    And the user can get the Serialized Code count on Serialized Code page
#    And the user can search within the Serialized Code on Serialized Code page
#    And the user can click on field button on Serialized Code page
#    And the user can check all check boxes on Serialized Code page
#    And the user can sort the Serialized Code table on Serialized Code page
#    And the user can open Serialized Code popup on Serialized Code page
#    And user can export the Serialized Codes
#    And user can import Serialized Codes