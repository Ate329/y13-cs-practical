# Q1
class BankAccount:
    def __init__(self, AccountHolderName, IBAN):
        self.__AccountHolderName = AccountHolderName
        self.__IBAN = IBAN

    def CreateNewAccount(self, NewAccountName, NewIBAN):
        self.__NewAccountHolderName = NewAccountName
        self.__NewIBAN = NewIBAN

    def SetAccountHolderName(self, NewAccountName):
        self.__AccountHolderName = NewAccountName

    def GetAccountHolderName(self):
        return self.__AccountHolderName

    def GetIBAN(self):
        return self.__IBAN

class PersonalAccount(BankAccount):
    def __init__(self, AccountHolderName, IBAN, MonthlyFee, PayStatus):
        super().__init__(AccountHolderName, IBAN)
        self.__IBAN = IBAN
        self.__AccountHolderName = AccountHolderName
        self.__MonthlyFee = MonthlyFee
        self.__PayStatus = PayStatus

    def GetMonthlyFee(self):
        return self.__MonthlyFee

    def GetPayStatus(self):
        return self.__PayStatus

    def SetGetPayStatus(self, status):
        self.__PayStatus = status

    def SetMonthlyFee(self, MonthlyFee):
        self.__MonthlyFee = MonthlyFee

class SavingsAccount(BankAccount):
    def __init__(self, Savings, InterestRate, AccountHolderName, IBAN):
        super().__init__(AccountHolderName, IBAN)
        self.__Savings = Savings
        self.__InterestRate = InterestRate

    def SetInterestRate(self, InterestRate):
        self.__InterestRate = InterestRate

    def GetSavings(self):
        return self.__Savings

# Q2C
#new_customer = ContractTicketHolder("A. Smith", "xyz@abc.xx", 10.0)

# Q3
class NodeClass:
    def __init__(self):
        self.data = ""      # Initialize Data to an empty string
        self.pointer = -1   # Initialize Pointer to -1

    def set_data(self, d: str):
        self.data = d

    def set_pointer(self, x: int):
        self.pointer = x

    def get_data(self) -> str:
        return self.data

    def get_pointer(self) -> int:
        return self.pointer

class QueueClass:
    def __init__(self):
        self.queue = [""] * 50  # List to store NodeClass objects
        self.head = -1  # Initialize Head to -1
        self.tail = -1  # Initialize Tail to -1

    def join_queue(self, new_item: str):
        new_node = NodeClass()  # Create a new Node
        new_node.set_data(new_item)  # Assign the value to Data attribute

        if self.tail == -1:  # If queue is empty
            self.head = 0
            self.tail = 0
        else:
            self.tail += 1  # Move tail forward

        self.queue[self.tail - 1] = new_node.get_data()  # Append Node to the end of the queue
