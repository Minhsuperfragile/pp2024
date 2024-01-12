from input import sampleCourses,sampleStudents
from os import system as st, name as osn
from random import shuffle

def sortGPA(studentList:list) -> None:
    n = len(studentList)

    for i in range(n): #bubble sort
        swapped = False
        for j in range(0,n-i-1):
            if studentList[j].get__gpa() < studentList[j+1].get__gpa():
                studentList[j], studentList[j+1] = studentList[j+1], studentList[j]
                swapped = True
        if swapped == False:
            break

def listAllOut(students:list)->None:
    for student in students:
        student.printOut()

def clear() -> None:
    st('cls' if osn == 'nt' else 'clear')

#region button function
studentList = sampleStudents(sampleCourses())

def sortButtonCmd() -> None:
    sortGPA(studentList)

def listAllOutCmd() -> None:
    listAllOut(studentList)

def shuffleButtonCmd() -> None:
    shuffle(studentList)
#endregion