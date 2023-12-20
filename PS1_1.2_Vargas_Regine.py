# This is a simple registration program using Python that instantiate a class Person
# with values name and birthdate. In 3 times using loop.

def person_data():

    for index in range(1):
        name1 = str(input("Enter your Name: "))
        birth1 = str(input("Enter your Birthdate: "))
        name2 = str(input("\nEnter your Name: "))
        birth2 = str(input("Enter your Birthdate: "))
        name3 = str(input("\nEnter your Name: "))
        birth3 = str(input("Enter your Birthdate: "))

        print("\n{} was born on {} ".format(name1, birth1))
        print("{} was born on {} ".format(name2, birth2))
        print("{} was born on {} ".format(name3, birth3))

person_data()