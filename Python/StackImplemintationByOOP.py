class Stack:

	def __init__(self):
	 	self.stack = []

	def push(self,item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def is_empty(self):
		if self.stack == []:
			return True
		else:
			return False

	def __str__(sel
		st=''
		for i in self.stack:
			st=st+' '+str(i)
		return  st[1:]


stack=Stack()
n = int(input())
for i in range(n):	
	choice=input().split()

	if choice[0]=='Push':
		stack.push(int(choice[1]))

	elif choice[0]=='Pop':
		if stack.is_empty():
			continue
		else:
			stack.pop()

	elif choice[0]=='Output':
		print(stack)

