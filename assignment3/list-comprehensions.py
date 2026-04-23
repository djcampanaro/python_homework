import csv

with open('../csv/employees.csv', 'r') as file:
    reader = list(csv.reader(file))

employee_names = [f'{reader[x][1]} {reader[x][2]}' for x in range(1, len(reader))]
print(employee_names)

employee_names_with_e = [y for y in employee_names if 'e' in y]
print(employee_names_with_e)
