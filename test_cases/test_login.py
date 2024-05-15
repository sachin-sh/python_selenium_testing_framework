import time
from test_cases.conftest import setup
from page_object.home_page import home_page
from page_object.login_page import LoginPage
from utils.read_properties import read_config
from selenium.common.exceptions import NoSuchElementException
from utils.loggers import log_generator


class Test1login:
    rc = read_config()
    lg = log_generator.loggen()


    def test_login(self, setup):
        self.lg.info("**************************Test_001_Login**********************")
        self.driver = setup
        self.HP = home_page(self.driver)
        self.LP = LoginPage(self.driver)
        self.LP.setusername(username=self.rc.get_username())
        self.LP.setpassword(password=self.rc.get_password())
        self.LP.clicklogin()
        print(self.driver.current_url)
        self.lg.info("**************************Home Page Title verify **********************")
        if self.driver.title == "Demo Web Shop":
            assert True
        else:
            self.driver.save_screenshot(".\\screen_shots\\" + "test_loginTitle.png")
            self.driver.close()
            assert False
        self.lg.info("**************************Logged in User verify **********************")
        if self.HP.get_loggedin_username() == self.rc.get_username():
            assert True
        else:
            self.driver.save_screenshot(".\\screen_shots\\" + "test_loggedin_user.png")
            self.driver.close()
            assert False
        self.HP.click_logout()
        time.sleep(2)
        try:
            print(self.HP.get_loggedin_username())
        except Exception as e :
            print(f"Exception occured: {NoSuchElementException}")



