# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Barry Massoudi>,<5/28/2025>,<Classes and Functions>
# ------------------------------------------------------------------------------------------ #
import json
import os
from importlib.metadata import pass_none

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

class file_processor:
    def __init__(self, FILE_NAME: str) -> str:
        '''
        :param FILE_NAME: This is the name of the file to read.
        '''
        self.FILE_NAME = FILE_NAME
        pass


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
@staticmethod
def Read_From_File(FILE_NAME: str, students: list[dict[str, str]]) -> dict:
    '''

    :param FILE_NAME: Contains the name of the file to read.
    :param students: Contains the students data to read.
    :return: Returns the students data.
    '''
    student: dict = {}

    try:
        file = open(FILE_NAME, "r")
        Loaded_Data = json.load(file)
        students.extend(Loaded_Data)
        for student in students:
            print(student["FirstName"],student["LastName"],student["CourseName"])
        file.close()

    except Exception as e:
        print("Error: There was a problem with reading the file.")
        print("Please check that the file exists and that it is in a json format.")
        print("-- Technical Error Message -- ")
        print(e.__doc__)
        print(e.__str__())
    finally:
        if file.closed == False:
            file.close()
    pass

@staticmethod
def Enter_User_Data(students: list[dict[str, str]]) -> dict:
    '''
    :param students: Contains the students data to read.
    :return: Returns the students data.
    '''
    # Input user data
    student_first_name: str = ''  # Holds the first name of a student entered by the user.
    student_last_name: str = ''  # Holds the last name of a student entered by the user.
    course_name: str = ''  # Holds the name of a course entered by the user.
    student_data: dict = {}  # one row of student data
    try:
         student_first_name = input("Enter the student's first name: ")
         if not student_first_name.isalpha():
            raise ValueError("The first name should not contain numbers.")
         student_last_name = input("Enter the student's last name: ")
         if not student_last_name.isalpha():
               raise ValueError("The last name should not contain numbers.")
         course_name = input("Please enter the name of the course: ")
         student_data = {"FirstName": student_first_name,
                         "LastName": student_last_name,
                         "CourseName": course_name}
         students.append(student_data)
         print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
    except ValueError as e:
          print(e)  # Prints the custom message
          print("-- Technical Error Message -- ")
          print(e.__doc__)
          print(e.__str__())
    except Exception as e:
          print("Error: There was a problem with your entered data.")
          print("-- Technical Error Message -- ")
          print(e.__doc__)
          print(e.__str__())
    pass

    # Present the current data

@staticmethod
def Print_User_Data(students: list[dict[str, str]]) -> dict:
    """
    :param students: Contains the students data to read.
    :return: Returns the students data.
    """

    # Process the data to create and display a custom message
    print("-" * 50)
    for student in students:
        print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
    print("-" * 50)
    pass

@staticmethod
def Write_to_File(FILE_NAME: str, students: list[dict[str, str]]):
    """
    :param FILE_NAME: Contains the name of the file to write.
    :param students: Contains the students data to write.
    :return: Returns the students data.
    """

    try:
        file = open(FILE_NAME, "w")
        json.dump(students, file, indent=4)

        file.close()
        print("The following data was saved to file!")
        for student in students:
            print(f'Student {student["FirstName"]} '
              f'{student["LastName"]} is enrolled in {student["CourseName"]}')
    except Exception as e:
        if file.closed == False:
            file.close()
        print("Error: There was a problem with writing to the file.")
        print("Please check that the file is not open by another program.")
        print("-- Technical Error Message -- ")
        print(e.__doc__)
        print(e.__str__())
        pass

#Main input and output class
class IO:

    #Run the main body of the program
    @staticmethod
    def main():
        """

        :return: Runs the main body of the program.
        """
        # Read the contents of .json file
        Read_From_File(FILE_NAME, students=students)

        while (True):

            # Present the menu of choices
            print(MENU)
            menu_choice = input("What would you like to do: ")
            if menu_choice == "1":  # This will not work if it is an integer!
                Enter_User_Data(students= students)
                continue

            elif menu_choice == "2":
                Print_User_Data(students= students)
                continue

            elif menu_choice == "3":
                Write_to_File(FILE_NAME, students= students)
                continue

            elif menu_choice == "4":
                break  # out of the loop

            else:
                print("Please only choose option 1, 2, or 3")

        print("Program Ended")

    if __name__ == "__main__":
        main()





