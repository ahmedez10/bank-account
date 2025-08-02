class balanceException(Exception):

    pass


class bankAccount:
    def __init__(self,initialamount,acctname):
        self . balance= initialamount
        self.name=acctname
        print(f"\n account'{self.name}'created.\n balance= $'{self.balance}'")

    def getbalance(self):

        print(f"\n account'{self.name}'\n balance= $'{self.balance}'")

    def deposit(self,amount) :
        self.balance += amount
        print (f"\n Deposit complete. \n account'{self.name}'\n balance= $'{self.balance}'")
        self.getbalance()
    def viabletransaction(self,amount):
        if amount <= self.balance:
            return
        else:
            raise  balanceException(
                f"\n sorry,account'{self.name}'only has a balance $'{self.balance}'"
            )
    def withdraw(self,amount):
        try:
            self.viabletransaction(amount)
            self.balance =self.balance - amount
            print("\n withdraw complete")
            self.getbalance()
        except balanceException as error:

            print(f"\n withdraw interrupter:'{error}'")
    def transfer(self,amount,account):
        try :
            print('\n***********\n\n beginning'
                  'transfer..🤑')
            self.viabletransaction(amount)
            self. withdraw(amount)
            account.deposit(amount)
            print('\n transfer complete!(●◡●)')
        except balanceException as error:
            print(f"\n transfer interrupter:'{error}'")



class interestrewardsacct(bankAccount):
    def deposit(self,amount):
        self.balance += (amount * 1.05)
        print ("\n deposit complete")
        self.getbalance()


class savingacct(interestrewardsacct):
    def __init__(self,initialamount,acctname):
        super().__init__(initialamount,acctname)
        self . fee=5
    def withdraw(self,amount):
        try:
            self.viabletransaction(amount+self.fee)
            self.balance =self.balance - (amount+self.fee)
            print("\n withdraw complete.")
            self.getbalance()
        except balanceException as error:
            print(f"\n withdraw interrupter:'{error}'")










                