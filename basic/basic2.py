def main():
    #정수형 변수
    watch = 100000
    print(watch)

    #실수형 변수
    float = 1.1
    print(float)

    print(watch * float)

    #문자열 변수
    string1 = "hello"
    string2 = 'python'
    multiString = """Hello,
    Python"""#여러줄 문자
    print(multiString)
    print(string1 + ' ' + string2)

    #불리언 변수 선언
    isTrue = True
    isFalse = False
    #다른 언어와 다르게 true, false의 첫글자를 대문자로 표기함

    print('===========리스트')
    #리스트 자료형
    list1 = [1,2,3,4,5]
    list2 = ['apple','banana','cherry']
    list3 = [1,'hello',True,3.14]
    list2.append('lemon')
    print(list1)
    print(list2)
    print(list3)

    print('===========세트')
    #세트 자료형
    set1 = {1,2,3,4,5}
    set2 = {'apple', 'banana'}
    print(set1)
    print(set2)

    print('===========딕셔너리')
    #딕셔너리 자료형
    dict1 = {'name':'John', 'age':30}
    print(dict1)
if __name__ == "__main__":
    main()