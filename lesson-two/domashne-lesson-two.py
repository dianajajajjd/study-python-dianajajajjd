string = "HI, how have you been?"
print(type(string))

integer = 12345
print(type(int))

num_2 = 12.345
print(type(num_2))

check = True
print(type(check))

lst = ["HI", "how", "have", "you", "been"]
print(type(lst))

dct = {'Name': "LOLO", 'Age': 99}
print(type(dct))

num_3 = 12, 34, 5
print(type(num_3))

set_ex = {12, 34, 56, 12}
print(set_ex)
print(type(set_ex))

print(type(None))


lst = [1,2,3,4,5,6,7,8,9]
dct = {'name': "HIHI", 'age': 10}
name = "HIHI"
tpl = "H", "O", "C"

result = dct ['age'] in lst
print(result)

print(dct['age'] == dct['name'])

print(dct['name'] == name and dct['age'] == 10)



#Робота з рядками:
#1
num_str = 125
num_str = str(num_str)
print(type(num_str))
#2
message = 'Hi, my name is Python!'
message = message.replace ("y", "0")
message = message.replace ("i", "1")
print(message)
#3
split_test = 'This is a split test'
split_test = split_test.split()
print(split_test)
split_test = "" .join(split_test)
print(split_test)
print (len(split_test))

#Робота зі списками:
#1
list_append = [1, 2, 3]
print(list_append)
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)
#2
list_extend = [4, 5, 6]
print(list_extend)
list_extend.extend([7, 8, 9])
print(list_extend)
#3
print(list_extend.index(6))
#4
print(len(list_append))

#Робота зі словниками:
#1
dict_test = {"car": 'Toyota', 'price': 4900, 'where': 'EU'}
print()
print()
#2
print(dict_test.keys())
print(dict_test.values())
#3
print(dict_test.items())