@profile
Feature: Test Profile Page
  As a registered user
  I want to manage my profile settings
  So that I can keep my account information up-to-date

  @navigation
  Scenario: User navigates to profile page
    When the user clicks on the profile icon
    Then the profile page should be displayed

  @brand_management
  Scenario: Add or update brand name
    When the user enters or updates the brand name
    And clicks the save button on profile page
    Then the brand name should be successfully saved

  @brand_management
  Scenario: Add or update website homepage URL
    When the user enters or updates the website homepage URL
    And clicks the save button on profile page
    Then the website URL should be successfully saved

  @brand_management
  Scenario: Enable hyperlink to home URL
    When the user toggles the hyperlink option
    Then the website URL should become clickable

  @facebook
  Scenario: Add social media links
    When the user adds Facebook platform link
    And clicks the save button on profile page
    Then the social media links should be saved

  @instagram
  Scenario: Add Instagram link
    When the user adds an Instagram platform link
    And clicks the save button on profile page
    Then the social media links should be saved

  @threads
  Scenario: Add Threads link
    When the user adds a Threads platform link
    And clicks the save button on profile page
    Then the social media links should be saved


  @discord
  Scenario: Add Discord link
    When the user adds a Discord platform link
    And clicks the save button on profile page
    Then the social media links should be saved


  @youtube
  Scenario: Add YouTube link
    When the user adds a YouTube platform link
    And clicks the save button on profile page
    Then the social media links should be saved


  @phone
  Scenario: Add phone number
    When the user adds a phone number
    And clicks the save button on profile page
    Then the social media links should be saved


  @email
  Scenario: Add email address
    When the user adds an email address
    And clicks the save button on profile page
    Then the social media links should be saved


  @twitter
  Scenario: Add Twitter (X) link
    When the user adds a Twitter (X) platform link
    And clicks the save button on profile page
    Then the social media links should be saved


  @tiktok
  Scenario: Add TikTok link
    When the user adds a TikTok platform link
    And clicks the save button on profile page
    Then the social media links should be saved

  @linkedin
  Scenario: Add LinkedIn link
    When the user adds a LinkedIn platform link
    And clicks the save button on profile page
    Then the social media links should be saved


  @contact_info
  Scenario: Add or update contact information
    When the user enters or updates contact information
    And clicks the save button on profile page
    Then the contact information should be saved

  @legal
  Scenario: Add legal and compliance information
    When the user enters legal and compliance information
    And clicks the save button on profile page
    Then the legal information should be saved

  @security
  Scenario: Change password
    When the user selects the change password option
    And enters valid new credentials
    Then the password should be successfully updated

  @security @destructive
  Scenario: Delete profile
    When the user selects the delete profile option
    And confirms the deletion
    Then the profile should be permanently deleted

  @authentication
  Scenario: User logout
    When the user clicks the logout button
    Then the user should be logged out and redirected to the login page

  @terms_privacy
  Scenario: View terms and privacy
    When the user clicks on terms and privacy
    Then the terms and privacy policy should be displayed

  @brand_management
  Scenario: Update brand profile information
    When the user updates brand profile information
    And clicks the save button on profile page
    Then the brand profile should be successfully updated

  @brand_management
  Scenario: Modify brand settings
    When the user modifies brand settings
    And clicks the save button on profile page
    Then the brand settings should be successfully updated