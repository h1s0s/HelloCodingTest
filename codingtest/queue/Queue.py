#stack 2개로 queue 구현
class Queue(object):
    def __init__(self):
        self.instack=[] #스택 선언
        self.outstack=[]

    def enqueue(self, element):
        self.instack.append(element) #파이썬의 stack은 pop X -> append
        #시간복잡도는 O(1)

    def dequeue(self):
        if not self.outstack: #outstack이 비어있는지? 비어있으면 True, 비어있지 않으면 Fasle
            while self.instack: #instack에 값이 있으면 True, 없으면 False
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()