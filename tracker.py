import csv
import datetime
import plyer


budget_limit = 1000
notification_threshold = 0.8 * budget_limit

def check_expenses():
    # Read expenses from CSV file
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        expenses = list(reader)[1:] # Skip header row

    amount = 0
    for expense in expenses:
        try:
            amount += float(expense[1])
        except (ValueError, TypeError):
            print(f"Invalid expense: {expense}")
            continue

    print(f"Total expenses: {amount}")

    if amount >= notification_threshold:
        message = f"You have spent {amount} out of {budget_limit}. Consider reducing your spending."
        plyer.notification.notify(title='Budget reminder', message=message, timeout=10)

    if amount >= budget_limit:
        message = f"You have exceeded your budget of {budget_limit}. Please reduce your spending."
        plyer.notification.notify(title='Budget warning', message=message, timeout=10)

def adding_expenses():
    while True:
        name = input('Expense name (press n to exit): ')
        if name.lower() == 'n':
            break

        while True:
            try:
                amount = float(input('Expense amount: '))
                break
            except ValueError:
                print("Invalid amount!")

        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        expense = {'name': name, 'amount': amount, 'date': date}

        with open('expenses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['Name', 'Amount', 'Date'])
            writer.writerow([expense['name'], expense['amount'], expense['date']])

        print("Expense added successfully.")
        check_expenses()

def main():
    print("___Expenses Tracker___")
    while True:
        user_input = input("Add expenses (y or n): ")
        if user_input.lower() == 'y':
            adding_expenses()
          
        elif user_input.lower() == 'n':
            break
        else:
            print("Invalid input")

if __name__ == '__main__':
    main()
