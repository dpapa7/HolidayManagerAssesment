from datetime import datetime
import json
import csv
from bs4 import BeautifulSoup
from hamcrest import none
import requests
from dataclasses import dataclass





# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------

class Holiday:
    
    """Holiday Class"""

    def __init__(self, name, date):
        self.__name = name
        dateTime = datetime.strptime(date,"%Y-%m-%d")
        self.__date = dateTime.strftime('%Y-%m-%d')

    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name
   
    @property 
    def date(self):
        return self.__date

    @date.setter
    def date(self, new_date):
        self.__date = new_date
    
    @date.deleter
    def date(self):
        del self.__date

    def __str__ (self):
        return "%s : %s" % (self.name, self.date)

        # String output
        # Holiday output when printed.


# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------


class HolidayList:

    def __init__(self):
       self.innerHolidays = []

    
    def addHoliday(self, holidayObj):
        
        if (type(holidayObj) == Holiday):
            self.innerHolidays.append(holidayObj)
            print(f"{holidayObj} has been added")
        else:
            print("You can only input a Holiday Object")

        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday

    def findHoliday(self, HolidayName, Date):
        
        
        for holiday in self.innerHolidays:
            if holiday.name == HolidayName and holiday.date == Date:
                return holiday
        
        return None

        # Find Holiday in innerHolidays
        # Return Holiday

    def removeHoliday(self, HolidayName, Date):
        
        for i in range(len(self.innerHolidays)):
            
            holiday = self.innerHolidays[i]

            if holiday.name == HolidayName and holiday.date == Date:
                print(f"Deleting {HolidayName} from list")
                del self.innerHolidays[i]
            else:
                print("Sorry the Holiday selected could not be found")       

        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday

    def read_json(self, filelocation):
        
        with open(filelocation, 'r') as f:
            data = json.load(f)['holidays']

        for i in range (len(data)):
            name = data[i]['name']
            date = data[i]['date']
            holiday = Holiday(name,date)
            self.addHoliday(holiday)

        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

    def save_to_json(self, filelocation):
        pass

        # Write out json file to selected file.
        
    def scrapeHolidays(self):
        

        try:
            holidays = []
        
            for year in range(2020,2025):

                url = (f'https://www.timeanddate.com/holidays/us/{year}?hol=33554809')
                response = requests.get(url)
                html = response

                soup = BeautifulSoup(html, 'html.parser')
                table = soup.find('table', attrs={'id':'holidays-table'})
                body = table.find('tbody')


                for row in body.find_all('tr'):
                    
                    #Holiday Dictionary
                    Holiday = {}

                    date = row.find('th')
                    name = row.find('a')

                    #check rows where date and name are not None
                    if date is not None and name is not None:
                        
                        #format date correctly
                        date = date.text
                        date = f"{date} {year}"
                        date= datetime.strptime(date,"%b %d %Y")
                        date = date.strftime('%Y-%m-%d')
                        
                        Holiday['Name'] = name.text
                        Holiday['Date'] = date
                    
                    holidays.append(Holiday)

                    #remove empty dictionaries from list
                    while {} in holidays:
                        holidays.remove({}) 

                    #remove duplicate holidays
                    holidays = [dict(t) for t in {tuple(d.items()) for d in holidays}]


            #write holiday list to csv
            with open("holidays.csv","w", encoding="utf-8") as file:
                writer= csv.DictWriter(file, fieldnames = holidays[0].keys())
                writer.writeheader()
                writer.writerows(holidays)
                
        except Exception as e:
                print(e)

        




        # Scrape Holidays from https://www.timeanddate.com/holidays/us/2022?hol=33554809
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.     

    def numHolidays(self):
        return(len(self.innerHolidays))

        # Return the total number of holidays in innerHolidays
    
    def filter_holidays_by_week(self, year, week_number):
        
        holidays = list(filter(lambda a: a))


        return holidays

        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays

    def displayHolidaysInWeek(holidayList):
        pass

        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    def getWeather(weekNum):
        pass

        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek():
        pass

        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results




# def main():


#     stillgoing = True

#     while stillgoing:

#         print("Holiday Menu \n============ \n1. Add a holday \n2. Remove a Holiday \n3. Save Holiday List \n4. View Holidays \n5. Exit ")
#         choice = int(input("Your choice: "))
        
#         #Add a Holiday
#         if choice == 1:
#             print("\nYou chose Add a Holiday")


#         #Remove a Holiday
#         elif choice == 2:
#             print("\nYou chose Remove a Holiday")

#         #Save Holiday List
#         elif choice == 3:
#             print("\nYou chose Save Holiday List")

#         #View Holidays    
#         elif choice == 4:
#             print("\nYou chose View Holidays")

#         #Exit
#         elif choice == 5:
#             print("Exit \n===== \nAny unsaved changes will be lost! \n")
#             exitLoop = str(input("Are you sure you want exit? [y/n]: ").lower())


#             if exitLoop == "y":
#                 print("\nExiting Program")
#                 stillgoing = False
            
#             elif exitLoop == "n":
#                 print("\nReturning to the main menu\n")
#                 restartLoop = True
            
#             else:
#                 print("\nInvalid Entry! \nReturning to the main menu\n")
#                 restartLoop = True
        
#         #Catch non valid choices
#         else:
#             print("That is not a valid choice. \nReturning to the main menu\n")
#             stillgoing = True

#     # Large Pseudo Code steps
#     # -------------------------------------
#     # 1. Initialize HolidayList Object
#     # 2. Load JSON file via HolidayList read_json function
#     # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
#     # 3. Create while loop for user to keep adding or working with the Calender
#     # 4. Display User Menu (Print the menu)
#     # 5. Take user input for their action based on Menu and check the user input for errors
#     # 6. Run appropriate method from the HolidayList object depending on what the user input is
#     # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


# if __name__ == "__main__":
#     main()


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.





