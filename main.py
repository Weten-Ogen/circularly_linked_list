import tarfile

class Empty(Exception):
  pass

class CircularQueue:
  """This is an implementation of a circularly linked queue"""
  class Node:
    """A light weight class for repr the element and the reference to the next"""
    def __init__(self,element,next):
      self._element = element
      self._next = next

  def __init__(self):
    self._tail = None
    self._size = 0
  
  def is_empty(self):
    return self._size == 0
  
  def __len__(self):
    return self._size
  
  def dequeue(self):

    if self.is_empty():
      raise Empty('No Elements')
    oldhead = self._tail._next
    if self._size == 1:
      self._tail.next = None
    else:
      self._tail._next = oldhead._next
    


