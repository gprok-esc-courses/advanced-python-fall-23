import random

def login():
    user = input("Username: ")
    password = input("Password: ")
    err = None
    # Look into the db
    roles = ['Clerk', 'Delivery', 'Manager']
    r = random.randint(0, 2)
    role = roles[r]
    return user, role, err

def clerk_menu():
    print("<<< CLERK >>>")
    print("1. Add order")
    print("2. Add order(new customer")
    print("3. Assign order to delivery")
    print("4. View pending orders")
    print("0. Exit")
    return int(input("Choose: "))

def delivery_menu():
    print("<<< DELIVERY >>>")
    print("1. Complete order")
    print("2. My orders")
    print("0. Exit")
    return int(input("Choose: "))

def manager_menu():
    print("<<< MANAGER >>>")
    print("1. Customer profile")
    print("2. Orders on day")
    print("3. Orders set by clerk")
    print("4. Pending orders")
    print("5. export Customers")
    print("6. export Employees")
    print("7. export Orders")
    print("0. Exit")
    return int(input("Choose: "))


while True:
    user, role, err = login()
    if err is None:
        if role == 'Clerk':
            choice = clerk_menu()
        elif role == "Delivery":
            choice = delivery_menu()
        elif role == "Manager":
            choice = manager_menu()
    else:
        print(err)
