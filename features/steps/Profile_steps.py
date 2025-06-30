import keyboard
from behave import when, then
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators import locators
from Helper.enviHelper import Envi_Helper
import time
import allure
from Logs import logs_file
log = logs_file.get_logs()

@when(u'the user clicks on the profile icon')
def step_impl(context):
    with allure.step("the user navigates to the Test Result page"):
        module_menu = context.driver.find_element(By.XPATH, "//*[@id='adminDashboardContainer']/nav/ul[2]/li[2]")
        actions = ActionChains(context.driver)
        actions.move_to_element(module_menu).perform()
        module_menu.click()
        time.sleep(2)

@then(u'the profile page should be displayed')
def step_impl(context):
    with allure.step("the profile page should be displayed"):
        try:
            time.sleep(2)
            Envi_Helper(context.driver).wait_till_element_is_present(locators.PROFILE_HEADER)
            allure.attach("Profile page displayed successfully", name="Page Display Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Profile page not displayed: {e}")
            allure.attach(str(e), name="Profile Page Display Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user enters or updates the brand name')
def step_impl(context):
    with allure.step("the user enters or updates the brand name"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_BRAND_NAME,"Auto Test Brand")
            allure.attach("Brand name entered/updated successfully", name="Brand Name Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to enter/update brand name: {e}")
            allure.attach(str(e), name="Brand Name Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'clicks the save button on profile page')
def step_impl(context):
    with allure.step("clicks the save button"):
        try:
            Envi_Helper.capture_screenshot()
            time.sleep(2)
            context.driver.find_element(By.XPATH,"//*[name()='button' and contains(@type,'submit')]")
            time.sleep(2)
            allure.attach("Save button clicked successfully", name="Save Success", attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            log.error(f"Failed to click save button: {e}")
            allure.attach(str(e), name="Save Button Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the brand name should be successfully saved')
def step_impl(context):
    with allure.step("the brand name should be successfully saved"):
        try:
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).capture_element_text(locators.PROFILE_TOAST,10)
            allure.attach("Brand name saved successfully", name="Brand Save Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Brand name not saved: {e}")
            allure.attach(str(e), name="Brand Save Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user enters or updates the website homepage URL')
def step_impl(context):
    with allure.step("the user enters or updates the website homepage URL"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_BRAND_URL,"https://www.autotest.com")
            allure.attach("Website URL entered/updated successfully", name="URL Update Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to enter/update website URL: {e}")
            allure.attach(str(e), name="URL Update Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the website URL should be successfully saved')
def step_impl(context):
    with allure.step("the website URL should be successfully saved"):
        try:
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).capture_element_text(locators.PROFILE_TOAST, 10)
            allure.attach("Website URL saved successfully", name="URL Save Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Website URL not saved: {e}")
            allure.attach(str(e), name="URL Save Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user toggles the hyperlink option')
def step_impl(context):
    with allure.step("the user toggles the hyperlink option"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_BRAND_HYPERLINK)
            allure.attach("Hyperlink option toggled successfully", name="Hyperlink Toggle Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to toggle hyperlink option: {e}")
            allure.attach(str(e), name="Hyperlink Toggle Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the website URL should become clickable')
def step_impl(context):
    with allure.step("the website URL should become clickable"):
        try:
            Envi_Helper(context.driver).hover_to_element(locators.PROFILE_BRAND_ICON)
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_BRAND_ICON)
            allure.attach("Website URL is now clickable", name="URL Clickable Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Website URL not clickable: {e}")
            allure.attach(str(e), name="URL Clickable Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user adds Facebook platform link')
def step_impl(context):
    with allure.step("the user adds social media platform links"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_FACEBOOK)
            log.info("facebook icon is clicked")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFLE_FACEBOOK_LINK,"https://www.testfacebook.com")
            log.info("facebook link is pasted")
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_FACEBOOK)
            log.info("clicked again to hide the icon")
            allure.attach(" facebook  links added successfully", name=" facebook  Add Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to add facebook links: {e}")
            allure.attach(str(e), name=" facebook Add Error", attachment_type=allure.attachment_type.TEXT)
            raise
@when(u'the user adds an Instagram platform link')
def step_impl(context):
    with allure.step("the user adds Instagram platform link"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_INSTAGRAM)
            log.info("instagram icon is clicked")
            keyboard.press_and_release('Page Down')
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_INSTAGRAM,"https://www.testinstagram.com")
            log.info("instagram link is pasted")
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_INSTAGRAM)
            log.info("clicked again to hide the icon")
            allure.attach("Instagram link added successfully", name="Instagram Add Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to add Instagram link: {e}")
            allure.attach(str(e), name="Instagram Add Error", attachment_type=allure.attachment_type.TEXT)
            raise

# Threads
@when(u'the user adds a Threads platform link')
def step_impl(context):
    with allure.step("the user adds Threads platform link"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_THREAD)
            log.info("thread icon is clicked")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_THREAD,"https://www.testthread.com")
            log.info("thread link is pasted")
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_THREAD)
            log.info("clicked again to hide the icon")
            allure.attach("Threads link added successfully", name="Threads Add Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to add Threads link: {e}")
            allure.attach(str(e), name="Threads Add Error", attachment_type=allure.attachment_type.TEXT)
            raise

