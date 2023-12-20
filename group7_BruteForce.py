# Learning Task (Brute Force Algorithm)
# Group7_Vargas_DimanarigArjunRashid
# PIN Combinations - Brute Force Algorithm

# we must first import the time for time execution
import time

# defining the runtime execution
def runtime():
    # defining the PIN code
    pin_code = "97531"
    max_tries = 5

    def verify_pin(the_pin):
        return the_pin == pin_code

    def len_ght():
        if pin_code > 5:
            print("Pin code has 5 numbers!")

    def main():
        tries = 0
        length = 5

        while tries < max_tries:
            print('\n------------------------------------')
            print("Clue:")
            print("1. It has 5 decreasing numbers.")
            print("2. Consecutive odd numbers.")
            print('------------------------------------')
            print('------------------------------------')
            print("Caution:")
            print("You only have 5 attempts")
            print('------------------------------------')
            print('\n------------------------------------')
            pin = input("Please enter your pin code: ")
            print('------------------------------------')

            if verify_pin(pin):
                print("\nCorrect. Vault is opened!\n")
                break
            else:
                print("\nIncorrect. Please try again!")
            tries += 1

        else:
            print("I am LOCKIN' Please be back after 24 hours!\n")

    if __name__ == '__main__':
        main()

# get the start time
st = time.time()

# main program
runtime()

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')


# References
# StackOverFlow.com
# Algorithm Analysis runtime.py