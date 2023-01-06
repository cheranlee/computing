
# replacement
# removing at the beginning
# removing anywhere
# removing at the end


class Node:
    def __init__(self, data, nextNode):
        self._data = data
        self._nextNode = nextNode

    def setData(self, data):
        self._data = data

    def getData(self):
        return self._data

    def setNext(self, nextNode):
        self._nextNode = nextNode

    def getNext(self):
        return self._nextNode

    def __str__(self):
        if self.getNext():
            return "Data: {} \t Next: {}".format(self.getData(), self.getNext().getData())
        else:
            return "Data: {} \t Next: {}".format(self.getData(), self.getNext())

class SingleLinkedList():
    def __init__(self):
        self._head = None

    # tells if it is empty
    def isEmpty(self):
        return not self._head

    # returns size
    def size(self):
        probe = self._head
        size = 0
        while probe != None:
            size += 1
            probe = probe.getNext()
        return size

    # appends to the back
    def append(self, data):
        if self._head:
            probe = self._head
            while probe.getNext() != None:
                probe = probe.getNext()
            probe.setNext(Node(data, None))
        else:
            self._head = Node(data, None)

    # index starts from 1
    def insert(self, index, newData):
        probe = self._head

        # insert at the beginning
        if index == 1:
            probe = self._head
            self._head = Node(newData, probe)

        # insert anywhere else
        else:
            for i in range(index-2):
                probe = probe.getNext()
            probe.setNext(Node(newData, probe.getNext()))

    def pop(self):
        probe = self._head
        while probe != None:
            if probe.getNext().getNext() != None:
                probe = probe.getNext()
            else:
                probe.setNext(None)

    def remove(self, index):
        if index == 1:
        	tempdata = self._head.getData()  
        	self._head = self._head.getNext() 

        else: 
        	probe = self._head 
        	for i in range(index-2): 
        		probe = probe.getNext() 
        	tempdata = probe.getNext().getData() 
        	probe.setNext(probe.getNext().getNext())
        return tempdata

    def find(self, val): 
    	probe = self._head 
    	found = False 
    	count = 1
    	while probe != None and found != True: 
    		if probe.getData() != val: 
    			probe = probe.getNext() 
    			count += 1 
    		else: 
    			found = True
    	if found: 
    		return count 
    	else: 
    		return "ERROR VALUE NOT IN LIST"

    def replace(self, target, newVal): 
   		probe = self._head 
   		while probe != None and probe.getData() != target: 
   			probe = probe.getNext() 
   		if probe: 
   			probe.setData(newVal) 
   		else: 
   			return "ERROR TARGET NOT FOUND"

    # traversal and print the whole linked list
    def __str__(self):
        probe = self._head 
        retv = ''
        while probe.getNext() != None:
            retv += '\n' + probe.__str__()
            probe = probe.getNext()
        retv += '\n' + probe.__str__() 
        return retv

x = SingleLinkedList()
for i in range(1, 6):
    x.append(i)
print(x)

print('\n') 
y = x.remove(5)
print(y)
print(x)

print('\n') 
x.insert(3, 3)
print(x)

print('\n') 
h = x.find(7)
print(h)

print('\n')
x.replace(3, 7)
print(x) 

