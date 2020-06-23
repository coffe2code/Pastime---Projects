from collections import defaultdict

class Ops:

	def __add__(self, other):
		return Add(self, other)

	def __mul__(self, other):
		return Mul(self, other)

	def __sub__(self, other):
		return Add(self, Neg(other))

	def __truediv__(self, other):
		return Mul(self, Inv(other))

class Var(Ops):
	"""A leaf node"""
	def __init__(self, value):
		self.value = value

class Add(Ops):

	def __init__(self, a, b):
		self.value = a.value + b.value
		self.grad = [(a, 1), (b, 1)]

class Mul(Ops):

	def __init__(self, a, b):
		self.value = a.value*b.value
		self.grad = [(a, b.value), (b, a.value)]

class Neg(Ops):

	def __init__(self, var):
		self.value = -1*var.value
		self.grad = [(var, -1)]

class Inv(Ops):

	def __init__(self, var):
		self.value = 1/var.value
		self.grad = [(var, -var.value**-2)]

def get_gradients(parent_node):

	gradients = defaultdict(lambda : 0)
	stack = parent_node.grad.copy()
	while stack:
		node, route_value = stack.pop()
		gradients[node] += route_value

		if not isinstance(node, Var):

			for child_node, child_route_value in node.grad:
				stack.append((child_node, child_route_value*route_value))

	return dict(gradients)

