with open("calcfile.txt", 'r') as f:
	calc_string = f.read().splitlines()
	my_tuple = calc_string[0].split()

# def calculator(String, a, b):
	string = my_tuple[1]
	a = int(my_tuple[2])
	b = int(my_tuple[3])

	if string == '+':
		result = a + b
		print (result)
	elif string == 'x':
		result = a * b
		print (result)
	elif string == '-':
		result = a - b
		print (result)
	elif string == '/':
		result = a / b
		print (result)
	elif string == '%':
		result = a % b
		print (result)
	else: 
		print('Invald operator, please try again')

# calcs = [ calculator(my_tuple[1], my_tuple[2], my_tuple[3]) for calc in calc_string.split[0] ]
# print(calcs)

# for calc in calc_string:
# 	i = float(calc)
# 	my_tuple = calc_string[i].split()
# 	calculator(my_tuple[1], my_tuple[2], my_tuple[3])
# 	i+1
# 	break