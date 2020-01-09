class Employee:

    empcount=0
    name=''
    salary=0
    def __init__(self):
        Employee.empcount+=1

    def displayCount(self):
        print("Total number of count:%d"%Employee.empcount)

    def displayEmployee(self):
        print("Name:",Employee.name,"Salary=%d"%Employee.salary)


emp1=Employee()
emp2=Employee()
emp3=Employee()
emp1.name="Harshal"

print(hasattr(emp1,"salary"))
print(getattr(emp1,"salary"))
setattr(emp1,"salary",2000)
print(getattr(emp1,"salary"))

emp1.displayCount()
