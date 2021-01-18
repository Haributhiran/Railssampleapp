import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

desired_cap = {
 'os_version': '10',
 'resolution': '1440x900',
 'browser': 'Chrome',
 'browser_version': '83.0',
 'os': 'Windows',
 'name': 'BStack-[Python] Sample Test', # test name
 'build': 'BStack Build Number 1',
 'browserstack.debug':'True' # CI/CD job or build name
}

class RailsSampleApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor='https://haributhirand1:LufW1REAoy75zHPtUVfz@hub-cloud.browserstack.com/wd/hub', desired_capabilities=desired_cap)         
    
    def test_sign_up(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")
        elem = driver.find_element_by_xpath('/html/body/div[1]/section/a')
        elem.send_keys(Keys.RETURN)
        #self.assertIn("Rails sample app | Sign up", driver.title)
        elem = driver.find_element_by_xpath('//*[@id="user_name"]')  
        elem.send_keys("Hari")
        elem = driver.find_element_by_xpath('//*[@id="user_email"]')  
        elem.send_keys("hari@yahoo.com")
        elem = driver.find_element_by_xpath('//*[@id="user_password"]')  
        elem.send_keys("123456")
        elem = driver.find_element_by_xpath('//*[@id="user_password_confirmation"]')  
        elem.send_keys("123456")
        elem = driver.find_element_by_xpath('//html/body/div/section/form/div[5]/input') 
        elem.send_keys(Keys.RETURN)         
        print(driver.title) 
    
    def test_signin_page(self):
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
          
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
