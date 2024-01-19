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

def writeToTextFile(path:str,students:list,courses:list) -> int:
    studentPath = path + "student.txt"
    coursePath = path + "course.txt"
    markPath = path + "mark.txt"
        
    try:
        with open(studentPath) as file:
            for st in students:
                file.write(st)
    except:
        print(f'no {studentPath}')
        return -1

    try:
        with open(coursePath) as file:
            for cs in courses:
                file.write(cs)
    except:
        print(f"no {coursePath}")
        return -2
    
    try:
        with open(markPath) as file:
            for st in students:
                if st.get__numberOfCourses() == 1:
                    markStr = f"{st.get__mark()}\n"
                else:
                    markStr = ""
                    for i in range(st.get__numberOfCourses()):
                        markStr += f" {st.get__mark()[i]}"
                    markStr += "\n"
                file.write(markStr)
    except:
        print(f"no {markPath}")
        return -3

def unitTest(students:list, courses:list):
    for st in students:
        print(st)
    for cs in courses:
        print(cs)
    for st in students:
        if st.get__numberOfCourses() == 1:
            markStr = f"{st.get__mark()}\n"
        else:
            markStr = ""
            for i in range(st.get__numberOfCourses()):
                markStr += f" {st.get__mark()[i]}"
            markStr += "\n"
        print(markStr)

#region button function
courseList = sampleCourses()
studentList = sampleStudents(courseList)

def sortButtonCmd() -> None:
    sortGPA(studentList)

def listAllOutCmd() -> None:
    listAllOut(studentList)

def shuffleButtonCmd() -> None:
    shuffle(studentList)

def writeToTextFileCmd()-> None:
    path = __file__[:-len(__file__.split('\\')[-1])]
    print(__file__)
    writeToTextFile(path,studentList,courseList)
#endregion

if __name__ == "__main__":
    unitTest(studentList, courseList)
