import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class RailsSampleApp(unittest.TestCase):

#The setUp is part of initialization, this method will get called before every test function. Here creating instance firefox driver

    def setUp(self):    
        self.driver = webdriver.Firefox() 
        USERNAME ='' 
        
#Validating signup functionality         
        
    def test_A_sign_up(self):
        driver = self.driver
        driver.implicitly_wait(5)       
        driver.get("https://blooming-lake-3455.herokuapp.com/")
        driver.find_element_by_xpath('/html/body/div[1]/section/a').click()              
        driver.find_element_by_xpath('//*[@id="user_name"]').send_keys(self.USERNAME)         
        driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(self.USERNAME + '@gmail.com')          
        driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(self.USERNAME + '123')          
        driver.find_element_by_xpath('//*[@id="user_password_confirmation"]').send_keys(self.USERNAME + '123')         
        driver.find_element_by_xpath('//html/body/div/section/form/div[5]/input').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/div")))
        assert self.USERNAME in driver.title  
        print(self.USERNAME + ' signup validated: passed')
        
#Validating already existing users        

    def test_B_sign_up(self):
        driver = self.driver
        driver.implicitly_wait(5)       
        driver.get("https://blooming-lake-3455.herokuapp.com/")
        driver.find_element_by_xpath('/html/body/div[1]/section/a').click()              
        driver.find_element_by_xpath('//*[@id="user_name"]').send_keys(self.USERNAME)         
        driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(self.USERNAME + '@gmail.com')          
        driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(self.USERNAME + '123')          
        driver.find_element_by_xpath('//*[@id="user_password_confirmation"]').send_keys(self.USERNAME + '123')         
        driver.find_element_by_xpath('//html/body/div/section/form/div[5]/input').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/form/div[1]/ul/li")))
        elem = driver.find_element_by_xpath('/html/body/div/section/form/div[1]/ul/li').text
        self.assertEqual(elem, 'Email has already been taken') 
        print('Duplicate profile not allowed: passed')
                                       
#Validating profile signin

    def test_C_profile(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")
        #self.assertIn("Rails sample app | Sign in", driver.title)
        driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[3]/a').click()        
        driver.find_element_by_xpath('//*[@id="session_email"]').send_keys(self.USERNAME + '@gmail.com')        
        driver.find_element_by_xpath('//*[@id="session_password"]').send_keys(self.USERNAME + '123')        
        driver.find_element_by_xpath('/html/body/div/section/form/div[3]/input').click() 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/table/tbody/tr/td[1]/h1/img")))           
        assert self.USERNAME in driver.title
        print('signin validated: passed')
        
#validating microposts and its count
           
        driver.find_element_by_xpath('/html/body/div/header/nav/ul/li[1]/a').click()
        elem = driver.find_element_by_xpath('/html/body/div/section/table/tbody/tr/td[2]/div[1]/a/span[2]').text 
        li = elem.split()     
        i_count = int(li[0])    #storing initial post count                   
        driver.find_element_by_xpath('//*[@id="micropost_content"]').send_keys("Good Day")   #posting "good day"       
        driver.find_element_by_xpath('/html/body/div/section/table/tbody/tr/td[1]/form/div[2]/input').click()   #submitting     
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="success"]')))   
        elem = driver.find_element_by_xpath('//div[@class="success"]').text    
        self.assertEqual(elem, 'Micropost created!')
        elem = driver.find_element_by_xpath('/html/body/div/section/table/tbody/tr/td[2]/div[1]/a/span[2]').text 
        li = elem.split()     
        f_count = int(li[0])  
        self.assertEqual(i_count + 1 ,f_count) #comparing counts of posts before and after posting
        print('microposts and their counts validated: passed')
                     
