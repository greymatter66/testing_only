#OOP practice 2

class Employee:

    bonus_amount = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    def apply_bonus(self):
        self.pay_plus = int(self.pay * self.bonus_amount)
        return self.pay_plus
        

    def details(self):
        print("Employee Name: {} {}\n Monthly Pay: {:,}\n Bonus Rate: {} %".format(self.first,self.last,self.pay,Employee.bonus_amount))
    
emp1 = Employee('John', 'Ryan', 3500)
emp2 = Employee('Martin', 'Burke', 4000)

print("Name: {} {}\n Pay: {}\n Pay plus Bonus: {:,} euro".format(emp1.first, emp1.last, emp1.pay, emp1.apply_bonus()))
print()

print("Name: {} {}\n Pay: {}\n Pay plus Bonus: {:,} euro".format(emp2.first, emp2.last, emp2.pay, emp2.apply_bonus()))
print()   

print(Employee.details(emp1))
print()

print(Employee.details(emp2))

