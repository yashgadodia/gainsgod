from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.trumba.com/calendars/SMU_OSL_Gym')

rsvpBtn = driver.find_element_by_id('rootDiv')
# button =  driver.getElementByName('rsvpBtn')
print(rsvpBtn)

# .find_elements_by_class_name('rsvpBtn')