#Словари

user ={1:"Dias", 2:"Tom"}
email = {"dias@gmail.com":"Dias"}
obj = {}
obj1 = dict()
userlist = [
    ["+1234","Bob"],
    ["+20000", "Tom"],
    ["+10000", "Klon"]
]
user_dict = dict(userlist)
print(userlist)
print("============")
print(user_dict)
print("============")
print(userlist[2][0])
print("============")
user[3] = "Jein"
print(user)

if user[3] == "Jein":
    print("Yes")

print("============")
users = user.pop(2)   #Удаляет элемент с индексом 2 из Словаря
print(users)

for element in user:
    print(f'Index {element}, User {user[element]}')