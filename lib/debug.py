#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department
from employee import Employee
import ipdb


def reset_database():
    Employee.drop_table()
    Department.drop_table()
    Department.create_table()
    Employee.create_table()

    # Create seed data
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    human_resources = Department.create(
        "Human Resources", "Building C, East Wing")
    Employee.create("Amir", "Accountant", payroll.id)
    Employee.create("Bola", "Manager", payroll.id)
    Employee.create("Charlie", "Manager", human_resources.id)
    Employee.create("Dani", "Benefits Coordinator", human_resources.id)
    Employee.create("Hao", "New Hires Coordinator", human_resources.id)


reset_database()
ipdb.set_trace()


Department.get_all()
#==> [<Department 1: Payroll, Building A, 5th Floor>, <Department 2: Human Resources, Building C, East Wing>]

Employee.get_all()
#==> [<Employee 1: Amir, Accountant, Department ID: 1>, <Employee 2: Bola, Manager, Department ID: 1>, <Employee 3: Charlie, Manager, Department ID: 2>, <Employee 4: Dani, Benefits Coordinator, Department ID: 2>, <Employee 5: Hao, New Hires Coordinator, Department ID: 2>]


# An employee works in one department. Let's get the first employee:
employee = Employee.find_by_id(1)
employee
#==> <Employee 1: Amir, Accountant, Department ID: 1>

# We can use the employee `department_id` value to get the single associated `Department` instance:
Department.find_by_id(employee.department_id)
#==> <Department 1: Payroll, Building A, 5th Floor>


# A department may have many employees. Let's select the payroll department:
payroll = Department.find_by_id(1)
payroll
#==> <Department 1: Payroll, Building A, 5th Floor>


# We can call the employees() method to get the list of employees that work in the payroll department.
payroll.employees()
# ==> [<Employee 1: Amir, Accountant, Department ID: 1>, <Employee 2: Bola, Manager, Department ID: 1>]

