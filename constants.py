from selenium.webdriver.common.by import By
WEBSITE = "https://www.publix.org/passport/scheduling/schedule" # URL to access schedule page
LOGIN_BUTTON = (By.XPATH, '/html/body/main/div[3]/div/div/form/button') # login button to begin login process
NEXT_BUTTON = (By.ID, 'idSIButton9') # "next" button to proceed after entering username and password.
EMAIL_FIELD = (By.ID, 'i0116') # username field
PASSWORD_FIELD = (By.ID, 'i0118') # password field
AUTH_BUTTON = (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div') # MS Authenticator button to complete login
NEXT_WEEK_BUTTON = (By.XPATH, '/html/body/main/div[3]/div[1]/div/div[1]/div[3]/a/i') # button to view most recent schedule week
SCOPES = ["https://www.googleapis.com/auth/calendar.events"] # OAuth 2.0 scope for Google Calendar API v3 (see, edit, share, delete)