import array
symbols = "$&@~#"
A_tuple = tuple(ord(symbol) for symbol in symbols)
print(f"A_tuple = {A_tuple}")

A_array = array.array('I', (ord(symbol) for symbol in symbols))
print(f"A_array = {A_array}")