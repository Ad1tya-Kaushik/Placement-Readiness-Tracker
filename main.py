students = [
    {
        "name": "Aditya",
        "roll_no": "2481095",
        "aptitude": 92,
        "verbal": 88,
        "coding": 95
    },
    {
        "name": "Manas",
        "roll_no": "2481132",
        "aptitude": 75,
        "verbal": 85,
        "coding": 82
    },
    {
        "name": "Prithvi",
        "roll_no": "2481161",
        "aptitude": 45,
        "verbal": 50,
        "coding": 35
    },
    {
        "name": "Akash",
        "roll_no": "2481026",
        "aptitude": 85,
        "verbal": 78,
        "coding": 90
    },
    {
        "name": "Wangang",
        "roll_no": "2481069",
        "aptitude": 55,
        "verbal": 60,
        "coding": 48
    }
]

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

while True:
    aptitude = int(input("Enter aptitude score: "))
    if 0 <= aptitude <= 100:
        break
    else:
        print("Invalid score! Enter between 0 and 100.")

while True:
    verbal = int(input("Enter verbal score: "))
    if 0 <= verbal <= 100:
        break
    else:
        print("Invalid score! Enter between 0 and 100.")

while True:
    coding = int(input("Enter coding score: "))
    if 0 <= coding <= 100:
        break
    else:
        print("Invalid score! Enter between 0 and 100.")

students.append({
    "name": name,
    "roll_no": roll_no,
    "aptitude": aptitude,
    "verbal": verbal,
    "coding": coding
})

def average(student):
    total = (
        student["aptitude"]
        + student["verbal"]
        + student["coding"]
    )
    return total / 3

def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Needs practice"

def top_scorer(students):
    return max(students, key=average)

def needs_practice(students, limit=40):
    result = []
    for student in students:
        if average(student) < limit:
            result.append(student)
    return result

print("\nPLACEMENT READINESS REPORT")
print("-" * 75)

print(
    f"{'Name':<12}"
    f"{'Roll No':<12}"
    f"{'Average':<12}"
    f"{'Grade':<20}"
)

print("-" * 75)

for student in students:
    avg = average(student)
    student_grade = grade(avg)

    print(
        f"{student['name']:<12}"
        f"{student['roll_no']:<12}"
        f"{avg:<12.2f}"
        f"{student_grade:<20}"
    )

print("-" * 75)

topper = top_scorer(students)
print("\nTop Scorer:", topper["name"])
print("Highest Average:", round(average(topper), 2))

print("\nStudents Who Need Practice:")
weak_students = needs_practice(students)
if weak_students:
    for student in weak_students:
        print(student["name"], "-", round(average(student), 2))
else:
    print("No students need extra practice.")