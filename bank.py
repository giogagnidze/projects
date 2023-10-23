balance = 0

print("Menu")
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")

choice = input("Enter choice: ")

if choice == "1":
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    
    print("Deposited" + " " + str(amount))
    print("Current balance: " + " " + str(balance))

elif choice == "2":
    amount = float(input("Enter amount to withdraw: "))
    if balance >= amount:
        balance -= amount
        print("Withdrew" + " " + str(amount))
        print("Current balance: " + " " + str(balance))
    else:
        print("Insufficient balance.")

elif choice == "3":
    print("Current balance: " + " " + str(balance))

elif choice == "4":
    print("Bye Bye")


