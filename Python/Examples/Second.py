class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance
    
acc=BankAccount()
n=int(input())
for i in range(n):	
	choice=input().split()

	if choice[0]=='Deposite':
		acc.deposit(int(choice[1]))

	elif choice[0]=='Withdraw':
		acc.withdraw(int(choice[1]))

	elif choice[0]=='Balance':
		print(acc.get_balance())

