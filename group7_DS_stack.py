# Learning Task(Linear DS-Stack)
# Implementing Stack Abstract Data Structure
# using Array
# Group7_Vargas_DimanarigArjunRashid

from array import array
from typing import List


def indi_details():
    print("---------------------------------------------")
    a = int(input("\nNumber of elements in the array: "))
    stack1 = list(map(int, input("Enter Elements of Stack1: ").strip().split()))
    stack2 = list(map(int, input("Enter Elements of Stack2: ").strip().split()))
    stack3 = list(map(int, input("Enter Elements of Stack3: ").strip().split()))
    # list = [n]
    print("---------------------------------------------")

    print("Stack 1 total height: {}".format(sum(stack1)))
    print("Stack 2 total height: {}".format(sum(stack2)))
    print("Stack 3 total height: {}".format(sum(stack3)))

    if stack1 == stack2 == stack3:
        print("\nAll stacks are equal at Height: {}".format(sum(stack1)))
    else:
        print("\nStack Heights will never be equal!")
    print("---------------------------------------------")

    print("Do you want to continue? 'Y' or 'N'\n""Please type 'Yes' if you want to proceed")
    option = str(input("Yes or No: "))
    if option == "Yes":
        print("\nThank You!")
    else:
        indi_details()


indi_details()

# REFERENCES
# geeksforgeeks.com
# w3schools.com