from datetime import datetime
import json
import csv
from bs4 import BeautifulSoup
from hamcrest import none
import requests
from dataclasses import dataclass
import datetime




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
        dateTime = datetime.datetime.strptime(date,"%Y-%m-%d")
        self.__date = dateTime.date()
     

    
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
            # else:
            #     return (f"\n{HolidayName} not found in the list\n")
        return False

        # Find Holiday in innerHolidays
        # Return Holiday

    def removeHoliday(self, HolidayName, Date):
        
        x = self.findHoliday(HolidayName, Date)

        if x == False:
            print("\nError:\n")
            print(f"Sorry {HolidayName} could not be found") 
            
        else:
            print("\nSuccess\n")
            print(f"Deleting {HolidayName} from list")
            self.innerHolidays.remove(x)
                  

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
        
        with open(filelocation, "w") as f:
            tempList = []

            for i in self.innerHolidays:
                holiday = {'name':i.name, 'date':i.date}
                tempList.append(holiday)
                
            json.dump(tempList, f,default=str)

        

        # Write out json file to selected file.
        
    def scrapeHolidays(self):
        

        try:
            holidays = []
        
            for year in range(2020,2025):

                url = (f'https://www.timeanddate.com/holidays/us/{year}?hol=33554809')
                response = requests.get(url)
                html = response.text

                soup = BeautifulSoup(html, 'html.parser')
                table = soup.find('table', attrs={'id':'holidays-table'})
                body = table.find('tbody')


                for row in body.find_all('tr'):
                    
                    #Holiday Dictionary
                    HolidayDict = {}

                    date = row.find('th')
                    name = row.find('a')

                    #check rows where date and name are not None
                    if date is not None and name is not None:
                        
                        #format date correctly
                        date = date.text
                        date = f"{date} {year}"
                        date= datetime.datetime.strptime(date,"%b %d %Y")
                        date = date.date()
                        # .strftime('%Y-%m-%d')
                        
                        HolidayDict['Name'] = name.text
                        HolidayDict['Date'] = date
                    
                    holidays.append(HolidayDict)

                    #remove empty dictionaries from list
                    while {} in holidays:
                        holidays.remove({}) 

                    #remove duplicate holidays
                    holidays = [dict(t) for t in {tuple(d.items()) for d in holidays}]

            
            for i in holidays:

                hol = (Holiday(i['Name'], i['Date']))

                if hol not in self.innerHolidays:
                    self.innerHolidays.append(hol)

            # # write holiday list to csv
            # with open("holidays.csv","w", encoding="utf-8") as file:
            #     writer= csv.DictWriter(file, fieldnames = holidays[0].keys())
            #     writer.writeheader()
            #     writer.writerows(holidays)
                
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
        
        holidays = list(filter(lambda x: x.date.isocalendar()[1] == week_number and x.date.isocalendar()[0] == year, self.innerHolidays))

        return holidays

        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays

    def displayHolidaysInWeek(self, holidayList):

        for holiday in holidayList:
            print(holiday)
        
        

        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    # def getWeather(self, weekNum):
    #     pass

        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek(self):
        today = datetime.datetime.now()
        todayWeek = today.isocalendar()[1]

        return todayWeek

        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results

#helper function to check date format
def ValiDate(date):

    format = "%Y-%m-%d"
    res = True
    try: 
        res = bool(datetime.datetime.strptime(date, format))
        return True

    except:
        return False


def main():

    mainList = HolidayList()
    mainList.read_json('Assesments/HolidayManagerAssesment/holidays.json')
    # mainList.scrapeHolidays()

    stillgoing = True

    while stillgoing:

        try:

            print("\nHoliday Menu \n============ \n1. Add a holday \n2. Remove a Holiday \n3. Save Holiday List \n4. View Holidays \n5. Exit \n")
            choice = int(input("Your choice: "))
            
            #Add a Holiday
            if choice == 1:

                print("\nAdd a Holiday\n===========\n")
                hol = str(input("Holiday: "))
                date = str(input("Date: "))

                dateFormat = ValiDate(date)

                #ensure proper date format was entered
                while dateFormat == False:               
                    print("\nError: Invalid Date Format \nMust be in the following format: YYYY-MM-DD\n")
                    date = str(input(f"Date for {hol}: "))
                    dateFormat = ValiDate(date)

                #adding user input holidayList
                print("Success:\n")
                mainList.addHoliday(Holiday(hol,date))

            #Remove a Holiday
            elif choice == 2:
                print("\nRemove a Holiday\n================\n")

                hol = str(input("Holiday Name: "))
                date = str(input(f"Enter the date for {hol}: "))
                dateFormat = ValiDate(date)

                #ensure proper date format was entered
                while dateFormat == False:               
                    print("\nError: Invalid Date Format \nMust be in the following format: YYYY-MM-DD\n")
                    date = str(input(f"Date for {hol}: "))
                    dateFormat = ValiDate(date)

                date = datetime.datetime.strptime(date,"%Y-%m-%d")
                date = date.date()
                mainList.removeHoliday(hol, date)

            #Save Holiday List
            elif choice == 3:
                print("\nSave Holiday List\n=============")
                
                saveLoop = True
                while saveLoop:
                    save = str(input("\nAre you sure you want to save your changes? [y/n]: ").lower())

                    if save == "y":
                        print("\nSuccess:\nYour changes have been saved.")
                        mainList.save_to_json('SavedHolidays.json')
                        saveLoop = False
                    elif save == "n":
                        print("\nCanceled:\nHoliday list file save canceled.\n")
                        saveLoop = False
                    else:
                        print("\n*Invalid Entry!*\n")


            #View Holidays    
            elif choice == 4:
                print("\nView Holidays\n=============")
                
                yearCheck = False
                while yearCheck == False:
                    try:
                        yr = int(input("\nWhich Year?: "))
                        yearCheck = True
                    except:
                        print("\nError: please enter an integer for year!\n")
                        

                weekCheck = False
                while weekCheck == False:
                    wk = (input("Which Week?: #[1-52, Leave blank for the current week]: "))

                    if wk == "":
                        wk = mainList.viewCurrentWeek()
                        weekCheck = True
                    else:
                        try:
                            wk =int(wk)
                            weekCheck = True
                        
                        except:
                            print("\nError: please enter an integer for week!\n")
            
                x = mainList.filter_holidays_by_week(yr, wk)

                if len(x) == 0:
                    print(f"\nThere are no Holidays for {yr} Week #{wk}.")
                else:
                    print(f"\nThese are the Holidays for {yr} Week #{wk}:")
                    mainList.displayHolidaysInWeek(x)

            #Exit
            elif choice == 5:
                print("Exit \n===== \nAny unsaved changes will be lost! \n")
                exitLoop = str(input("Are you sure you want exit? [y/n]: ").lower())


                if exitLoop == "y":
                    print("\nExiting Program")
                    stillgoing = False
                
                elif exitLoop == "n":
                    print("\nReturning to the main menu\n")
                    stillgoing = True
                
                else:
                    print("\nInvalid Entry! \nReturning to the main menu\n")
                    stillgoing = True
            
            #Catch non valid choices
            else:
                print("That is not a valid choice. \nReturning to the main menu\n")
                stillgoing = True
        
        #catch non int choices
        except:
            print("\nPlease only input numbers\n")
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


