'''
This script is used to directly pass the schedule HTML file 
obtained manually by the user. The data is then processed and 
events are created in the user's calendar.
'''
from schedule_processor import process_html
from schedule_uploader import update_calendar

def main():
    # Prompt user for HTML file to process
    file = input("Enter the name of the HTML file you would like to process:")
    html_content = open(file, 'r')
    events = process_html(html_content)
    update_calendar(events)
    input('All done! Press ENTER to close end the program...')
    exit()
if __name__ == '__main__':
    main()