Feature: User login

Scenario: Validate user is redirected to home page after successful login
        Given the user is on the login page
        When the user enters valid credentials
        Then the user should be redirected back to the original URL