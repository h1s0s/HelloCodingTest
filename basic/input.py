if __name__ == "__main__":
    # input()은 문자열을 입력받는 함수
    n = int(input()) #1, int로 감싸지 않으면 문자열로 받아짐.
    print(n) #1

    # map()은 리스트의 ㅁ든 원소에 각각 특정한 함수를 적용할때 사용
    #공백을 기준으로 구분된 데이터를 입력 받을때는 다음과 같이 사용
    array = list(map(int, input().split())) #1 2 3 4 5
    print(array) #[1,2,3,4,5]

    #공백을 기준으로 데이터의 개수가 많다면
    a, b, c = map(int, input().split())#1 2 3
    print(a)#1
    print(b)#2
    print(c)#3

    print(1, end = " ") #엔터 안함
    print(2, end = " ")