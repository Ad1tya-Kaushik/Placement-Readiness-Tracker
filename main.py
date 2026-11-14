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