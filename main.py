import tarfile

class Empty(Exception):
  pass

class CircularQueue:
  """This is an implementation of a circularly linked queue"""
  class _Node:
    """A light weight class for repr the element and the reference to the next"""
    def __init__(self,element,next):
      """used to create the Nodes of the queue"""
      self._element = element
      self._next = next

  def __init__(self):
    """non public member data for the queue"""
    self._tail = None
    self._size = 0
  
  def is_empty(self):
    """returns True if the queue is empty"""
    return self._size == 0
  
  def __len__(self):
    return self._size
  
  def dequeue(self):
    """This removes an element from the start of the circular queue
        with the tail as pointer 
    """

    if self.is_empty():
      raise Empty('No Elements')
      # this get the current head and initialize it as the oldhead
    oldhead = self._tail._next
    # if only one member then the next of the tail must point to None
    if self._size == 1:
      self._tail.next = None
    else:
      #otherwise the tail point to the new header 
      self._tail._next = oldhead._next
      self._size -= 1
      return oldhead._element
  
  def enqueue(self,e):
    """This create a new node for the e that was passed as an arg"""

    newest = self._Node(e,None)
    if self.is_empty():
      # empty queue then the newest must point to it self
      newest._next = newest
    else:
      #newest is inserted at the start of the circulation using the tail 
      newest._next = self._tail._next
      #the tail then points to the newest .
      self._tail._next = newest
      #the tail is set to be the newest
    self._tail = newest
    # decrease the size to reflect the change
    self._size += 1
    


    


