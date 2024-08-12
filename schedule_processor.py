# Publix Schedule Scraper by Haaris Khalique
'''
This module processes the schedule html to 
retrieve the desired information.
'''
import re
from datetime import datetime
from bs4 import BeautifulSoup


# Day object to hold data for each work shift
class WorkDay:
    def __init__(self, start, end, meal_start, meal_end):
        self.start = start
        self.end = end
        self.meal_start = meal_start
        self.meal_end = meal_end


# This function combines each shift date and time
# into ISO format for Google Calendar compatibility.
def format_time(date, time_range):
    date = datetime.strptime(date, '%m/%d/%Y')

    if time_range == None:
        return None, None
    else:
        start_time, end_time = time_range.replace('.', '').split(' - ')

        if ':' in start_time:
            start = datetime.strptime(start_time, '%I:%M %p').time()
        else:
            start = datetime.strptime(start_time, '%I %p').time()

        if ':' in end_time:
            end = datetime.strptime(end_time, '%I:%M %p').time()
        else:
            end = datetime.strptime(end_time, '%I %p').time()
        
        datetime_start = datetime.combine(date,start)
        datetime_end = datetime.combine(date,end)

        iso_start = datetime_start.strftime('%Y-%m-%dT%H:%M:%S')
        iso_end = datetime_end.strftime('%Y-%m-%dT%H:%M:%S')
        
        return iso_start, iso_end
# end of format_time


# This function processes the HTML text using BeautifulSoup4 and retrieves shift dates and times
# Shift information is used to create WorkDay objects which will be sent to calendar as events
def process_html(html_content):
    
    # arrays to store data from HTML
    dates, shifts, meals, workdays = [], [], [], []

    # create soup from html
    soup = BeautifulSoup(html_content, 'html.parser')
        
    # extract current year using schedule week string and regex
    schedule_week = soup.find('div', class_='text-center week-header pt-1').text.strip()
    match = re.search(r'\b\d{4}\b', schedule_week)
    if match:
        current_year = match.group()
        
    # retrieve scheduled shift dates
    dates_td = soup.find_all('td', class_='col-md-2 pb-4 pt-3')
    for td in dates_td:
        td_sibling = td.find_next_sibling('td', class_='col-md-12')
        if td_sibling:
            continue
        else:
            date = td.find('span').find_next_sibling('span').text.strip().replace('.','')
            dates.append(f'{date}/{current_year}')
                
    # retrieve scheduled shift by finding div element
    shift_information = soup.find_all('div', class_='collapse col-xs-12 hidden-md hidden-lg')
    for div in shift_information:
        shift_time = div.find('div', class_='row').find('div', class_='col-xs-6 shift p-0')
        if shift_time:
            shifts.append(shift_time.text)
        else:
            continue
            
        # retrieve meal times, if any
        meal_div = div.find('div', class_='col-xs-6 shift', string='Meal')
        if meal_div: # check if a div for Meal exists, then check for sibling containing meal time
            meal_time = meal_div.find_next_sibling('div', class_='col-xs-6 shift p-0')    
            if meal_time: # append to meals array
                meals.append(meal_time.text.strip())
            
        else: # if no meal is scheduled
                meals.append(None)

    # create WorkDay objects, store in workdays
    for i in range(0, len(dates)):
        shift_start, shift_end = format_time(dates[i], shifts[i])
        meal_start, meal_end = format_time(dates[i], meals[i])
        workdays.append(WorkDay(shift_start,shift_end,meal_start,meal_end))

    return workdays