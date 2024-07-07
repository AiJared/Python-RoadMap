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