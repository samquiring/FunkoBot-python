from selenium import webdriver
from time import sleep
import pdb

class funkobot():
    def __init__(self, webpage, email, password):
        self.webpage = webpage
        self.email = email
       # self.first_name = first_name
        #self.last_name = last_name
        #self.address = address
        #self.city = city
        #self.zip = zip
        #self.card_number = card_number
        #self.name_card = card_name
        #self.expr_date = expr_date
        #self.secr_code = secr_code
        self.password = password
        self.driver = webdriver.Chrome('/Users/Sam/Downloads/chromedriver')

    def login(self):
        self.driver.get('https://www.funko.com/login')
        self.driver.implicitly_wait(30)
        email_in = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div/div/div/div/div[2]/form/div/div[1]/label/input')
        email_in.send_keys(self.email)
        password_in = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div/div/div[2]/form/div/div[2]/label/input')
        password_in.send_keys(self.password)
        login_button = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div/div/div/div/div[2]/form/div/div[3]/button')
        login_button.click()
        self.driver.implicitly_wait(30)

    #need to find an unavailable product to implement this
    def check_availablity(self):
        check_available = self.driver.find_element_by_class_name('method-descr')
        while(check_available.text == 'Not available for shipping'):
            self.driver.refresh()
            self.driver.implicitly_wait(30)
            #sleep(random.uniform(.5, 5))
            check_available = self.driver.find_element_by_class_name('method-descr')


    def get_funko(self):
        self.driver.get(self.webpage)

        self.driver.implicitly_wait(30)

        add_cart_button = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div/div/div[1]/div[2]/div[1]/div[2]/button')
        add_cart_button.click()

        self.driver.implicitly_wait(30)
        sleep(2) 

        self.driver.get('https://www.funko.com/cart')
        checkout_button = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div/div[2]/div[1]/div[2]/button')
        checkout_button.click()
    
    ##not needed but kept incase user doesnt want to do checkout quick
    def checkout_funko(self):
        
        self.driver.implicitly_wait(30) 

        email_in = self.driver.find_element_by_xpath('//*[@id="checkout_email"]')
        f_name_in = self.driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]')
        l_name_in = self.driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]')
        address_in = self.driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]')
        city_in  = self.driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]')
        zip_in = self.driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]')

        email_in.send_keys(self.email)
        f_name_in.send_keys(self.first_name)
        l_name_in.send_keys(self.last_name)
        address_in.send_keys(self.address)
        city_in.send_keys(self.city)
        zip_in.send_keys(self.zip)
        
        checkout_button = self.driver.find_element_by_xpath('//*[@id="continue_button"]')
        checkout_button.click()
        to_payment_button = self.driver.find_element_by_xpath('//*[@id="continue_button"]')
        to_payment_button.click()

    def checkout_quick(self):
        self.driver.implicitly_wait(30) 
        
        checkout_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div')
        checkout_button.click()

        self.driver.implicitly_wait(30) 

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(self.email)
        shoppay_contin = self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[1]/div/div[1]/form/section/div/button')
        shoppay_contin.click()
    
    
    def pay_funko(self):

        sleep(5)

        card_in = self.driver.find_element_by_xpath('//*[@id="number"]')
        name_in = self.driver.find_element_by_xpath('//*[@id="name"]')
        expr_in = self.driver.find_element_by_xpath('//*[@id="expiry"]')
        secr_in = self.driver.find_element_by_xpath('//*[@id="verification_value"]')
        card_in.send_keys(self.card_number)
        name_in.send_keys(self.name_card)
        expr_in.send_keys(self.expr_date)
        secr_in.send_keys(self.secr_code)

        pay_button = self.driver.find_element_by_xpath('//*[@id="continue_button"]')
        pay_button.click()
