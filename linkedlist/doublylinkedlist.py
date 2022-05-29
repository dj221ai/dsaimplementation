class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def checkLength(self):
        currnode = self.head
        length = 0

        while currnode is not None:
            length += 1
            currnode = currnode.next
        print("length is ", length)
        return length
    
    def isEmpty(self):
        if self.head is not None:
            return True
        else:
            return False



    def insertAtEnd(self, newnode):
        if self.head is None:
            self.head = newnode
            return
        else:
            currnode = self.head
            while currnode.next is not None:
                currnode = currnode.next
            currnode.next = newnode
            newnode.previous = currnode
            newnode.next = None

    def insertAtHead(self, newnode):
        if self.head is None:
            self.head = newnode
            return
        else:
            currnode = self.head
            if self.head.previous is None:
                self.head = newnode
                newnode.next = currnode
                currnode.previous = newnode
                newnode.previous = None

    def insertInBetween(self, newnode, posval):
        if posval < 0 or posval > self.checkLength():
            print(f"Invalid postion value for {newnode.data} please check")
            return
        elif posval == 0:
            self.insertAtHead(newnode=newnode)
            return
        elif posval == self.checkLength():
            self.insertAtEnd(newnode=newnode)
            return
        else:
            currnode = self.head
            counter = 0
            while True:
                if counter == posval:
                    currnode.previous.next = newnode
                    newnode.previous = currnode.previous
                    newnode.next = currnode
                    currnode.previous = newnode
                    return
                currnode = currnode.next
                counter += 1

                

    def printDLL(self):
        if self.head is None:
            print("List is Empty ")
            return
        else:
            currnode = self.head
            print("begining to end >>> ")
            while currnode is not None:
                print(currnode.data)
                if currnode.next is None:
                    reversalnode = currnode
                currnode = currnode.next

            print("from end in reverse >>> ")
            while reversalnode is not None:
                print(reversalnode.data)
                reversalnode = reversalnode.previous





node1 = Node('node 1')
node2 = Node('node 2')
node3 = Node('node 3')
node4 = Node('node 4')
node5 = Node('node 5')
dll = LinkedList()
dll.insertAtHead(node1)
# dll.insertAtEnd(node2)
dll.insertAtEnd(node3)
dll.insertInBetween(node2, 1)
# dll.insertAtHead(node4)
# dll.insertAtHead(node5)
dll.printDLL()
