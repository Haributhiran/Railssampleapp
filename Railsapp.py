from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
desired_cap = {
 'os_version': '7',
 'resolution': '1440x900',
 'browser': 'Firefox',
 'browser_version': '75.0',
 'os': 'Windows',
 'name': 'BStack-[Python] Sample Test', # test name
 'build': 'BStack Build Number 1', # CI/CD job or build name
 'browserstack.debug': 'True'
}


driver = webdriver.Remote(command_executor='https://haributhirand1:LufW1REAoy75zHPtUVfz@hub-cloud.browserstack.com/wd/hub', desired_capabilities=desired_cap)


driver.get("https://blooming-lake-3455.herokuapp.com/")
if not "Rails sample app | Home" in driver.title:
    raise Exception("Unable to load Rails sample app!")
elem = driver.find_element_by_xpath('/html/body/div[1]/section/a')
elem.send_keys(Keys.RETURN)
print(driver.title)
if (driver.title[:26]=="Rails sample app | Sign up"):
	driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
else:
	driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')

#Navigate Back to Home
driver.get("https://blooming-lake-3455.herokuapp.com/")
if not "Rails sample app | Home" in driver.title:
    raise Exception("Unable to load Rails sample app Home page!")
elem = driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[1]/a')
elem.send_keys(Keys.RETURN)

#Navigate Back to Home
driver.get("https://blooming-lake-3455.herokuapp.com/")
if not "Rails sample app | Help" in driver.title:
    raise Exception("Unable to load Rails sample app Help Page!")
elem = driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[2]/a')
elem.send_keys(Keys.RETURN)

#Navigate Back to Home
driver.get("https://blooming-lake-3455.herokuapp.com/")
if not "Rails sample app | Sign in" in driver.title:
    raise Exception("Unable to load Rails sample app sign in page!")
elem = driver.find_element_by_xpath('/html/body/div[1]/header/nav/ul/li[3]/a')
elem.send_keys(Keys.RETURN)

driver.quit() 
