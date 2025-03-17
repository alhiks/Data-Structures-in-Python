class queue:
    def __init__(self,max):
        self.front,self.rear,self.max=-1,-1,10
        self.arr=[0]*max
    def enqueue(self):
        if self.rear==self.max:
            print("Overflow occurs")
            exit(0)
        elif self.front==self.rear==-1:
            self.front,self.rear=0,0
            self.arr[self.front]=int(input("Enter data element:"))
        else:
            self.rear+=1
            self.arr[self.rear]=int(input("Enter data element:"))
    def dequeue(self):
        if self.rear==self.front==-1:
            print("Underflow occurs")
        elif self.front==self.rear==0:
            print("Deleted element is ", self.arr[self.front])
            self.arr[self.front] = None
            self.front,self.rear=-1,-1
        else:
            print("Deleted element is ",self.arr[self.rear])
            self.arr[self.front]=None
            self.front+=1
    def display(self):
            if self.front==self.rear==-1:
                print("Underflow occurs")
                exit(0)
            else:
                for i in self.arr:
                    if i==0 or i==None:
                        pass
                    else:
                        print("Element:",i)
    def peek(self):
        if self.rear==-1 and self.front==-1:
            print("Underflow occurs")
            exit(0)
        else:
            print("Top most element is ",self.arr[self.front])
q=queue(10)
while True:
    print("1.Enqueue()\n2.Dequeue()\n3.display()\n4.Peak\n5.Exit\n")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        q.enqueue()
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.display()
    elif ch == 5:
        exit(0)
    elif ch == 4:
        q.peek()
    else:
        print("Invalid choice")




