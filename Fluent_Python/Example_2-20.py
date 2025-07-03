from array import array
from random import random

floats = array("d", (random() for _ in range(10**7)))
print(floats[-1])  # Print the last element to confirm the array is populated

fp = open('floats.bin', 'wb')
floats.tofile(fp)  # Write the array to a binary file
fp.close()  # Close the file 

floats2 = array("d")  # Create a new empty array
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)  # Read the same number of elements from the file
fp.close()  # Close the file
print(floats2[-1])  # Print the last element to confirm it matches the original
print(floats2 == floats)  # Check if the two arrays are equal