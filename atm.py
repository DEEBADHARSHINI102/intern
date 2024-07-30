import time

print("Insert your card")
time.sleep(1)
password = 5436
pin = int(input("Enter your pin: "))
balance = 5000

if pin == password:
    while True:
        print("1 == Balance amount")
        print("2 == Withdraw amount")
        print("3 == Deposit balance")
        print("4 == Exit")
        try:
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter a valid option.")
            continue
        
        if option == 1:
            print("Your current balance is", balance)
            print("************")
            print("************")
        elif option == 2:
            withdraw_amount = int(input("Enter your withdraw amount: "))
            print("************")
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(withdraw_amount, "is debited from your account")
                print("************")
                print("Your current balance is", balance)
                print("************")
            else:
                print("Insufficient balance")
                print("************")
        elif option == 3:
            deposit_amount = int(input("Please enter your deposit amount: "))
            balance += deposit_amount
            print(deposit_amount, "is credited to your account")
            print("************")
            print("Your current balance is", balance)
            print("************")
        elif option == 4:
            break
        else:
            print("Try again")
else:
    print("Incorrect pin")