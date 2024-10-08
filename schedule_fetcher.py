# Publix Schedule Scraper by Haaris Khalique
'''
This module will retrieve your latest schedule info
from Publix PASSPort and return the HTML for processing.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

import time
import constants
# This function logs in to Publix PASSPort and accesses the schedule page
def access_schedule(username, password):
    try:
        # You may choose to use Firefox or Chrome below, instead.
        #driver = webdriver.Edge()
        driver = webdriver.Firefox()
        #driver = webdriver.Chrome()

        #Request webpage containing schedule
        driver.get(constants.WEBSITE)

        # Wait until login button is clickable and click to begin login process
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(constants.LOGIN_BUTTON)).click()

        # Wait until username field is present, populate the field, and click "next" button to proceed to password entry
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(constants.EMAIL_FIELD)).send_keys(username)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(constants.NEXT_BUTTON)).click()

        # Wait until password field is present, populate the field, click next (now labeled "sign in" in browser) button, and select Microsoft Authenticator
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(constants.PASSWORD_FIELD)).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(constants.NEXT_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(constants.AUTH_BUTTON)).click()
        
        '''
        # Waits for elements to be present on page
        while True:
            if len(driver.find_elements(By.CSS_SELECTOR, '#futureWeekButton')) > 0:
                break
        
        time.sleep(2)
        '''

        next_week_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#futureWeekButton')))
        # Click button to display latest week in schedule table    
        next_week_button.click()
        time.sleep(2)
        next_week_button.click()
        time.sleep(3)

        schedule_page = driver.page_source
        driver.quit()
        
        return schedule_page         
    # end of try

    except Exception as e:
        print("AN ERROR OCCURRED.")
'''
def main():
    access_schedule('   ', '   ')

if __name__ == '__main__':
    main()
'''