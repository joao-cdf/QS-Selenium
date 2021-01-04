import unittest
import page
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless")

class Test01_Register(unittest.TestCase):

    # This URL is the result of a successful sign up, 
    # we can use it to verify if the test passed or not.
    _expected_url = 'https://smart-home-assistant.herokuapp.com/sign_in'

    # Setup functions called when initialized
    def setUp(self):
        self.driver = webdriver.Chrome('./driver/chromedriver.exe')
        self.driver.get('https://smart-home-assistant.herokuapp.com/sign_up')

    '''
    Verify if a user cannot sign up when the email field
    is empty.
    '''
    def test011_verify_email_field(self):

        # get register page
        regPage = page.RegisterPage(self.driver)
        assert regPage.is_title_matches()

        # Insert username.
        regPage.username_text_element = 'Tufao'
        
        # Insert email.
        regPage.email_text_element = ''

        # Insert password
        regPage.password_text_element = '123'

        # Insert confirm password
        regPage.confirm_password_text_element = '123'

        # Click button.
        regPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare the current url with the expected one.
        self.assertNotEqual(self.driver.current_url, self._expected_url)
    
    '''
    Verify if a user cannot sign up when the username field
    is empty.
    '''
    def test012_verify_username_field(self):

        # Get the sign up page.
        regPage = page.RegisterPage(self.driver)
        assert regPage.is_title_matches()

        # Insert username.
        regPage.username_text_element = ''

        #insert email
        regPage.email_text_element = 'joaoferreira7991@gmail.com'

        # Insert password.
        regPage.password_text_element = '123'

        # Insert confirm password
        regPage.confirm_password_text_element = '123'

        # Click button.
        regPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare the current url with the expected one.
        self.assertNotEqual(self.driver.current_url, self._expected_url)
    '''
    Verify if a user cannot sign up when the password field
    is empty.
    '''
    def test013_verify_password_field(self):
        # Get the sign up page.
        regPage = page.RegisterPage(self.driver)
        assert regPage.is_title_matches()

        # Insert username.
        regPage.username_text_element = 'Tufao'

        # Insert email.
        regPage.email_text_element = 'joaoferreira7991@gmail.com'

        # Insert password confirmation.
        regPage.password_text_element = ''

        # Insert confirm password
        regPage.confirm_password_text_element = '123'

        # Click button.
        regPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare the current url with the expected one.    
        self.assertNotEqual(self.driver.current_url, self._expected_url)
    '''
    Verify if a user cannot sign up when the password confirm field
    is empty.
    '''
    def test014_verify_password_confirm_field(self):
        # Get the sign up page.
        regPage = page.RegisterPage(self.driver)
        assert regPage.is_title_matches()

        # Insert username.
        regPage.username_text_element = 'Tufao'

        # Insert email.
        regPage.email_text_element = 'joaoferreira7991@gmail.com'

        # Insert password.
        regPage.password_text_element = '123'

        # Insert confirm password
        regPage.confirm_password_text_element = ''

        # Click button.
        regPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare the current url with the expected one.    
        self.assertNotEqual(self.driver.current_url, self._expected_url)
    '''
    Verify if a user cannot login when all fields are empty.
    '''
    def test015_empty_fields(self):
        # Get the sign up page.
        regPage = page.RegisterPage(self.driver)
        assert regPage.is_title_matches()

        # Click button.
        regPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare the current url with the expected one.
        self.assertNotEqual(self.driver.current_url, self._expected_url)

    '''
    Verify if a user will be able to sign up with a valid username, a valid email
    and a valid password with a invalid password confirmation.
    '''
    def test016_invalid_password(self):

        # Get the sign up page.
        regPage = page.RegisterPage(self.driver)
        assert regPage.is_title_matches()

        # Insert username.
        regPage.username_text_element = 'Tufao'

        # Insert email.
        regPage.email_text_element = 'joaoferreira7991@gmail.com'

        # Insert password.
        regPage.password_text_element = '123'

        # Insert different password confirmation.
        regPage.confirm_password_text_element = 'blink182'

        # Click button.
        regPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare the current url with the expected one.
        self.assertNotEqual(self.driver.current_url, self._expected_url)
    '''
    Verify if a user will be able to sign up with a valid username, a valid email
    and a valid password/password confirmation.
    '''
    def test017_valid_sign_up(self):
        # Get the sign up page.
        regPage = page.RegisterPage(self.driver)
        assert regPage.is_title_matches()

        # Insert username.
        regPage.username_text_element = 'Tufao'

        # Insert email.
        regPage.email_text_element = 'joaoferreira7991@gmail.com'

        # Insert password.
        regPage.password_text_element = '123'

        # Insert password confirmation.
        regPage.confirm_password_text_element = '123'

        # Click button.
        regPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare the current url with the expected one. 
        self.assertEqual(self.driver.current_url, self._expected_url)

    # End of test
    def tearDown(self):
        self.driver.close()

