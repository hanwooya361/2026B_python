# 217p. 딕셔너리
# 딕셔너리란? {}중괄호 선언하고 키:값 형태로 쉼표로 연결
# {Key:value, Key:value, Key:value}
# Key중복x / value 중복o

# 1. 선언
dict_a = {'name':'어벤져스 엔드게임', 'type':'영화'}
# 2. 값 호출, 딕셔너리명['key']
print(dict_a['name'])
print(dict_a['type'])
# 3. 속성값추가, 딕셔너리명[새로운key] = 새로운값
dict_a['price'] = 5000
print(dict_a)
# 4. 속성값 수정
dict_a['type'] = '호러 무비'
print(dict_a)
# 5. 속성값 삭제, del 딕셔너리['key']
del dict_a['price']
print(dict_a)
# 6. 딕셔너리내부확인 , 찾을키 in 딕셔너리명
print('price' in dict_a)    # False
print('name' in dict_a)     # True
# 7. 속성값 호출, 방법1: 딕셔너리명['key'], 방법2: 딕셔너리명.get(key)
# 차이점: 방법1은 존재하지않으면 예외발생, 방법2는 존재하지 않으면 None반환
print(dict_a.get('name'))
print(dict_a.get('price'))  # None
# 8. for반복문과 딕셔너리, 딕셔너리내 key 하나씩 for에서 순회
# for key 반복변수 in 딕셔너리명 :
#       실행코드
for key in dict_a :
    print(dict_a.get(key))
    print(dict_a[key])