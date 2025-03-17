class stack:
    def __init__(self,max):
        self.top=-1
        self.max=max
        self.arr=[0]*max
        #### pushing elements into stack
    def push(self):
        if self.top==self.max:
            print("Sorry you cant push elements in stack")
            exit(0)
            # self.top+=1
            # self.arr[self.top]=(int(input("Enter data element:")))
        else:
            self.top+=1
            self.arr[self.top] = (int(input("Enter data element:")))
            ####  poping out elements from stack
    def pop(self):
        if self.top==-1:
            print("underflow occurs")
            exit(0)
        else:
            print("Deleted element is ",self.arr[self.top])
            self.arr[self.top]=None
            self.top-=1

    def pip(self):
        if self.top==-1:
            print("underflow occurs")
            exit(0)
        else:
            for i in self.arr:
                if i==0 or i==None:
                    pass
                else:
                    print("Element:",i)
    def peek(self):
        if self.top==-1:
            print("Underflow occurs")
        else:
            print("Top most element is ",self.arr[self.top])

s=stack(5)
while True:
    print("1.Push()\n2.Pop()\n3.Pip()\n4.Peak\n5.Exit\n")
    ch=int(input("Enter your choice:"))
    if ch==1:
        s.push()
    elif ch==2:
        s.pop()
    elif ch==3:
        s.pip()
    elif ch==5:
        exit(0)
    elif ch==4:
        s.peek()
    else:
        print("Invalid choice")
