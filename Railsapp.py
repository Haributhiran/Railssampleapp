from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
desired_cap = {
 'os_version': '10',
 'resolution': '1440x900',
 'browser': 'Chrome',
 'browser_version': '83.0',
 'os': 'Windows',
 'name': 'BStack-[Python] Sample Test', # test name
 'build': 'BStack Build Number 1' # CI/CD job or build name
}
driver = webdriver.Remote(
    command_executor='https://haributhirand1:LufW1REAoy75zHPtUVfz@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
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
driver.quit() 
