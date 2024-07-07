class CreditCard:
    """
    A consumer credit card.
    """

    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.

        The initial balance is zero
        customer is the name of the customer
        bank in the name of the bank
        acnt is the account identifier
        limit is the credit limit
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """
        Return customer name.
        """
        return self._customer
    
    def get_bank(self):
        """
        Return the bank's name
        """
        return self._bank
    
    def get_account(self):
        """
        Return the card identifying number (typically stored as a string)
        """
        return self._account
    
    def get_limit(self):
        """
        Return current credit limit.
        """
        return self._limit
    
    def get_balance(self):
        """
        Return current balance.
        """
        return self._balance
    
    def charge(self, price):
        """
        Charge given to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payments(self, amount):
        """
        Process customer payment that reduces balance.
        """
        self._balance -= amount