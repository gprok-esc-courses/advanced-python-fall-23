import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='bank'
)

cursor = db.cursor()


class Account:
    def __init__(self, aid, name, balance, pin):
        self.id = aid
        self.name = name
        self.balance = balance
        self.pin = pin

    def deposit(self, amount, cursor):
        if amount > 0:
            self.balance += amount
            cursor.execute("UPDATE accounts SET balance=" + str(self.balance) + " WHERE id=" + str(self.id))

    def withdraw(self, amount, cursor):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            cursor.execute("UPDATE accounts SET balance=" + str(self.balance) + " WHERE id=" + str(self.id))


class Bank:
    def get_account(self, aid, pin, cursor):
        cursor.execute("SELECT * FROM accounts WHERE id=" + aid + " AND pin='" + pin + "'")
        account = cursor.fetchone()

        if account is None:
            return None
        else:
            return Account(account[0], account[1], account[2], account[3])

    def get_choice(self):
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("O. Exit")
        choice = input("Choose: ")
        return choice

    def login(self):
        account_id = input("Account (0 to exit): ")
        pin = input("PIN: ")
        return account_id, pin


bank = Bank()

while True:
    print("BANK")
    account_id, pin = bank.login()
    if account_id == '0':
        break

    account = bank.get_account(account_id, pin, cursor)

    if account is None:
        print("Invalid Account")
    else:
        while True:
            choice = bank.get_choice()
            if choice == '1':
                print(account.balance)
            elif choice == '2':
                amount = int(input("Amount: "))
                account.deposit(amount, cursor)
            elif choice == '3':
                amount = int(input("Amount: "))
                account.withdraw(amount, cursor)
            elif choice == '0':
                break
            else:
                print("Wrong choice")

db.commit()
db.close()