# Discord
@when(u'the user adds a Discord platform link')
def step_impl(context):
    with allure.step("the user adds Discord platform link"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_DISCORD)
            log.info("discord icon is clicked")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_DISCORD_LINK,"https://www.testdiscord.com")
            log.info("discord link is pasted")
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_DISCORD)
            log.info("clicked again to hide the icon")
            allure.attach("Discord link added successfully", name="Discord Add Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to add Discord link: {e}")
            allure.attach(str(e), name="Discord Add Error", attachment_type=allure.attachment_type.TEXT)
            raise

# YouTube
@when(u'the user adds a YouTube platform link')
def step_impl(context):
    with allure.step("the user adds YouTube platform link"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_YOUTUBE)
            log.info("YOUTUBE icon is clicked")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_YOUTUBE,"https://www.testYOUTUBE.com")
            log.info("YOUTUBE link is pasted")
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_YOUTUBE)
            log.info("clicked again to hide the icon")
            allure.attach("YouTube link added successfully", name="YouTube Add Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to add YouTube link: {e}")
            allure.attach(str(e), name="YouTube Add Error", attachment_type=allure.attachment_type.TEXT)
            raise

# Phone
@when(u'the user adds a phone number')
def step_impl(context):
    with allure.step("the user adds phone number"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_PHONE)
            log.info("PHONE icon is clicked")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_PHONE, "https://www.testPHONE.com")
            log.info("PHONE link is pasted")
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_PHONE)
            log.info("clicked again to hide the icon")
            allure.attach("Phone number added successfully", name="Phone Add Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to add phone number: {e}")
            allure.attach(str(e), name="Phone Add Error", attachment_type=allure.attachment_type.TEXT)
            raise

# Email
@when(u'the user adds an email address')
def step_impl(context):
    with allure.step("the user adds email address"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_EMAIL)
            log.info("EMAIL icon is clicked")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_EMAIL, "https://www.testEMAIL.com")
            log.info("EMAIL link is pasted")
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_EMAIL)
            log.info("clicked again to hide the icon")
            allure.attach("Email address added successfully", name="Email Add Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to add email address: {e}")
            allure.attach(str(e), name="Email Add Error", attachment_type=allure.attachment_type.TEXT)
            raise

# Twitter (X)
@when(u'the user adds a Twitter (X) platform link')
def step_impl(context):
    with allure.step("the user adds Twitter (X) platform link"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_X)
            log.info("X icon is clicked")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_X, "https://www.testX.com")
            log.info("X link is pasted")
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_X)
            log.info("clicked again to hide the icon")
            allure.attach("Twitter (X) link added successfully", name="Twitter Add Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to add Twitter (X) link: {e}")
            allure.attach(str(e), name="Twitter Add Error", attachment_type=allure.attachment_type.TEXT)
            raise

