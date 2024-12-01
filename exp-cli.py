from tabulate import tabulate
import datetime
import argparse
import json
import os

class ExpenseTracker:
    '''
        project link: https://roadmap.sh/projects/expense-tracker
    '''

    def __init__(self) -> None:
        self.__path = os.path.abspath(os.path.join(os.path.dirname(__file__), "expense.json"))
        if not os.path.exists(self.__path):
            self.__expenses = {"Balance" : 0.0, "Entry" : []}    # Enter your balance
            with open(self.__path, 'w', encoding = 'UTF-8') as f:
                json.dump(self.__expenses, f, ensure_ascii = False)

        else:
            with open(self.__path, 'r', encoding = 'UTF-8') as f:
                self.__expenses = json.load(f)

        self.__balance = self.__expenses['Balance']

    def list_exp(self) -> None:
        '''
            List the expenses

            Args: None

            Returns: None
        '''     
        head = ["ID", "Date", "Description", "Amount", "Balance"]
        table = []

        for i in self.__expenses['Entry']:
            table.append([
                i.get("ID"),
                i.get("Date"),
                i.get("Description"),
                i.get("Amount"),
                f"₹{self.__balance}"
            ])

        print(tabulate(table, head, tablefmt = "grid"))


    def add(self, description : str, amount : float) -> bool:
        '''
            Add the expense to the table

            Args:
                description(str) : description of the expense
                amount(float) : amount of the expense

            Return:
                bool: Expense added or not
        '''
        try:
            self.__expenses['Entry'].append({
                'ID' : len(self.__expenses['Entry']) + 1,
                'Date' : datetime.datetime.now().strftime("%d-%m-%y"),
                "Description" : description,
                "Amount" : f"₹{amount}",
            })

            self.__expenses["Balance"] = self.__balance = self.__balance - amount

            with open(self.__path, 'w', encoding = 'UTF-8') as f:
                json.dump(self.__expenses, f, indent = 4, ensure_ascii = False)

            return True
        
        except:
            return False
        
    def update(self, id : int, description : str | None = None, amount : float | None = None) -> bool:
        '''
            Updates the expenses

            Args:
                id(int) : id of the expense
                description(str) : Updated description (optional)
                amount(float) : updated amount (optional)

            Returns:
                bool: Expense updated or not
        '''
        if id > len(self.__expenses['Entry']):
            return False
        try:
            if description:
                self.__expenses['Entry'][id - 1]['Description'] = description
            if amount:
                self.__expenses['Entry'][id - 1]['Amount'] = f"₹{amount}"
                self.__expenses["Balance"] = self.__balance = self.__balance - amount

            with open(self.__path, 'w', encoding = 'UTF-8') as f:
                json.dump(self.__expenses, f, indent = 4, ensure_ascii = False)

            return True
        except:
            return False
        

    def delete(self, id : int) -> bool:
        '''
            Delete an expense based on ID

            Args:
                id(int): id of the expense

            Returns:
                bool: Expense deleted or not
        '''
        if id > len(self.__expenses['Entry']):
            return False
        
        try:
            self.__expenses["Balance"] = self.__balance = self.__balance + float(self.__expenses['Entry'][id - 1]["Amount"][1:])
            self.__expenses['Entry'].pop(id - 1)

            for index, exp in enumerate(self.__expenses['Entry']):
                exp['ID'] = index + 1

            with open(self.__path, 'w', encoding = 'UTF-8') as f:
                json.dump(self.__expenses, f, indent = 4, ensure_ascii = False)

            return True
        except:
            return False
        

    def summary(self, month : int | None = None, year : int | None = None) -> float:
        '''
            Calculates the sum of the expenses

            Args:
                month(int) : month of the expense
                year(int) : year of the expense

            Returns: 
                sum(float) : total expenditure
        '''
        sum = 0
        for i in self.__expenses['Entry']:
            if month and month != int(i.get("Date").split("-")[1]):
                continue

            if year and year != int(i.get("Date").split("-")[2]):
                continue

            sum += float(i.get("Amount").replace("₹", ""))

        print(f"Total expenses: ₹{sum}")
        return sum


def args() -> argparse.Namespace:
    '''
        Parse command-line arguments for the Expense Tracker application.

        This function sets up and parses the command-line arguments needed for
        various operations in the Expense Tracker application. The supported
        commands are 'add', 'list', 'summary', 'update', and 'delete'. 

        Returns:
            argparse.Namespace: An object containing the parsed command-line arguments.
        
        Command-Line Arguments:
            command (str): The command to execute. Must be one of 'add', 'list', 'summary', 'update', or 'delete'.
            --desc (str, optional): Description of the expense. Required for 'add' and 'update' commands.
            --amt (float, optional): Amount of the expense. Required for 'add' and 'update' commands.
            --id (int, optional): ID of the expense. Required for 'update' and 'delete' commands.
            -m (int, optional): Month for filtering expenses in the 'summary' command.
            -y (int, optional): Year for filtering expenses in the 'summary' command.
    '''
    parser = argparse.ArgumentParser(description = "Expense Tracker")
    parser.add_argument('command', choices = ['add', 'list', 'summary', 'update', 'delete'], help = "Commands for the expense tracker")
    parser.add_argument('--desc', type = str, help = "Expense Description")
    parser.add_argument('--amt', type = float, help = "Expense amount")
    parser.add_argument('--id', type = int, help = "Expense id")
    parser.add_argument('-m', type = int, help = "Month input")
    parser.add_argument('-y', type = int, help = "Year input")

    return parser.parse_args()



if __name__ == "__main__":
    t = ExpenseTracker()
    args = args()
    cmd = args.command

    if cmd == 'add':
        if not args.desc or not args.amt:
            print("Enter all the credentials!")
            exit()
        feedback = t.add(description = args.desc, amount = args.amt)

        if feedback:
            print("Expense added successfully!")
        else:
            print("Expense not added!")
        
    elif cmd == 'list':
        t.list_exp()

    elif cmd == 'summary':
        mon = args.m
        yr = args.y
        if mon:
            mon = int(mon)
        if yr:
            yr = int(yr)
        t.summary(month = mon, year = yr)

    elif cmd == 'update':
        amt = args.amt
        if amt:
            amt = float(amt)

        feedback = t.update(id = args.id, description = args.desc, amount = amt)

        if feedback:
            print("Expense updated successfully!")
        else:
            print("Cannot update the expense!")

    elif cmd == 'delete':
        if not args.id:
            print("Enter the ID")
            exit()
        feedback = t.delete(id = args.id)

        if feedback:
            print("Deleted Successfully!")
        else:
            print("Cannot Delete!")
    
    else:
        print("Wrong command!\nTry 'exp-cli -h' for help")
