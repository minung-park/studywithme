from collections import deque


q = deque()
q.rotate()


user_input = "9 3"
inputs = user_input.split(" ")
n = int(inputs[0])
interval = int(inputs[1])

arr = list()

for i in range(1, n+1):
    arr.append(i)

ans = []
idx = interval - 1
for i in range(n):
    if idx >= len(arr):
        cnt = arr.count(0)
        for _ in range(cnt):
            arr.remove(0)
        print(arr)
        idx = (len(arr) % interval)-1

    t = arr[idx]
    while t == 0:
        idx += 1
        print(idx)
        if idx >= len(arr):
            idx = (len(arr) % interval) - 1
        t = arr[idx]
    print(idx, t)
    ans.append(t)
    arr[idx] = 0

    idx += interval

print(ans)
