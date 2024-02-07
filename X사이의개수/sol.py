def solution(myString):
    remove_x = myString.split("x")
    # x를 기준으로 문자열을 나눠준뒤 remove_x로 정의한 후 
    return [len(i) for i in remove_x]
    # len 함수를 사용해 remove_x의 길이를 찾았다.

# 다른사람의 풀이
# def solution(myString):
#     return [len(w) for w in myString.split('x')]

