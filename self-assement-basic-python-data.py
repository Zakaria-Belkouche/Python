# Write a script that performs the following steps:

# Collect the following individual pieces of data from the user:
# First name
# Last name
# City where they live
# Their hourly wage
# The number of hours they work each week
# Present the collected information based on the data input in a format like:

# Hi, Firstname Lastname! How are you?
# I hope the weather is nice in City.
# Based on the information you provided, you earn X dollars per week, approximately Y dollars per month, and Z dollars per year.

fname = input("First Name: ")
lname = input("Last Name: ")
city = input("City of Residence: ")
hourlyWage = float(input("Hourly wage: "))
workingHours = int(input("Hours worked per week: "))


def weeklyPay(pay, hours):
    return pay * hours

def monthlyPay(pay, hours):
    return pay * hours * 4

def yearlyPay(pay, hours):
    return pay * hours * 52


    
x = weeklyPay(hourlyWage, workingHours)
y = monthlyPay(hourlyWage, workingHours)
z = yearlyPay(hourlyWage, workingHours)



print(f"Hi, {fname} {lname}! How are you?")
print(f"I hope the weather is nice in {city}")
print(f"Based on the information you provided, you earn {x} dollars per week, approximately {y} dollars per month, and {z} dollars per year.")