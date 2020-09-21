from selenium import webdriver
from time import sleep

class target_bot():
    def __init__(self,website,username,password):
        self.site = website
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('/Users/Sam/Downloads/chromedriver')

    def login(self):
        self.driver.implicitly_wait(30)
        email_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        email_in.send_keys(self.username)
        password_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        password_in.send_keys(self.password)
        login_button = self.driver.find_element_by_xpath('//*[@id="login"]')
        login_button.click()
        self.driver.implicitly_wait(30)

    def get_item(self):
        self.driver.get(self.site)
        self.driver.implicitly_wait(30)
        buy = self.driver.find_element_by_xpath('//*[@id="viewport"]/div[5]/div/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[2]/button')
        buy.click()
        self.driver.implicitly_wait(30)
    
    def checkout(self):
        self.driver.get('https://www.target.com/co-cart')
        move_to_login = self.driver.find_element_by_xpath('//*[@id="orderSummaryWrapperDiv"]/div/div/div[2]/button')
        move_to_login.click()
        self.driver.implicitly_wait(30)