#Create a Library Management System where different library items calculate borrowing charges differently.
#Library item (parent class)
#Book and magazie (child class)
#LibraryApp(main class)

#Book IS-A libraryitem
#Magazine IS-A libraryitem
#LibraryApp HAS-A libraryitem

#Output format
#Item Type: Book
#Borrow Days: 5
#Borrowing Charge: 50
#Or 
#Item Type: Magazine
#Borrow Days: 3
#Borrowing Charge: 30'''

class Libraryitem:
    def __init__(self,typee,borrow_days):
        self.item_type = typee    
        self.borrow_days = borrow_days
    def b_charge(self):                             #abstract
        pass

class Book(Libraryitem):
    def __init__(self,typee,borrow_days):
        super().__init__(typee,borrow_days)
    def b_charge(self):
        return self.borrow_days*10

class Magazine(Libraryitem):                        #Inheritance
    def __init__(self,typee,borrow_days):
        super().__init__(typee,borrow_days)
    def b_charge(self):
        return self.borrow_days*10              #polymorphism

class LibraryApp:
    def __init__(self):
        self.item = None
    def create_item(self,typee):
        if typee.lower() == "book":
            self.item = Book("Book",3)
        elif typee.lower() == "magazine":
            self.item = Magazine("Magazine",9)
        return "Book type retrieved!"

    def get_charge(self):
        
        return self.item.b_charge()

    
app = LibraryApp()
print(app.create_item("Book"))
print("Book Borrow Charge:",app.get_charge())
print(app.create_item("Magazine"))
print("Magazine borrow charge:",app.get_charge())

        

        
        
        
        
        
