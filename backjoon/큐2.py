
if __name__ == "__main__":
    N = int(input()) #입력횟수
    list = list()
    for _ in range(N):
        i = input()
        if i == "pop":
            if len(list) == 0:
                print("-1")
            else :
                print(list.pop(0))
        elif i == "size":
            print(len(list))
        elif i == "empty":
            word = 1 if len(list) == 0 else 0
            print(word)
        elif i == "front":
            if len(list) == 0:
                print("-1")
            else:
                print(list[0])
        elif i == "back":
            if len(list) == 0:
                print("-1")
            else:
                print(list[len(list)-1])
        else:
            value = i.split()
            list.append(value[1])
