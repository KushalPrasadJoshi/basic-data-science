# Author: Kushal Prasad Joshi
# This is written for generating csv files on which we will learn data analysis
# This is very simple data for supervised machine learning only to understand concepts

import csv
import random

# You can change number of calculations according to need
no_of_persons = 500

# Define columns
columns = ["Age", "Salary", "Purchase"]

# Generate required rows of data with some missing values
suscription_data = [columns]
for i in range(no_of_persons):
    age = random.randint(18, 35) if random.random() > 0.2 else random.randint(30, 50)
    salary = random.randint(15000, 50000)
    if age < 32:
        salary = random.randint(15000, 40000) if random.random() > 0.1 else random.randint(35000, 70000)
        purchase = 0 if random.random() > 0.01 else 1
    else:
        salary = random.randint(35000, 70000) if random.random() > 0.1 else random.randint(15000, 40000)
        purchase = 1 if random.random() > 0.01 else 0

    numbers = [age, salary, purchase]
    
    suscription_data.append([age, salary, purchase,])
    
# Write to CSV file
with open(".\\assets\\csv-files\\suscription.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(suscription_data)

print("Your CSV file is generated successfully!!!")
