from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge()
website = "https:www.publix.org"


#username = input("Enter your username: ")
#password = input("Enter your password: ")
#authCode = input("Enter the Two-Factor Authentication code:")

#print(username + "\n" + password +"\n" + authCode)


driver.get(website)

driver.quit()