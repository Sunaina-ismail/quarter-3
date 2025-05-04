# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
 
    bank_name = "National Bank."
    
    def __init__(self):
        print(f"Current bank for the customer: {Bank.bank_name}")
        
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"The bank name has been updated to: {cls.bank_name}")



customer1 = Bank()   

Bank.change_bank_name("Meezan Bank.")


customer3 = Bank()   
