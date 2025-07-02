
# Example 2-1: Using ord() to get Unicode code points of symbols with a for loop
symbols = '$&@~#'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
    
print("Unicode code points using for loop:", codes)

#Example 2-2: Using list comprehension to get Unicode code points of symbols
codes_comp = [ord(symbol) for symbol in symbols]
print("Unicode code points using list comprehension:", codes_comp)