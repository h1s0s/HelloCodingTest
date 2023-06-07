if __name__ == "__main__":
    #표준 라이브러리

    #1. 내장함수 : 기본 입출력 함수부터 정렬함수까지 기본적인 함수

    #sum()
    print(sum([1, 2 ,3])) #튜플은 안되고 리스트만 가능한듯?

    #min(), max()
    print(min(1, 2, 3))
    print(max(1, 2, 3))
    #eval() 수식을 계산해줌
    print(eval("(3+5)*7"))

    #sorted()
    print(sorted([9 , 1, 8, 5, 4]))
    print(sorted([9 , 1, 8, 5, 4], reverse=True))

    #sorted() with key
    array = [('홍길동', 35), ('이순신', 75)]
    print(sorted(array, key=lambda x: x[1], reverse=True)) #2번쨰 원소를 기준으로 정렬

    #==============================================================================================================================================

    #2. itertools : 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공

    #순열 : 서로다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것, {'A', 'B', 'C'}에서 3개를 선택해 나열하는 경우 : 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
    from itertools import permutations
    from itertools import product
    print(list(permutations(['A', 'B', 'C'], 3))) #모든 순열 구하기
    print(list(product(['A', 'B', 'C'], repeat=3))) #중복 순열 구하기

    #조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
    from itertools import combinations
    from itertools import combinations_with_replacement
    print(list(combinations(['A', 'B', 'C'], 2))) # 2개를 뽑는 모든 조합 구하기
    print(list(combinations_with_replacement(['A', 'B', 'C'], 2)))  # 중복 조합 구하기

    # ==============================================================================================================================================

    #3. heapq : 힙 자료구조 제공
    #우선순위 큐 구현시 사용

    # ==============================================================================================================================================

    #4. bisect : 이진탐색 기능 제공

    # ==============================================================================================================================================

    #5. collections : 덱, 카운터 등 포함

    #Counter : 등장 획수를 세는 기능
    from collections import Counter

    counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
    print(counter['blue'])#블루 등장 횟수
    print(counter['red'])#레드 등장 횟수
    print(dict(counter))#딕셔너리로 변환
    print(counter)

    # ==============================================================================================================================================

    #6. math : 필수적인 수학적 기능

    #팩토리얼, 제곱근, 최대공약수, 삼각함수 관련부터, 파이같은 상수 포함

    #최대공약수 gcd()
    import math
    a = 21
    b = 14
    print(math.gcd(a,b)) #최대 공약수 7
    print(a*b//math.gcd(a,b))#최소 공배수 42