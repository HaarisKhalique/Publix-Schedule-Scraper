'''
This script is used to automate the login process and HTML
retrieval. The data is then processed and events are created
in the user's calendar.
'''
from schedule_fetcher import access_schedule
from schedule_processor import process_html
from schedule_uploader import update_calendar
from getpass import getpass

def main():
    # Prompt user for credentials on command line prior to automated login
    username = input("Enter your Publix PASSPort username: ")
    password = getpass("Enter your Publix PASSPort password: ")

    html_content = access_schedule(username, password)
    events = process_html(html_content)
    update_calendar(events)
    input('All done! Press ENTER to close end the program...')
    exit()
if __name__ == '__main__':
    main()