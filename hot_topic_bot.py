from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
import random

class hot_topic_bot():
    
    def __init__(self, email, password, webpage, name, cc, expr, security):
        self.option = webdriver.ChromeOptions()
        self.chrome_prefs = {}
        self.option.experimental_options["prefs"] = self.chrome_prefs
        self.chrome_prefs["profile.default_content_settings"] = { "popups": 0 }
        self.driver = webdriver.Chrome(chrome_options=self.option,executable_path = '/Users/Sam/Downloads/chromedriver')
        self.driver.get('https://www.hottopic.com/account')
        self.driver.implicitly_wait(30)
        self.login = email
        self.password = password
        self.webpage = webpage
        self.name = name
        self.credit_card = cc
        self.expr = expr
        self.secr = security

    def popup_closer(self):
        close_pop_button = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/button')
        close_pop_button.click()

    def user_login(self):
        login_in = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[2]/div[1]/div/div/form/fieldset/div[1]/input')
        login_in.send_keys(self.login)
        password_in = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[2]/div[1]/div/div/form/fieldset/div[2]/input')
        password_in.send_keys(self.password)
        sign_in_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[2]/div[1]/div/div/form/fieldset/div[3]/button')
        sign_in_button.click()
        self.driver.implicitly_wait(30)

    def goto_page(self):
        self.driver.get(self.webpage)
        self.driver.implicitly_wait(30)

    def popup_blocker(self):
        popup_button = self.driver.find_element_by_id('Combined-Shape')
        popup_button.click()

    def check_availablity(self):
        check_available = self.driver.find_element_by_class_name('method-descr')
        while(check_available.text == 'Not available for shipping'):
            self.driver.refresh()
            self.driver.implicitly_wait(30)
            sleep(random.uniform(.5, 5))
            check_available = self.driver.find_element_by_class_name('method-descr')

    def bag(self):
        try:
            select_qty = Select(self.driver.find_element_by_id('Quantity'))
            select_qty.select_by_value('5')
            add_bag_button = self.driver.find_element_by_xpath('//*[@id="add-to-cart"]')
            add_bag_button.click()
            sleep(1)
            self.driver.get('https://www.hottopic.com/checkout')
            self.driver.implicitly_wait(30)
        except:
            self.popup_blocker()
            self.bag()

    def checkout(self):
        try:
            billing_countin = self.driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress"]/div[2]/fieldset/div/button')
            billing_countin.click()
            self.driver.implicitly_wait(30)
        except:
            self.popup_blocker()
            self.checkout()

    def billing(self):
        try:
            name_cc = self.driver.find_element_by_id('first-data-payment-field-name')
            name_cc.send_keys(self.name)
            cc = self.driver.find_element_by_id('first-data-payment-field-card')
            cc.send_keys(self.credit_card)
            expr_date = self.driver.find_element_by_id('first-data-payment-field-exp')
            expr_date.send_keys(self.expr)
            security_code = self.driver.find_element_by_id('dwfrm_billing_paymentMethods_creditCard_cvn')
            security_code.send_keys(self.secr)
            review_button = self.driver.find_element_by_xpath('//*[@id="creditcard-payment-type"]/div[2]/div[6]/button')
            review_button.click()
        except:
            self.popup_blocker()
            self.billing()


#user = hot_topic_bot()
#user.popup_closer()
#user.user_login()
#user.goto_page()
#user.check_availablity()
#user.bag()
#user.checkout()
#user.billing()