from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://quantumexperience.ng.bluemix.net/qx/account/advanced")
assert "IBM Q" in driver.title




driver.close()
