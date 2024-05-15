from selenium import webdriver
from locators.page_locators import home_page_locators
from utils.read_properties import read_config
from selenium.webdriver.common.by import By


class home_page:
    h_p_locators = home_page_locators()
    read_config = read_config()

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.read_config.get_base_URL())

    def get_login_page(self):
        self.driver.find_element(By.XPATH, self.h_p_locators.login_button).click()


    def get_register_page(self):
        self.driver.find_element(self.h_p_locators.register_button).click()

    def get_loggedin_username(self):
        loggedin_user = self.driver.find_element(By.CSS_SELECTOR, self.h_p_locators.loggedin_user).get_attribute('text')
        return loggedin_user

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.h_p_locators.logout_button).click()
