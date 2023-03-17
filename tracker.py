import csv
import datetime
import plyer


# setting budget limit
budget_limit = 1000
Notification_threshold = 0.8 * budget_limit



#setting check expeneses
def check_expenses():
    with open('expenses.csv', 'r') as f:
        reader = csv.reader(f)
        expenses = list(reader)

    total_expenses = 0
    for expense in expenses:

        try:
            total_expenses += float(expense[1])
        except (ValueError, TypeError):
            print(f"Invalid expense: {expense}")
            continue
    
    print(f"Total expenses: {total_expenses}")
    
    if total_expenses >= Notification_threshold:
        message = f"You have reached your {total_expenses} out of {budget_limit}. \nPlease reduce your expenses."
        plyer.notification.notify(title='Budget reminder', message=message, timeout=10)

    if total_expenses >= budget_limit and total_expenses < Notification_threshold:
        message = f"You have reached your {budget_limit} budget limit. \nPlease reduce your expenses."
        plyer.notification.notify(title="Budget reminder", message=message, timeout=10)




#functino of taking input name, amount and adding expenses and storing data on csv...
def add_expenses():
    
    name = input("enter the expenses name- ")
    amount = input("enter the expenses amount- ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("expenses.csv", 'a', newline= '') as file:
        writer= csv.writer(file)
        writer.writerow([name, amount , date])
        
    print("Expense added successfully!")

#this is main function which will asked user to add expenses or not

def main():
 
    while True:
       
        # check_expenses()
        # time.sleep(3600)
        
        try: 
            add = input("Do you want to add expenses.(y/n) :  ")
        except:
            print("invalid!")  
            if add.lower() == 'y':
                add_expenses()
            else: 
                break
            check_expenses()
     
            
    
if __name__ == '__main__':
    main()
    

