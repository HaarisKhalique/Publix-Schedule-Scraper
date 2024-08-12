WEBSITE = "https://www.publix.org/passport/scheduling/schedule" # URL to access schedule page
LOGIN_BUTTON = (By.XPATH, '/html/body/main/div[3]/div/div/form/button') # Locate login button to begin login process
NEXT_BUTTON = (By.ID, 'idSIButton9') # Locate "next" button to proceed after entering username and password.
EMAIL_FIELD = (By.ID, 'i0116') # Locate username field
PASSWORD_FIELD = (By.ID, 'i0118') # Locate password field
AUTH_BUTTON = (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div') # Locate MS Authenticator button to complete login
NEXT_WEEK_BUTTON = (By.XPATH, '/html/body/main/div[3]/div[1]/div/div[1]/div[3]/a/i')