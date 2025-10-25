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
