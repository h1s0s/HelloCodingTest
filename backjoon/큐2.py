
if __name__ == "__main__":
    N = input() #입력횟수
    A = list(map(int, input().split()))
    list = list()
    for i in range(len(A)):
        if i == "pop":
            if len(list) == 0:
                print("-1")
            else :
                list.pop(0)
        elif i == "size":
            print(list.size)
        elif i == "empty":
            word = 1 if len(list) == 0 else 0
            print(word)
        elif i == "front":
            print("a")
        elif i == "back":
            print("a")
        else:
            value = i.split()
            list.append(value[2])
