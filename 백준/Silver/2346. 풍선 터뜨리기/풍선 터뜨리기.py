import sys
from typing import List
from collections import deque


total_balloon = int(sys.stdin.readline())
user_input = sys.stdin.readline()
rotation_num = user_input.split(" ")


def pop_balloons(total: int, rotations: List[str]):
    ans = ''
    balloons = deque()
    for i in range(total):
        balloons.append(i+1)

    for i in range(total):
        # target = balloons[0]  # 제일 앞에 있는 풍선
        target = balloons.popleft()
        ans += str(target) + ' '
        balloon_id = target-1
        rotation = int(rotations[balloon_id]) * -1 + 1 if int(rotations[balloon_id]) > 0 else int(rotations[balloon_id]) * -1
        # print(rotation)
        balloons.rotate(rotation)
        # balloons.remove(target)

    return ans.strip()


x = pop_balloons(total_balloon, rotation_num)
print(x)
