import time
from locator import *
from element import BasePageElement, BasePageElementById
from selenium.webdriver.support.color import Color

class UsernameTextElement(BasePageElement):
    locator = 'username'

class EmailTextElement(BasePageElement):
    locator = 'email'

class PasswordTextElement(BasePageElement):
    locator = 'password'

class ConfirmPasswordTextElement(BasePageElement):
    locator = 'confirm_password'

class ActuatorNameTextElement(BasePageElementById):
    locator = 'nameActuator'

class ActuatorIpTextElement(BasePageElementById):
    locator = 'ipActuator'

class ControllerNameTextElement(BasePageElementById):
    locator = 'nameController'

class ControllerRedTextElement(BasePageElementById):
    locator = 'redController'

class ControllerGreenTextElement(BasePageElementById):
    locator = 'greenController'

class ControllerBlueTextElement(BasePageElementById):
    locator = 'blueController'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    # These elements provide descriptor methods to retrieve and change
    #   the values in an element.
    username_text_element = UsernameTextElement()
    password_text_element = PasswordTextElement()

    def is_title_matches(self):
        return 'Sign in - Smart Home Assistant' in self.driver.title

    def click_submit_button(self):
        element = self.driver.find_element(*LoginPageLocator.SUBMIT_BUTTON)
        element.click()

class RegisterPage(BasePage):
    # These elements provide descriptor methods to retrieve and change
    #   the values in an element.
    username_text_element = UsernameTextElement()
    email_text_element = EmailTextElement()
    password_text_element = PasswordTextElement()
    confirm_password_text_element = ConfirmPasswordTextElement()

    def is_title_matches(self):
        return 'Sign up - Smart Home Assistant' in self.driver.title

    def click_submit_button(self):
        element = self.driver.find_element(*LoginPageLocator.SUBMIT_BUTTON)
        element.click()

class DashboardPage(BasePage):
    # These elements provide descriptor methods to retrieve and change
    #   the values in an element.
    actuator_name_text_element = ActuatorNameTextElement()
    actuator_ip_text_element = ActuatorIpTextElement()
    controller_name_text_element = ControllerNameTextElement()
    controller_red_text_element = ControllerRedTextElement()
    controller_green_text_element = ControllerGreenTextElement()    
    controller_blue_text_element = ControllerBlueTextElement()

    def is_title_matches(self):
        return 'Index - Smart Home Assistant' in self.driver.title

    # Actuator related functions

    def actuator_click_add_button(self):
        element = self.driver.find_element(*DashboardPageLocator.ACTUATOR_FORM_SHOW_BUTTON)
        element.click()        

    def actuator_click_submit_button(self):
        element = self.driver.find_element(*DashboardPageLocator.ACTUATOR_FORM_SUBMIT_BUTTON)
        element.click()

    def actuator_frame_exists(self):
        if self.driver.find_element(*DashboardPageLocator.ACTUATOR_FRAME):
            return True
        return False

    def actuator_frame_click_delete(self):
        element = self.driver.find_element(*DashboardPageLocator.ACTUATOR_FRAME_DELETE_BUTTON)
        element.click()

    def actuator_frame_click_onoff(self):
        element = self.driver.find_element(*DashboardPageLocator.ACTUATOR_FRAME_ONOFF_BUTTON)
        element.click()

    def is_actuator_on(self):
        color = self.driver.find_element(*DashboardPageLocator.ACTUATOR_FRAME_ONOFF_BUTTON).value_of_css_property('color')        
        hex = Color.from_string(color).hex
        if '#0376fe' == hex:
            return True
        return False

    # Controller related functions

    def controller_click_add_button(self):
        element = self.driver.find_element(*DashboardPageLocator.CONTROLLER_FORM_SHOW_BUTTON)
        element.click()  

    def controller_click_submit_button(self):
        element = self.driver.find_element(*DashboardPageLocator.CONTROLLER_FORM_SUBMIT_BUTTON)
        element.click()

    def controller_frame_exists(self):
        if self.driver.find_element(*DashboardPageLocator.CONTROLLER_FRAME):
            return True
        return False

    def controller_frame_click_delete(self):
        element = self.driver.find_element(*DashboardPageLocator.CONTROLLER_FRAME_DELETE_BUTTON)
        element.click()

    def controller_frame_click_onoff(self):
        element = self.driver.find_element(*DashboardPageLocator.CONTROLLER_FRAME_ONOFF_BUTTON)
        element.click()

    def controller_frame_click_colorshift(self):
        element = self.driver.find_element(*DashboardPageLocator.CONTROLLER_FRAME_COLORSHIFT_BUTTON)
        element.click()

    def is_controller_on(self):
        color = self.driver.find_element(*DashboardPageLocator.CONTROLLER_FRAME_ONOFF_BUTTON).value_of_css_property('color')        
        hex = Color.from_string(color).hex
        if '#0376fe' == hex:
            return True
        return False

    def is_controller_colorshift_on(self):
        color = self.driver.find_element(*DashboardPageLocator.CONTROLLER_FRAME_COLORSHIFT_BUTTON).value_of_css_property('color')        
        hex = Color.from_string(color).hex
        if '#efce6a' == hex:
            return True
        return False