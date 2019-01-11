try:
  from config import *
  assert "" not in API_TOKEN
except:
  from selenium import webdriver

  driver = webdriver.Firefox()
  driver.get("https://quantumexperience.ng.bluemix.net/qx/account/advanced")
  assert "IBM Q" in driver.title
  copy_api_token = driver.find_element_by_id('button')
  copy_api_token.click()
  driver.close()
