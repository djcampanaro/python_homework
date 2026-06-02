import pandas as pd
import numpy as np


# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

# Part 1: Creating a DataFrame from a Dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)

# Part 2: Add a New Column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

# Part 3: Modify an Existing Column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1

# Part 4: Save the DataFrame as a CSV File
task1_older.to_csv('employees.csv', index=False)


# Task 2: Loading Data from CSV and JSON

# Part 1: Read data from a CSV file
task2_employees = pd.read_csv('employees.csv')

# Part 2: Read data from a JSON file
json_employees = pd.read_json('additional_employees.json')

# Part 3: Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)


# Task 3: Data Inspection - Using Head, Tail, and Info Methods

# Part 1: Use the head() method
first_three = more_employees.head(3)

# Part 2: Use the tail() method
last_two = more_employees.tail(2)

# Part 3: Get the shape of a DataFrame
employee_shape = more_employees.shape

# Part 4: Use the info() method
more_employees.info()


# Task 4: Data Cleaning

dirty_data = pd.read_csv('dirty_data.csv')
clean_data = dirty_data.copy()
clean_data = clean_data.drop_duplicates()
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors="coerce")
clean_data['Age'] = clean_data['Age'].replace('unknown', pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors="coerce")
clean_data['Salary'] = clean_data['Salary'].replace('unknown', pd.NA)
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format='mixed', errors='coerce')
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
