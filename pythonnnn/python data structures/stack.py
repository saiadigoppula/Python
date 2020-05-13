
class Stack():
	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return self.items == []


	def get_stack(self):
		return self.items

	def peek(self):
		if not self.is_empty():
			return self.items[-1]
		else:
			return 'empty'


#s = Stack()

#print(s.is_empty())
#print('peek',s.peek())
#s.push('A')
#print(s.is_empty())
#s.push('B')
#s.push('C')
#s.push('D')
#print('peek',s.peek())

#print(s.get_stack())

#print(s.pop())

#s.push('E')
#print(s.get_stack())

