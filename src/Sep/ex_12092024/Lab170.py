from collections import deque

d=deque([1,2,3])
print(d)

d.append(4)
print(d)

d.extend([5,6])
print(d)

d.appendleft(0)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.reverse()
print(d)