class Account:

    def __init__(self, owner, amount=0):

        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    # String representation of objects
    def __repr__(self):
        print "Class Name : ", self.__class__.__name__
        # Official string representation of an object.
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        # Informal printable string representation of an object.
        return 'Account of {} with starting amount: {}'.format(self.owner, 
                                                              self.amount)

    def __reversed__(self):
        return self[::-1]

    def __call__(self):
        print 'Start amount: {}'.format(self.amount)
        print 'Transactions: ',
        for transaction in self:
            print transaction,
        print '\nBalance : {}'.format(self.balance)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('Please use int for amount!')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    """
    A context manager is a simple "protocol" (or interface) that your object 
    needs to follow so it can be used with the with statement. Basically all
    you need to do is add __enter__ and __exit__ methods to an object if you 
    want it to function as a context manager.
    """
    def __enter__(self):
        print "ENTER WITH: Making backup of transactions for rollback"
        self._copy_transactions = list(self._transactions)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #print "EXIT WITH: ", end=" "
        if exc_type:
            self._transactions = self._copy_transactions
            print "Rolling back to previous transactions"
            print "Transacton resulted in {} ({})".format(
                exc_type.__name__, exc_val)
        else:
            print "Transaction OK"


def validate_transaction(acc, amount_to_add):
    with acc as a:
        print 'Adding {} to account'.format(amount_to_add)
        a.add_transaction(amount_to_add)
        print 'New balance would be: {}'.format(a.balance)
        if a.balance < 0:
            raise ValueError('Sorry! can not go in debt!')
        

if __name__ == '__main__':

    acc = Account('salim', 20)
    
    print str(acc)
    print repr(acc)

    acc.add_transaction(20)
    acc.add_transaction(-10)
    acc.add_transaction(50)
    acc.add_transaction(-20)
    print "Account balance is : ", acc.balance

    print "Transaction length : ", len(acc)
    print "Transation list is : ",
    for t in acc:
        print t, 

    acc.add_transaction(100)
    acc.add_transaction(-40)
    print "\nCall callable method : ", acc()

    acc4 = Account('kabeer', 100)
    print '\nBalance start: {}'.format(acc4.balance)
    try:
        validate_transaction(acc4, 20)
    except ValueError as exc:
        print exc
    print '\nBalance ends: {}'.format(acc4.balance)
