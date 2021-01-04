from selenium.webdriver.common.by import By


# Each class records every necessary id from a page,
#   to help distinguish variables with the same name
#   but from a different page.

class LoginPageLocator(object):
    SUBMIT_BUTTON = (By.ID, 'submit')

class RegisterPageLocator(object):
    SUBMIT_BUTTON = (By.ID, 'submit')

class DashboardPageLocator(object):
    ACTUATOR_FORM_SHOW_BUTTON = (By.ID, 'button_addActuator')
    ACTUATOR_FORM_SUBMIT_BUTTON = (By.ID, 'submitActuator')
    CONTROLLER_FORM_SHOW_BUTTON = (By.ID, 'button_addController')
    CONTROLLER_FORM_SUBMIT_BUTTON = (By.ID, 'submitController')
    ACTUATOR_FRAME = (By.CSS_SELECTOR, '[id^=led-switch]')
    CONTROLLER_FRAME = (By.CSS_SELECTOR, '[id^=led-controller]')
    ACTUATOR_FRAME_DELETE_BUTTON = (By.CSS_SELECTOR, '[id^=del-button]')
    ACTUATOR_FRAME_ONOFF_BUTTON = (By.CSS_SELECTOR, '[id^=switch-onoff]')
    CONTROLLER_FRAME_DELETE_BUTTON = (By.CSS_SELECTOR, '[id^=del-button]')
    CONTROLLER_FRAME_ONOFF_BUTTON = (By.CSS_SELECTOR, '[id^=controller-onoff]')
    CONTROLLER_FRAME_COLORSHIFT_BUTTON = (By.CSS_SELECTOR, '[id^=controller-colorshift]')
