# ==========================================
#       PERSONAL EXPENSE TRACKER
# ==========================================

expenses = []


# ------------------------------------------
# 1. ADD EXPENSE
# ------------------------------------------

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    # Tuple
    expense = (name, amount, category)

    # Add tuple to list
    expenses.append(expense)

    print("✅ Expense added successfully!")


# ------------------------------------------
# 2. VIEW ALL EXPENSES
# ------------------------------------------

def view_expenses():

    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n========== ALL EXPENSES ==========")

    # enumerate()
    for number, expense in enumerate(expenses, start=1):

        name, amount, category = expense

        print(
            f"{number}. {name} - ₹{amount} - {category}"
        )


# ------------------------------------------
# 3. TOTAL SPENDING
# ------------------------------------------

def total_spending():

    if len(expenses) == 0:
        print("No expenses found.")
        return

    # map()
    amounts = list(
        map(lambda expense: expense[1], expenses)
    )

    total = sum(amounts)

    print(f"\nTotal Spending: ₹{total}")


# ------------------------------------------
# 4. SHOW UNIQUE CATEGORIES
# ------------------------------------------

def show_categories():

    # Set
    categories = set()

    for expense in expenses:
        categories.add(expense[2])

    print("\n========== CATEGORIES ==========")

    for category in categories:
        print("-", category)


# ------------------------------------------
# 5. CATEGORY-WISE SPENDING
# ------------------------------------------

def category_spending():

    category_total = {}

    for expense in expenses:

        category = expense[2]
        amount = expense[1]

        if category not in category_total:
            category_total[category] = 0

        category_total[category] += amount

    print("\n====== CATEGORY SPENDING ======")

    for category, amount in category_total.items():

        print(f"{category}: ₹{amount}")


# ------------------------------------------
# 6. EXPENSES ABOVE ₹200
# ------------------------------------------

def expensive_expenses():

    # filter() + lambda
    expensive = list(
        filter(
            lambda expense: expense[1] > 200,
            expenses
        )
    )

    print("\n====== EXPENSES ABOVE ₹200 ======")

    if len(expensive) == 0:
        print("No expensive expenses found in the above list.")
        return

    for number, expense in enumerate(expensive, start=1):

        name, amount, category = expense

        print(
            f"{number}. {name} - ₹{amount} - {category}"
        )


# ------------------------------------------
# 7. SORT EXPENSES
# ------------------------------------------

def sort_expenses():

    # lambda
    sorted_expenses = sorted(
        expenses,
        key=lambda expense: expense[1],
        reverse=True
    )

    print("\n====== EXPENSES (HIGH → LOW) ======")

    for number, expense in enumerate(
        sorted_expenses,
        start=1
    ):

        name, amount, category = expense

        print(
            f"{number}. {name} - ₹{amount} - {category}"
        )


# ------------------------------------------
# 8. SEARCH BY CATEGORY
# ------------------------------------------

def search_category():

    search = input(
        "Enter category to search: "
    )

    # list comprehension
    result = [
        expense
        for expense in expenses
        if expense[2].lower() == search.lower()
    ]

    print(
        f"\n====== EXPENSES IN {search.upper()} ======"
    )

    if len(result) == 0:
        print("No expenses found.")
        return

    for number, expense in enumerate(
        result,
        start=1
    ):

        name, amount, category = expense

        print(
            f"{number}. {name} - ₹{amount} - {category}"
        )


# ------------------------------------------
# 9. HIGHEST EXPENSE
# ------------------------------------------

def highest_expense():

    if len(expenses) == 0:
        print("No expenses found.")
        return

    highest = max(
        expenses,
        key=lambda expense: expense[1]
    )

    print("\n====== HIGHEST EXPENSE ======")

    print(
        f"Name     : {highest[0]}"
    )

    print(
        f"Amount   : ₹{highest[1]}"
    )

    print(
        f"Category : {highest[2]}"
    )


# ------------------------------------------
# 10. LOWEST EXPENSE
# ------------------------------------------

def lowest_expense():

    if len(expenses) == 0:
        print("No expenses found.")
        return

    lowest = min(
        expenses,
        key=lambda expense: expense[1]
    )

    print("\n====== LOWEST EXPENSE ======")

    print(
        f"Name     : {lowest[0]}"
    )

    print(
        f"Amount   : ₹{lowest[1]}"
    )

    print(
        f"Category : {lowest[2]}"
    )


# ------------------------------------------
# 11. ZIP EXAMPLE
# ------------------------------------------

def category_summary():

    category_total = {}

    for expense in expenses:

        category = expense[2]
        amount = expense[1]

        if category not in category_total:
            category_total[category] = 0

        category_total[category] += amount

    categories = list(category_total.keys())
    totals = list(category_total.values())

    print("\n====== CATEGORY SUMMARY ======")

    # zip()
    for category, total in zip(categories, totals):

        print(
            f"{category} → ₹{total}"
        )


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

while True:

    print("\n")
    print("================================")
    print("     PERSONAL EXPENSE TRACKER")
    print("================================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Show Categories")
    print("5. Category-wise Spending")
    print("6. Expenses Above ₹200")
    print("7. Sort Expenses")
    print("8. Search by Category")
    print("9. Highest Expense")
    print("10. Lowest Expense")
    print("11. Category Summary")
    print("12. Exit")

    choice = input("\nEnter your choice: ")


    if choice == "1":

        add_expense()


    elif choice == "2":

        view_expenses()


    elif choice == "3":

        total_spending()


    elif choice == "4":

        show_categories()


    elif choice == "5":

        category_spending()


    elif choice == "6":

        expensive_expenses()


    elif choice == "7":

        sort_expenses()


    elif choice == "8":

        search_category()


    elif choice == "9":

        highest_expense()


    elif choice == "10":

        lowest_expense()


    elif choice == "11":

        category_summary()


    elif choice == "12":

        print("Thank you for using Expense Tracker! 👋")
        break


    else:

        print("❌ Invalid choice. Please try again.")