from input import getPath,decompress,pickleRead
from os import system as st, name as osn
from random import shuffle
from pandas import DataFrame
from pickle import dump

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

def writeToTextFile(path:str,students:list,courses:list) -> int:
    studentPath = path + "student.txt"
    coursePath = path + "course.txt"
    markPath = path + "mark.txt"
        
    try:
        with open(studentPath,'w',encoding= 'utf-8') as file:
            file.seek(0)
            for st in students:
                file.write(st.__str__() + "\n")
    except Exception as e:
        print(f'no {studentPath} \n{e}')
        return -1

    try:
        with open(coursePath,'w',encoding='utf-8') as file:
            for cs in courses:
                file.write(cs.__str__() + '\n')
    except Exception as e:
        print(f"no {coursePath}\n{e}")
        return -2
    
    try:
        with open(markPath,'w',encoding='utf-8') as file:
            for st in students:
                if st.get__numberOfCourses() == 1:
                    markStr = f"{st.get__mark()}\n"
                else:
                    markStr = ""
                    for i in range(st.get__numberOfCourses()):
                        markStr += f" {st.get__mark()[i]}"
                    markStr += "\n"
                file.write(markStr)
    except Exception as e:
        print(f"no {markPath}\n{e}")
        return -3

def compress(students:list) -> int:
    data = {
        'name':  [],
        'id': [],
        'dob': [],
        'course': [],
        'size of course': [students[0].get__numberOfCourses()],
        'gpa': []
        }
    
    for i in range(data['size of course'][0]):
        data[students[0].get__course()[i].get__name()] = []
        data['course'].append(students[0].get__course()[i].get__id()+'@'+str(students[0].get__course()[i].get__credit()))

    for st in students:
        data['name'].append(st.get__name())
        data['id'].append(st.get__id())
        data['dob'].append(st.get__dob())
        data['gpa'].append(st.get__gpa())
        for i in range(data['size of course'][0]):
            data[st.get__course()[i].get__name()].append(st.get__mark()[i])

    for i in range(len(data['course']),len(data['name'])):
        data['course'].append('')

    for i in range(1,len(data['name'])):
        data['size of course'].append(None)
    
    DataFrame(data).to_csv('students.dat')
    return 0

def pickleWrite(studentList:list):
    with open(getPath() + 'students.dat', 'wb') as file:
        for st in studentList:
            dump(st, file)


#region button CMD

courseList = []
studentList = []

if decompress(studentList,courseList):
    studentList = pickleRead()
    courseList = studentList[0].get__course()

class cmdFunction:
    @staticmethod
    def clear() -> None:
        st('cls' if osn == 'nt' else 'clear')
    @staticmethod
    def sortButtonCmd() -> None:
        sortGPA(studentList)
    @staticmethod
    def listAllOutCmd() -> None:
        listAllOut(studentList)
    @staticmethod
    def shuffleButtonCmd() -> None:
        shuffle(studentList)
    @staticmethod
    def writeToTextFileCmd() -> None:
        writeToTextFile(getPath(),studentList,courseList)
#endregion