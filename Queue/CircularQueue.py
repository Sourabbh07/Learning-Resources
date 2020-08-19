'''#Types of queues 
1 -> Circular queues
2 -> Priority queues
3 -> Dequeue'''

class Circular:
  def __init__(self,k):
    self.k=k
    self.queue=[None]*k
    self.head=-1
    self.tail=-1

  def Enqueue(self,data):
    if (self.tail+1) % self.k ==self.head:
      print("Overflow occured in the queue")
    elif self.head==-1:
      self.head=0
      self.tail=0
      self.queue[self.tail]=data
    else:
      self.tail=(self.tail+1)%self.k
      self.queue[self.tail]=data

  def printQ(self):
    for i in range(self.head,self.tail+1):
        print(self.queue[i])

  def Deletequeue(self):
    if self.head==-1:
      print("Queue is Unerflow state")
    if  self.tail==self.head:
      temp=self.queue[self.head]
      self.tail=-1
      self.head=-1
      return temp
    else:
      temp=self.queue[self.head]
      self.head=(self.head+1)%self.k
      return temp


    
q=Circular(3)
q.Enqueue(3)
q.Enqueue(4)
q.printQ()
val=q.Deletequeue()
print(val)
q.printQ()


'''#Conditions to follow 
1-> If Queue is Overflow ie if tail+1==head 
2-> then if queue contains no element add one ie here inceremnt the tail and the head  and add data
3-> If there are elements in the queue then inceremnt the tail mod len of the queue and add the element into the tail

Delete:
1->Check for the Underflow Conition 
2-> Check if only only one elemet to delete
3->check if existting to be deleted '''