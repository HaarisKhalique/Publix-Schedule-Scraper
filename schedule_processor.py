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
            
    
    shift_information = soup.find_all('div', class_='collapse col-xs-12 hidden-md hidden-lg')
    
    for div in shift_information:
        #retrieve scheduled shift by finding div element
        shift_time = div.find('div', class_='row').find('div', class_='col-xs-6 shift p-0')
        if shift_time:
            shifts.append(shift_time.text)
        else:
            continue
        
        #retrieve meal times, if any
        meal_div = div.find('div', class_='col-xs-6 shift', string='Meal')
        if meal_div: #check if a div for Meal exists, then check for sibling containing meal time
            meal_time = meal_div.find_next_sibling('div', class_='col-xs-6 shift p-0')
            
            if meal_time: #append to meals array
                meals.append(meal_time.text.strip())
        
        else: #if no meal is scheduled
            meals.append('none')
            
    print(dates)
    print(shifts)
    print(meals)

   
finally:
    html_file.close()