# Learning Task5(Divide & Conquer Algorithm)
# Algorithms and Complexity
# Group7_Vargas_DimanarigArjunRashid

import math

print("\n               INPUT")
print('------------------------------------')
D = int(input("Demographics: "))  # getting input for demographics
if D > 100:  # condition if input is greater than 100
    print("\nValues must not be greater than 100 and less than 0!\n")
    exit()
elif D < 0:  # Condition
    print("\nValues should not be less than 0!\n")
    exit()

print('------------------------------------')
G = int(input("Geography: "))
if G > 100:  # condition
    print("\nValues must not be greater than 100 and less than 0!\n")
    exit()
elif G < 0:  # Condition
    print("\nValues should not be less than 0!\n")
    exit()

print('------------------------------------')
S = int(input("Socio-Economics: "))
if S > 100:  # condition
    print("\nValues must not be greater than 100 and less than 0!\n")
    exit()
elif S < 0:  # Condition
    print("\nValues should not be less than 0!\n")
    exit()

print('------------------------------------')
B = int(input("Behavioral: "))
if B > 100:  # condition
    print("\nValues must not be greater than 100 and less than 0!\n")
    exit()
elif B < 0:  # Condition
    print("\nValues should not be less than 0!\n")
    exit()

print('------------------------------------')
V = int(input("Governor: "))
if V > 100:  # condition
    print("\nValues must not be greater than 100 and less than 0!\n")
    exit()
elif V < 0:  # Condition
    print("\nValues should not be less than 0!\n")
    exit()
print('------------------------------------')


# method              # function for rounding to whole number
getNumofRegion = math.ceil((((D/100) + (G/100) + (S/100) + (B/100)) / 4) * V)

# displaying estimated number of regions
print("\n              OUTPUT")
print('------------------------------------')
print("Number of Region: ", getNumofRegion)
print(" ")

# REFERENCES
# Group_Venn