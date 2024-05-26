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


tree = {}
tree['v'] = get_random_op()

# DFS

stack = [(tree, 1)]

# number of parentheses
MAX_DEPTH = 2

while stack:
	node, depth = stack.pop()

	for d in ['left', 'right']:
		node[d] = {}
		thing = random.choice(['op', 'num'])
		if thing == 'op' and depth <= MAX_DEPTH:
			node[d]['v'] = get_random_op()
			stack.append((node[d], depth + 1))
		else:
			node[d]['v'] = get_random_number()


def get_equation(tree):
	if tree['v'] in ['+', '-', '*', '/']:
		return f'({get_equation(tree["left"])} {tree["v"]} {get_equation(tree["right"])})'
	return tree['v']


def get_tree_result(tree):
	if tree['v'] in ['+', '-', '*', '/']:
		return get_result(get_tree_result(tree['left']),
		                  get_tree_result(tree['right']), tree['v'])
	return tree['v']


# debug
print(tree)
equation = get_equation(tree)[1:-1]
print(equation)
print('tree traversal', get_tree_result(tree))
print('eval(equation)', eval(equation))
