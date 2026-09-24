class SalaryEngine:

    def __init__(self, salary):
        self.salary = salary

    def calculate_tax(self):
        if self.salary <= 25000:
            return 0
        elif self.salary <= 50000:
            return round(self.salary * 0.10, 2)
        elif self.salary <= 100000:
            return round(self.salary * 0.20, 2)
        else:
            return round(self.salary * 0.30, 2)

    def calculate_deduction(self):
        return round(self.salary * 0.05, 2)

    def calculate_bonus(self):
        if self.salary >= 50000:
            return round(self.salary * 0.10, 2)
        else:
            return 0

    def calculate_net_salary(self):
        tax = self.calculate_tax()
        deduction = self.calculate_deduction()
        bonus = self.calculate_bonus()

        return round(self.salary + bonus - tax - deduction, 2)

    def display(self):
        print("Basic Salary:", self.salary)
        print("Tax:", self.calculate_tax())
        print("Deduction:", self.calculate_deduction())
        print("Bonus:", self.calculate_bonus())
        print("Net Salary:", self.calculate_net_salary())
salary = input("Enter salary: ")
try:
    salary = float(salary)
    if salary <= 0:
        print("Invalid salary. Salary must be greater than 0.")
    else:
        employee = SalaryEngine(salary)
        employee.display()
except ValueError:
    print("Invalid input. Please enter a number.")