from random import random

studentDictionary = {
    "students": [],
    "numberOfStudents": 0,
    "numberOfCourses": 0,
    "courses": []
}

#region Input Functions
def getNumberOfStudent(n:int):
    studentDictionary["numberOfStudents"] = n
    studentDictionary["blankStudent"] = n

def getStudentInformation(name:str, Id:str,Dob:str):
    if len(studentDictionary["students"]) == studentDictionary["numberOfStudents"]:
        studentDictionary["numberOfStudents"] += 1
    student = {
        "name":name,
        "id":Id,
        "dob":Dob
    }
    studentDictionary["students"].append(student)

def getNumberOfCourses(n:int):
    studentDictionary["numberOfCourses"] = n

def getCourseInfomation(Id:str,name:str):
    if len(studentDictionary["courses"]) == studentDictionary["numberOfCourses"]:
        studentDictionary["numberOfCourses"] += 1
    course = {
        "name":name,
        "id":Id,
        "mark": []
    }
    for i in range(0,studentDictionary["numberOfStudents"]):
        course['mark'].append(0)
    studentDictionary["courses"].append(course)

def getStudentMark(studentID:str,courseID:str,mark:float):
    index = 0
    for student in studentDictionary["students"]:
        if student["id"] == studentID:
            break
        index += 1

    for course in studentDictionary["courses"]:
        if course["id"] == courseID:
            course["mark"][index] = mark
#endregion

#region Listing Functions
def listCourses():
    for course in studentDictionary["courses"]:
        print(f"Course Name: {course['name']} - ID: {course['id']}")

def listStudent():
    for student in studentDictionary["students"]:
        print(f"{student['name']} - {student['id']} - {student['dob']}")

def listMark(courseID:str):
    for course in studentDictionary["courses"]:
        if courseID == course["id"]:
            for i in range(0,studentDictionary["numberOfStudents"]):
                print(f"{studentDictionary['students'][i]['name']} got {course['mark'][i]:.2f} in {course['name']}")
#endregion

#region main
#add students
getNumberOfStudent(5)
getStudentInformation("Nguyễn Trọng Minh","22BI13304","27/10/2004")
getStudentInformation("Trần Lương Hoàng Anh","22BI13039","02/11/2004")
getStudentInformation("Lê Duy Anh","22BI13017","04/03/2004")
getStudentInformation("Nguyễn Mạnh Hưng","22BI13183","11/02/2004")
getStudentInformation("Lê Xuân Lộc","22BI13256","12/06/2004")
getStudentInformation("Nguyễn Văn Minh","22BI13306","30/01/2004")
getStudentInformation("Vũ Hoàng Mai Nhi","22BI13352","11/04/2004")
getStudentInformation("Lê Thuận Ninh","22BI13354","19/07/2004")
getStudentInformation("Nguyễn Thị Vân","22BI13459","18/09/2004")

#add courses
getNumberOfCourses(3)
getCourseInfomation("ADS","Algorithm and Data Structure")
getCourseInfomation("OOP","Object Oriented Programming")
getCourseInfomation("APP","Advanced Programming with Python")

#add mark
for student in studentDictionary["students"]:
    getStudentMark(student["id"],"ADS",random() * 20)
    getStudentMark(student["id"],"APP",random() * 20)
    getStudentMark(student["id"],"OOP",random() * 20)

#listing all out
print("\nAll students:\n")
listStudent()
print("\nAll courses:\n")
listCourses()
print("\nStudent Mark in APP:\n")
listMark("APP")
print("\nStudent Mark in ADS\n")
listMark("ADS")
print("\nStudent Mark in OOP\n")
listMark("OOP")

#endregion