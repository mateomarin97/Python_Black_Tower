import bisect
import random

#Number of elemnts to add to the sorted list
n = 10
#Seed for reproducibility
random.seed(42)

sorted_list = []

for _ in range(n):
    #Generate a random number
    num = random.randrange(n*2)
    #Insert the number into the sorted list using bisect.insort
    bisect.insort(sorted_list, num)
    print(f"Inserted {num}: {sorted_list}")
    