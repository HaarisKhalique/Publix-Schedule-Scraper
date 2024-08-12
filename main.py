from schedule_fetcher import access_schedule
from schedule_processor import process_html, WorkDay
#from schedule_uploader import
import getpass
def main():
    # Prompt user for credentials on command line prior to automated login
    username = input("Enter your Publix PASSPort username: ")
    password = getpass("Enter your Publix PASSPort password: ")

    html_content = access_schedule(username, password)
 

if __name__ == '__main__':
    main()