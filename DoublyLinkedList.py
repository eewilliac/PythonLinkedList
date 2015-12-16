from Node import Node

class LinkedList:
	def __init__(self):
		self._header=Node(None,None,None)
		self._trailer=Node(None,None,None)
		self._header.next=self._trailer
		self._trailer.prev=self._header

	def add(self,data):
		newNode=Node(data,None,None)
		frontNode=self._header
		backNode=frontNode.next
		frontNode.next=newNode
		backNode.prev=newNode
		newNode.prev=frontNode
		newNode.next=backNode

	def display(self):
		aNode=self._header
		while(aNode.next is not None):
			print (aNode.data)
			aNode=aNode.next

if __name__=='__main__':
	ll=LinkedList()
	ll.add("Ettienne")
	ll.add("Aida")
	ll.add("Aida Pauline")
	ll.add("lolita")

	ll.display()			
