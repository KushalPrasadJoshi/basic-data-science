# Author: Kushal Prasad Joshi
# This is written for generating csv files on which we will learn data analysis
# This is very simple data for supervised machine learning only to understand concepts

import csv
import random

# You can change number of calculations according to need
no_of_calculations = 5000

# Define columns
columns = ["Number1", "Number2", "Number3", "Total Sum"]

# Generate required rows of data with some missing values
calculations_data = [columns]
for i in range(no_of_calculations):
    number1 = random.uniform(1, 1000) if random.random() > 0.1 else None
    number2 = number1 + random.uniform(1, 1000) if number1 is not None and random.random() > 0.1 else None
    number3 = number1 + random.uniform(1, 1000) if number1 is not None and random.random() > 0.1 else None

    numbers = [number1, number2, number3]
    valid_numbers = [num for num in numbers if num is not None]
    
    total_sum = sum(valid_numbers) if random.random() > 0.1 else None
    
    calculations_data.append([number1, number2, number3, total_sum])
    
# Write to CSV file
with open(".\\assets\\csv-files\\maths.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(calculations_data)

print("Your CSV file is generated successfully!!!")
