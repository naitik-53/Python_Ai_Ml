#  ------ EXPENSE TRACKER PROJECT 💸 ------


# 1. Empty list to store all expenses
expenses = []


# 2. Function To Add New Expense
def add_expense():
    category = input("ENTER THE EXPENSE CATEGORY: ")
    amount = float(input("ENTER AMOUNT: "))


    #ek dictionary me store karenge
    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)   #list me add
    print("Expense Added Successfully!\n")



# 3. Function To View All Expenses
def view_expenses():
    if len(expenses) == 0:
        print("No Expenses added yet!\n")
        return
    

    print("\n------- ALL EXPENSES ---------")
    for e in expenses:
        print(f"Category: {e['category']} | Amount: {e['amount']}")
        print()



#4. Function To Calculate Total
def total_expense():
    total = 0
    for e in expenses:
        total += e["amount"]
    print(f"\nTotal Expenses = {total}\n")




#5. Main Menu Loop
while True:
    print("=== Expense Tracker 💸 ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")

