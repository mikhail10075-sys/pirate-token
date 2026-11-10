class Account():
    def __init__(self,store_owner,pin):
        self.store_owner = store_owner
        self.__pin = pin
    def check_pin_status(self):
        print("Owner Status:", self.store_owner)
        print("PIN is safe.")
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated successfully")
    def check_pin(self,entered_pin):
        if entered_pin == self.__pin:
            print("Access granted")
        else:
            print("Access denied")
    def __str__(self):        
        return "Account holder: "+ self.store_owner

my_account = Account("Ethan",2958)    
print(my_account)

my_account.check_pin_status()

my_account.__pin = '9090'
print("Tried changing the pin from outside!")

my_account.check_pin('9090')
my_account.check_pin('2958')

my_account.set_pin('9090')
my_account.check_pin('9090')

