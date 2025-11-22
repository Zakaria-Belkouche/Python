=================================================================

			Task 1

🧪 Task 1 (Beginner Python Task)

Write a Python program that:

Asks the user for their name

Asks the user for their age

Prints a friendly sentence using both values

Example idea (but not the final answer!):

“Hello ___, you are ___ years old!”

Keep it simple.
Don’t worry about validation yet — just basic input + print.


=================================================================

			Task 2

🧪 Task 2 (Beginner → Slightly Harder)

Write a Python program that:

Asks the user for a number

Converts it into an integer

Prints whether the number is even or odd

			Task2a


🧪 Rewrite Task (Lambda Version)  

Create a lambda function that:

Takes a number

Returns the string "Even" or "Odd"

Then:

Ask the user for a number

Convert it to an integer

Use the lambda to determine even/odd

Print the result in a sentence

=================================================================


			Task 3

🧪 Task 3

Write a Python program that:

Asks the user for three numbers

Converts them to integers

Determines which of the three numbers is the largest

Prints the result as a simple message



=================================================================

			Task 4

🧪 Task 4 (Beginner → Logic + Loops Practice)

Write a Python program that:

Asks the user for a word

Loops through each letter in that word

Counts how many vowels the word contains

vowels are: a, e, i, o, u (lowercase is fine)

Prints the final count of vowels


=================================================================

			Task 5

🧪 Task 5 (Beginner → Intermediate: Loops + Logic + Lists)

Write a Python program that:

Asks the user for a sentence (multiple words)

Splits the sentence into individual words

Counts how many words are longer than 4 letters

Prints the count

=================================================================

			Task 6

Write a Python program that:

Asks the user to enter a sentence (or multiple sentences).

Splits the text into individual words.

Counts how many times each word appears.

Prints the result in a clear way, for example:

Word counts:
hello: 3
world: 1
python: 2

==============================================================

			Task 7

Using the code you just wrote (your word counter), extend it so that:

After building the counts dictionary

You sort the words by how often they appear

You print them in descending order (most frequent → least frequent)

Example output format:

The word 'hello' appears 5 times
The word 'world' appears 3 times
The word 'python' appears 1 time

==============================================================

			Task 8

Asks the user to enter a sentence

Converts the sentence into a list of words

Produces the following slices from that list, and prints each one:

The first 3 words

The last 3 words

Every second word

The list reversed

The middle section (from index 2 to index -2)

Do not use loops for any slicing.

================================================================

			Task 9

Write a Python program that does the following:

1. Ask the user for a filename

Example prompt:

Enter the filename: 

2. Open the file and read its contents

Load the entire text into a string.

3. Clean the text

convert to lowercase

remove punctuation

remove extra spaces

4. Split the text into a list of words
5. Produce the following results:
✔ A. Total number of words
✔ B. The first 10 words
✔ C. The last 10 words
✔ D. The 10 most frequent words (sorted by count)
✔ E. The entire text reversed (word order reversed)
6. Print all results clearly


================================================================

			Task 10

🧪 Task 10: Create a Dog class with:

A constructor (__init__) that takes:

a name

an age

Two methods:

bark() → prints "Woof! My name is ___"

birthday() → increases the dog’s age by 1

Make a dog object and test the methods.

================================================================

			Task 11

Create two classes:
1. Dog class

Attributes:
name, age, breed

Methods:
bark() → returns "Woof! I'm <name>!"
birthday() → increases age by 1
info() → returns a string describing the dog

2. Owner class
Attributes:
name, dogs → a list that will hold Dog objects

Methods:
add_dog(dog) → adds a Dog to the list
list_dogs() → prints info for each dog
oldest_dog() → returns the Dog with the highest age
number_of_dogs() → returns how many dogs the owner has

Your main program should:
Create one Owner
Create 2 or 3 Dog objects
Add the dogs to the Owner

Print:
all dogs the owner has
the oldest dog
the number of dogs

