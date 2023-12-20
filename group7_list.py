# Learning Task(Linear DS-List)
# Linked List Data Structure
# Group7_Vargas_DimanarigArjunRashid

from ast import Index
from dataclasses import dataclass
from pickle import NONE
from re import I


# creating class Node
class Node:
    def __init__(self, data=100, ref=None):
        self.data = data
        self.ref = ref

    def print(self):
        pass

    # defining Linked List


class LinkedList:
    def __init__(self):
        self.head = None

    # insert node at the start
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # insert node at the end
    def insert_at_end(self, data):
        n = self.head
        if n:
            while n.ref:
                n = n.ref
            n.ref = Node(data, n.ref)
        else:
            self.head = Node(data, self.head)

    # Insert At Position
    def insert_at_position(self, index, data):
        n = self.head

        if n and index > 0:
            j = 0
            while n.ref and j < index - 1:
                j += 1
                n = n.ref
            n.ref = Node(data, n.ref)
        else:
            self.head = Node(data, self.head)

    # delete at Start
    def delete_at_start(self):
        if self.head is None:
            return
        self.head = self.head.ref

    # delete at end
    def delete_at_end(self):
        n = self.head
        if n:
            while n.ref:
                j = n
                n = n.ref
                j.ref = n.ref
        return n

    # delete at position
    def delete_at_position(self, index):
        n = self.head
        if n:
            if index > 0:
                k = 0
                while n.ref and k < index:
                    k += 1
                    j = n
                    n = n.ref
                    j.ref = n.ref
            elif index == 0:
                self.head = self.head.ref
        return n

    # searching value
    def search_item(self, data):
        n = self.head
        j = -1
        k = 0
        while n:
            if n.data == data:
                j = k
                break
            k += 1
            n = n.ref
        return

    # Display data
    def display(self):
        n = self.head
        print(' ', end='-')
        while n:
            print(n.data, end=' ''- ')
            n = n.ref
        print(' ')

        # Display Number At Position

    def display_num_at_position(self, index):
        n = self.head
        if n and index > 0:
            j = 0
        while n.ref and j < index:
            j += 1
            n = n.ref
        return n

    # assigning LinkedList to nlinklist


nlinklist = LinkedList()


# creating menu
def menu():
    print("[0] Exit")
    print("[1] Insert At Start")
    print("[2] Insert At End")
    print("[3] Insert At Position")
    print("[4] Delete At Start")
    print("[5] Delete At End")
    print("[6] Delete At Position")
    print("[7] Delete Number")
    print("[8] Search Number")
    print("[9] Display Number At Position")
    print("[10] Display List\n")


menu()
while True:
    selection = int(input("Please input your Choice: "))
    # condition for selction in the menu
    if selection == 0:  # assigning 0 for exit
        print("\nDo you want to Exit the program?\n"
              "Please type 'Yes' if you want to proceed")
        option = str(input("Yes or No: "))
        if option == "Yes":
            print("Thank You!")
        else:
            menu()
    elif selection == 1:  # assigning 1 for inserting node at head
        data = int(input("Enter Value of Number to be Inserted at the Start: "))
        nlinklist.insert_at_start(data)
        # assigning data as index
        index = data
    elif selection == 2:  # assigning 2 for inserting value at end
        data = int(input("Enter Value of number to be Inserted at the end: "))
        nlinklist.insert_at_end(data)
    elif selection == 3:  # assigning 3 for inserting value at desired position
        data = int(input("Enter a number: "))
        index = int(input("Enter a Value where the Number is to be Inserted: "))
        nlinklist.insert_at_position(index, data)
        print("The Data entered at the Point of: ", index)
    elif selection == 4:  # assigning 4 for deleting node at start
        nlinklist.delete_at_start()
    elif selection == 5:  # assigning 5 for deleting node at end
        nlinklist.delete_at_end()
    elif selection == 6:  # assigning 6 for deleting node at position
        index = int(input("Enter Position to be Deleted: "))
        nlinklist.delete_at_position(index)
        print("The Value is Deleted at: ", index)
    elif selection == 7:  # assigning 7 for deleting value instantly
        data = int(input("Enter Value to be Deleted: "))
        nlinklist.delete_at_position(data)
        if index == 1:
            print("Value", data, '"is not on the List and cannot be Deleted."')
        else:
            print("Value", data, '"has been Successfully Deleted."')
    elif selection == 8:  # assigning 8 for searching value in the data
        data = int(input("Enter Number to be Searched: "))
        index = nlinklist.search_item(data)
        print("Value is Found at Position", data)
        if index == -1:
            print("Value", data, "not Found.")
        else:
            print("Value", data, 'is Found')

    elif selection == 9:  # assigning 9 for displaying value and its position
        index = int(input("Enter Value to Display: "))
        print("The Value at the Position", index, "is", nlinklist.display_num_at_position(index).data)

    elif selection == 10:  # assigning 10 for displaying updated output
        nlinklist.display()

    # Displaying the output
    nlinklist.display()

# REFERENCES

# codescracker.com
# geeksforgeeks.org
# stackabuse.com
# appdividend.com
# Mata_Tanay_Marano