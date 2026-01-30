class BankAccount():
    def __init__(self,acc_no,name,balance):
        self.acc_no = acc_no                            #Abstract class
        self.name = name
        self._bal = balance

    
    def deposit(self,amount):
        self._bal+=amount
        return self._bal
    
    def withdraw(self,amount):
        if amount>self._bal:
            return "Insuficient funds!!"
        else:
            self._bal-=amount
            return self._bal
    
    def get_balance(self):
        return self._bal
    
    def calc_interest(self):
        pass                    #Abstract class method

class SavingsAccount(BankAccount):
    def calc_interest(self):
        interest = self._bal * 0.04
        return interest

class CurrentAccount(BankAccount):
    def calc_interest(self):
        return 0

class BankApp:
    def __init__(self):
        self.account = None
    def create_account(self,acc_no,name,balance,acc_type):
        if acc_type.lower()=="savings":
            self.account = SavingsAccount(acc_no,name,balance)        
        elif acc_type.lower() == "current":
            self.account = CurrentAccount(acc_no,name,balance)
        return "Account Created Successfully"
    
    def withdrawmoney(self,amount):
        return self.account.withdraw(amount)            #Composition1
    def depositmoney(self,amount):
        return self.account.deposit(amount)             #Composition2
    def check_bal(self):
        return self.account.get_balance()               #Composition3
    def get_interest(self):
        return self.account.calc_interest()             #Composition4

app =BankApp()
print(app.create_account(100,"Rahul",10000,"Savings"))
print("Balance after Withdraw: ",app.withdrawmoney(2000))
print("Balance after Deposit: ",app.depositmoney(2000))
print("Balance is",app.check_bal())