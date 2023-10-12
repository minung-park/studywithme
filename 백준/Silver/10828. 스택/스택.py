import sys
from typing import List
from collections import deque


USER_CMD = {"push": "push", "pop": "pop", "size": "size", "empty": "empty", "top": "top"}
def command_func(commands: List, deq: deque):
    cmd = commands[0]
    val = commands[-1]

    is_valid = USER_CMD.get(cmd, None)
    if not is_valid:
        return

    if cmd == "push":
        deq.append(val)
        return deq

    if cmd == "pop":
        if check_deq_size(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
        return deq

    if cmd == "size":
        print(check_deq_size(deq))
        return deq

    if cmd == "empty":
        if check_deq_size(deq) == 0:
            print(1)
        else:
            print(0)
        return deq

    if cmd == "top":
        if check_deq_size(deq) == 0:
            print(-1)
        else:
            val = deq.pop()
            print(val)
            deq.append(val)
        return deq


def check_deq_size(deq: deque):
    return len(deq)


if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    sample_deq = deque()
    for _ in range(n):
        cmds = sys.stdin.readline()
        cmds = str(cmds).split()
        command_func(cmds, sample_deq)