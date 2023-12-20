def fact(n):  # iteration
    # fact = 1
    # count = 2
    # while count <= n:
    # fact = fact * count

        # count += 1
        # return fact

     # recurtion
    if n <= 1:
        return 1
    else:  # recursive step
        return (n * fact (n-1))

    print(fact(6))