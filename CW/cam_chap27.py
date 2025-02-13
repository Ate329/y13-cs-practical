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
    
