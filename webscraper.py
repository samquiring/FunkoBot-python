from time import sleep
from selenium import webdriver
import pdb

class webscraper():
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/Sam/Downloads/chromedriver')

    def get_funko(self):
        self.driver.get('https://www.google.com')
        pdb.set_trace()

        #sleep(5)

        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.send_keys('testing')

test = webscraper()
test.get_funko()