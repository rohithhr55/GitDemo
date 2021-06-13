from selenium import webdriver


class Login:
    def __init__(self, driver):
        self.driver = driver

        self.username_id = "email"
        self.password_id = "pass"
        # self.login_id = "button[name="login"]"

    def username(self, username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def login(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div["
                                          "2]/button").click()
