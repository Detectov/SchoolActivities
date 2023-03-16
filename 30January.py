from dataclasses import dataclass
import os
os.system("cls")
@dataclass 
class Course: 
    name: str
    grade: float
   


def create_course():
    print("Type the name of the class: ")
    name = input()
    print("Type the grade you got in the course: ")
    grade = float(input())
    course = Course(name, grade)
    return course

def courses () -> list[str]:

    print("How many courses are you taking?")
    numcourses = int(input())
    courselist = [create_course() for course in range(numcourses)]

    return courselist

def calculateGPA(courses: list[str]) -> float:
    gpa = sum(course.grade for course in courses)/ len (courses)

    return gpa

courses = courses()

print(calculateGPA(courses), courses)

