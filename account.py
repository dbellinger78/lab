class Account:
    '''
    A class representing an Account object.
    '''
    def __init__(self, acccount_name: str, balance=0) -> None:
        '''
        Constructor method takes an account name and creates an Account object.
        :param account_name: This is the name of the person that has the account.
        :param account_balance: This is the currency balance of the account. The 
        account balance is set to 0 at initialization.
        '''
        self.__acccount_name = acccount_name
        self.__account_balance = balance

    def deposit(self, amount: float) -> bool:
        '''
        Setter function takes the amount and verifies that it is a is a positive float 
        value and then updates the account_balance variable of the Account object. 

        :param amount: This is the dollar amount that is to be deposited in the account.
        :return: If the account_balance is successfully updated the method returns a 
        boolean value of True. If amount is not a positive float value and the 
        account_balance is not updated a boolean value of False is returned.
        '''
        if amount <= 0:
            return False
        elif amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False   

    def withdraw(self, amount: float) -> bool:
        '''
        Setter function takes the amount and verifies that it is a is a positive float 
        value and that the amount is not greater than the current account_balance, 
        then updates the account_balance variable of the Account object. 

        :param amount: This is the dollar amount that is to be withdrawn from the account.
        :return: If the account_balance is successfully updated the method returns a 
        boolean value of True. If amount is not a positive float value or is greater than
        the current account_balance, the account_balance is not updated a boolean value of 
        False is returned.
        '''
        if amount <= 0 or amount > self.__account_balance:
            return False
        elif amount > 0 and amount <= self.__account_balance:
            self.__account_balance = self.__account_balance - amount
            return True
        else:
            return False      
    
    def get_balance(self) -> float:
        '''
        Getter function is used to retrieve the account_balance of the Account object.

        :return: The float value stored in the account_balance variable will returned.
        ''' 
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Getter function is used to retrieve the account_name of the Account object.

        :return: The string value stored in the account_name variable will returned.
        ''' 
        return self.__acccount_name 

