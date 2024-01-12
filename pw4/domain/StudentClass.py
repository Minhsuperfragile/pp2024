from domain.CourseClass import Course
from math import floor

class Student():
    __name:str
    __id:str
    __dob:str
    __course:list|Course
    __mark:list|float
    __gpa:float
    __numberOfCourse:int

    def addCourse(self, course:Course, mark:float = 0) -> None:
        self.__course.append(course)
        self.__mark.append(mark)
        self.__numberOfCourse += 1

    def __calculateGPA(self) -> float:
        gpa:float = 0
        totalCredit:int = 0
        for i in range(0,self.__numberOfCourse):
            course = self.__course[i]
            mark = self.__mark[i]
            totalCredit += course.get__credit()
            gpa += course.get__credit() * mark 
        return gpa/totalCredit

    def __init__(self,name:str,id:str,dob:str,course:Course|list,mark:float|list=0) -> None:
        if type(course) == list:
            noc = len(course)
            self.__numberOfCourse = noc
            if type(mark) != list:
                mark = [mark]
                for i in range(1,noc):
                    mark.append(0)
            elif len(mark) < noc:
                for i in range(len(mark),noc):
                    mark.append(0)
        else:
            self.__numberOfCourse = 0
            if type(mark) == list:
                self.addCourse(course,mark[0])
            else:
                self.addCourse(course,mark)

        for i in range(0,len(mark)):
            mark[i] = floor(mark[i])
        
        self.__course = course
        self.__mark = mark
        self.__gpa = self.__calculateGPA()
        self.__name = name
        self.__id = id
        self.__dob = dob

    def set__mark(self, mark:list) -> None:
        self.__mark = mark

    def get__name(self) -> str:
        return self.__name

    def get__dob(self) -> str:
        return self.__dob
    
    def get__id(self) -> str:
        return self.__id
    
    def get__gpa(self) -> float:
        return self.__gpa
    
    def get__mark(self) -> list:
        return self.__mark

    def printOut(self) -> None:
        print(f'{self.__name}, {self.__id}, {self.__dob} has GPA: {self.__gpa} and involved these courses:')
        for i in range(0,self.__numberOfCourse):
            print(f'{self.__course[i].get__name()}: {self.__mark[i]}')
