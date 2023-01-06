class queuelist: 

	DEFAULTCAPACITY = 10 

	def __init__(self): 
		self._list = [None] * queuelist.DEFAULTCAPACITY
		self._rear = -1 
		self._front = 0
		self._size = 0 

	def enqueue(self, data): 
		if self._rear <= queuelist.DEFAULTCAPACITY-2: 
			self._rear += 1 
			self._list[self._rear] = data 
			self._size += 1 
		else: 
			if self.__len__() < queuelist.DEFAULTCAPACITY: 
				self._rear = 0 
				self._list[self._rear] = data 
			else: 
				return 'ERROR LIST IS FULL'

	def dequeue(self): 
		if self._rear < 0: 
			return 'ERROR LIST IS EMPTY'
		else: 
			self._size -=1 
			temp = self._list[self._front]
			self._list[self._front] = None 
			self._front += 1 
			return temp 

	def peek(self): 
		if self._rear < 0: 
			return 'ERROR LIST IS EMPTY'
		else: 
			return self._list[self._front]

	def isEmpty(self): 
		return not self._list

	def __len__(self): 
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
		if self._next: 
			return 'Data: {} \t Next: {}'.format(self.getData(), self.getNext().getData())
		else: 
			return 'Data: {} \t Next: {}'.format(self.getData(), self.getNext())

class queueLinked: 

	def __init__(self): 
		self._front = None 
		self._rear = None 
		self._size = 0 

	def enqueue(self, data): 
		if self._rear: 
			self._rear.setNext(Node(data, None))
			self._rear = self._rear.getNext() 
		else: 
			self._rear = Node(data, None)
			self._front = self._rear 
		self._size += 1 

	def dequeue(self): 
		if self._front: 
			temp = self._front.getData() 
			self._front = self._front.getNext() 
			self._size -= 1 
		else: 
			return 'ERROR LIST IS EMPTY'

	def peek(self): 
		return self._front.getData() 

	def isEmpty(self): 
		return not self._list 

	def __len__(self): 
		return self._size 

	def __str__(self): 
		ret = '' 
		probe = self._front 
		while probe.getNext() != None: 
			ret += probe.__str__() + '\n'
			probe = probe.getNext() 
		ret += probe.__str__() 
		return ret 


q = queuelist() 
for i in range(10): 
	q.enqueue(i) 
print(q) 

for j in range(3): 
	q.dequeue() 
print(q) 

for t in range(2): 
	q.enqueue(t) 
print(q) 







