student_details =[
    {
        "roll_number": 101,
        "name": "Anil Sharma",
        "age": 20,
        "gender": "Male",
        "course": "B.Tech",
        "fasther_name": "Ramesh Sharma",
        "mother_name": "Sita Sharma",
        "Address": "123, ABC Street, City, State, Country"
    },
    {
        "roll_number": 102,
        "name": "Priya Singh",
        "age": 19,
        "gender": "Female",
        "course": "B.Sc",
        "fasther_name": "Rajesh Singh",
        "mother_name": "Sunita Singh",
        "Address": "456, XYZ Street, City, State, Country"
    },
    {
        "roll_number": 103,
        "name": "Rahul Verma",
        "age": 21,
        "gender": "Male",
        "course": "B.Com",
        "fasther_name": "Suresh Verma",
        "mother_name": "Anita Verma",
        "Address": "789, PQR Street, City, State, Country"
    },
    {
        "roll_number": 104,
        "name": "Sneha Patel",
        "age": 20,
        "gender": "Female",
        "course": "B.A",
        "fasther_name": "Manish Patel",
        "mother_name": "Kavita Patel",
        "Address": "321, LMN Street, City, State, Country"
    },
]


# Make Function to Get Id and Output the Student Details

def get_stuident_details(roll_number:int):
    for student in student_details:
        if student["roll_number"]== roll_number:
            return {
                "roll_number": student["roll_number"],
                "name": student["name"],
                "age": student["age"],
                "gender": student["gender"],
                "Address": student["Address"]
            }

    return "Student not found : please check the roll number and try again"


def get_student_details_by_name(name:str):
    for student in student_details:
        if student["name"].lower() == name.lower():
            return student

    return "Student not found : please check the name and try again"


def get_student_details_by_course(course:str):
    for student in student_details:
        if student["course"].lower() == course.lower():
            return {
                "roll_number": student["roll_number"],
                "name": student["name"],
                "age": student["age"],
                "gender": student["gender"],
                "Address": student["Address"]
            }

    return "Student not found : please check the course and try again"

def get_student_details_by_age(age:int):
    for student in student_details:
        if student["age"] == age:
            return student

    return "Student not found : please check the age and try again"

def get_student_details_in_oragnize_way():
    for student in student_details:
        print("Roll Number:", student["roll_number"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Gender:", student["gender"])
        print("Address:", student["Address"])

print("Student Details fatching by roll number")

num =int(input("Enter the roll number of student:-"))

print(get_stuident_details(num))