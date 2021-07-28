from selenium import webdriver

class LoginPage:
    testbox_username_id="Email"
    testbox_password_id="Password"
    button_login_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    Link_logout_linktest="Logout"
    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element_by_id(self.testbox_username_id).clear()
        self.driver.find_element_by_id(self.testbox_username_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element_by_id(self.testbox_password_id).clear()
        self.driver.find_element_by_id(self.testbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.Link_logout_linktest).click()





