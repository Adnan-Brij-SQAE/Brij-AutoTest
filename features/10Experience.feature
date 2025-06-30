Feature: Experience Page Management

  @allure.feature.ExperiencePage @navigation
  Scenario: The user accesses the Experience page
    When the user navigates to the Experience page
    Then the Experience page is displayed

#  @allure.feature.FilteringStatus @filters
#  Scenario: The user can filter with Status
#    When the user filters by Status
#    Then only experiences with that status are shown
#
#  @allure.feature.FilteringCategory @filters
#  Scenario: The user can filter with Category
#    When the user filters by Category
#    Then only experiences with that category are shown
#
#  @allure.feature.FilteringExperienceType @filters
#  Scenario: The user can filter with Experience Types
#    When the user filters by Experience Types
#    Then only experiences with that type are shown
#
#  @allure.feature.Navigation @navigation
#  Scenario: The user access notification panel
#    When the user clicks the notification icon
#    Then notifications are shown
#
#  @allure.feature.Navigation @navigation
#  Scenario: The user can access logout icon
#    When the user clicks the logout icon
#    Then the user is logged out
#
#  @allure.feature.count @Count
#  Scenario: The user get the count of experience
#    When the user get the experience count
#    Then the total experience count should be displayed
#
#  @allure.feature.Field @Field
#  Scenario: The user can access field button
#    When the user access the field button
#    Then user can display columns according to fields selected
#
#  @allure.feature.Sorting @table
#  Scenario: The user can sort the Experience table
#    When the user sorts by a columns
#    Then the table is sorted accordingly
##
#  @allure.feature.Searching @search
#  Scenario: The user can search within Experiences
#    When the user searches for an experience
#    Then matching experiences are displayed

#  @allure.feature.AddWebApp @experience
#  Scenario: The user can add web apps experience
#    When the user adds a new web apps experience
#    Then the experience is added successfully

#  @allure.feature.EditExperience @experience
#  Scenario: The user can edit web apps experience
#    Given a web apps experience exists
#    When the user edits the web apps experience
#    Then the changes are saved

