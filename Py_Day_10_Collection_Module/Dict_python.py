from collections import defaultdict

# Default value is int() → 0
dd = defaultdict(int)

dd['apple'] += 1
dd['banana'] += 2

print(dd)  # defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})
print(dd['mango'])  # 0 (no KeyError)