class Test02_Login(unittest.TestCase):

    # This URL is only acessible as a result of a sucessful login, 
    # we can use it to verify if the test passed or not.
    _expected_url = 'https://smart-home-assistant.herokuapp.com/index'

    # Setup functions called when initialized
    def setUp(self):
        self.driver = webdriver.Chrome('./driver/chromedriver.exe')
        self.driver.get('https://smart-home-assistant.herokuapp.com/sign_in')

    def test020_verify_username_field(self):
        
        # Get the login page elements.
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare the current url with the expected one.
        self.assertNotEqual(self.driver.current_url, self._expected_url)

    def test021_verify_password_field(self):
        
        # Enter the login page.
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username.
        loginPage.username_text_element = 'Tufao'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare the current url with the expected one.
        self.assertNotEqual(self.driver.current_url, self._expected_url)

    def test022_empty_fields(self):
        
        # Enter the login page.
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare the current url with the expected one.
        self.assertNotEqual(self.driver.current_url, self._expected_url)

    def test023_invalid_password(self):
    
        # Enter the login page.
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()
        
        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '124'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertNotEqual(self.driver.current_url, self._expected_url)    

    def test024_valid_sign_in(self):
        
        # Enter the login page.
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()
        
        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)

    # End of test
    def tearDown(self):
        self.driver.close()

