# Write a script that performs the following steps:

- Collect the following individual pieces of data from the user:
- First name
- Last name
- City where they live
- Their hourly wage
- The number of hours they work each week
- Present the collected information based on the data input in a format like:

Hi, Firstname Lastname! How are you?
I hope the weather is nice in City.
Based on the information you provided, you earn X dollars per week, approximately Y dollars per month, and Z dollars per year.


---------------------------------------------------------------------------------------------------------------------------------


Version 1: Procedural Version

The procedural code organizes logic into standalone functions (weeklyPay, monthlyPay, yearlyPay) and runs them in a linear, top-down flow.
It relies on direct input and function calls, without encapsulating data or behavior inside a class.

Version 2: OOP Version

The object-oriented code wraps related data (wage, hours) and behavior (pay calculations) inside a Person class.

A @classmethod (create_person_object) validates user input before object creation, ensuring that values such as wage (float) and hours (int) are correct before performing calculations.





 



