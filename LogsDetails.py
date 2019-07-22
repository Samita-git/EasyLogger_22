from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome('C:\\Users\\Preetam\\Downloads\\chromedriver_win32\\chromedriver.exe');

print("chrome environment setup")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://account.logger.mobi/login')
driver.find_element_by_id('username').send_keys('ranchhod.ramani@pulsesolutions.net')
driver.find_element_by_id('password').send_keys('1234567890')
driver.find_element_by_id('btnSubmit').click()
driver.execute_script("window.scrollTo(0,300);")
driver.find_element_by_xpath('/html/body/section/div[5]/div/div/div/div[4]/div[2]/div/table/tbody/tr[5]/td/a/span').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[10]/div/div[5]/a[1]').click()
driver.execute_script("window.scrollTo(0,200);")
time.sleep(2)
driver.find_element_by_css_selector('#step4 > a:nth-child(3)').click()

obj= Select(driver.find_element_by_id('drpDevices'))
Dropdown_Value1 = obj.select_by_index(3)

Dropdown_Value = driver.find_element_by_id('drpDevices')

print(Dropdown_Value1)

table_id = driver.find_element_by_id('sample_6')

print(table_id.text)

# driver.save_screenshot("screenshot.png")