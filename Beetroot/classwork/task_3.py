class Client:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Date of birth: {self.dob}")


class Account:
    def __init__(self, client):
        self.client = client
        self._balance = 0

    def _change_balance(self, amount):
        self._balance += amount

    def display_balance(self):
        print(f"Account balance: {self._balance}")


class GoldAccount(Account):
    def __init__(self, client):
        super().__init__(client)
        self.__balance = 0

    def __change_balance(self, amount):
        self.__balance += amount

    def display_balance(self):
        print(f"Gold account balance: {self.__balance}")

        # New methods for accessing protected and private methods and attributes

    def change_balance(self, amount):
        self._change_balance(amount)
        self.__change_balance(amount)

    def get_private_balance(self):
        return self.__balance

    def get_protected_balance(self):
        return self._balance


client1 = Client("John Smith", "01/01/1980")
client1.display_info()

account1 = Account(client1)
account1.display_balance()

gold_account1 = GoldAccount(client1)
gold_account1.display_balance()

gold_account1.change_balance(1000)

print(gold_account1.get_private_balance())
print(gold_account1.get_protected_balance())

client_2 = Client("Stanislav Zelinskyi", "09/08/1983")
client_2.display_info()
gold_account_2 = GoldAccount(client_2)
gold_account_2.change_balance(10000)
gold_account_2.display_balance()
print(gold_account_2.get_protected_balance())
print(gold_account_2.__dict__)