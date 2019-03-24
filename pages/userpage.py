class UserPage:
    def __init__(self,driver):
        self.driver=driver
        self.user_tab_xpath="//*[@id='topnav']/tbody/tr[1]/td[5]/a/div[2]"
        self.add_user_xpath="//*[@id='createUserDiv']/div/div[2]"

    def click_on_user_btn(self):
        self.driver.find_element_by_xpath(self.user_tab_xpath).click()

    def click_add_user_btn(self):
        self.driver.find_element_by_xpath(self.add_user_xpath).click()
