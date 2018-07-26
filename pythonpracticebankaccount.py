class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "%s's account. Balance: $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print round(balance, 2)
  
  def deposit(self, amount):
    if amount < 0:
      print("You must deposit a larger amount.")
    	return
    else:
      print(round(amount, 2))
    self.balance += amount
    self.show_balance()
   
  def withdraw(self, amount):
    if amount > BankAccount.balance:
      print("You cannot withdraw more than you have in your account.")
      return
    else:
      print round(amount, 2)
      self.balance -= amount
      self.show_balane()

my_account = BankAccount("Arthur")
print (__repr__(my_account))
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account.__repr__()

