from collections import deque

dq = deque([1, 2, 3])

dq.append(4)      # Add to right
dq.appendleft(0)  # Add to left
print(dq)         # deque([0, 1, 2, 3, 4])

dq.pop()          # Remove from right
dq.popleft()      # Remove from left
print(dq)         # deque([1, 2, 3])
