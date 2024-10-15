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
    
    def make_payment(self, amount):
        """
        Process customer payment that reduces balance.
        """
        self._balance -= amount

class PredatoryCreditCard(CreditCard):
    """
    An extension to CreditCard that compunds interest and fees.
    """
    def __init__(self, customer, bank, acnt, limit, apr):
        """
        Creates new predatory credit card instance.
        customer the name of the customer (e.g., "Jared Otieno")
        bank     the name of the bank(e.g., "Co-operative Bank of Kenya")
        acnt     the account identifier (e.g., "22334455")
        limit    credit limit (measured in dollars)
        apr      annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit) # calling the super constructor
        self._apr = apr

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit
        Return True if charge was processed
        Return False and assess $5 fee if charge is denied
        """
        success = super().charge(price) # call the inherted method
        if not success:
            self._balance += 5
        return success
    
    def process_month(self):
        """
        Assess monthly interest on outstanding balance.
        """
        if self._balance > 0:
            """If positive balance, convert APR to monthly multiplicative factor."""
            mothly_factor = pow(1 + self._apr, 1/12)
            self._balance *= mothly_factor
# Testing the class
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Jared Otieno', "Co-operative Bank",
                             "2345 1234 4567 5678", 25000))
    wallet.append(CreditCard('Jared Otieno', "Equity Bank",
                             "2312 3423 4534 5645", 50000))
    wallet.append(CreditCard("Jared Otieno", "KCB Bank",
                             '5678 2345 5678', 1000000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val) 

    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank =", wallet[c].get_bank())
        print("Account =", wallet[c].get_account())
        print("Limit =", wallet[c].get_limit())
        print("Balance =", wallet[c].get_balance())

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance =", wallet[c].get_balance())
        print()