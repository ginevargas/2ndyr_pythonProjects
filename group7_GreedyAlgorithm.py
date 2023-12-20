# Learning Task (Greedy Algorithm)
# Algorithms and Complexity
# Group7_Vargas_DimanarigArjunRashid

# finding minimum denominations for each changes
# from tokenize import Double

def findMin(pay):
    nums = [0.05, 0.10, 0.25, 1, 5, 10, 20, 50, 100, 200, 500, 1000]

    n = len(nums)

    # initialize the result
    ans = []
    # condition
    i = n - 1
    while (i >= 0):
        while (pay >= nums[i]):
            pay -= nums[i]
            ans.append(nums[i])
        i -= 1

    for i in range(len(ans)):
        print(ans[i], end=" ")

    # driver code

if __name__ == '__main__':
    pricePay = float(input("\nEnter the Amount to Pay: Php "))
    amount = float(input("Enter Amount of your Payment: Php "))
    n = (amount - pricePay)
    print("\nThe change is Php", n, ": ", end=" ")
    findMin(n)

    print(" ")
    numCostumer = int(input("\nNumber of Costumer Served: "))
    paid = (numCostumer * 50)
    print('Salary: Php', float(paid))
    print(" ")