#  @allure.feature.AddRebate @experience
#  Scenario: The user can add rebate experience
#    When the user adds a new rebate experience
#    Then the experience is added successfully
##
#  @allure.feature.EditRebate@experience
#  Scenario: The user can edit rebate experience
#    Given a rebate experience exists
#    When the user edits the rebate experience
#    Then the changes are saved
#
#  @allure.feature.AddDynamicLink @experience
#  Scenario: The user can add Dynamic link experience
#    When the user adds a new Dynamic Link experience
#    Then the experience is added successfully
#
#  @allure.feature.EditDynamicLink @experience
#  Scenario: The user can edit dynamic link experience
#    Given a dynamic link experience exists
#    When the user edits the dynamic link experience
#    Then the changes are saved
#
#  @allure.feature.AddDigitalHub @experience
#  Scenario: The user can add Digital Hub experience
#    When the user adds a new Digital Hub experience
#    Then the experience is added successfully
###
##  @allure.feature.EditDigitalHub @experience
#  Scenario: The user can edit Digital Hub experience
#    Given a Digital Hub experience exists
#    When the user edits the Digital Hub experience
#    Then the changes are saved
#
#  @allure.feature.Variants @variant
#  Scenario: The user can add web apps variant with hierarchy
#    Given the user is on a web apps experience
#    When the user adds a variant
#    Then the variant is added successfully
#
#  @allure.feature.Variants @variant
#  Scenario: The user can edit web apps variant to decentralized
#    Given a web apps variant exists
#    When the user edits the variant
#    Then the changes are saved
#
#  @allure.feature.Variants @variant
#  Scenario: The user can add rebate variant with hierarchy
#    Given the user is on a rebate experience
#    When the user adds a variant
#    Then the variant is added successfully
#
#  @allure.feature.Variants @variant
#  Scenario: The user can edit rebate variant to decentralized
#    Given a rebate variant exists
#    When the user edits the variant
#    Then the changes are saved
#
#  @allure.feature.Variants @variant
#  Scenario: The user can add Dynamic link variant with hierarchy
#    Given the user is on a Dynamic Link experience
#    When the user adds a variant
#    Then the variant is added successfully
#
#  @allure.feature.Variants @variant
#  Scenario: The user can edit dynamic link variant to decentralized
#    Given a Dynamic Link variant exists
#    When the user edits the variant
#    Then the changes are saved
#
#  @allure.feature.Variants @variant
#  Scenario: The user can add Digital Hub variant with hierarchy
#    Given the user is on a Digital Hub experience
#    When the user adds a variant
#    Then the variant is added successfully
#
#  @allure.feature.Variants @variant
#  Scenario: The user can edit Digital Hub variant to decentralized
#    Given a Digital Hub variant exists
#    When the user edits the variant
#    Then the changes are saved
#
#  @allure.feature.AddExperience @addExperience
#  Scenario: The user can add experience with registration and modules
#    When the user adds a new experience with registration and modules
#    Then the experience is added with modules
#
#  @allure.feature.AddExperience @form
#  Scenario: The user can add experience without registrations and modules
#    When the user adds a new experience without registration and modules
#    Then the experience is added successfully
##
#  @allure.feature.AddVerificationCriteria @WebApp
#  Scenario: The user can add verification criteria in Web App
#    When the user is creating a new Verification Criteria in Web App experience
#    Then the criteria are saved
#
#  @allure.feature.AddVerificationCriteria @Registration
#  Scenario: The user can add verification criteria in Registration
#    When the user is creating a new Verification Criteria in Registration experience
#    Then the criteria are saved
#
#  @allure.feature.AddVerificationCriteria @RebateCampaign
#  Scenario: The user can add verification criteria in Rebate Campaign
#    When the user is creating a new Verification Criteria in Rebate Campaign experience
#    Then the criteria are saved
#
#  @allure.feature.AddVerificationCriteria @Rebate
#  Scenario: The user can add verification criteria in Rebate
#    When the user is creating a new Verification Criteria in Rebate experience
#    Then the criteria are saved
#
#  @allure.feature.AddVerificationCriteria @DigitalHub
#  Scenario: The user can add verification criteria in Digital Hub
#    When the user is creating a new Verification Criteria inDigital Hub experience
#    Then the criteria are saved
#
#  @allure.feature.AddContentGate @WebApp
#  Scenario: The user can add content gate in Web App
#    When the user is creating a new Content Gate in Web App experience
#    Then the content gate is saved
#
#  @allure.feature.AddContentGate @Rebate
#  Scenario: The user can add content gate in Rebate
#    When the user is creating a new Content Gate in Rebate experience
#    Then the content gate is saved
#
#  @allure.feature.AddContentGate @DigitalHub
#  Scenario: The user can add content gate in Digital Hub
#    When the user is creating a new Content Gate in Digital Hub experience
#    Then the content gate is saved
##
#  @allure.feature.Analytics @hover
#  Scenario: The user can show QR code on hover
#    Given the user hovers over the QR code icon
#    Then the QR code preview appears
#
#  @allure.feature.Analytics @hover
#  Scenario: Hover the experience analytics
#    Given the user hovers on the analytics icon
#    Then the tooltip with analytics preview is displayed
#
#  @allure.feature.Code @code
#  Scenario: The user can get embed code for the experience
#    When the user clicks on "Get Embed Code"
#    Then the embed code is shown
#
#  @allure.feature.Duplicate @duplicate
#  Scenario: The user can duplicate experience
#    When the user duplicates an experience
#    Then a new copy of the experience is created
#
#  @allure.feature.Status @status
#  Scenario: The user can deactivate experience
#    When the user deactivates an experience
#    Then the experience status is updated to inactive
#
#  @allure.feature.ImportExport @import
#  Scenario: The user can import one or more experiences
#    When the user imports experiences
#    Then the experiences appear in the list
#
#  @allure.feature.ImportExport @export
#  Scenario: The user can export one or more experiences
#    When the user exports experiences
#    Then the export file is generated
#
#  @allure.feature.Syncing @sync
#  Scenario: The user can sync one or more experiences
#    When the user syncs experiences
#    Then the experiences are updated
#
#  @allure.feature.ShopifyIntegration @import
#  Scenario: The user can import experience with Shopify import
#    When the user imports using Shopify
#    Then the experience appears in the list
#
#  @allure.feature.Pagination @pagination
#  Scenario: The user can test pagination of experience page
#    When the user navigates through pages
#    Then the correct number of experiences is shown per page
#
#
#  @allure.feature.Analytics @analytics
#  Scenario: The user can view experience analytics
#    When the user clicks on the analytics icon
#    Then analytics data for the experience is displayed
#
#  @allure.feature.Code @code
#  Scenario: The user can view all codes
#    When the user selects "View All Codes"
#    Then a list of codes is shown
#
#  @allure.feature.Variants @variant-list
#  Scenario: The user can show variant list of experience
#    When the user expands the experience row
#    Then all variants are listed
#
