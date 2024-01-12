from openpyxl import load_workbook
from random import randint
from math import floor

class Course():
    __courseName:str
    __courseID:str
    __credit:int

    def __init__(self, courseName:str, courseID:str, courseCredit:int ) -> None:
        self.__courseName = courseName
        self.__courseID = courseID
        self.__credit = courseCredit

    def get__id(self) -> str:
        return self.__courseID
    
    def get__name(self) -> str:
        return self.__courseName 
    
    def get__credit(self) -> int:
        return self.__credit

    def printOut(self) -> None:
        print(f'Course: {self.__courseName}, ID: {self.__courseID}\n')

class Student():
    __name:str
    __id:str
    __dob:str
    __courses:dict = {
        "course": [],
        "mark": [],
    }
    __gpa:float

    def addCourse(self, course:Course, mark:float = 0) -> None:
        self.__courses["course"].append(course)
        self.__courses["mark"].append(mark)

    def __calculateGPA(self) -> float:
        gpa:float = 0
        totalCredit:int = 0
        for i in range(0,len(self.__courses["course"])):
            course = self.__courses["course"][i]
            mark = self.__courses["mark"][i]
            totalCredit += course.get__credit()
            gpa += course.get__credit() * mark 
        return gpa/totalCredit

    def __init__(self,name:str,id:str,dob:str,course:Course|list,mark:float|list=0) -> None:
        if type(course) == list:
            noc = len(course)

            if type(mark) != list:
                mark = [mark]
                for i in range(1,noc):
                    mark.append(0)
            elif len(mark) < noc:
                for i in range(len(mark),noc):
                    mark.append(0)
        
        for i in range(0,len(mark)):
            mark[i] = floor(mark[i])

        self.__courses["course"] = course
        self.__courses["mark"] = mark
        self.__gpa = self.__calculateGPA()
        self.__name = name
        self.__id = id
        self.__dob = dob

    def set__courses(self, c:dict) -> None:
        self.__courses = c

    def get__name(self) -> str:
        return self.__name

    def get__dob(self) -> str:
        return self.__dob
    
    def get__id(self) -> str:
        return self.__id
    
    def get__gpa(self) -> float:
        return self.__gpa

    def printOut(self) -> None:
        print(f'{self.__name}, {self.__id}, {self.__dob} has GPA: {self.__gpa} and involved these courses:')
        for i in range(0,len(self.__courses["course"])):
            print(f'{self.__courses["course"][i].get__name()}: {self.__courses["mark"][i]}')



def main():
    path = __file__[:-len(__file__.split('\\')[-1])]
    
    wb = load_workbook(path + "studentData.xlsx")
    ws = wb.active

    app = Course("Advanced Programming with Python","APP",4)
    ads = Course("Algorithm and Data Structure","ADS",3)
    oop = Course("Object Oriented Programming","OOP",3)
    courseList = [app,ads,oop]
    studentList = []

    for i in range(2,471):
        name = ws.cell(row=i,column=2).value +" "+ ws.cell(row=i,column=3).value
        
        dob = str(ws.cell(row=i,column=4).value)

        if len(dob) > 10:
            dob = dob[:-9]

        id = ws.cell(row=i,column=1).value

        markList = [0,0,0]
        markList[0] = randint(5,18)
        markList[1] = randint(5,18)
        markList[2] = randint(5,18)

        student = Student(name,id,dob,courseList,markList)
        studentList.append(student)
        student.printOut()


main()   