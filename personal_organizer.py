
# Check for and adjust month input if necessary
def validate_month(month):
    while(month > 12 or month < 1):
        month = int(input("Invalid month. Please enter value from 1-12: "))
    return month

# Check for and adjust day input if necessary
# (don't forget about leap year)
def validate_day(month, day, year):
    leap = 0
    if(year % 4 == 0):
        leap = 1
    if(year % 100 == 0 and year % 400 != 0):
        leap = 0

    num_days=31

    if(month == 4 or month == 6 or month == 9 or month == 11):
        num_days=30
    if(month == 2):
        if (leap == 1):
            num_days = 29
        else:
            num_days = 28
    while(day < 1 or day > num_days):
        day = int(input("Invalid day. Please enter value from 1-"+str(num_days)+": "))
    return day

# This function is used to print all events to the user in the format
# Event
# Date: Month Day, Year
def print_events():
    months = ["January","February","March","April","May","June","July", "August","September","October","November","December"]
    print("\n******************** List of Events ********************")
    for i, _ in enumerate(event_name):
        print(event_name[i])
        print("Date: " + str(months[event_month[i]-1]) + " " + str(event_day[i]) + ", " + str(event_year[i]))

# This function is used to prompt, adjust and
# append values to the 4 parallel arrays
def add_event():
    # Prompt the user for the event details
    add_name = input("What is the event: ")
    add_year = int(input("What is the year: "))
    add_month = int(input("What is the month (number): "))
    add_month = validate_month(add_month)
    add_day = int(input("What is the date: "))
    add_day = validate_day(add_month, add_day, add_year)

    event_name.append(add_name)
    event_month.append(add_month)
    event_day.append(add_day)
    event_year.append(add_year)

#*********** MAIN **********
event_name = []
event_month = []
event_day = []
event_year = []

add_event()
cont = input("Do you want to enter another date? NO to stop: ")
while cont != "NO":
    add_event()
    cont = input("Do you want to enter another date? NO to stop: ")

print_events()