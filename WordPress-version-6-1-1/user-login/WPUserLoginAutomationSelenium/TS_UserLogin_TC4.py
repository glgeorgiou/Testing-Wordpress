"""
User Login Scenario. Test Case No4
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Pre-requisite: Open the login WordPress site in Firefox
fxDriver = webdriver.Firefox()
fxDriver.get('https://wordpresstest.ggeorgiou.work/wp-login.php')

# Enter an invalid user name
fxDriver.find_element(By.ID, 'user_login').send_keys('invalidUserName')

# Enter an invalid password
fxDriver.find_element(By.ID, 'user_pass').send_keys('invalidPassWord')

# Click on "Login" button
fxDriver.find_element(By.ID, 'wp-submit').click();

# Evaluate the test case
errText = fxDriver.find_element(By.ID, 'login_error').text
assert "The username invalidUserName is not registered on this site" in errText

fxDriver.close() # closes the driver