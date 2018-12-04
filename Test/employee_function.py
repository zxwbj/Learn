from employee import Employee

my_employee = Employee('zxw', 10000)
print(my_employee.name)
print(my_employee.salary)

my_employee.give_raise()
print(my_employee.salary)

my_employee.give_raise(3000)
print(my_employee.salary)
