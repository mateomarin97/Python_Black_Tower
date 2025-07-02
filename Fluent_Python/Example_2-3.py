symbols = "$&@~#"
codes_beyond_64 = [ord(symbol) for symbol in symbols if ord(symbol) >= 64]
print("Unicode code points greater than or equal to 64:", codes_beyond_64)