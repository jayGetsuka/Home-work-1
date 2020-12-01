class Node: 
  #constructor to initialize the node object
  def __init__(self, data = None, next_node = None): 
    self.data = data 
    self.next_node = next_node 
    self.data = data 
    
  def get_data(self): 
    return self.data 

  def set_next(self,new_next): 
    self.next_node = new_next 
  #method for getting the next field of the node 
  def get_next(self): 
    return self.next_node 
  #returns true if the node points to another node 
class SinglyLinkedList:
    #constructor to initialize the Linked List object with a single head node
    def __init__(self, head=None):
        self.head = head
        self.size = 0
    def traverse(self):
        curr = self.head
        while curr:
             print(curr.data, end=" ")
             curr = curr.get_next()
    def insertAfter(self, prev_node, new_data):
        n = self.head
        while n is not None:
              if n.data == prev_node:
                  break
              n = n.next_node
        if n is None: 
          print("The given previous node not in LinkedList.")
          return
        new_node = Node(new_data)
        new_node.next_node = n.next_node
        n.next_node = new_node
    def addFisrt(self,newdata):
        NewNode = Node(newdata)
        NewNode.next_node = self.head
        self.head = NewNode
    def addEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next_node):
            laste = laste.next_node
        laste.next_node=NewNode

    def delete(self, data):
      current = self.head
      previous = None
      found = False
      while current and found is False:
        if current.get_data() == data:
            found = True
        else:
          previous = current
          current = current.get_next()
        if current is None:
          raise ValueError("Data not  in list")
        if previous is None:
          self.head = current.get_next()
        else:
          previous.set_next(current.get_next())

mysll = SinglyLinkedList()
mysll.addFisrt(10)
mysll.addFisrt(20)
mysll.addFisrt(30)
mysll.insertAfter(10, 15)
mysll.delete(20)
mysll.addEnd(40)
mysll.traverse()
