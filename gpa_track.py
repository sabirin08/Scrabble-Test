"""

Program Description:
This program allows a user to add multiple students to the course until a stop word has been entered.

Author: Sabirin Mohamed
"""
#Stores the first name, last name, and gpa of each student entered.
class Student:
    def __init__(self, first, last, gpa):
        self.first = first
        self.last = last
        self.gpa = gpa


    def get_first(self):
        return self.first


    def get_last(self):
        return self.last
    
    def get_gpa(self):
        return self.gpa


#Stores the Student objects into the roster list.
class Course:
    def __init__(self):
        self.roster = []

#Adds a student to the roster.
    def add_student(self, student):
        self.roster.append(student)
        
#Returns the amount of students in the roster.
    def course_size(self):
        return len(self.roster)

#Finds the student with the highest gpa among those stored in the roster.
    def find_student_highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError('Exception: Course Roster is Empty')
        return max(self.roster, key=lambda student: student.get_gpa())

class EmptyRosterError(Exception):
    pass

def main():
    course = Course()
    
#Creates a loop for the user to add multiple students.
    while True:
        print("Welcome to CSC/DSCI 1301: Principles in CS/DS 1")
        print("Please Add Students to the Course: (quit or q to exit).")

        first_name = input("\nEnter First Name: ")
        
#Allows the user to enter a stop word for the program to stop.
        if first_name.lower() == 'quit' or first_name.lower() == 'q':
            break

        last_name = input("Enter Last Name: ")

        try:
            gpa = float(input("Enter GPA: "))
            
#Presents an error and tells the user a non-numeric gpa was entered.
        except ValueError:
            print("Error: Enter a Numeric GPA")
            continue

        student = Student(first_name, last_name, gpa)
        course.add_student(student)
    print(f"Course Size: {course.course_size()} students")

    try:
        top_student = course.find_student_highest_gpa()
        print(f"Top Student: {top_student.get_first()} {top_student.get_last()} (GPA: {top_student.get_gpa()})")

#Tells the user the roster is empty.
    except EmptyRosterError as e:
        print(e)

if __name__ == "__main__":

    main()
