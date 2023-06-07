if __name__ == "__main__":
    #딕셔너리(사전 자료형)은 키와 값의 쌍을 데이터로 가지는 자료형
    #변경 불가능한 자료형
    #파이썬의 딕셔너리는 해시 테이블을 이용하므로 조회, 수정에 있어 O(1)의 시간에 처리 가능

    data = dict() #초기화
    b = {
        '홍길동': 99,
        '홍길동2': 100,
    }
    data['사과'] = 'Apple' #key에 값을 넣는 코드임, key가 겹칠경우 덮어 씌워지니 주의
    data['바나나'] = 'banana'
    data['코코넛'] = 'Coconut'

    if '사과' in data: #in 연산자를 통해 존재하는지 확인 가능. 파이썬에서 제공하는 엄청난 기능임
        print("'사과'를 키로 가지는 데이터가 존재합니다")

    #관련 메서드
    print(data.keys()) #키만 뽑아냄

    print(data.values()) #밸류만 뽑아냄

    key_list = data.keys()
    for key in key_list:
        print(data[key]) #이렇게 활용 가능
