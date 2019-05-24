from selenium import webdriver

class Flipkart(object):
    def __init__(self):
        self.url="https://www.flipkart.com"
        self.xpaths = { 'usernameTxtBox' : "//input[@name='username']",
                   'passwordTxtBox' : "//input[@name='password']",
                   'submitButton' :   "//button[@type='submit']",
                   'searchBox' : "//input[@type='text']"}
    
    def Launch(self):
        driver.maximize_window()
        driver.get(self.url)

    def searchItem(self, searchFor='laptops'):
        driver.find_element_by_xpath(self.xpaths['searchBox']).clear()
        driver.find_element_by_xpath(self.xpaths['searchBox']).send_keys(searchFor)
        driver.find_element_by_xpath(self.xpaths['submitButton']).click()

    def sort(self, Type='popularity'):
        sortPop="////*[@id='container']/div/div[2]/div[2]/div/div[2]/div[2]/div/section/ul/li[2]"
        driver.find_element_by_xpath(sortPop).click()

if __name__=='__main__':
    driver = webdriver.Chrome()
    flip = Flipkart()
    flip.Launch()
    flip.searchItem()
    flip.sort()
