class Employee:
    def __init__(self, eid, ename):
        self.eid = eid
        self.ename = ename
        #self.calsalary = 15000
        #self.calfund = 0
        
    def toString(self):
        print("ID: ", self.eid)
        print("Name: ", self.ename) 
        print("Salary: ", self.calsalary)
        print("Fund: ", self.calfund)
        print()

    def Calsalary(self):
        self.calsalary = 15000

    def CalFund(self):
        self.calfund = 0

class Permanent_emp(Employee):
    def __init__(self,eid, ename, month_salary = 15000):
        super().__init__(eid, ename)
        self.month_salary  = month_salary
    
    def Calsalary(self):
        self.month_tax = self.month_salary / 100
        self.calsalary = (self.month_salary - (self.month_tax * 3)) - (self.month_tax*5)
    
    def CalFund(self):
        self.calfund = 2 * (self.month_tax * 3)

class TmpEmployee(Employee):
    def __init__(self,eid, ename,  hours):
        Employee.__init__(self, eid, ename)
        self.hours = hours
    def CalFund(self):
        self.calfund = ((self.hours * 200) / 100) * 3
    def Calsalary(self):
        self.calsalary = self.hours * 200

employee2 = Permanent_emp(6311454, "Khajornsak", 150000)
employee2.Calsalary()
employee2.CalFund()
employee2.toString()

employee = TmpEmployee(6311455, "JaChin", 8) 
employee.Calsalary()
employee.CalFund()
employee.toString()      
