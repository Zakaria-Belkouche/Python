# Zakaria Belkouche 22/10/25

# This is the same task as before, but this time, I OOP  

fname = input("First Name: ")
lname = input("Last Name: ")
city = input("City of Residence: ")
hourlyWage = float(input("Hourly wage: "))
workingHours = int(input("Hours worked per week: "))


class Person:
    def __init__(self, wage, hours):
        self.wage = wage
        self.hours = hours

    @classmethod
    def create_person_object(cls, x, y):
        if not isinstance(x, float):
            print("wage has to be a float")
            return None
        if not isinstance(y, int):
            print("Hours worked has to be an integer")
            return None

        return cls(x, y)


    def weeklyPay(self):
        return self.wage * self.hours

    def monthlyPay(self):
        return self.wage * self.hours * 4

    def yearlyPay (self):
        return self.wage * self.hours * 52


x = Person.create_person_object(hourlyWage, workingHours)

if x:
    print(f"Hi, {fname} {lname}! How are you?")
    print(f"I hope the weather is nice in {city}")
    week = x.weeklyPay()
    monthly = x.monthlyPay()
    yearly = x.yearlyPay()

    print(f"Based on the information you provided, you earn {week} dollars per week, approximately {monthly} dollars per month, and {yearly} dollars per year.")


