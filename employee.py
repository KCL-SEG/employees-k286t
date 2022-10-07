"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract="", commission="", m_salary = 0, hour=0, h_rate=0, concomm=0, c_rate=0, bonus=0):
        self.name = name
        self.contract = contract
        self.m_salary = m_salary
        self.commission = commission
        self.hour = hour
        self.h_rate = h_rate
        self.concomm = concomm
        self.c_rate = c_rate
        self.bonus = bonus

    def get_pay(self):
        total = 0
        if self.contract=="Salary":
            total+=self.m_salary
        elif self.contract=="Hourly":
            total+=self.hour*self.h_rate
        if self.commission=="Bonus":
            total+=self.bonus
        elif self.commission=="Contract":
            total+=self.concomm*self.c_rate
        return total


    def __str__(self):
        report = ""
        report += self.name + " works on a " + self.contract_message() 
        if self.commission_message():
            report += " and " + self.commission_message()  
        report+= ". Their total pay is " + str(self.get_pay()) + "."
        return report

    def contract_message(self):
        message = ""
        if self.contract=="Salary":
            message+="monthly salary of " + str(self.m_salary)
        elif self.contract=="Hourly":
            message+="contract of " + str(self.hour) + " hours at " + str(self.h_rate) + "/hour" 
        return message

    def commission_message(self):
        message = ""
        if self.commission=="Contract":
            message+="receives a commission for " + str(self.concomm) + " contract(s) at " + str(self.c_rate) + "/contract."
        elif self.commission=="Bonus":
            message+="receives a bonus commission of " + str(self.bonus) 
        return message


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',contract="Salary", m_salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',contract="Hourly", hour=100, h_rate=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', contract="Salary", m_salary=3000, commission="Contract",concomm=4, c_rate=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',contract="Hourly", hour=150, h_rate=25, commission="Contract",concomm=3, c_rate=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', contract="Salary", m_salary=2000, commission="Bonus", bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contract="Hourly", hour=120, h_rate=30, commission="Bonus", bonus=600)

