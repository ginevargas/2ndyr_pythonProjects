# Learning Task (Sorting)
# Group7_Vargas_DimanarigArjunRashid

import time

# getting unsorted inputs
n = int(input("Enter size of the list: "))
ar = list(map(int, input().strip().split()))[:n]
print("")

# condition for sorting elements using insertion
# displaying
'''
for i in range(1, len(ar)):
    while ar[i - 1] > ar[i] and i > 0:
        ar[i - 1], ar[i] = ar[i], ar[i - 1]
        i -= 1
    #print("Insertion Sort Runtime: ", m)
print(ar)#end - start
'''
start2 = time.time()
for i in range(1, len(ar)):

    # print(f"{i} ", end="")
    while ar[i - 1] > ar[i] and i > 0:
        # print("*", end="")

        ar[i - 1], ar[i] = ar[i], ar[i - 1]
        i -= 1
end2 = time.time()
print(f"Running time: {end2 - start2}")
# 9
# ar = [8,7,6,5,4,3,2,1]
print("")
print(ar)

start1 = time.time()


def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


end1 = time.time()

print("")
size = len(ar)
print('Selection Sort:')
selectionSort(ar, size)
print(f"Running time: {end1 - start1}")
print(ar)
print("")

