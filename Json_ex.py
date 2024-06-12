import json

x = '{"name" : "Ann","age" :21}'

y = json.loads(x)

print(y)
print(type(y))

z = json.dumps(y)
print(z)
print(type(z))