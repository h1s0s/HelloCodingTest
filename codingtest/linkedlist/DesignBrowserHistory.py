from codingtest.linkedlist.Node import Node


class DesignBrowserHistory(object):
    def __init__(self):
        self.head = None
        self.tail = None

    #호출시 브라우저는 homepage에서 시작, None을 리턴
    def BrowserHistory(self, url):
        new_page = Node(url)
        if self.head is None:
            self.head = new_page
            self.tail = new_page
        else:
            self.tail.next = new_page
            self.tail = self.tail.next
        return None

    #호출시 현재 page의 앞에있는 페이지는 다 삭제되고, url로 방문(리스트에 추가)
    def visit(self, url):
        new_page = Node(url)
        self.head = new_page
        self.tail = new_page
        return None

    #steps 수만큼 뒤로가기, 뒤로가기를 할 수 있는 page수가 x이고 step > x면 x번만큼만 뒤로가기.
    #뒤로가기가 완료하면 현재 url을 리턴한다
    def back(self, steps):
        if self.head is None:
            return None
        else:
            current = self.head
            for _ in range(steps):


            #연결리스트에서 전체갯수를 구할 수 있나?