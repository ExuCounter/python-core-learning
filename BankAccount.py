min_transaction_amount = 0


class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= min_transaction_amount:
            raise TypeError(f"Deposit amount should be greater than {min_transaction_amount}")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= min_transaction_amount:
            raise TypeError(f"Deposit amount should be greater than {min_transaction_amount}")

        self._balance -= amount

        return self.balance

    def __repr__(self):
        return f"A {self.__class__.__name__} with {self.balance}$ in it"


class Savings(BankAccount):
    def __init__(self, interest_rate=0.0035):
        super().__init__()
        self.interest_rate = interest_rate

    def pay_interest(self, amount):
        self._balance += amount * (1 + self.interest_rate)


class HighInterest(Savings):
    def __init__(self, interest_rate=0.007, fee=5):
        super().__init__(interest_rate)
        self.fee = fee

    def withdraw(self, amount):
        self._balance -= amount + self.fee

        return self.balance


class LockedIn(HighInterest):
    def __init__(self, interest_rate=0.009):
        super().__init__(interest_rate)

    def withdraw(self, amount):
        raise TypeError("You can't withdraw")


bankAcc = BankAccount(100)
print(bankAcc)
savingsAcc = Savings()
print(savingsAcc)
savingsAcc.pay_interest(200)
print(savingsAcc)
savingsAcc.pay_interest(400)
savingsAcc.pay_interest(200)
print(savingsAcc)
highInterestAcc = HighInterest()
print(highInterestAcc.withdraw(200))
print(highInterestAcc.withdraw(200))
lockedIn = LockedIn()
lockedIn.deposit(500)
print(lockedIn.withdraw(300))
