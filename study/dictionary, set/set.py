# 집합 : 중복 안되고 순서가 없는
my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3}

# 집합의 활용
javaA = {"태연", "윤아", "수영"}
pythonA = set(["태연", "티파니"])

#교집합 : {'태연'}
print(javaA & pythonA)  # {'태연'}
print(javaA.intersection(pythonA))

# 합집합 : {'티파니', '윤아', '태연', '수영'}
print(javaA | pythonA)
print(javaA.union(pythonA))

# 차집합 : {'수영', '윤아'}
print(javaA - pythonA)
print(javaA.difference(pythonA))

# set에 추가
pythonA.add("윤아")
print(pythonA)  # {'태연', '티파니', '윤아'}

# set에서 제거
javaA.remove("수영")
print(javaA)  # {'윤아', '태연'}
