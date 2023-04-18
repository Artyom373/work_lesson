number = [1,2,3,4,5,6]
name =["Petr","Van","bob"]
object =["Person", True,1,2,3,6]
# print(number)
# print(name)
# print(object)
#
# number2 = [5] * 6   # список из 5 шетсрок
# print(number2)
#
# print(name[-1]) # Вывод последнего элекиннн из списка
# name[1] = "Klon" #Заменили bob на Klon
# print(name)

# Перебираем список
# i=0
# while i < len(name):
#     print(name[i])
#     i=i+1

name.append("Alisa") #Добавляем в список Алису
print(name)

name.insert(2,"Josh") #Добавляем в список Josh вторым индексом
print(name)

name.extend(["Mike","Sem"]) #Добавить еще список
print(name)

index_start = name.index("Petr") #Находим под каким индеком Петр
print(index_start)

renoved_id = name.pop(1)   #Удалить элемент под индексом 1
print(renoved_id)
print(name)

name.remove("Alisa") #Удалить элемент Алиса
print(name)

# name.clear() #Удалить все
# print(name)

#Найти Josh и удалить
if "Josh" in name:
    name.remove("Josh")
    print(name)