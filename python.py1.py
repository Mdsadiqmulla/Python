/
# for i in range(1,6):
#     for j in range(1,6):
#         print()
#         print("\n")
#
# n = int([6,5,84,10,37,45,5])
# for i in range(n):
#     for j in range(n-i-1):
#         if(l[j]>l[j+1]):
#             l[j],l[j+1] = l[j+1],l[j]
# print(sort,l)


class Queue:
    def __init__(self):
        self.q=[]
        self.front=-1
        self.rear=-1

    def enqueue(self,ele):
        if(self.front==-1):
            self.front=self.front+1
            self.rear=self.rear+1
        else:
            self.rear=self.rear+1
            self.q.append(ele)

    def dequeue(self):
        self.front=self.front+1

obj=Queue();
obj.enqueue(1);
obj.enqueue(5);
obj.enqueue(5);
obj.dequeue();
obj.dequeue()
obj.dequeue()
print(obj.q,obj.front,obj.rear);
