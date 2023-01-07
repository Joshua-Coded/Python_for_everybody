class CreditCard:
    """ A consumer credit card. """

    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.
        
        The initial balance is zero.
        
        customer the name of the customer is ("alana joshua.")
        bank the name of the bank (zenith bank)
        acnt the account identifier ("22787283726372")
        limit credit limit (measure in naira)
        
        """

        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """return the name of the customer"""
        return self._customer

    def get_bank(self):
        """ return the bank's name """
        return self._bank

    def get_account(self):
        """ return the card identifying number """
        return self._account

    def get_limit(self):
        """ return the current credit limit """
        return self._limit

    def get_balance(self):
        """ return current balance """
        return self._balance

    def charge(self, price):
        """ charge given price to the card.
        
        return TRUE IS CHARGE WAS PROCEESED; FALSE IF CHARGE WAS DENIED
        """

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """ process customer payment that reduce balance """

        self._balance -= amount
        

""" testing the cards number """

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard("joshua alana", "rwanda", "5442647462746232", 6734))
    wallet.append(CreditCard("joshua alana", "rwanda", "5442647462746232", 42323))
    wallet.append(CreditCard("joshua alana", "rwanda", "5442647462746232", 637642))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge( 3*val)

    for c in range(3):
        print("Customer = ", wallet[c].get_customer())
        print("Bank = ", wallet[c].get_bank())
        print("Account =", wallet[c].get_account())
        print("Limit = ", wallet[c].get_limit())
        print("Balance =", wallet[c].get_balance())

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance =", wallet[c].get_balance())
            print()
          
