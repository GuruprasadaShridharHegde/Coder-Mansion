import json

g = '{"name": "guru", "age": "24", "weight":"54"}'
y = json.loads(g)
print(y["age"],y["weight"])