colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# Using a generator expression to create combinations of colors and sizes
# This is a more memory-efficient way to generate combinations on-the-fly
# without storing them all in memory at once. The generator expression
# yields each combination one at a time, which is useful for large datasets.
# The generator expression is enclosed in parentheses, which allows it to be
# iterated over without creating a list in memory.
for t_shirt in (f"{color} {size}" for color in colors for size in sizes):
    print(t_shirt)