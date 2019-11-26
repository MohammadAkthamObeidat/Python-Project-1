from functools import reduce

from Employee import Employee
from Student import Student

# Employees==================================================================================

employee1 = Employee(1000, 500, 'HR Consultant', [434, 200, 1020], 'Ahmad Yazan', 'Amman, jordan')
employee2 = Employee(2000, 750, 'Department Manager', [150, 3000, 250], 'Rana Hala',
                     'Aqaba, jordan')
employee3 = Employee(3000, 600, 'HR S Consultant', [304, 1000, 250, 300, 500, 235],
                     'Mohammad Obeidat', 'Irbid, jordan')
employee4 = Employee(4000, 865, 'Director', [], 'Yasmeen Mohammad', 'Karak, jordan')

# Students ===================================================================================
student1 = Student(20191000, 'Java Programming Language', {
    'english': 80,
    'arabic': 90,
    'art': 95,
    'management': 75
}, 'Mohammad Obeidat', 'Irbid, Jordan')

student2 = Student(20182000, 'Software Eng.', {
    'english': 80,
    'arabic': 90,
    'calculus': 85,
    'management': 75,
    'OS': 73,
    'Programming': 90
}, 'Reem Hani', 'Zarqa, Jordan')

student3 = Student(20161001, 'Arts', {
    'english': 83,
    'arabic': 92,
    'art': 90,
    'management': 70
}, 'Nawras Abdullah', 'Amman, Jordan')

student4 = Student(20172030, 'Computer Eng.', {
    'english': 80,
    'arabic': 90,
    'art': 95,
    'calculus': 85,
    'management': 75,
    'OS': 79,
    'Programming': 91
}, 'Amal Raed', 'Tafelah, Jordan')

# ==============================================================================================
# Exercise 1
employees_list = [employee1, employee2, employee3, employee4]
for i in employees_list:
    print(i.show_employee_info())
    print(f'Loans : {i.get_loans()}')

print('===========================================================================================')

# ================================================================================================

# Exercise 2
students_list = [student1, student2, student3, student4]
# for z in students_list:
#     print(z.show_student_info())
print('===========================================================================================')

# ================================================================================================

# Exercise 3
print(f'Total number of employee is {len(employees_list)}')
print('===========================================================================================')

# =================================================================================================
# Exercise 4
print(f'Total number of students is {len(students_list)}')
print('===========================================================================================')

# =================================================================================================
# Exercise 5
for stu in students_list:
    all_avg = [stu.get_avg()]
    print(f'Highest Student Average : {max(all_avg)}')
print('===========================================================================================')

# =================================================================================================
# Exercise 6 + 7
for emp in employees_list:
    print(f'Maximum Loan for employee {emp.number}: {max(emp.get_loans())}')
    print(f'minimum Loan for employee {emp.number}: {min(emp.get_loans())}')
print('===========================================================================================')

# =================================================================================================
# Exercise 8
summation = 0
for employee in employees_list:
    summation = summation + sum(employee.get_loans())
    print(
        f'Loans for employee {employee.number} is {employee.get_loans()} and the average is {sum(employee.get_loans()) / len(employee.get_loans())}')
print(f'The grand average is {summation}')

# =================================================================================================
# Exercise 9
loan_dic = {}
for z in employees_list:
    loan_dic[z.number] = z.get_loans()

# =================================================================================================
# Exercise 10
for o in loan_dic.values():
    print(f'Minimum value in Loan Dic {reduce(lambda a, b: a if a < b else b, o)}')
    print(f'Maximum value in Loan Dic {reduce(lambda a, b: a if a > b else b, o)}')

# =================================================================================================
# Exercise 11

for st in students_list:
    for mark in st.get_marks().values():
        if mark >= 90:
            print(f'{st.get_name()}, the subject is {st.get_subject()} and the marks are {st.get_marks()}')

# =================================================================================================
# Exercise 12
hi_salary = employees_list[0]
for em in employees_list:
    if em.get_salary() > hi_salary:
        hi_salary = em.get_salary()
print(f'The highest salary = {hi_salary}')

# =================================================================================================
# Exercise 13
low_salary = employees_list[0]
for em in employees_list:
    if em.get_salary() < low_salary:
        low_salary = em.get_salary()
print(f'The lowest salary = {low_salary}')

# =================================================================================================
# Exercise 14
for total in employees_list:
    print(f'Total Salaraies = {sum(total.get_salary())}')

# =================================================================================================
# Exercise 15
