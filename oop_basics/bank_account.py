class BankAccount:

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Счет пополнен на {amount}. Текущий баланс: {self.balance}.")
        else:
            print("Сумма пополнения должна быть положительной.")
            
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Со счета снято {amount}. Текущий баланс: {self.balance}.")
            else:
                print(f"Недостаточно средств. Доступно: {self.balance}.")
        else:
            print("Сумма снятия должна быть положительной.")

    def get_balance(self):
        return self.balance
    

account1 = BankAccount("Иван Петрович")
account2 = BankAccount("Мария Смирнова")

print(f"Начальный баланс {account1.account_holder}: {account1.get_balance()}") # Выводим начальный баланс account1

print("\n--- Операции для account1 ---")
account1.deposit(1000.0)
account1.withdraw(200.0)
account1.withdraw(900.0) # Недостаточно средств
account1.deposit(-500.0) # Сумма пополнения должна быть положительной
account1.withdraw(-100.0) # Сумма снятия должна быть положительной

print(f"\nТекущий баланс {account1.account_holder}: {account1.get_balance()}")

print("\n--- Операции для account2 ---")
account2.deposit(500.0)
account2.withdraw(150.0)

print(f"\nТекущий баланс {account2.account_holder}: {account2.get_balance()}")
