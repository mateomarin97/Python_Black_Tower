colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# In this list the sizes change first, then the colors.
# The new line for the second for loop is just for readability.
tshirts = [(color, size) for color in colors
                         for size in sizes]

print("T-shirts combinations:", tshirts)

#We can also arrange them the other way around, where the colors change first, then the sizes.
tshirts_reversed = [(color, size) for size in sizes
                               for color in colors]

print("T-shirts combinations (reversed):", tshirts_reversed)