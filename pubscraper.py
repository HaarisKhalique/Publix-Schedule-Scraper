from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

#options to prevent browser from closing automatically during testing
options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Edge(options = options)

WEBSITE = "https://www.publix.org/passport/scheduling/schedule"
LOGIN_BUTTON = (By.XPATH, "/html/body/main/div[3]/div/div/form/button")
NEXT_BUTTON = (By.ID, "idSIButton9")

EMAIL_FIELD = (By.ID, "i0116")
PASSWORD_FIELD = (By.ID, "i0118")

AUTH_BUTTON = (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div')

def main():
    #prompt user for credentials
    username = input("Enter your Publix PASSPort username: ")
    password = getpass("Enter your Publix PASSPort password: ")

    try:
        driver.get(WEBSITE)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EMAIL_FIELD)).send_keys(username)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AUTH_BUTTON)).click()

    except Exception as e:
        print("An error occurred")

    input("All done! Press enter to close the browser...")
    driver.quit()

if __name__ == '__main__':
    main()