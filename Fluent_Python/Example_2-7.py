#Example about unpacking tuples

city, year, pop, chg, area = ('Tokyo', 2003, 32450, -0.1, 8014)
print(f"{city:10} | {year:4d} | {pop:9,d} | {chg:6.2%} | {area:5,d}")

travel_ids = [('USA', '31432544'), ('Japan', '12345678'), ('France', '98765432')]

for pasaport in sorted(travel_ids):
    print('%s/%s' % pasaport)
    
for country, _ in travel_ids:
    print(country)
    
    
#Using * to unpack the rest of the tuple
a, b, *rest = range(5)
print("############")
print("a, b, *rest = range(5)")
print(a, b, rest)
print("############")

a, *middle, c = range(5)
print("a, *middle, c = range(5)")
print(a, middle, c)
print("############")

*head, b, c = range(5)
print("*head, b, c = range(5)")
print(head, b, c)
print("############")

#Using * to unpack tuples for function inputs
def add(x, y):
    return x + y

x= 10
y = 20
print("add(x, y) = ", add(x, y))
xy = (x, y)
print("add(*xy) = ", add(*xy))
    