#With the slice object you can give names to each slice, which can make your code more readable.

numbers = "0123456789"
zero_to_three = slice(0, 4)
four_to_seven = slice(4, 8)
eight_to_nine = slice(8, None)

print(numbers[zero_to_three])  # Output: 0123
print(numbers[four_to_seven])  # Output: 4567
print(numbers[eight_to_nine])  # Output: 89