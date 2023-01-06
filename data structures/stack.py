# using python in-built lists 
class stackList: 

	DEFAULTCAPACITY = 10

	def __init__(self): 
		self._list = [None] * stackList.DEFAULTCAPACITY
		self._top = -1 
		self._size = 0 

	def push(self, data): 
		if self._top >= stackList.DEFAULTCAPACITY -1: 
			return 'ERROR STACK IS FULL'
		else: 
			self._top += 1 
			self._size += 1 
			self._list[self._top] = data

	def pop(self): 
		if self._top == -1: 
			return 'ERROR STACK IS EMPTY'
		else: 
			tempvar = self._list[self._top]
			self._list[self._top] = None 
			self._top -= 1 
			self._size -= 1 
			return tempvar 

	def peek(self): 
		if self._top == -1: 
			return 'ERROR STACK IS EMPTY'
		else: 
			return self._list[self._top]

	def size(self): 
		return self._size 

	def __str__(self): 
		ret = '' 
		for i in self._list: 
			ret += str(i) + ' '
		return ret 

class Node: 

	def __init__(self, data, Next): 
		self._data = data 
		self._next = Next 

	def setData(self, data): 
		self._data = data 

	def getData(self): 
		return self._data 

	def setNext(self, Next): 
		self._next = Next 

	def getNext(self): 
		return self._next 

	def __str__(self): 
		if self.getNext() != None: 
			return "Data: {} \t Next: {}".format(self.getData(), self.getNext().getData())
		else: 
			return "Data: {} \t Next: {}".format(self.getData(),self.getNext())

class stackLinkedList: 

	def __init__(self): 
		self._top = None 
		self._size = 0

	def push(self, data): 
		if self._top: 
			probe = self._top
			self._top = Node(data, probe)
		else: 
			self._top = Node(data, None)
		self._size += 1 

	def pop(self): 
		if self._top:
			self._size -= 1 
			x = self._top.getData() 
			self._top = self._top.getNext() 
			return x 
		else: 
			return 'ERROR STACK IS EMPTY'

	def peek(self): 
		if self._top: 
			return self._top.getData() 
		else: 
			return 'ERROR STACK IS EMPTY'

	def size(self): 
		return self._size 

	def __str__(self): 
		ret = ''
		probe = self._top 
		while probe.getNext() != None: 
			ret += '\n' + probe.__str__() 
			probe = probe.getNext() 
		ret += '\n' + probe.__str__() 
		return ret 

s = stackLinkedList() 
for i in range(5): 
	s.push(i) 
print(s) 

print('\n') 
s.pop() 
print(s) 

y = s.size() 
print(y) 













