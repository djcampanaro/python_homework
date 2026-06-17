import csv
import custom_module
import os
import traceback

from datetime import datetime

# Task 2

def read_employees():
    employee_data = {}
    entries = []
    first_row = True

    try:
        with open('../csv/employees.csv', 'r') as file: 
            reader = csv.reader(file)
            for row in reader:
                if first_row:
                    employee_data['fields'] = row
                    first_row = False
                elif not first_row:
                    entries.append(row)
            employee_data['rows'] = entries
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    else:
        return employee_data

employees = read_employees()

# Task 3
def column_index(column_header=""):
    return employees['fields'].index(column_header)
    
employee_id_column = column_index('employee_id')

# Task 4
first_name_column = column_index('first_name')
def first_name(row_num=int):
    return employees['rows'][row_num][first_name_column]

# Task 5
def employee_find(employee_id=int):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees['rows']))
    return matches

# Task 6
def employee_find_2(employee_id=int):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# Task 7
def sort_by_last_name():
    last_name_index = column_index('last_name')
    employees['rows'].sort(key=lambda row : row[last_name_index])
    return employees['rows']

sort_by_last_name()

# Task 8
def employee_dict(row=[]):
    employee_info = {}
    fields = employees['fields']
    employee_zip = list(zip(fields, row))
    for i in range(1, len(employee_zip)):
        employee_info[employee_zip[i][0]] = employee_zip[i][1]
    return employee_info

thomas_dict = employee_dict(employees['rows'][1])

# Task 9
def all_employees_dict():
    employees_dict = {}
    for row in employees['rows']:
        employee_id = row[employee_id_column]
        employee_information = employee_dict(row)
        employees_dict[employee_id] = employee_information
    return employees_dict

all_employees_by_id = all_employees_dict()

# Task 10
def get_this_value():
    this_value = os.environ.get(key='THISVALUE')
    return this_value

# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret('Shamaz')

# Task 12
def read_minutes():

    def read_csv_files(csv_file):
        minutes_dict = {}
        minutes_rows = []
        first_row = True

        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if first_row:
                        minutes_dict['fields'] = row
                        first_row = False
                    elif not first_row:
                        minutes_rows.append(tuple(row))
                minutes_dict['rows'] = minutes_rows
        except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
        else:
            return minutes_dict
    
    min1 = read_csv_files('../csv/minutes1.csv')
    min2 = read_csv_files('../csv/minutes2.csv')
    return min1, min2

minutes1, minutes2 = read_minutes()
print(type(minutes1))

# Task 13
def create_minutes_set():
    minutes1_set = set(minutes1['rows'])
    minutes2_set = set(minutes2['rows'])
    minutes_combine_set = minutes1_set.union(minutes2_set)
    return minutes_combine_set

minutes_set = create_minutes_set()

# Task 14
def create_minutes_list():
    minutes_as_list = list(map(lambda x : (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    return minutes_as_list

minutes_list = create_minutes_list()

# Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda entry : entry[1])
    minutes_list_sort = list(map(lambda x : (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    try:
        with open('./minutes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1['fields'])
            for row in minutes_list_sort:
                writer.writerow(row)
    except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
    return minutes_list_sort

write_sorted_list()
