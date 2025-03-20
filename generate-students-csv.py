# Author: Kushal Prasad Joshi
# This is written for generating csv files on which we will learn data analysis


import csv
import random

# You can change number of students according to need
no_of_students = 500

# Following facilities are provided by a university
student_id_start = 100000  # Student id starts with this number
faculties = ["Engineering", "Management", "Education", "Law"]  # Has these faculties
levels = ["Graduate", "Post Graduate", "Phd"]
programs_under_engineering = [
    "Computer",
    "Civil",
    "Architecture",
    "Electrical",
    "IT",
    "Electronic and Communication",
]
programs_under_management = ["BBA", "BBS", "BBM"]
programs_under_education = ["English", "Nepali"]
programs_under_law = ["LLB"]
enrollment = ["Physical", "Online"]

# Don't change these values because it can create problems in other files
file_name = "Students.csv"
# Define columns
columns = [
    "Roll No",
    "Name",
    "Gender",
    "Age",
    "Faculty",
    "Level",
    "Program",
    "Year",
    "Year of Study",
    "GPA",
    "Enrollment Status",
    "Phone Number",
    "Email",
]

# Generate required rows of data with some missing values
students_data = [columns]
for i in range(student_id_start, student_id_start + no_of_students):
    roll_no = i
    name = f"Student{i - student_id_start}"
    gender = random.choice(["M", "F"]) if random.random() > 0.1 else None
    faculty = random.choice(faculties) if random.random() > 0.1 else None

    # Choosing level according to faculty
    if faculty is not None:
        level = random.choice(levels) if random.random() > 0.1 else None
    else:
        level = None

    # Choosing program according to faculty and level
    if faculty == "Engineering":
        program = (
            random.choice(programs_under_engineering) if random.random() > 0.1 else None
        )
    elif faculty == "Management":
        program = (
            random.choice(programs_under_management) if random.random() > 0.1 else None
        )
    elif faculty == "Education":
        program = (
            random.choice(programs_under_education) if random.random() > 0.1 else None
        )
    elif faculty == "Law":
        program = random.choice(programs_under_law) if random.random() > 0.1 else None
    else:
        program = None

    # Choosing age based on level
    if level == "Graduate":
        age = (
            random.choice([i for i in range(19, 27)]) if random.random() > 0.1 else None
        )
    elif level == "Post Graduate":
        age = (
            random.choice([i for i in range(24, 35)]) if random.random() > 0.1 else None
        )
    elif level == "Phd":
        age = (
            random.choice([i for i in range(26, 60)]) if random.random() > 0.1 else None
        )
    else:
        age = (
            random.choice([i for i in range(19, 60)]) if random.random() > 0.1 else None
        )

    year = (
        random.choice([2020, 2021, 2022, 2023, 2024]) if random.random() > 0.1 else None
    )
    gpa = round(random.uniform(2.0, 4.0), 2) if random.random() > 0.1 else None

    # select year of study according to  level
    if level == "Graduate":
        year_of_study = 4
    elif level == "Post Graduate":
        year_of_study = 3
    elif level == "Phd":
        year_of_study = 2
    else:
        year_of_study = None

    enrollment_status = random.choice(enrollment) if random.random() > 0.1 else None
    email = f"student{i}@university.edu" if random.random() > 0.1 else None
    phone_number = (
        f"977-{random.randint(9800000000, 9899999999)}"
        if random.random() > 0.1
        else None
    )

    students_data.append(
        [
            roll_no,
            name,
            gender,
            age,
            faculty,
            level,
            program,
            year,
            year_of_study,
            gpa,
            enrollment_status,
            phone_number,
            email,
        ]
    )

# Write to CSV file
with open(".\\assets\\csv-files\\students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

print("Your CSV file is generated successfully!!!")
