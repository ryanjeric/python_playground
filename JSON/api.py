import json
from urllib.request import urlopen

with urlopen("https://jsonplaceholder.typicode.com/todos") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

for item in data:
    print(item['title'])
