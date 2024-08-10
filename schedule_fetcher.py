#Publix Schedule Scraper by Haaris Khalique
'''
This module will retrieve your latest schedule info
from Publix PASSPort and return the HTML for processing.

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from getpass import getpass

import time

#Options to prevent browser from closing automatically during testing
options = webdriver.FirefoxOptions()
#options.add_experimental_option("detach",True)
driver = webdriver.Firefox(options = options)

#Constants
WEBSITE = "https://www.publix.org/passport/scheduling/schedule" #URL to access schedule page
LOGIN_BUTTON = (By.XPATH, '/html/body/main/div[3]/div/div/form/button') #Locate login button to begin login process
NEXT_BUTTON = (By.ID, 'idSIButton9') #Locate "next" button to proceed after entering username and password.
EMAIL_FIELD = (By.ID, 'i0116') #Locate username field
PASSWORD_FIELD = (By.ID, 'i0118') #Locate password field
AUTH_BUTTON = (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div') #Locate MS Authenticator button to complete login
NEXT_WEEK_BUTTON = (By.XPATH, '/html/body/main/div[3]/div[1]/div/div[1]/div[3]/a/i')


#This function logs in to Publix PASSPort and accesses the schedule page
def access_schedule(username, password):
    try:
        driver.get(WEBSITE)

        #Wait until login button is clickable and click to begin login process
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()

        #Wait until username field is present, populate the field, and click "next" button to proceed to password entry
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EMAIL_FIELD)).send_keys(username)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

        #Wait until password field is present, populate the field, click next (now labeled "sign in" in browser) button, and select Microsoft Authenticator
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AUTH_BUTTON)).click()


        #Waits for elements to be present on page
        while True:
            if len(driver.find_elements(By.ID, "scheduledweek")) > 0:
                break
        
        time.sleep(3)
        
        #Click button to display next week in schedule table    
        button = driver.find_element(By.XPATH, "//div[@id='scheduledweek']/div/div[3]/a/i")
        button.click()     

        time.sleep(3)
        schedule_page = driver.page_source
        return schedule_page         
    #end of try

    except Exception as e:
        print("AN ERROR OCCURRED.")
        #driver.close()

def main():
    #Prompt user for credentials on command line prior to automated login
    username = input("Enter your Publix PASSPort username: ")
    password = getpass("Enter your Publix PASSPort password: ")

    html_content = access_schedule(username, password)
    driver.quit()

if __name__ == '__main__':
    main()