# Learning Task (Searching)
# Group7_Vargas_DimanarigArjunRashid
# Linear Search (Policeman and thieves)

# re for calculations
import re


# class and attributes
def policeThieves(arr, n, k):
    i = 0
    l = 0
    r = 0
    res = 0
    thi = []
    pol = []

    # store indices in list
    while i < n:
        if arr[i] == 'P':
            pol.append(i)
        elif arr[i] == 'T':
            thi.append(i)
        i += 1

    # track lowest current indices of
    # thief: thi[l], police: pol[r]
    while l < len(thi) and r < len(pol):

        # can be caught
        if (abs(thi[l] - pol[r]) <= k):
            res += 1
            l += 1
            r += 1

        # increment the minimum index
        elif thi[l] < pol[r]:
            l += 1
        else:
            r += 1

    return res


# Driver program

def main():
    T = int(input("\n"))

    # number of iterations
    for index in range(T):
        # getting inputs w/ spaces
        k, n = map(int, input().split())
        row1 = str(input(""))
        row2 = str(input(""))
        row3 = str(input(""))

        # displaying thieves caught
        n = len(row1)
        print(("Maximum thieves reachable: {}".format(policeThieves(row1, n, k))))
        n = len(row2)
        print(("Maximum thieves reachable: {}".format(policeThieves(row2, n, k))))
        n = len(row3)
        print(("Maximum thieves reachable: {}".format(policeThieves(row3, n, k))))

        print("Thieves Caught: ", k)

        # finding and summing the numbers of 'T' in array
        th = len(re.findall('T', row1 + row2 + row3))
        print("Total thieves: {}".format(th))

main()
