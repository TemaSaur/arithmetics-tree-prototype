import random


def get_random_number(start=1, end=10):
	return random.randint(start, end)


def get_random_op():
	return random.choice(['+', '-', '*', '/'])


def get_result(a, b, op):
	if op == '+':
		return a + b
	if op == '-':
		return a - b
	if op == '*':
		return a * b
	if op == '/':
		return a / b
	return None


ops = get_random_number(1, 3)
print(ops)

a = get_random_number()
b = get_random_number()
op = get_random_op()
equation = f'{a} {op} {b}'

res = get_result(a, b, op)

for i in range(1, ops):
	c = get_random_number()
	op = get_random_op()

	equation = f'({equation}) {op} {c}'
	res = get_result(res, c, op)

print(equation)
print(res)
