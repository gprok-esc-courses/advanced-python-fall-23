import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='bank'
)

cursor = db.cursor()

while True:
    print("BANK")
    account_id = input("Account (0 to exit): ")
    if account_id == '0':
        break
    pin = input("PIN: ")

    cursor.execute("SELECT * FROM accounts WHERE id=" + account_id + " AND pin='" + pin + "'")
    account = cursor.fetchone()

    if account is None:
        print("Invalid Account")
    else:
        while True:
            print("1. Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("O. Exit")
            choice = input("Choose: ")
            if choice == '1':
                print("Balance", account[2])
            elif choice == '2':
                amount = int(input("Amount: "))
                if amount > 0:
                    account = (account[0], account[1], account[2] + amount, account[3])
                    cursor.execute("UPDATE accounts SET balance=" + str(account[2]) + " WHERE id=" + account_id)
            elif choice == '3':
                amount = int(input("Amount: "))
                if amount > 0 and amount <= account[2]:
                    account = (account[0], account[1], account[2] - amount, account[3])
                    cursor.execute("UPDATE accounts SET balance=" + str(account[2]) + " WHERE id=" + account_id)
            elif choice == '0':
                break
            else:
                print("Wrong choice")

db.commit()
db.close()
