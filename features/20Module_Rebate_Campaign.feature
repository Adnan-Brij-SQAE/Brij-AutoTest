Feature: Test Rebate Campaign Module page

  @allure.feature.RebateCampaignPage @allure.severity:blocker
  Scenario: Navigate to Rebate Campaign Module Page
  When the user navigate to the Rebate Campaign Module page
    Then the user should be navigated to the Rebate Campaign Module page

  @allure.feature.RebateCampaignPage @page_elements @allure.severity:normal
  Scenario: Access Notification Button on Rebate Campaign Module page
    Then the user can access the notification button on Rebate Campaign Module page

  @allure.feature.RebateCampaignPage @page_elements @allure.severity:normal
  Scenario: Access Logout Button on Rebate Campaign Module page
    Then the user can access the logout button on Rebate Campaign Module page

  @allure.feature.RebateCampaignPage @page_elements @allure.severity:normal
  Scenario: Access Field Button on Rebate Campaign Module page
    Then the user can access the field button on Rebate Campaign Module page

  @allure.feature.RebateCampaignPage @checkbox @allure.severity:normal
  Scenario: Select All Checkbox on Rebate Campaign Module page
    Then the user can select All checkbox on Rebate Campaign Module page

  @allure.feature.RebateCampaignPage @sorting @allure.severity:normal
  Scenario: Sort Table on Rebate Campaign Module page
    Then the user can sort the table on Rebate Campaign Module page

@allure.feature.RebateCampaignPage @pagination
  Scenario: Verify pagination functionality on the Rebate Campaign Page
    Then the user want to see the number of rows on Rebate Campaign Page

  @allure.feature.RebateCampaignPage @create_module @allure.severity:critical
  Scenario: Create New Rebate Campaign Module
    Then the user can create new Rebate Campaign module from on Rebate Campaign Module page

  @allure.feature.RebateCampaignPage @rebate_Campaign_module @allure.severity:normal
  Scenario: Test functionality duplicate Rebate Campaign Page
    Then the user can create duplicate Rebate Campaign page

  @allure.feature.RebateCampaignPage @edit_module @allure.severity:critical
  Scenario: Edit Existing Rebate Campaign Module
    Then the user can edit the previous Rebate Campaign module on Rebate Campaign Module page

  @allure.feature.RebateCampaignPage @Delete @allure.severity:critical
  Scenario: Delete Rebate Campaign Module
    Then the user can delete the unused Rebate Campaign module
    Then the user can delete more than one unused Rebate Campaign module

    @allure.feature.RebateCampaignPage @search @allure.severity:normal
  Scenario: Use Search Feature on Rebate Campaign Module page
    Then the user use search feature to search between the modules on Rebate Campaign Module page