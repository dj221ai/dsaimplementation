class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircluarSinglyLL:
    def __init__(self):
        self.head = None

    def insertEnd(self, newnode):
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
            return
        else:
            curnode = self.head
            while curnode.next is not self.head:
                curnode = curnode.next
            curnode.next = newnode
            newnode.next = self.head

    def insertHead(self, newnode):
        curnode = self.head
        while curnode.next is not self.head:
            curnode = curnode.next
        newnode.next = self.head
        curnode.next = newnode

    def deleteEnd(self):
        curnode = self.head
        while curnode.next is not self.head:
            prevnode = curnode
            curnode = curnode.next
        curnode.next = None
        prevnode.next = self.head

    def deleteHead(self):
        lastnode = self.head
        while lastnode.next is not self.head:
            lastnode = lastnode.next
        prevhead = self.head
        self.head = self.head.next
        lastnode.next = self.head
        prevhead.next = None



    def printList(self):
        if self.head is None:
            print("List is Empty")
            return
        else:
            curnode = self.head
            while True:
                print(curnode.data)
                if curnode.next is self.head:
                    break
                curnode = curnode.next
            curnode = curnode.next
            print(curnode.data)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
cll = CircluarSinglyLL()
cll.insertEnd(node1)
cll.insertEnd(node2)
cll.insertEnd(node4)
cll.insertHead(node3)
# cll.deleteEnd()
cll.deleteHead()
cll.printList()
