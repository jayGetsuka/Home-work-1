class NodeD:
  def __init__(self, data, prevNode, nextNode):
    self.data = data
    self.prevNode = prevNode
    self.nextNode = nextNode

class DoublyLinkedList:
  def __init__(self, data = None):
    self.head = None
    self.tail = None
    self.count = 0
  def addFirst(self, data):
    if self.count == 0:
      self.head = NodeD(data, None, None)
      self.tail = self.head
    elif self.count > 0:
      node = NodeD(data, None, self.head)
      self.head.prevNode = node
      self.head = node
    self.current = self.head
    self.count += 1

  def addLast(self, data):
      if self.count == 0:
        self.addFirst(0)
      else:
        self.tail.nextNode = NodeD(data, self.tail, None)
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
      node = NodeD(data, current, current.nextNode)
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
            
dll = DoublyLinkedList()
dll.addFirst("A")
dll.addFirst("B")
dll.addLast("C")
dll.insertAfter("C", "E")
dll.traverse()
