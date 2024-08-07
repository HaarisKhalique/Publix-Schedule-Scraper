#Publix Schedule Scraper by Haaris Khalique
'''
This module processes the schedule html to 
retrieve the desired information.

'''
from bs4 import BeautifulSoup


#Day object to hold data for each work shift
class WorkDay:
    def __init__(self, date, shift, meal):
        self.date = date
        self.shift = shift
        self.meal = meal


workdays = []   #array of WorkDay objects to send to calendar app
dates = []      #stores all dates the employee is scheduled to work
shifts = []     #stores scheduled shifts (start-end time)
meals = []      #stores all scheduled meal breaks (start-end time)

#in final, pass the html in from schedule_fetcher
html_file = open('schedule.html', 'r', encoding= 'utf-8')

try:
    #create soup from html file
    html_content = html_file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    
    '''use this to get the year somehow'''
    #print(soup.find('div', class_='text-center week-header pt-1'))

    #retrieve scheduled shift dates
    dates_td = soup.find_all('td', class_='col-md-2 pb-4 pt-3')
    for td in dates_td:
        td_sibling = td.find_next_sibling('td', class_='col-md-12')
        if td_sibling:
            continue
        else:
            date = td.find('span').find_next_sibling('span').text.strip()
            dates.append(date)
            
    #retrieve scheduled shift and meal start-end times
    shift_and_meal_divs = soup.find_all('div', class_='col-xs-6 shift p-0')
    for div in shift_and_meal_divs:
        print(div)



finally:
    html_file.close()