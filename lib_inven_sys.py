import pandas as pd

Inventory = {}
record = {}

class Book:
    def __init__(self):
        self.book_id = 0
        self.title = ""
        self.total_qty = 0
        self.available_qty = 0
  
    def add_book(self):
        self.book_id = int(input("Enter the book id: "))
        self.title = input("Enter the Book name: ")
        self.total_qty = int(input("Enter the total quantity: "))
        self.available_qty = self.total_qty
        Inventory[self.book_id] = [self.title, self.total_qty, self.available_qty]
        print("Book added successfully!\n")
  
    def remove_book(self):
        self.book_id = int(input("Enter the book id you want to remove: "))
        if self.book_id in Inventory:
            Inventory.pop(self.book_id)
            print(f"Book with id {self.book_id} is removed.")
        else:
            print("Book not found")

    def update_book(self):
        self.book_id = int(input("Enter the book id you want to update: "))
        if self.book_id in Inventory:
            print("Enter a negative number if you want to decrease the quantity")
            qty_change = int(input("Enter the quantity change: "))
            Inventory[self.book_id][1] += qty_change
            Inventory[self.book_id][2] += qty_change
            print("Quantity updated")
        else:
            print("Book not found!")

    def print_books(self):
        if Inventory:
            df = pd.DataFrame.from_dict(Inventory, orient='index', columns=['Title', 'Total Quantity', 'Available Quantity'])
            print(df.to_string(index=True))
        else:
            print("No stock available.")


class Record:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.book_id = 0
        self.book_name = ""
        self.status = ""
        self.condition = ""

    def rent_book(self):
        self.name = input("Enter your name: ")
        self.roll_no = input("Enter your Roll number: ")
        self.book_id = int(input("Enter the book id you want to rent: "))
        if self.book_id in Inventory and Inventory[self.book_id][2] > 0:
            self.book_name = Inventory[self.book_id][0]
            self.status = "Rent"
            self.condition = "Good"
            record[self.roll_no] = [self.name, self.book_id, self.book_name, self.status, self.condition]
            Inventory[self.book_id][2] -= 1
            print("Book rented successfully!")
        else:
            print("Item not available or invalid Book ID.")

    def return_book(self):
        self.roll_no = input("Enter your Roll number: ")
        self.condition = input("Enter the returned condition (Good/Damaged): ")
        
        if self.roll_no in record:
            self.book_id = record[self.roll_no][1]
            if self.condition == 'Good':
                record[self.roll_no][3] = "Returned"
                record[self.roll_no][4] = self.condition
                Inventory[self.book_id][2] += 1
                print(f"Student Name: {record[self.roll_no][0]}")
                print(f"Student Roll number: {self.roll_no}")
                print(f"Book ID: {self.book_id}")
                print(f"Book Name: {record[self.roll_no][2]}")
                print(f"Status: {record[self.roll_no][3]}")
                print(f"Condition: {record[self.roll_no][4]}")
                print("Book returned successfully!")
            else:
                print("Book condition is not good, you have to pay a fine.")
        else:
            print("Record not found for the given Roll number.")

    def print_records(self):
        if record:
            df = pd.DataFrame.from_dict(record, orient='index', columns=['Name', 'Book ID', 'Book Name', 'Status', 'Condition'])
            print(df.to_string(index=True))
        else:
            print("No records available.")


def management_system():
    book_obj = Book()
    while True:
        print("--------------BOOK MANAGEMENT MENU---------------")
        print("1. Add book ")
        print("2. Remove book ")
        print("3. Update book ")
        print("4. Print Inventory ")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_obj.add_book()
        elif choice == 2:
            book_obj.remove_book()
        elif choice == 3:
            book_obj.update_book()
        elif choice == 4:
            book_obj.print_books()
        elif choice == 5:
            break
        else:
            print("Invalid input!")


def main():
    book_obj = Book()
    record_obj = Record()
    while True:
        print("--------------LIBRARY MENU---------------")
        print("1. Book Management System")
        print("2. Rent Book")
        print("3. Return Book")
        print("4. Print Records")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            management_system()
        elif choice == 2:
            record_obj.rent_book()
        elif choice == 3:
            record_obj.return_book()
        elif choice == 4:
            record_obj.print_records()
        elif choice == 5:
            break
        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()
