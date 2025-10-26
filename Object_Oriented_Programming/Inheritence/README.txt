						Inheritance Self-Assessment: File System

Completion requirements:

- For this assessment, you will use Python to model a computer's file system.
- Create a class called FileItem that represents any file in an operating system.
- Research and identify attributes that are common to all files in an OS, such as permissions, owner, size, and so on.
- Create a class called CsvFile that inherits from FileItem and that represents a CSV file in an operating system.
- Include attributes that are specific to a CSV file.
- Create a class JpgFile that inherits from FileItem and that represents a JPG file in an operating system.
- Include attributes that are specific to a JPG file.
- Create a class Mp3File that inherits from FileItem and that represents an MP3 file in an operating system.
- Include attributes that are specific to an MP3 file.

Challenge:

- Create a class Directory that inherits from FileItem and that represents a directory in an operating system.
- Create a filesystem with at least 20 objects
- Include at least three objects of each type (CsvFile, JpgFile, Mp3File, and Directory)
- Include a directory structure with a depth of at least three (directory in a directory in a directory)
- Include at least one directory that contains at least two other directories and at least two files.

Requirements:
- Include your name and a current date in a comment on the first line of code.
- Use meaningful names so that another developer can easily read your code to understand what it does.
- The final version of this file must include at least four separate classes: the original FileItem class and three child classes that inherit from FileItem.
- Each class must include appropriate attributes for that class.


						------------------------------------------


								Burger Shop


You have been tasked with building a user interface for a new restaurant named Burger Shop that allows customers to place custom orders for hamburgers.

Instructions:

Update the code below to create a working program.

The provided code includes a framework for the program, including a series of classes that represent each item a customer might purchase, such as burgers, sides (e.g., fries, onion rings, or a garden salad), drinks, and combo platters that include multiple items. Note that each of these classes inherits from a FoodItem class that should define the properties that are common to all items on the menu. The framework also includes functions that you will define to work with the classes and create the customer's order.

Start by asking the customer for their name, which will be used to identify the order. The program should then perform the following steps:

- Ask the customer if they want a burger, a side, a drink, or a combo.
- A combo must include a burger, a side, and a drink.
- Prompt them for details about their selection, such as condiments for a burger, what kind and size of drink, and so on.
- Create the item based on their selections.
- Add the item to the Order class.
- Repeat these steps until the customer doesn't want to order anything else.
- Display the order details including the price.
- Thank the customer for their business.
- A complete order output should include at least one of the items on the menu, the price for each item ordered, and the total price based on all items in the order.

- Also include an option that allows the customer to cancel their order at any point in the ordering process. The output should thank the user for their business but not display anything ordered.
