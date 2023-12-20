# Learning Task (Linear DS-Queue)
# Group7_Vargas_DimanarigArjunRashid
# Queue implementation using Array in Python

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)  # add element at the end

    # Remove an element
    def dequeue(self, item):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)  # removes the first element (index 0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


# A queue implemented using a array
q = Queue()


def menu():
    print("-------------------------------")
    print("----")
    print("[0] Exit")
    print("[1] Enqueue Workload")
    print("[2] Dequeue Workload")


menu()
while True:
    # getting input from the user
    print("-------------------------------")
    choice = int(input("Choice: "))
    print("-------------------------------")

    # condition for exit
    if choice == 0:
        print("\nThank You!")
        print(" ")
        exit()

    # condition for enqueue
    elif choice == 1:
        Num = int(input("Enter input: "))
        print("")
        print("{} is being added in the array!".format(Num))
        q.enqueue(Num)

    # condition for dequeue
    elif choice == 2:
        print("Element has been dequeued!")
        q.dequeue(Num)

    # display the output
    q.display()