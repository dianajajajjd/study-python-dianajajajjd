### Умовні конструкції:

#1  **Перевірка паролю:**
string = "password123"

if "password123" in string:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

#2 **Визначення днів тижня:**

num = 4 #Задане число
if num == 1:
    print("Понеділок")
elif num == 2:
    print("Вівторок")
elif num == 3:
    print("Середа")
elif num == 4:
    print("Четвер")
elif num == 5:
    print("П'ятниця")
elif num == 6:
    print("Субота")
elif num == 7:
    print("Неділя")

else:
    print("Помилка")

### Цикли:

#1 **Таблиця множення:**
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #множники
d = 8 #заданий множник
for num in num_list:
    print(num * d)

#2 ** Сума чисел: **
num_list2 = [20, 30, 40 ,50]
print(sum(num_list2))

#3 **Факторіал числа:**
num = 6 #Задане число
result = 1
for factor in range(1, num + 1):
    result *= factor
print(result)


#4 **Парні числа:**
a = 0
while a < 50:
    a += 2
    print (a)

#5 **Пошук простих чисел:**
num_list5 = [1,2,3,4,5,6,7,8,9,10,11]
for num in range(2, 12):
    result = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            result = False
    if result:
        print(num)