import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


# url ='https://www.timeanddate.com/holidays/us/2022?hol=33554809'

# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
@dataclass
class Holiday:
    
    name: str
    date: datetime    

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name
   
    @property 
    def date(self):
        return self.date

    @date.setter
    def date(self, new_date):
        self.__date = new_date
    
    @date.deleter
    def date(self):
        del self.__date

    def __str__ (self):
        return "%s falls on %s" % (self.name, self.date)

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
   

    def addHoliday(holidayObj):
        
        Holiday(holidayObj)
        innerHolidays.append(holidayObj)
        print("Holiday has been added")

        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday

    def findHoliday(HolidayName, Date):
        
        Holidayname = Holiday.name()
        Date = Holiday.date()
        
        pass



        # Find Holiday in innerHolidays
        # Return Holiday

    def removeHoliday(HolidayName, Date):
        pass

        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday

    def read_json(filelocation):
        pass

        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

    def save_to_json(filelocation):
        pass

        # Write out json file to selected file.
        
    def scrapeHolidays():
        pass

        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.     

    def numHolidays():
        pass

        # Return the total number of holidays in innerHolidays
    
    def filter_holidays_by_week(year, week_number):
        pass

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



def main():


    stillgoing = True

    while stillgoing:

        print("Holiday Menu \n============ \n1. Add a holday \n2. Remove a Holiday \n3. Save Holiday List \n4. View Holidays \n5. Exit ")
        choice = int(input("Your choice: "))
        
        #Add a Holiday
        if choice == 1:
            print("\nYou chose Add a Holiday")


        #Remove a Holiday
        elif choice == 2:
            print("\nYou chose Remove a Holiday")

        #Save Holiday List
        elif choice == 3:
            print("\nYou chose Save Holiday List")

        #View Holidays    
        elif choice == 4:
            print("\nYou chose View Holidays")

        #Exit
        elif choice == 5:
            print("Exit \n===== \nAny unsaved changes will be lost! \n")
            exitLoop = str(input("Are you sure you want exit? [y/n]: ").lower())


            if exitLoop == "y":
                print("\nExiting Program")
                stillgoing = False
            
            elif exitLoop == "n":
                print("\nReturning to the main menu\n")
                restartLoop = True
            
            else:
                print("\nInvalid Entry! \nReturning to the main menu\n")
                restartLoop = True
        
        #Catch non valid choices
        else:
            print("That is not a valid choice. \nReturning to the main menu\n")
            stillgoing = True

    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    # 2. Load JSON file via HolidayList read_json function
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    # 3. Create while loop for user to keep adding or working with the Calender
    # 4. Display User Menu (Print the menu)
    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main()


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