class Test03_Dashboard(unittest.TestCase):
    
    # This URL is only acessible as a result of a sucessful login, 
    # we can use it to verify if the test passed or not.
    _expected_url = 'https://smart-home-assistant.herokuapp.com/index'

    # Setup functions called when initialized
    def setUp(self):
        self.driver = webdriver.Chrome('./driver/chromedriver.exe')
        self.driver.get('https://smart-home-assistant.herokuapp.com/sign_in')

    # Actuator form related tests.
    
    '''
    Test if the user cannot submit the actuator form with all fields empty
    '''
    def test0300_actuator_form_all_fields_empty(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)

        dbPage = page.DashboardPage(self.driver)        
        assert dbPage.is_title_matches()

        # Click the add actuator button
        dbPage.actuator_click_add_button()

        # Insert empty name
        dbPage.actuator_name_text_element = ''

        # Insert empty IPv4 address
        dbPage.actuator_ip_text_element = ''

        # Click button
        dbPage.actuator_click_submit_button()

        # Wait 1 second
        time.sleep(1)

        # Verify if both fields had been filled with 'Required Field.'
        self.assertEqual('Required Field.', dbPage.actuator_name_text_element)
        self.assertEqual('Required Field.', dbPage.actuator_ip_text_element)

    '''
    Test if the user cannot submit the actuator form with an empty device name.
    '''
    def test0301_actuator_form_name_field_empty(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click the add actuator button
        dbPage.actuator_click_add_button()

        # Insert empty name
        dbPage.actuator_name_text_element = ''

        # Insert empty IPv4 address
        dbPage.actuator_ip_text_element = '192.168.1.65'

        # Click button
        dbPage.actuator_click_submit_button()

        # Wait 1 second
        time.sleep(1)

        # Verify if name field has been filled with 'Required Field.'
        self.assertEqual('Required Field.', dbPage.actuator_name_text_element)

    '''
    Test if the user cannot submit the actuator forum with an empty ip field.
    '''
    def test0302_actuator_form_ip_field_empty(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click the add actuator button
        dbPage.actuator_click_add_button()

        # Insert empty name
        dbPage.actuator_name_text_element = 'smart switch'

        # Insert empty IPv4 address
        dbPage.actuator_ip_text_element = ''

        # Click button
        dbPage.actuator_click_submit_button()

        # Wait 1 second
        time.sleep(1)

        # Verify if ip field has been filled with 'Required Field.'
        self.assertEqual('Required Field.', dbPage.actuator_ip_text_element)

    '''
    Test if the user can submit an appropriate actuator form
    '''
    def test0303_actuator_form_success(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click the add actuator button
        dbPage.actuator_click_add_button()

        # Insert name
        dbPage.actuator_name_text_element = 'smart switch'

        # Insert empty IPv4 address
        dbPage.actuator_ip_text_element = '192.168.1.65'

        # Click button
        dbPage.actuator_click_submit_button()

        # Wait 1 second
        time.sleep(1)

        # Check if a new actuator frame was created.
        assert dbPage.actuator_frame_exists()

    # Controller form related tests.
    
    def test0304_controller_form_all_fields_empty(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click the add controller button
        dbPage.controller_click_add_button()

        # Insert empty name
        dbPage.controller_name_text_element = ''

        # Insert empty red
        dbPage.controller_red_text_element = ''

        # Insert empty green
        dbPage.controller_green_text_element = ''

        # Insert empty blue
        dbPage.controller_blue_text_element = ''

        # Click button
        dbPage.controller_click_submit_button()

        # Wait 1 second
        time.sleep(1)

        # Verify if all fields had been filled with 'Required Field.'
        self.assertEqual('Required Field.', dbPage.controller_name_text_element)
        self.assertEqual('Required Field.', dbPage.controller_red_text_element)
        self.assertEqual('Required Field.', dbPage.controller_green_text_element)
        self.assertEqual('Required Field.', dbPage.controller_blue_text_element)

    def test0305_controller_form_name_field_empty(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click the add controller button
        dbPage.controller_click_add_button()

        # Insert empty name
        dbPage.controller_name_text_element = ''

        # Insert empty red
        dbPage.controller_red_text_element = '17'

        # Insert empty green
        dbPage.controller_green_text_element = '27'

        # Insert empty blue
        dbPage.controller_blue_text_element = '22'

        # Click button
        dbPage.controller_click_submit_button()

        # Wait 1 second
        time.sleep(1)

        # Verify if name field has been filled with 'Required Field.'
        self.assertEqual('Required Field.', dbPage.controller_name_text_element)

    def test0306_controller_form_red_field_empty(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click the add controller button
        dbPage.controller_click_add_button()

        # Insert empty name
        dbPage.controller_name_text_element = 'led strip'

        # Insert empty red
        dbPage.controller_red_text_element = ''

        # Insert empty green
        dbPage.controller_green_text_element = '27'

        # Insert empty blue
        dbPage.controller_blue_text_element = '22'

        # Click button
        dbPage.controller_click_submit_button()

        # Wait 1 second
        time.sleep(1)

        # Verify if red field has been filled with 'Required Field.'
        self.assertEqual('Required Field.', dbPage.controller_red_text_element)

    def test0307_controller_form_green_field_empty(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click the add controller button
        dbPage.controller_click_add_button()

        # Insert empty name
        dbPage.controller_name_text_element = 'led strip'

        # Insert empty red
        dbPage.controller_red_text_element = '17'

        # Insert empty green
        dbPage.controller_green_text_element = ''

        # Insert empty blue
        dbPage.controller_blue_text_element = '22'

        # Click button
        dbPage.controller_click_submit_button()

        # Wait 1 second
        time.sleep(1)

        # Verify if green field has been filled with 'Required Field.'
        self.assertEqual('Required Field.', dbPage.controller_green_text_element)           

    def test0308_controller_form_blue_field_empty(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click the add controller button
        dbPage.controller_click_add_button()

        # Insert empty name
        dbPage.controller_name_text_element = 'led strip'

        # Insert empty red
        dbPage.controller_red_text_element = '17'

        # Insert empty green
        dbPage.controller_green_text_element = '27'

        # Insert empty blue
        dbPage.controller_blue_text_element = ''

        # Click button
        dbPage.controller_click_submit_button()

        # Wait 1 second
        time.sleep(1)

        # Verify if blue field has been filled with 'Required Field.'
        self.assertEqual('Required Field.', dbPage.controller_blue_text_element)

    def test0309_controller_form_malformed_pin_values(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click the add controller button
        dbPage.controller_click_add_button()

        # Insert empty name
        dbPage.controller_name_text_element = 'led strip'

        # Insert empty red
        dbPage.controller_red_text_element = 'qwrwerqr'

        # Insert empty green
        dbPage.controller_green_text_element = 'qwerwerqw'

        # Insert empty blue
        dbPage.controller_blue_text_element = 'werwrw'

        # Click button
        dbPage.controller_click_submit_button()

        # Wait 1 second
        time.sleep(1)

        # Verify if pin fields have been filled with 'Required Field.'
        self.assertEqual('Required Field.', dbPage.controller_red_text_element)
        self.assertEqual('Required Field.', dbPage.controller_green_text_element)
        self.assertEqual('Required Field.', dbPage.controller_blue_text_element)

    def test0310_controller_form_success(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click the add controller button
        dbPage.controller_click_add_button()

        # Insert empty name
        dbPage.controller_name_text_element = 'led strip'

        # Insert empty red
        dbPage.controller_red_text_element = '17'

        # Insert empty green
        dbPage.controller_green_text_element = '27'

        # Insert empty blue
        dbPage.controller_blue_text_element = '22'

        # Click button
        dbPage.controller_click_submit_button()

        # Wait 1 second
        time.sleep(1)

        # Check if a new actuator frame was created.
        assert dbPage.controller_frame_exists()

    # Actuator button related tests.

    def test0311_actuator_frame_onoff_button(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click button then wait for it turn on
        dbPage.actuator_frame_click_onoff()
        time.sleep(5)

        # Assert if color has changed
        assert dbPage.is_actuator_on()

    def test0312_actuator_frame_delete_button(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click delete button
        dbPage.actuator_frame_click_delete()

        # Check if it exists
        assert dbPage.actuator_frame_exists()

    # Controller button related tests.

    def test0313_controller_frame_colorshift_button_while_off(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click coloshift button
        dbPage.controller_frame_click_colorshift()

        # Check if it changed color
        assert not (dbPage.is_controller_colorshift_on())

    def test0314_controller_frame_onoff_button(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click button then wait for it turn on
        dbPage.controller_frame_click_onoff()
        time.sleep(5)

        # Assert if color has changed
        assert dbPage.is_controller_on()

    def test0315_controller_frame_colorshift_button_while_on(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click colorshift button
        dbPage.controller_frame_click_colorshift()
        time.sleep(5)

        # Check if it changed color
        assert dbPage.is_controller_colorshift_on()

    def test0316_controller_frame_delete_button(self):
        # Get sign in page
        loginPage = page.LoginPage(self.driver)
        assert loginPage.is_title_matches()

        # Insert username that is valid for login.
        loginPage.username_text_element = 'Tufao'

        # Insert correct password.
        loginPage.password_text_element = '123'

        # Click button.
        loginPage.click_submit_button()

        # Wait 1 second 
        time.sleep(1)

        # Compare current url with the expected one.
        self.assertEqual(self.driver.current_url, self._expected_url)        
        
        # Get dashboard page
        dbPage = page.DashboardPage(self.driver)
        assert dbPage.is_title_matches()

        # Click delete button
        dbPage.controller_frame_click_delete()

        # Check if it exists
        assert dbPage.controller_frame_exists()
    
    # End of test
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)