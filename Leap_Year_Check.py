def message():

        print("Please wait!!! we are confirming.")
def check_leap_year():

    print("Welcome to the script, this help you\ncheck if any year is a leap year or not")
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        message()
        
        print(f"Thank you for using this service\n{year} is a Leap Year")
    else:
        message() 
        
        print(f"Thank you for using this service \n{year} is NOT a Leap Year")

check_leap_year()
