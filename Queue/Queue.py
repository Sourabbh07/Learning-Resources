class Queue:
  def __init__(self):
    self.queue=[]

  def Enque(self,item):
    self.queue.append(item)
  
  def Deque(self):
    if len(self.queue) < 1 :
      return None
    else:
      self.queue.pop(0)
  
  def printqueue(self):
    print(self.queue)

q=Queue()
q.Enque(10)
q.Enque(20)
q.Enque(30)
q.printqueue()
q.Deque()
q.printqueue()

'''#Queue:
-------
->Inserted at one end an removed at the another end
->Follows FIFO Order

#drawbacks are 
 ->after we remove an elemnt from the queue the space will be wasted so we use circular queue

#apps
->Cpu scheduling,disk scheduling'''