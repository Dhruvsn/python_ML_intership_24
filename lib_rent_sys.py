import pandas as pd

# Dictionaries to store inventory and records
Inventory = {}
RecordData = {}

# User data for authorization
userData = {}

# Class to manage book details and operations
class Book:
    def __init__(self):
        self.book_id = 0
        self.title = ""
        self.total_qty = 0 
        self.available_qty = 0

    # Method to add a new book to the inventory
    def add_book(self):
        try:
            self.book_id = int(input("Enter the book id: "))
            self.title = input("Enter the book name: ")
            self.total_qty = int(input("Enter the total quantity: "))
            self.available_qty = self.total_qty  # Available quantity should be equal to total initially
            Inventory[self.book_id] = [self.title, self.total_qty, self.available_qty]
            print("Book added successfully!\n")
        except ValueError:
            print("Invalid input! Please enter numeric values for book id and quantity.")
       
    # Method to remove a book from the inventory
    def remove_book(self):
        try:
            self.book_id = int(input("Enter the book id you want to remove: "))
            if self.book_id in Inventory:
                Inventory.pop(self.book_id)
                print(f"Book with id {self.book_id} has been removed.")
            else:
                print("Book not found.")
        except ValueError:
            print("Invalid input! Please enter a numeric value for book id.")
        
    # Method to update the quantity of a book in the inventory
    def update_book(self):
        try:
            self.book_id = int(input("Enter the book id you want to update: "))
            if self.book_id in Inventory:
                print("Enter a negative number if you want to decrease the quantity.")
                qty_update = int(input("Enter the quantity you want to add: "))
                if Inventory[self.book_id][2] + qty_update >= 0:
                    Inventory[self.book_id][1] += qty_update
                    Inventory[self.book_id][2] += qty_update
                    print("Quantity updated.")
                else:
                    print("Insufficient stock to decrease the quantity.")
            else:
                print("Book not found!")
        except ValueError:
            print("Invalid input! Please enter numeric values for book id and quantity.")
       
    # Method to print the current inventory
    def print_books(self):
        if Inventory:
            df = pd.DataFrame.from_dict(Inventory, orient='index', columns=['Title', 'Total Qty', 'Available Qty'])
            print(df.to_string(index=False))
        else:
            print("No stock available.")

# Class to manage records of rented and returned books
class Record:
    def __init__(self):
        self.Name = ""
        self.Rollno = ""
        self.book_id = 0
        self.Book_name = ""
        self.status = ""
        self.condition = ""

    # Method to rent a book
    def rent_book(self):
        try:
            self.Name = input("Enter your name: ")
            self.Rollno = input("Enter your Roll number: ")
            self.book_id = int(input("Enter the book id you want to rent: "))
            if self.book_id in Inventory and Inventory[self.book_id][2] > 0:
                self.Book_name = Inventory[self.book_id][0]
                self.status = "Rented"
                self.condition = "Good"
                RecordData[self.Rollno] = [self.Name, self.book_id, self.Book_name, self.status, self.condition]
                Inventory[self.book_id][2] -= 1
                print("Book rented successfully!")
            else:
                print("Item not available or invalid book ID.")
        except ValueError:
            print("Invalid input! Please enter numeric values for book id.")

    # Method to return a rented book
    def return_book(self):
        try:
            self.Rollno = input("Enter your Roll number: ")
            self.condition = input("Enter the returned condition (Good/Damaged): ")

            if self.Rollno in RecordData:
                if self.condition == 'Good':
                    RecordData[self.Rollno][3] = "Returned"
                    print("Student Name:", RecordData[self.Rollno][0])
                    print("Student Roll number:", self.Rollno)
                    print("Book Id:", RecordData[self.Rollno][1])
                    print("Book Name:", RecordData[self.Rollno][2])
                    print("Status:", RecordData[self.Rollno][3])
                    RecordData[self.Rollno][4] = self.condition
                    Inventory[RecordData[self.Rollno][1]][2] += 1
                else:
                    print("Book condition is not good, so you have to pay a fine.")
            else:
                print("Record not found for the given Roll number.")
        except ValueError:
            print("Invalid input!")

    # Method to print the record of rented and returned books
    def print_records(self):
        if RecordData:
            df = pd.DataFrame.from_dict(RecordData, orient='index', columns=["StudentName", "Book id", "BookName", "STATUS", "CONDITION"])
            print(df.to_string(index=True))
        else:
            print("No records available.")

# Function to manage the book inventory system
def management_system():
    temp = Book()
    while True:
        print("--------------MENU---------------")
        print("1. Add book")
        print("2. Remove book")
        print("3. Update book")
        print("4. Print Inventory")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            temp.add_book()
        elif choice == 2:
            temp.remove_book()
        elif choice == 3:
            temp.update_book()
        elif choice == 4:
            temp.print_books()
        elif choice == 5:
            break
        else:
            print("Invalid input!")

# Main function to manage user interaction
def main():
    temp = Book() 
    rec = Record()
    while True:
        print("--------------Welcome to Library Inventory Management System---------------")
        print("1. Management system")
        print("2. Rent Book")
        print("3. Return Book")
        print("4. Print Record")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            management_system()
        elif choice == 2:
            rec.rent_book()
        elif choice == 3:
            rec.return_book()
        elif choice == 4:
            rec.print_records()
        elif choice == 5:
            break
        else:
            print("Invalid input!")

# Class to handle user authorization
class AuthorizeUser:
    def __init__(self):
        self.userId = ""
        self.userPassword = ""
        
    # Method to verify user credentials
    def user_verification(self):
        while True:
            try:
                self.userId = input("Enter your id: ")
                self.userPassword = input("Enter password: ")
                if self.userId in userData and userData[self.userId] == self.userPassword:
                    print("Login successfully!")
                    main()
                else:
                    print("Incorrect password or ID!")
            except Exception as e:
                print(f"An error occurred: {e}")

    # Method to add a new user
    def add_user(self):
        username = input("Enter your Id: ")
        if username in userData:
            print('User already exists!')
        else:
            password = input("Enter your password: ")
            userData[username] = password
            print(f"{username} added!")

# Main entry point
if __name__ == "__main__":
    obj = AuthorizeUser()
    while True:
        print("1. Add user")
        print('2. Login')
        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj.add_user()
        elif choice == 2:
            obj.user_verification()
        else:
            print("Invalid input!")
