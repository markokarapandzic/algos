# Strings
print(5 ** 2)
print(5 / 2)
print(5 // 2)
print('test' 'test123' 'sadasd')

test = "some string"
print(test[0:4])
print(test[5:])
print(len(test))

# Lists
list = [1, 2, 3, 4, 5]
print(list)
print(list[:2])
print(list[:]) # Shallow Copy
print(list + [6, 7, 8, 9])
list.append(6)
print(list)
list[2:4] = [8, 9]
print(list)
list[4:] = []
print(list)
list[:] = []
print(list)
print(len(list))

# Control Flow
users = {'Hans': 'active', 'Marko': 'inactive', 'Someone': 'active'}

for user, status in users.items():
	print(user + ' ' + status)

print(range(5, 10))
print(range(5, 10, 3))

for n in range(0, 10):
	print(n)
else: # Called after For is finished
	print('Finished')

status = 403

match status:
	case 400:
		print('400')
	case 401:
		print('401')
	case 402 | 403 | 404:
		print('402 - 404')
	case _:
		print('Nothing')