#validating password change
        
        driver.find_element_by_xpath('/html/body/div/header/nav/ul/li[5]/a').click()
        driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(self.USERNAME + '1234')
        driver.find_element_by_xpath('//*[@id="user_password_confirmation"]').send_keys(self.USERNAME + '1234')       
        driver.find_element_by_xpath('/html/body/div/section/form/div[5]/input').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@class='gravatar']"))) 
        elem = driver.find_element_by_xpath('/html/body/div/section/div').text       
        self.assertEqual(elem, 'profile updated!') 
        print('password change validated:passed')  
        
#Validating invalid emails and prompt for new profile creation 
        
    def test_D_invalid_email(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")
        #self.assertIn("Rails sample app | Sign in", driver.title)
        driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[3]/a').click()        
        driver.find_element_by_xpath('//*[@id="session_email"]').send_keys(self.USERNAME + '@gmail.com')        
        driver.find_element_by_xpath('//*[@id="session_password"]').send_keys(self.USERNAME + '1231')        
        driver.find_element_by_xpath('/html/body/div/section/form/div[3]/input').click() 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='error']")))
        elem = driver.find_element_by_xpath('//div[@class ="error"]').text
        self.assertEqual(elem, 'invalid email/password combination.')
        driver.find_element_by_xpath('//a[@href="/signup"]').click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='error']")))
        assert 'Sign up' in driver.title 
        print('Authentication and signup href verified')  
        
#validating followers count and follow/unfollow button
        
    def test_E_followers_count(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")
        driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[3]/a').click()        
        driver.find_element_by_xpath('//*[@id="session_email"]').send_keys(self.USERNAME + '@gmail.com')        
        driver.find_element_by_xpath('//*[@id="session_password"]').send_keys(self.USERNAME + '1234')        
        driver.find_element_by_xpath('/html/body/div/section/form/div[3]/input').click() 
        t = driver.current_url.split('/')
        driver.get("https://blooming-lake-3455.herokuapp.com/users/"+ str(int(t[4])-1))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/table/tbody/tr/td[1]/h1/img")))  
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        elem=driver.find_element_by_xpath('//input[@type="submit"]').get_attribute("value")      
        driver.find_element_by_xpath('/html/body/div/header/nav/ul/li[1]/a').click()
        following = driver.find_element_by_xpath('//span[@id="following"]').text.split()
        self.assertEqual(elem,'Unfollow')      #checking if value of button changed to unfollow
        self.assertEqual('1' ,following[0])    #checking followers count                       
        print('following count and follow/unfollow button verified')
        
#validating help href in main page

    def test_F_help_href(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")        
        driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[2]/a').click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div/section/span")))           
        elem = driver.find_element_by_xpath('/html/body/div/section/p').text            
        self.assertEqual(elem, 'This is Help page')
        print('Help href verified') 
        
#validating home href from help page      
        
    def test_G_home_href(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/help")        
        driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[1]/a').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/p[2]')))         
        elem = driver.find_element_by_xpath('/html/body/div/section/p').text            
        self.assertEqual(elem, 'This is the home page')
        print('home href verified')
        
#validating contact href in main page       

    def test_H_contact_href(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")        
        driver.find_element_by_xpath('//a[@href="/contact"]').click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div/section/span"))) 
        elem = driver.find_element_by_xpath('/html/body/div/section/p').text            
        self.assertEqual(elem, 'This is the contact page')                 
        print('contact href verified')
        
#validating about href in main page
        
    def test_I_about_href(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://blooming-lake-3455.herokuapp.com/")        
        driver.find_element_by_xpath('//a[@href="/about"]').click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div/section/span"))) 
        elem = driver.find_element_by_xpath('/html/body/div/section/p').text            
        self.assertEqual(elem, 'This is About page') 
        print('About href verified')   
        
#The tearDown method will get called after every test method. This is a place to do all cleanup actions.                   
                
    def tearDown(self):
        self.driver.close()          
                        
if __name__ == "__main__":

    if len(sys.argv) > 1:
        RailsSampleApp.USERNAME = sys.argv.pop()
       
    unittest.main()
