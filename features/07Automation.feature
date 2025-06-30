@automation @regression @high
Feature: Automation Management
  As an administrator
  I want to manage marketing automations
  So I can streamline customer engagement processes


  @severity(allure.severity_level.CRITICAL) @epic("Automation")
  Scenario: Verify Automation page navigation
    When the user navigate to Automation page

  @severity(allure.severity_level.NORMAL) @epic("UI")
  Scenario: Verify notification button accessibility
    Then the user can access the notification button on Automation page

  @severity(allure.severity_level.CRITICAL) @epic("UI")
  Scenario: Verify logout functionality
    Then the user can access the logout button on Automation page

  @severity(allure.severity_level.NORMAL) @epic("Search") @feature("Functionality")
  Scenario: Verify search functionality
    Then the user can search within the Automation on Automation page

  @severity(allure.severity_level.NORMAL) @epic("UI")
  Scenario: Verify field button functionality
    Then the user can click on field button on Automation page

  @severity(allure.severity_level.NORMAL) @epic("UI")
  Scenario: Verify checkbox functionality
    Then the user can check all check boxes on Automation page

  @severity(allure.severity_level.NORMAL) @epic("Tables") @feature("Functionality")
  Scenario: Verify table sorting
    Then the user can sort the Automation table on Automation page

  @severity(allure.severity_level.CRITICAL) @epic("Automation") @feature("Lifecycle") @story("Creation")
  Scenario: Create new automation with live state
    When the user creates a new Automation
    Then the automation should be created successfully

  @severity(allure.severity_level.NORMAL) @epic("Automation") @feature("Configuration") @story("Save")
  Scenario: Create automation with pause state
    Then the user can save new automation but pause

  @severity(allure.severity_level.CRITICAL) @epic("Automation") @feature("Lifecycle") @story("Status")
  Scenario: Activate paused automation
    When the user makes the previous automation live
    Then the automation status should change to active

  @severity(allure.severity_level.CRITICAL) @epic("Automation") @feature("Lifecycle") @story("Status")
  Scenario: Pause active automation
    When the user pauses the automation
    Then the automation status should change to paused


  @severity(allure.severity_level.CRITICAL) @epic("Automation") @feature("Lifecycle") @story("Modification")
  Scenario: Edit existing automation
    When the user edits the previous Automation
    Then the automation should be updated successfully


  @severity(allure.severity_level.CRITICAL) @epic("Automation") @feature("Lifecycle") @story("Draft")
  Scenario: Save automation as draft
    When the user drafts the automation for future use
    Then the draft should be saved successfully

  @severity(allure.severity_level.NORMAL) @epic("Tables") @feature("Navigation") @story("Data")
  Scenario: Verify pagination controls
    Then the user can test the pagination on Automation page















#Feature: Test Automation page
#  @Serialized_Code
#  Scenario: test Automation page
#    When The user navigate to Customer Automation page
#    Then the user can access the notification button on Automation page
#    And the user can access the logout button on Automation page
#    And the user can get the Automation count on Automation page
#    And the user can search within the Automation on Automation page
#    And the user can click on field button on Automation page
#    And the user can check all check boxes on Automation page
#    And the user can sort the Automation table on Automation page
#    And the user can create a new Automation
#    And the user can edit the previous Automation
#    And the user can draft the automation for future use
#    And the user can save new automation but pause
#    And the user can pause the automation
#    And the user can live the previous automation
#    And user can test the pagination on Automation page