#Example with extra methods that namedtuple have access to

import collections

City = collections.namedtuple('City', ['name', 'country', 'population', 'coordinates'])
print(City._fields)
Tokyo_data = ('Tokyo', 'Japan', 9_273_000, (35.6895, 139.6917))
Tokyo = City(*Tokyo_data)
#Alternatively, you can use:
#Tokyo = City._make(Tokyo_data)

for key, value in Tokyo._asdict().items():
    print(f'{key} = {value}')