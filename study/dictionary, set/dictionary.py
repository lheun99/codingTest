dictionary = {'이름': '홍길동', '학번': 20201001,
              '학년': 2, '전공': '통계학과', '부전공': '영어영문학'}
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('전공' in dictionary)  # True
print(9 in list)  # True


cabinet = {3: "태연", 100: "수영"}  # key:3 , value:태연

print(cabinet[3])  # 태연
print(cabinet.get(3))  # 태연

# print(cabinet[5]) 오류 프로그램 종료
print(cabinet.get(5))  # none + 계속 진행
print(cabinet.get(5), "사용 가능")  # none대신 사용가능 출력?

# 캐비넷 확인
print(3 in cabinet)  # True
print(5 in cabinet)  # False

cabinet = {"A-3": "태연", "B-100": "수영"}  # string도 가능
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
cabinet["C-20"] = "서현"
cabinet["D-52"] = "유리"
cabinet["A-3"] = "윤아"  # 이미 있으면 UPDATE
print(cabinet)  # {'A-3': '윤아', 'B-100': '수영', 'C-20': '서현', 'D-52': '유리'}

# 간 손님 -> 삭제
print(cabinet.pop("B-100"))  # 수영
del cabinet["A-3"]  # 반환값 없음

# key 혹은 value들만 출력
print(cabinet.keys())  # dict_keys(['C-20', 'D-52'])
print(cabinet.values())  # dict_values(['서현', '유리'])
print(cabinet.items())  # 쌍으로 출력
# dict_items([('C-20', '서현'), ('D-52', '유리')])

# 캐비넷 다 비우기
cabinet.clear()
print(cabinet)  # {}
