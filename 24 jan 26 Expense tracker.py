#expense manager project
file_name = "expenses.txt"
amount = 0
category = ""
date = ""
#load expense
def load_expense():
    global amount,category,date
    try:
        file = open(file_name,"r")
        lines = file.readlines()
        file.close()
        amount = int(lines[0].strip())
        category = lines[1].strip()
        date = lines[2].strip()
    except:
        pass

#add_expense
def add_expenses():
    global amount,category,date
    amount = int(input("Add your Amount: "))
    category = input("Category: ")
    date = input("Date: ")
    try: 
        file = open(file_name,"a")
        file.write(str(amount)+"\n")
        file.write(category+"\n")
        file.write(date+"\n")
        file.close()
        print("Expense added successfully")
    except:
        print("Error adding expense")

        
#view expense
def view_expense():
    global amount,category,date
    print("Amount:",amount)
    print("Category:",category)
    print("Date:",date)
#total expense  
def total_expense():
    global amount,category,date
    print("Total Expense:",amount,"\nCategory:",category,"\nDate:",date)
    return amount,category,date
#exit
def exit_app():
    print("Thank you for using expense manager")
def main():
    load_expense()
    while True:
        print("\n****Welcome to expense manager****")
        print("\n1.Add expense\n2.View expense\n3.Total expense\n4.Exit")
        ch = int(input("Enter your choice: "))
        if(ch == 1):
            add_expenses()
        elif(ch == 2):
            view_expense()
        elif(ch == 3):
            total_expense()
        elif(ch == 4):
            exit_app()
            break
        else:
            print("Invalid choice!!")
    print("         **Thank you**")

main()