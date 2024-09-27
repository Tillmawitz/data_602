# Q1: Create a class called BankAccount that has four attributes: bankname, firstname,
# lastname, and balance.
# The default balance should be set to 0.
# In addition, create ...
# ● A method called deposit() that allows the user to make deposits into their balance.
# ● A method called withdrawal() that allows the user to withdraw from their balance.
# ● Withdrawal may not exceed the available balance. Hint: consider a conditional argument
# in your withdrawal() method.
# ● Use the __str__() method in order to display the bank name, owner name, and current
# balance.
# ● Make a series of deposits and withdrawals to test your class

class BankAccount():
    
    def __init__(self, bankname, firstname, lastname, balance = 0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def deposit(self, money):
        if money >= 0:
            self.balance += money
        else:
            print("Negative deposits are not accepted. Make a withdrawal instead.")
        
    def withdrawal(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            print("Withdrawals cannot exceed the current balance.")
        
    def __str__(self) -> str:
        return f"The account of {self.firstname} {self.lastname} at {self.bankname} has a balance of ${self.balance}"
    
def main():
    joe = BankAccount("1st National", "Joe", "Smith")
    print(joe)
    joe.deposit(-1)
    joe.deposit(100)
    print(joe)

    jane = BankAccount("Last Local", "Jane", "Doe", 500)
    print(jane)
    joe.withdrawal(500)
    joe.withdrawal(50)
    print(joe)

    jane.deposit(1000)
    joe.deposit(20)
    print(jane)
    print(joe)

if __name__=="__main__":
    main()