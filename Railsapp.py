import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#setting up the desired configuration of OS, Browser, Version

desired_cap = {
 'os_version': '10',
 'resolution': '1440x900',
 'browser': 'Chrome',
 'browser_version': '83.0',
 'os': 'Windows',
 'name': 'RailsSampleApp', # test name
 'build': 'Rails Build Number 1',
 'browserstack.debug':'True' # CI/CD job or build name
}

#inheriting unittest framework

class RailsSampleApp(unittest.TestCase):

 #creating instance of browser using remote webdriver and Browserstack URL
 
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='https://haributhirand1:LufW1REAoy75zHPtUVfz@hub-cloud.browserstack.com/wd/hub', desired_capabilities=desired_cap) 
    
 #Validating the signup functionality     
     
    def test_sign_up(self):
        driver = self.driver
        driver.implicitly_wait(5)       
        driver.get("https://blooming-lake-3455.herokuapp.com/")
        elem = driver.find_element_by_xpath('/html/body/div[1]/section/a')
        elem.send_keys(Keys.RETURN)
        #self.assertIn("Rails sample app | Sign up", driver.title)
        elem = driver.find_element_by_xpath('//*[@id="user_name"]')  
        elem.send_keys('abcd')
        elem = driver.find_element_by_xpath('//*[@id="user_email"]')  
        elem.send_keys('abc@yahoo.com')
        elem = driver.find_element_by_xpath('//*[@id="user_password"]')  
        elem.send_keys('123456')
        elem = driver.find_element_by_xpath('//*[@id="user_password_confirmation"]')  
        elem.send_keys('123456')
        elem = driver.find_element_by_xpath('//html/body/div/section/form/div[5]/input') 
        elem.send_keys(Keys.RETURN)         
        print(driver.title)

#Validating the 'Email already taken' Error         
    
    def test_multiple_sign_up(self):
        driver = self.driver       
        self.test_sign_up()
        Error = driver.find_element_by_xpath('/html/body/div/section/form/div[1]/ul/li[1]').text
        if Error == 'Email has already been taken':
            print('Passed')
        else:
            print('Failed')   

#Validating signin functionality          
    
    def test_profile(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")
        #self.assertIn("Rails sample app | Sign in", driver.title)
        elem = driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[3]/a')
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_xpath('//*[@id="session_email"]')
        elem.send_keys("hari@yahoo.com")
        elem = driver.find_element_by_xpath('//*[@id="session_password"]')
        elem.send_keys("123456")
        elem = driver.find_element_by_xpath('/html/body/div/section/form/div[3]/input')
        elem.send_keys(Keys.RETURN)        
        print(driver.title)
        elem = driver.find_element_by_xpath('/html/body/div/header/nav/ul/li[1]/a')
        elem.send_keys(Keys.RETURN)           
        elem = driver.find_element_by_xpath('//*[@id="micropost_content"]')
        elem.send_keys("Good Day")
        elem = driver.find_element_by_xpath('/html/body/div/section/table/tbody/tr/td[1]/form/div[2]/input')
        elem.send_keys(Keys.RETURN)  

#Validating Micropost functionality 

        elem = driver.find_element_by_xpath('/html/body/div/header/nav/ul/li[4]/a')               
        elem.send_keys(Keys.RETURN)          
        content = driver.find_element_by_xpath('/html/body/div/section/table/tbody/tr/td[1]/table/tbody/tr[1]/td/span[1]').text
        if content == 'Good Day':
            print('Passed')
        else:
            print('Failed') 

#Validating help page
         
    def test_help_page(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")
        #self.assertIn("Rails sample app | Help", driver.title)
        elem = driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[2]/a')
        elem.send_keys(Keys.RETURN)
        print(driver.title)     
            
    def tearDown(self):
        self.driver.close()     
    
if __name__ == "__main__":
    unittest.main()
