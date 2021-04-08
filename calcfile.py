with open("calcfile.txt", 'r') as f:
	calc_string = f.read().splitlines()

calcs = [calc_string[calc].split() for calc in calc_string if calc<len(calc_string) ]
print(calcs)

def calculator(String, a, b):
	if String == '+':
		result = a + b
		print (result)
	elif String == 'x':
		result = a * b
		print (result)
	elif String == '-':
		result = a - b
		print (result)
	elif String == '/':
		result = a / b
		print (result)
	else: 
		print('Invald operator, please try again')

# calcs = [ 
# 	calc_string.split[x]
# 	for calc_string
# 	in calc_string.split[0] 
# 	if ]


# my_tuple = calc_string[0].split()

# print(calcs)

# for calc in calc_string:
# 	i = float(calc)
# 	my_tuple = calc_string[i].split()
# 	calculator(my_tuple[1], my_tuple[2], my_tuple[3])
# 	i+1
# 	break