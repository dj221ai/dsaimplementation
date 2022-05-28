# create nodes
# create linkedlist
# add nodes to linked list
# print linked list

# Every node has data and next field, where data is the data we want to store and next stores the address of another node


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        # print(self.data, self.next, "nodes created ")


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    #check length if list
    def lengthofList(self):
        curNode = self.head
        length = 0

        while curNode is not None:
            length += 1
            curNode = curNode.next
        return length

    #checking if list is empty
    def isEmptyList(self):
        if self.head is not None:
            return True
        else:
            return False


    # insertion of nodes from here
    def insertAtEnd(self, new_node):
        if self.head is None:
            self.head = new_node

        else:
            tempNode = self.head
            # print(tempNode.data, "temp")

            while tempNode.next is not None:
                tempNode = tempNode.next
            tempNode.next = new_node

    # insertion at head
    def insertAtHead(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            tempNode = self.head
            self.head = newNode
            newNode.next = tempNode
            del tempNode

    # insertion in between
    def insertInBetween(self, newNode, indexVal):
        #check invalid
        if indexVal < 0 or indexVal > self.lengthofList():
            print(f"invalid postion! for {newNode.data}. please enter correct position value!!")
        
        # call insertAtEnd when index is last index
        elif indexVal == self.lengthofList():
            self.insertAtEnd(newNode)
            return

        # call insertAthead when index is 0
        elif indexVal == 0:
            self.insertAtHead(newNode=newNode)
        else:
            curNode = self.head
            counter = 0
            while counter <= indexVal:
                if counter == (indexVal - 1):
                    tempNode = curNode
                if counter == indexVal:
                    tempNode.next = newNode
                    newNode.next = curNode
                counter += 1
                curNode = curNode.next

    # delettion of nodes from here

    # deleting node at end
    def deleteAtEnd(self):
        if self.isEmptyList() is True:
            # checking if list has only one node
            if self.head.next is None:
                self.deleteAtHead()
                return
            curNode = self.head
            while True:
                if curNode.next is None:
                    prevNode.next = None
                    del curNode
                    return
                prevNode = curNode
                curNode = curNode.next
        else:
            print("list is empty can't delete End Node!!")

        # while curNode.next is not None:
        #     prevNode = curNode
        #     curNode = curNode.next
        # prevNode.next = None
        # del curNode

    # deleting node at head or deleting the first node
    def deleteAtHead(self):
        if self.isEmptyList() is True:
            curNode = self.head
            self.head = curNode.next
            del curNode
        else:
            print("List is Empty can't delete Head Node")

    # deleting between nodes
    def deleteInBetween(self, indexVal):
        if indexVal < 0 or indexVal > self.lengthofList():
            print("Invalid position provided!!")
            return
        elif indexVal == 0:
            self.deleteAtHead()
            return
        else:
            counter = 0
            curNode = self.head
            while counter <= indexVal:
                if counter == indexVal:
                    prevNode.next = curNode.next
                    curNode.next = None
                    break
                prevNode = curNode
                curNode = curNode.next
                counter += 1






    def printlist(self):
        if self.head is None:
            print("list is empty!!!")
        curNode = self.head

        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next


    
            
        

firstNode = Node("Node 1")
secNode = Node("Node 2")
thirdNode = Node("Node 3")
fourthNode = Node("Node 4")
fifthNode = Node("Node 5")
sixthNode = Node("Node 6")
seventhNode = Node("Node 7")
eighthNode = Node("Node 8")
llobj = LinkedList()
llobj.insertAtHead(thirdNode)
llobj.insertAtEnd(firstNode)
llobj.insertAtEnd(secNode)
llobj.insertAtHead(fourthNode)
llobj.insertInBetween(fifthNode, 4)
llobj.insertInBetween(sixthNode, 1)
llobj.insertInBetween(seventhNode, 0)
llobj.insertInBetween(eighthNode, 3)
print("before deleting ")
llobj.printlist()
llobj.deleteAtEnd()
llobj.deleteAtHead()
print("After deleting ")
llobj.deleteInBetween(0)
llobj.deleteInBetween(4)
llobj.printlist()
