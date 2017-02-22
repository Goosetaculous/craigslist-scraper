from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


d = DesiredCapabilities.CHROME
d['loggingPrefs'] = {'performance': 'ALL'}

driver = webdriver.Chrome('./driver/chromedriver')
#driver.set_window_size(375,667)
driver.get('https://industry-fe-dev.herokuapp.com')
login = driver.find_element_by_name('email')
login.send_keys('josephtrop@gmail.com')
login = driver.find_element_by_name('password')
login.send_keys('P)o9I*u7')
login.submit()
#//*[@id="main"]/section/section/header/section/div[3]/span

time.sleep(5)
driver.find_element_by_css_selector('.hamburger').click()
time.sleep(2)
driver.find_element_by_css_selector('.fa-user').click()
time.sleep(2)
driver.find_element_by_css_selector('.fa-pencil').click()
time.sleep(2)
username =driver.find_element_by_name('username')
username.clear()
time.sleep(2)
username.send_keys('wawawawa')
driver.get('https://industry-fe-dev.herokuapp.com')
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

driver.save_screenshot('test.png')

print (driver.find_element_by_css_selector('.shout-ca112rd'))

xpath='//*[@id="left-content"]/div[1]/div/div[3]/form/div[3]/div[2]/span'
driver.find_element_by_xpath(xpath).click()

performance_log = driver.get_log('performance')
print (str(performance_log).strip('[]'))
print(driver.current_url)
for entry in driver.get_log('performance'):
   print (entry)
driver.quit()
