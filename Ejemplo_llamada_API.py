import requests as req

#res = req.get("http://api.open-notify.org/astros.json")
res = req.get("https://jsonplaceholder.typicode.com/users")
data= res.json()
print("=============================================")
for user in data:
    print("Nombre:",user["name"],"\nEmail:",user["email"],"\n")

print("=============================================")