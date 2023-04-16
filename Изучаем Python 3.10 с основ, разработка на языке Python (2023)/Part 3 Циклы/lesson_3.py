# ////////FOR/////////

temp =[1,2,3,4,5,6,7,]
# for i in temp:
#     print(i) #Достаем данные из списка
#
# for i in temp:
#     print(i*i) #Квадрат чисел

# arr = len(temp) #Количество элекментов в temp
# for i in range(arr):
#     #print(i)   #Выводит индексы
#     print(temp[i]) #Выводит каждое число по индексу 0 = 1, 1 =2 и т.д.

# temp = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(temp)):
#     if temp[i] % 2 == 0:   # Вывод остатка
#         print(f"Четное число{temp[i]}")
#     else:
#         print(f"Нечетное число{temp[i]}")

# Находим пары с суммой 0 из двух списков и записываем в список эти пары и выводим резултат
# list1 =[2,4,-5,6,8,-2]
# list2=[2,-6,8,3,5,-2]
# res=[]
# for i in list1:
#     for j in list2:
#         if i+j == 0:
#             res.append((i,j))
# print(res)



# ////////WILE/////////

vals = [1,2,3,4,5,6,7,8,9,10]
sum = 0
i = 0

while i < len(vals):
    if vals[i] % 2 == 0:
        continue
    else:
        sum+=vals[i]
    if sum > 10:
        break
print(sum)

