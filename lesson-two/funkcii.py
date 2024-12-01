wrong = 1
print (type(wrong))
right = (int(wrong))
print (type(right))
print (right)
print (float(right))

string = (1, 2, 3, 4, 5)
print (len(string)) #Кількість данних

string = "1, 2, 3, 4, 5"
print(len(string)) #Кількість символів

string = "ha HA ha!"
print(string.upper()) #Всі великі
print(string.lower()) #Всі маленькі
print(string.capitalize()) #Тільки перша велика
string = string.replace ("!","?")
print(string)

string = string.split ()
print(string)
string = "".join (string)
print(string)

string = string.count ("a")
print(string)
