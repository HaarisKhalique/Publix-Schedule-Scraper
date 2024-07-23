'''
Publix Schedule Scraper by Haaris Khalique

This script will automate the login process to Publix PASSPort, 
retrieve your schedule information, and copy it into your preferred 
calendar app.

'''
'''
TO DO LIST (1 = COMPLETE, 0 = INCOMPLETE)

1 - Automate login process
0 - Scrape schedule information
0 - Copy data into Apple Calendar
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

#Options to prevent browser from closing automatically during testing
options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Edge(options = options)

#Constants
WEBSITE = "https://www.publix.org/passport/scheduling/schedule" #URL to access schedule page
LOGIN_BUTTON = (By.XPATH, "/html/body/main/div[3]/div/div/form/button") #Locate login button to begin login process
NEXT_BUTTON = (By.ID, "idSIButton9") #Locate "next" button to proceed after entering username and password.
EMAIL_FIELD = (By.ID, "i0116") #Locate username field
PASSWORD_FIELD = (By.ID, "i0118") #Locate password field
AUTH_BUTTON = (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div') #Locate MS Authenticator button to complete login


def main():
    #Prompt user for credentials on command line prior to automated login
    username = input("Enter your Publix PASSPort username: ")
    password = getpass("Enter your Publix PASSPort password: ")

    try:
        driver.get(WEBSITE)

        #Wait until login button is clickable and click to begin login process
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()

        #Wait until username field is present, populate the field, and click "next" button to proceed to password entry
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EMAIL_FIELD)).send_keys(username)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

        #Wait until password field is present, populate the field, and click next (now labeled "sign in" in browser) button to proceed to Two-Factor Authentication
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AUTH_BUTTON)).click()

    except Exception as e:
        print("An error occurred")


    #Halt after completion
    input("All done! Press enter to close the browser...")
    driver.quit()

if __name__ == '__main__':
    main()