# Group7_Vargas_DimanarigArjunRashid
# Learning Task (Mathematical Analysis on Recursive Algorithm)
# Algorithm and Complexity

# Recursive implementation of the described algorithm
def recursive(input):
    # Define the base case where the funtion will eventually fall on
    if input == 0:
        return 0
    # Case where it isn't base case
    else:
        # Reduce the next input that will be passed
        temp = input -1
        # Add the input and the result of the other recursion with the input temp
        return recursive(temp) + input

# Iterative implementation of the described algorithm
def iterative(input):
    # Initialize a variable to store the result
	sum = 0
    # Loop until input becomes 0
	while input != 0:
        # store the sum plus the input to the variable named sum
		sum += input
        # decrement the input variable in order to avoid an infinite loop
		input = input -1
    # return the sum
	return sum

#Getting input from the user
print("-----------")
input = int(input("Please enter your input: "))
print("-----------")
print(f'The recursive result is: {recursive(input)}')
print("-----------")
print(f'The iterative result is: {iterative(input)}')
print("-----------")