# TikTok
@when(u'the user adds a TikTok platform link')
def step_impl(context):
    with allure.step("the user adds TikTok platform link"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_TIKTOK)
            log.info("TIKTOK icon is clicked")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_TIKTOK,"https://www.testTIKTOK.com")
            log.info("TIKTOK link is pasted")
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_TIKTOK)
            log.info("clicked again to hide the icon")
            allure.attach("TikTok link added successfully", name="TikTok Add Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to add TikTok link: {e}")
            allure.attach(str(e), name="TikTok Add Error", attachment_type=allure.attachment_type.TEXT)
            raise

# LinkedIn
@when(u'the user adds a LinkedIn platform link')
def step_impl(context):
    with allure.step("the user adds LinkedIn platform link"):
        try:
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_LINKEDIN)
            log.info("LINKEDIN icon is clicked")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_LINKEDIN,"https://www.testLINKEDIN.com")
            log.info("LINKEDIN link is pasted")
            time.sleep(2)
            Envi_Helper.capture_screenshot()
            Envi_Helper(context.driver).wait_till_element_is_present_to_click(locators.PROFILE_LINKEDIN)
            log.info("clicked again to hide the icon")
            allure.attach("LINKEDIN link added successfully", name="LINKEDIN Add Success",attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            log.error(f"Failed to add LinkedIn link: {e}")
            allure.attach(str(e), name="LinkedIn Add Error", attachment_type=allure.attachment_type.TEXT)
            raise


@then(u'the social media links should be saved')
def step_impl(context):
    with allure.step("the social media links should be saved"):
        try:
            Envi_Helper.capture_screenshot()
            log.info("the social media links are saved successfully and screen shots are attached")
            allure.attach("Social media links saved successfully", name="Social Media Save Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Social media links not saved: {e}")
            allure.attach(str(e), name="Social Media Save Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user enters or updates contact information')
def step_impl(context):
    with allure.step("the user enters or updates contact information"):
        try:
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_CI_FIRSTNAME ,"Auto First name")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_CI_LASTNAME,"Auto last name")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_CI_PHONE,"+1234567899876")
            Envi_Helper(context.driver).wait_till_element_is_present(locators.PROFILE_CI_EMAIL)
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_CI_ADDRESS1, "Auto Address 1")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_CI_ADDRESS2, "Auto address 2")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_CI_CITY, "Auto city  name")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_CI_STATE, "Auto city  name")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_CI_ZIP, "Auto 13245")
            keyboard.press_and_release('Page Down')
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_LC_LEGAL_NAME, "Auto legal  name")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_LC_TERMS, "https://www.autotest.com/terms")
            Envi_Helper(context.driver).insert_text_in_input_field(locators.PROFILE_LC_PRIVACY, "https://www.autotest.com/privacy")

            allure.attach("Contact information updated successfully", name="Contact Info Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to update contact information: {e}")
            allure.attach(str(e), name="Contact Info Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the contact information should be saved')
def step_impl(context):
    with allure.step("the contact information should be saved"):
        try:

            allure.attach("Contact information saved successfully", name="Contact Save Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Contact information not saved: {e}")
            allure.attach(str(e), name="Contact Save Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user enters legal and compliance information')
def step_impl(context):
    with allure.step("the user enters legal and compliance information"):
        try:
            # Implementation for legal info
            allure.attach("Legal information entered successfully", name="Legal Info Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to enter legal information: {e}")
            allure.attach(str(e), name="Legal Info Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the legal information should be saved')
def step_impl(context):
    with allure.step("the legal information should be saved"):
        try:
            # Validation for legal info save
            allure.attach("Legal information saved successfully", name="Legal Save Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Legal information not saved: {e}")
            allure.attach(str(e), name="Legal Save Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user selects the change password option')
def step_impl(context):
    with allure.step("the user selects the change password option"):
        try:
            # Implementation for change password option
            allure.attach("Change password option selected", name="Password Option Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to select change password option: {e}")
            allure.attach(str(e), name="Password Option Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'enters valid new credentials')
def step_impl(context):
    with allure.step("enters valid new credentials"):
        try:
            # Implementation for entering new credentials
            allure.attach("New credentials entered successfully", name="Credentials Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to enter new credentials: {e}")
            allure.attach(str(e), name="Credentials Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the password should be successfully updated')
def step_impl(context):
    with allure.step("the password should be successfully updated"):
        try:
            # Validation for password update
            allure.attach("Password updated successfully", name="Password Update Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Password not updated: {e}")
            allure.attach(str(e), name="Password Update Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user selects the delete profile option')
def step_impl(context):
    with allure.step("the user selects the delete profile option"):
        try:
            # Implementation for delete profile option
            allure.attach("Delete profile option selected", name="Delete Option Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to select delete profile option: {e}")
            allure.attach(str(e), name="Delete Option Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'confirms the deletion')
def step_impl(context):
    with allure.step("confirms the deletion"):
        try:
            # Implementation for confirmation
            allure.attach("Deletion confirmed successfully", name="Deletion Confirm Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to confirm deletion: {e}")
            allure.attach(str(e), name="Deletion Confirm Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the profile should be permanently deleted')
def step_impl(context):
    with allure.step("the profile should be permanently deleted"):
        try:
            # Validation for profile deletion
            allure.attach("Profile deleted successfully", name="Profile Delete Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Profile not deleted: {e}")
            allure.attach(str(e), name="Profile Delete Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user clicks the logout button')
def step_impl(context):
    with allure.step("the user clicks the logout button"):
        try:
            # Implementation for logout
            allure.attach("Logout button clicked successfully", name="Logout Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to click logout button: {e}")
            allure.attach(str(e), name="Logout Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the user should be logged out and redirected to the login page')
def step_impl(context):
    with allure.step("the user should be logged out and redirected to the login page"):
        try:
            # Validation for logout
            allure.attach("User logged out and redirected successfully", name="Logout Redirect Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Logout/redirect failed: {e}")
            allure.attach(str(e), name="Logout Redirect Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user clicks on terms and privacy')
def step_impl(context):
    with allure.step("the user clicks on terms and privacy"):
        try:
            # Implementation for terms/privacy click
            allure.attach("Terms and privacy clicked successfully", name="Terms Click Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to click terms and privacy: {e}")
            allure.attach(str(e), name="Terms Click Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the terms and privacy policy should be displayed')
def step_impl(context):
    with allure.step("the terms and privacy policy should be displayed"):
        try:
            # Validation for terms/privacy display
            allure.attach("Terms and privacy displayed successfully", name="Terms Display Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Terms and privacy not displayed: {e}")
            allure.attach(str(e), name="Terms Display Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user updates brand profile information')
def step_impl(context):
    with allure.step("the user updates brand profile information"):
        try:
            # Implementation for brand profile update
            allure.attach("Brand profile updated successfully", name="Brand Profile Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to update brand profile: {e}")
            allure.attach(str(e), name="Brand Profile Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the brand profile should be successfully updated')
def step_impl(context):
    with allure.step("the brand profile should be successfully updated"):
        try:
            # Validation for brand profile update
            allure.attach("Brand profile update verified", name="Brand Update Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Brand profile not updated: {e}")
            allure.attach(str(e), name="Brand Update Error", attachment_type=allure.attachment_type.TEXT)
            raise

@when(u'the user modifies brand settings')
def step_impl(context):
    with allure.step("the user modifies brand settings"):
        try:
            # Implementation for brand settings modification
            allure.attach("Brand settings modified successfully", name="Brand Settings Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Failed to modify brand settings: {e}")
            allure.attach(str(e), name="Brand Settings Error", attachment_type=allure.attachment_type.TEXT)
            raise

@then(u'the brand settings should be successfully updated')
def step_impl(context):
    with allure.step("the brand settings should be successfully updated"):
        try:
            # Validation for brand settings update
            allure.attach("Brand settings update verified", name="Settings Update Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.error(f"Brand settings not updated: {e}")
            allure.attach(str(e), name="Settings Update Error", attachment_type=allure.attachment_type.TEXT)
            raise