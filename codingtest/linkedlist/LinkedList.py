from codingtest.linkedlist.Node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    #insert_back
    def append(self, value):
        new_node = Node(value)
        # self.head = new_node
        if self.head is None:
            self.head = new_node
        #맨 뒤의 node가(생성되는 노드 앞에 것) new_node를 가리켜야한다
        else:
            current = self.head
            #순차적으로 이동해 마지막 노드로 가기 위한, current를 생성하였음(링크드리스트의 특징임)
            while(current.next):#커렌트.next가 none이면 끝남
                current = current.next
            current.next = new_node
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    #insert_at 중간 삽입
    def insert(self, idx, value):
        new_node = Node(value)
        if idx == 0: #0번째 idx면
            new_node_next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.next #next address로 다음 노드로 한번씩 이동함
            new_node.next = current.next
            current.next = new_node

    #remove_at
    def delete(self, idx):
        if idx == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next  # next address로 다음 노드로 한번씩 이동함
            current.next = current.next.next

    #insert_back tail버전 시간복잡도 O(1)
    #링크드리스트는 정말 다양한 구현법이 있으니, 잘 활용해보자
    #링크드리스트는 자주 등장하는 자료구조는 아니지만
    #트리나 그래프 등을 구현할때 이 개념을 잘 공부해둬야 편함
    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

