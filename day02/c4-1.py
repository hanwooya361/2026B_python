# 192p.
# 리스트란? 대괄호[]에 자료를 쉼표로 구분해 여러 자료들을 저장
# [요소, 요소, 요소] , 요소element
# 인덱스란? 리스트내 요소들이 저장된 순서번호 , 0번시작~

#
list_a = [273 , 32, 103, "문자열", True, False]
print([list_a[2]])
print(list_a[1:3])
list_a[2] = 7
print(list_a[2])
print(list_a[-2])
print(list_a[3][1])
# print(list_a[1][1]) # 오류, 리터럴/1차원값
list_1 = [1,2,3] # 1차원
list_2 = [[1,2], [3,4], [5,6]] # 2차원
print(list_2[1][0]) # 3 , [행][열] => 판다스/데이터

# 196p.
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a + list_b) # 리스트 + 리스트 => 연결
print(list_a * 3)
print(len(list_a)) # 3
list_aa = [[1], [2], [3]]
print(list_a + list_aa)
list_a.append(4)
print(list_a)
list_a.insert(0,5)
print(list_a)

# 주의할점
list_c = [1,2]
list_c + [3]        # 방법1] [1,2,3] 새로운리스트 생성
list_c.append(3)    # 방법2] [1,2,3] 기존리스트 더함

# 202p. 요소삭제하기
list_a = [1,2,3,4,5]
del list_a[1]   # 1번 인덱스 삭제
print(list_a)   # [1,3,4,5]
list_a.pop(2)   
print(list_a)   # [1,3,5]
del list_a[0:2] # 슬라이싱 삭제 0~1까지
print(list_a)   # [5]
# 리스트명.remove(값) , 값 삭제
list_a.remove(5)    # 5값 삭제
# 리스트명.clear() , 전체삭제
list_a.clear()

# 204p. 슬라이싱 , [시작인덱스 : 끝인덱스 : 단계]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0:5:2])  # 0번부터 5-1번까지 2씩 증가 [1,3,5]
print(numbers[ : : -1]) # 시작인덱스 생략시 0, 끝인덱스 생략시 마지막인덱스 , -1

# 205p. 정렬 , 리스트명.sort(), 리스트명.sort(reverse=True)
list_e = [52, 273, 103, 32, 275, 1, 7] 
list_e.sort()
print(list_e)   # [1, 7, 32, 52, 103, 273, 275]
list_e.sort(reverse=True)
print(list_e)   # [275, 273, 103, 52, 32, 7, 1]

# 206p. 내부확인 , 찾을값 in 리스트
print(52 in list_e)         # True
print(51 in list_e)         # False
print(52 not in list_e)     # True -> False
print(51 not in list_e)     # False -> True
# 208p. 리스트와반복문, 리스트내 요소들이 순차적인 인덱스 구조
# for 반복변수 in 반복가능한 자료 :
#       실행코드
for i in list_e :
    print(i)
for char in "안녕하세요" :  # 문자열도 리스트/배열이다.
    print(char)
