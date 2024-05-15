from selenium import webdriver
from locators.page_locators import login_page_locators
from page_object.home_page import home_page
from selenium.webdriver.common.by import By

class LoginPage:
    l_p_locators = login_page_locators()


    def __init__(self, driver):
        self.driver = driver
        self.home_page = home_page(self.driver)
        self.home_page.get_login_page()

    def setusername(self, username):
        self.driver.find_element(By.XPATH, self.l_p_locators.username_field).clear()
        self.driver.find_element(By.XPATH, self.l_p_locators.username_field).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.XPATH, self.l_p_locators.password_field).clear()
        self.driver.find_element(By.XPATH, self.l_p_locators.password_field).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.l_p_locators.login_button).click()

