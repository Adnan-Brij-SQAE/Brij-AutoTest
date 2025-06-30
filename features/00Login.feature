#Feature: User login functionality
#  @login
#  Scenario Outline:login with invalid email
#    Given user is on the login page
#    When user input invalid email id "<invalid_login_id>"
#    Then user should see an error message
#
#      Examples: Invalid_Email
#      | invalid_login_id                 |
#      | sheikhsqae+rcbrand13@gmail.com   |
#      | abc@123.com                      |
#
#  Scenario Outline: login with valid email
#      When user entered valid email id "<valid_login_id>"
#      Then user should navigate to password screen
#
#    Examples: Credentials
#      | valid_login_id                 |
#      | sheikhsqae+rcbrand@gmail.com   |
#
#    Scenario Outline: Unsuccessful login with incorrect password
#      When user enter invalid password "<invalid_password>"
#      Then user should see an error message
#
#      Examples: invalid_password
#      | invalid_password   |
#      | brij123    |
#      | Brij@123   |
#
#  Scenario Outline: successful login with valid credentials
#    When user entered correct email id "<login_id>" and password "<password>"
#    Then user should be logged in successfully
#
#    Examples: Credentials
#      | login_id                       | password   |
#      | sheikhsqae+rcbrand@gmail.com   | P@$$w0rd!@ |