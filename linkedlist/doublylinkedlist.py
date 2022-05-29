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

    #deletion starts from here

    #delete at end
    def deleteAtEnd(self):
        if self.isEmpty() is not True:
            return
        # checking if list has only one node
        elif self.head.next is None:
            print("head next is none")
            self.deleteAtHead()
            return
        else:
            currnode = self.head
            while True:
                if currnode.next is None:
                    currnode.previous.next = None
                    # del currnode
                    break
                currnode = currnode.next

    #delete at head
    def deleteAtHead(self):
        if self.isEmpty() is True and self.head.next is not None:
            self.head = self.head.next
            self.head.previous.next = None
            self.head.previous = None
            return
        elif self.isEmpty() is True and self.head.next is None:
            del self.head
            return
        else:
            print("List is Empty can't delete Head Node")


    #delete in between
    def deleteInBetween(self, posval):
        if posval < 0 or posval > self.checkLength():
            print("Invalid position provided can't delete")
            return
        elif posval == 0:
            self.deleteAtHead()
            return
        else:
            curnode = self.head
            counter = 0
            while True:
                if counter == posval:
                    curnode.previous.next = curnode.next
                    curnode.next.previous = curnode.previous
                    break
                curnode = curnode.next
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
node6 = Node('node 6')
node7 = Node('node 7')
node8 = Node('node 8')
dll = LinkedList()
dll.insertAtHead(node1)
dll.insertAtEnd(node3)
dll.insertInBetween(node2, 1)
dll.insertAtHead(node4)
dll.insertAtEnd(node5)
dll.insertAtEnd(node6)
print("before deleting >>>>>>>>>>>>>>>>")
dll.printDLL()
dll.deleteAtEnd()
dll.deleteAtHead()
dll.deleteInBetween(0)
print("After deleting >>>>>>>>>>>>>>>>")
dll.printDLL()
