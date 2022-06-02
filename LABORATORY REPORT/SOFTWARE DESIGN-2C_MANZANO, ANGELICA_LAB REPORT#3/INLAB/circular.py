class Node:
 
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class LinkedList:
 
  def __init__(self):
    self.head = None


  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (True):
        print(temp.data, end=" ")
        temp = temp.next
        if(temp == self.head):
          break
      print()
    else:
      print("The list is empty.")


MyList = LinkedList()


first = Node(10)

MyList.head = first

first.next = MyList.head 
MyList.head.prev = first


second = Node(20)

second.prev = first
first.next = second

second.next = MyList.head 

MyList.head.prev = second

third = Node(30)

third.prev = second
second.next = third

third.next = MyList.head 

MyList.head.prev = third


MyList.PrintList()