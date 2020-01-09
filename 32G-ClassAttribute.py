class Employee:
    'Common base class for all employees'
    empCount = 0

    #The first method __init__() is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)



#This would create first object of Employee class
emp1 = Employee("Zara", 2000)

emp1.salary = 7000  # Add an 'salary' attribute.
emp1.name = 'xyz'  # Modify 'age' attribute.



emp1.displayEmployee()

del  emp1

emp1.displayEmployee()


print ("Total Employee %d" % Employee.empCount)