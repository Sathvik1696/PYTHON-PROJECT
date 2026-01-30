#ATM SIMULATOR
file_name="atm_data.txt"
balance = 1000                  #balance is a global variable that stores money
pin ="1234"                     #pin is a global variable that stores pin
#load data
def load_data():                
    global balance,pin          #global keyword allows us to modify outside variables
    try:
        file=open(file_name,"r")      #open a file in read mod
        lines=file.readlines()          #read all lines from the file into a list
        file.close()                    #close the file after reading
        pin=lines[0].strip()            #first line contains pin,strip removes \n
        balance=int(lines[1].strip())   #second line contains balance
    except:
                                        #if file does not exist or error occurs
        pass                            #pass do nothing
                                        #program will use default balance and pin

#check balance
def check_balance():                    
    print("Your balance is:",balance)

def save_data():                        # save data
    file=open(file_name,"w")            #opening file in write mode
    file.write(pin+"\n")                #write a pin into the file and go to 
    file.write(str(balance))            #write balance into string
    file.close()                        #close the file

#deposit money
def deposit_money():                                
    global balance                                  #global allows changing original balance
    try:
        amount=int(input("Enter amount to deposit:"))
        balance=balance+amount
        save_data()                                 #save updated balance to the file
        print("money deposited successfully")
    except:
        print("please enter numbers only")

#withdraw money
def withdraw_money():                    
    global balance
    try:
        amount=int(input("Enter the amount you want to withdraw:"))
        if amount>balance:
            print("Insufficient Balance")
        else:
            balance = balance-amount
            save_data()
            print("please collect your cash")
    except:
        print("please enter number only")

#change pin
def change_pin():                               
    global pin
    old_pin=input("Enter the old pin:")         #ask your old pin
    if old_pin==pin:                            #check if old pin matches
        new_pin=input("Enter the new pin:")     #ask for new pin
        pin=new_pin
        save_data()
        print("pin changed successfully")
    else:
        print("Incorrect pin")

#MAIN PROGRAM
def main():
    load_data()                                 #load data when program starts
    user_pin=input("Enter the  pin:")           #ask user to enter a pin
    if user_pin!=pin:                           #if pin is wrong stop the program
        print("Incorrect Pin")
        return
    while True:
        print("\n--------ATM MENU----------")
        print("1. Chech Balance")
        print("2. Depost Money")
        print("3. Withdraw Money")
        print("4. Change Pin")
        print("5. Exit")

        choice=input("Enter your choice:")
        if choice=="1":
            check_balance()
        elif choice=="2":
            deposit_money()
        elif choice=="3":
            withdraw_money()
        elif choice=="4":
            change_pin()
        elif choice=="5":
            print("Thankyou for using ATM")
            break
        else:
            print("Invalid Choice")
main()