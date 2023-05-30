#stack 2개로 queue 구현
class Queue(object):
    def __init__(self):
        self.instack=[] #스택 선언
        self.outstack=[]

    def enqueue(self, element):
        self.instack.append(element) #파이썬의 stack은 pop X -> append

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()