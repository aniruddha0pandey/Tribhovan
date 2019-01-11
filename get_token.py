try:
  from config import *
  assert "" in API_TOKEN
except:
  from selenium import webdriver

  driver = webdriver.Firefox()
  driver.get("https://quantumexperience.ng.bluemix.net/qx/account/advanced")
  assert "IBM Q" in driver.title
  button = driver.find_element_by_id('button')
  button.click()
  driver.close()
