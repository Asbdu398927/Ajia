class BankAccount:
  def __init__(self,account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number 
    self.__account_holder_name = account_holder_name 
    self.__account_balance =initial_balance 

  def deposit(self,amount):
    if amount > 0:
      self.__account_balance +=amount
      print (f"Deposited$(amount:2f)into account{self.__account_number}")
    else:
      print("invalid deposit amount. please deposita positive amount.")

  def withdrew(self,amount):
    if amount>0:
      if self.__account_balance >= amount:
        self.__account_balance -=amount 
        print(f"withdrew $ {amount:2f}from account {self.__account_number}")
      else:
        print("Insufficient balance.cannot withdrew. ")
    else:
      print ("invalid withdrew amount  please withdrewa positive amount. ")

  
  def display_balance(self):
    print (f"account{self.__account_number}balance:${self.__account_balance:2f}")


#testing the bank account class 
if __name__ =="__main__":
  account1 = BankAccount ("123456","John",1000.0)
#deposit money
  account1.deposit(500.0)
#withdrew money
  account1.withdrew(200.0)
#display balance 
  account1.display_balance()


                                                                         



  
