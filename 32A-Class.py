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
#This would create second object of Employee class
emp2 = Employee("Manni", 5000)


emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)