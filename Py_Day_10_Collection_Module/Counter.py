from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count = Counter(data)

print(count)        # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(count['apple']) # 3
print(count.most_common(2))  # [('apple', 3), ('banana', 2)]
