# Zakaria Belkouche 22/10/25

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
