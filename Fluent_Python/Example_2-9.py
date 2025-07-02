import collections

City = collections.namedtuple('City', ['name', 'country', 'population', 'coordinates'])
# Alternative way to define the namedtuple:
#City = collections.namedtuple('City', 'name country population coordinates')
Tokyo = City('Tokyo', 'Japan', 9_273_000, (35.6895, 139.6917))
print(Tokyo)
print(Tokyo.name)
print(Tokyo.country)
print(Tokyo.population)
print(Tokyo.coordinates)
print(Tokyo[0])  # Accessing by index
print(Tokyo[1])
print(Tokyo[2])
print(Tokyo[3])