import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class RailsSampleApp(unittest.TestCase):

    def setUp(self):    
        self.driver = webdriver.Firefox() 
        USERNAME ='' 
     
    def test_A_sign_up(self):
        driver = self.driver
        driver.implicitly_wait(5)       
        driver.get("https://blooming-lake-3455.herokuapp.com/")
        driver.find_element_by_xpath('/html/body/div[1]/section/a').send_keys(Keys.RETURN)              
        driver.find_element_by_xpath('//*[@id="user_name"]').send_keys(self.USERNAME)         
        driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(self.USERNAME + '@gmail.com')          
        driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(self.USERNAME + '123')          
        driver.find_element_by_xpath('//*[@id="user_password_confirmation"]').send_keys(self.USERNAME + '123')         
        driver.find_element_by_xpath('//html/body/div/section/form/div[5]/input').send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/div")))
        assert self.USERNAME in driver.title         

    def test_B_profile(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")
        #self.assertIn("Rails sample app | Sign in", driver.title)
        driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[3]/a').send_keys(Keys.RETURN)        
        driver.find_element_by_xpath('//*[@id="session_email"]').send_keys(self.USERNAME + '@gmail.com')        
        driver.find_element_by_xpath('//*[@id="session_password"]').send_keys(self.USERNAME + '123')        
        driver.find_element_by_xpath('/html/body/div/section/form/div[3]/input').send_keys(Keys.RETURN) 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/table/tbody/tr/td[1]/h1/img")))           
        assert self.USERNAME in driver.title
        driver.find_element_by_xpath('/html/body/div/header/nav/ul/li[1]/a').send_keys(Keys.RETURN)                   
        driver.find_element_by_xpath('//*[@id="micropost_content"]').send_keys("Good Day")        
        driver.find_element_by_xpath('/html/body/div/section/table/tbody/tr/td[1]/form/div[2]/input').send_keys(Keys.RETURN)          
        #driver.find_element_by_xpath('/html/body/div/header/nav/ul/li[4]/a').send_keys(Keys.RETURN)                                 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="success"]')))   
        elem = driver.find_element_by_xpath('//div[@class="success"]').text    
        self.assertEqual(elem, 'Micropost created!')      

    def test_help_href(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")        
        driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[2]/a').send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div/section/span")))           
        elem = driver.find_element_by_xpath('/html/body/div/section/p').text            
        self.assertEqual(elem, 'This is Help page')
        
    def test_home_href(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/help")        
        driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[2]/a').send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div/section/span")))          
        elem = driver.find_element_by_xpath('/html/body/div/section/p').text            
        self.assertEqual(elem, 'This is Help page')

    def test_contact_href(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")        
        driver.find_element_by_xpath('//a[@href="/contact"]').send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div/section/span"))) 
        elem = driver.find_element_by_xpath('/html/body/div/section/p').text            
        self.assertEqual(elem, 'This is the contact page')  
        
    def test_about_href(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")        
        driver.find_element_by_xpath('//a[@href="/about"]').send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div/section/span"))) 
        elem = driver.find_element_by_xpath('/html/body/div/section/p').text            
        self.assertEqual(elem, 'This is About page')                
                
    def tearDown(self):
        self.driver.close()          
                        
if __name__ == "__main__":

    if len(sys.argv) > 1:
        RailsSampleApp.USERNAME = sys.argv.pop()
       
    unittest.main()
