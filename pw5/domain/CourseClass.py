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
