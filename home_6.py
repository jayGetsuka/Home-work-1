class Node1:
  def __init__(self, data, prevNode, nextNode):
    self.data = data
    self.prevNode = prevNode
    self.nextNode = nextNode
  # Delete a node at front
class DoublyLinkedList:
  def __init__(self, data = None):
      self.head = None
      self.tail = None
      self.count = 0
  def addFirst(self, data):
    if self.count == 0:
      self.head = Node1(data, None, None)
      self.tail = self.head
    elif self.count > 0:
      node = Node1(data, None, self.head)
      self.head.prevNode = node
      self.head = node
    self.current = self.head
    self.count += 1

  def addLast(self, data):
      if self.count == 0:
        self.addFirst(0)
      else:
        self.tail.nextNode = Node1(data, self.tail, None)
        self.tail = self.tail.nextNode
        self.count += 1
  def insertAfter(self, prev_node, data):
      current = self.head
      while current is not None:
            if current.data == prev_node:
               break
            current = current.nextNode # now current is prev_node
      # 1. check if the given prev_node (current) is NULL
      if current is None:
         print("This node doesn't exist in DLL")
         return
      # 2. allocate node & 3. put in the data
      # 4. Make prev_node as previous of new_node
      # 5. Make next of new node as next of prev_node
      node = Node1(data, current, current.nextNode)
      # 6. Make the next of prev_node as new_node
      current.nextNode = node
      # 7. Change previous of new_node's next node
      if node.nextNode is not None:
         node.nextNode.prevNode = node
  def traverse(self):
      curr = self.head
      while curr:
            print(curr.data)
            curr = curr.nextNode

  def deleteFirst(self):
    if self.head is None:
      print("The list has no element to delete")
      return
    if self.head.nextNode is None:
      self.head = None
      return
    self.head = self.head.nextNode
    self.prevNode = None

  def deleteLast(self):
    if self.head is None:
       print("The list has no element to delete")
       return
    if self.head.nextNode is None:
       self.head = None
       return
    current = self.head
    while current.nextNode is not None:
        current = current.nextNode
    current.prevNode.nextNode = None

  def delete(self, value):
        # Delete a specific item
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False

        elif current.data == value:
            self.head = current.nextNode
            self.head.prevNode = None
            node_deleted = True

        elif self.tail.data == value:
            self.tail = self.tail.prevNode
            self.tail.nextNode = None
            node_deleted = True

        else:
            while current:
                if current.data == value:
                   current.prev.nextNode = current.nextNode
                   current.next.prevNode = current.prevNode
                   node_deleted = True
                current = current.nextNode

        if node_deleted:
            self.count -= 1

dll2 = DoublyLinkedList()
dll2.addFirst("A")
dll2.addFirst("B")
dll2.addFirst("C")
dll2.insertAfter("C", "F")
print("Before:")
dll2.traverse()
dll2.deleteFirst()
dll2.deleteLast()
dll2.delete("F")
print()
print("After: ")
dll2.traverse()