# ai)
class Employee():
    def __init__(self, Hourlypay:float = None, EmployeeNumber:str = None, JobTitle:str = None):
        self.Hourlypay = Hourlypay
        self.EmployeeNumber = EmployeeNumber
        self.JobTitle = JobTitle
        self.PayYear2022 = [None for _ in range(52)]
# aii)
def GetEmployeeNumber(self) -> str:
    return self.EmployeeNumber

# aiii)
def SetPay(self, week_number:int, hours_worked:float) -> None:
    global employee
    employee = Employee()
    employee.PayYear2022[week_number] = hours_worked * employee.Hourlypay

# aiv)
def GetTotalPay() -> float:
    global employee
    total = 0.0
    for money in employee.PayYear2022:
        total = total + money
    
    return total

# b)
class Manager(Employee):
    def __init__(self, Hourlypay:float = None, EmployeeNumber:str = None,
                JobTitle:str = None, BonusValue:float = None):
        super().__init__(Hourlypay, EmployeeNumber, JobTitle)
        self.BonusValue = BonusValue
    
    # bii)
    def SetPay(self, week_number:int, hours_worked:float) -> None:
        global employee
        self.PayYear2022[week_number] = self.Hourlypay * (hours_worked * (1 + (self.BonusValue / 100)))

# c)
Pay
