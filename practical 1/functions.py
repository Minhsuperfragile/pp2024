studentDictionary = {
    "students": [],
    "numberOfStudents": 0,
    "numberOfCourses": 0,
    "courses": []
}

#region Input Functions
def getNumberOfStudent(n:int):
    studentDictionary["numberOfStudents"] = n

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
                print(f"{studentDictionary['students'][i]['name']} got {course['mark'][i]:.2f}")
#endregion
                