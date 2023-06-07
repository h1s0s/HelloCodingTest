if __name__ == "__main__":
    a = list()
    b = [1, 2, 3]
    c = "1 2 3"
    d = list(c.split())#문자열 리스트로 변환

    print(d)
    print(b[-1]) #음수 인덱싱
    print(b[0:3]) #슬라이싱

    #리스트 컴프레싱
    print([i for i in range(10)]) #[0,1,2,3,4,5,6,7,8,9]
    print([i for i in range(10) if i % 2 == 0]) #[0,2,4,6,8]

    #2차원 배열 생성
    n = 3 #배열 갯수
    m = 2 #요소 갯수
    print([[0] * m for _ in range(n)]) #i가 필요 없을때 _로 비워놔도 됨, 0으로 고정

    #메서드
    a.append(1) #리스트에 원소 삽입, O(1)
    a.sort() #리스트 오름차순 정렬, O(NlogN)
    a.sort(reverse=True) #내림차순 정렬
    a.reverse() #O(N) 순서를 모두 뒤집음
    a.insert(3, 1) #O(N) 3번째에 1을 삽입
    a.count(3) #O(N)해당 요소의 개수를 count
    a.remove(3) #O(N) 특정 값을 갖는 요소를 삭제(단일)

    #특정 값을 가지는 원소 모두 제거
    p = [1,2,3,4,5,5,5]
    remove_set = {3, 5} #집합 자료형
    result = [i for i in a if i not in remove_set] #not in이라는 연산자를 활용해 새로운 리스트로 옮김 O(n)

