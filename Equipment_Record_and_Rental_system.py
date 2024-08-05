import pandas as pd

# Dictionaries to store stock and records
stock = {}
Records = {}

# ----------------------------------- Equipment class ------------------------------------------------------------------------------
class Equipment:
    def __init__(self):
        self.Eid = 0
        self.Ename = ''
        self.brand = ''
        self.Total_qty = 0
        self.Aval_qty = 0

    def Add_item(self):
        self.Eid = int(input('Enter the Equipment id: '))
        self.Ename = input('Enter the Equipment Name: ')
        self.brand = input('Enter the brand of Equipment: ')
        self.Total_qty = int(input('Enter the total qty: '))
        self.Aval_qty = int(input("Enter the Equipment Available Quantity: "))
        stock[self.Eid] = [self.Ename, self.brand, self.Total_qty, self.Aval_qty]

    def Remove_item(self):
        self.Eid = int(input("Enter the Equipment Id to Remove: "))
        if self.Eid in stock:
            stock.pop(self.Eid)
            print(f"Equipment with id {self.Eid} has been removed.")
        else:
            print("Equipment not found.")

    def update_item(self):
        self.Eid = int(input('Enter the Equipment Id to update: '))
        if self.Eid in stock:
            self.Total_qty = int(input('Enter the Equipment Quantity to update: '))
            stock[self.Eid][2] += self.Total_qty
            stock[self.Eid][3] += self.Total_qty
        else:
            print("Equipment not found.")

    def print_stock(self):
        if stock:
            df = pd.DataFrame.from_dict(stock, orient='index', columns=['Name', 'Brand', 'Total Qty', 'Available Qty'])
            print(df)
        else:
            print("No stock available.")

# ----------------------------------------------- Record Class ------------------------------------------------------------
class Record:
    def __init__(self):
        self.name = ""
        self.ID = 0
        self.Eid = 0
        self.Ename = ""
        self.status = ""
        self.condition = ""

    def rent_Equip(self):
        self.name = input("Enter your Name: ")
        self.ID = int(input("Enter Your ID: "))
        self.Eid = int(input("Enter Equipment ID of item you are renting: "))
        if self.Eid in stock and stock[self.Eid][3] > 0:
            self.Ename = stock[self.Eid][0]
            self.status = 'Rented'
            self.condition = "Good"
            stock[self.Eid][3] -= 1
            Records[self.ID] = [self.name, self.Eid, self.Ename, self.status, self.condition]
        else:
            print("Item not available or invalid equipment ID.")

    def return_Equip(self):
        self.ID = int(input("Enter Your ID: "))
        if self.ID in Records:
            print("Member Id= ", self.ID)
            print("Member Name = ", Records[self.ID][0])
            print("Equipment Id = ", Records[self.ID][1])
            print("Equipment Name = ", Records[self.ID][2])
            print("Status = ", Records[self.ID][3])
            self.condition = input("Enter the returned condition (Good/Damaged): ")
            Records[self.ID][3] = "Returned"
            Records[self.ID][4] = self.condition
            stock[Records[self.ID][1]][3] += 1
        else:
            print("Record not found for the given ID.")

    def print_Records(self):
        if Records:
            df = pd.DataFrame.from_dict(Records, orient='index', columns=['Name', 'Eid', 'Ename', 'Status', 'Condition'])
            print(df)
        else:
            print("No records available.")

# -------------------------- Stock Management Function ------------------------------------------
def stock_management():
    temp = Equipment()
    while True:
        print("--------------MENU---------------")
        print("1. Add item ")
        print("2. Remove item ")
        print("3. Update item ")
        print("4. Print stock ")
        print("5. Exit")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            temp.Add_item()
        elif choice == 2:
            temp.Remove_item()
        elif choice == 3:
            temp.update_item()
        elif choice == 4:
            temp.print_stock()
        elif choice == 5:
            print("Exiting Stock Management. Thank you.")
            break
        else:
            print("Invalid input")

# ---------------------------------------- Main Function of Program ----------------------------------------------------------------
def main():
    rec = Record()
    while True:
        print("--------------MENU---------------")
        print("1. Stock Management ")
        print("2. Rent item ")
        print("3. Return item ")
        print("4. Print Records ")
        print("5. Exit")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            stock_management()
        elif choice == 2:
            rec.rent_Equip()
        elif choice == 3:
            rec.return_Equip()
        elif choice == 4:
            rec.print_Records()
        elif choice == 5:
            print("All data saved. Exiting... Thank you.")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
