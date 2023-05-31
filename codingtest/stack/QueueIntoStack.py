class Stack(object):
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, element):#시간복잡도는 O(1)
        self.q1.put(element) #q1에 담음

    def pop(self):#q1에 있는 n개의 원소들 중 n-1개를 q2에 옮겨야 하므로 O(n)의 시간복잡도를 가짐
        while self.q1.qsize() > 1: #1개가 남을때까지
            self.q2.put(self.q1.get()) #enqueue가 get(), inqueue가 put()

        #q1과, q2의 변수이름을 바꿈
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

        return self.q2.get()