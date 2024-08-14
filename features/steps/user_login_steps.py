from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given("the user is on the login page")
def the_user_is_on_the_login_page(context):
        context.driver = webdriver.Chrome()
        context.driver.get('https://bluebird-teaching.com/login') # Change to whatever link you need.

@when("the user enters valid credentials")
def the_user_enters_valid_credentials(context):
        email_field = context.driver.find_element(By.XPATH, "//input[@placeholder='E-mail Address']")
        password_field = context.driver.find_element(By.XPATH, "//input[@placeholder='Password']")

        email_field.send_keys('sample@gmail.com')
        password_field.send_keys('lkajsd;flkj')
        time.sleep(10)
        # password_field.send_keys(Keys.RETURN)

        login_button = context.driver.find_element(By.XPATH, "//button[@class='button']")
        login_button.click()

@then("the user should be redirected back to the original URL")
def the_user_should_be_redirected_back_to_the_original_url(context):
        time.sleep(4)
        assert 'https://bluebird-teaching.com/' in context.driver.current_url
        context.driver.quit()