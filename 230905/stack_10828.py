# https://www.acmicpc.net/problem/10828
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#
# 명령은 총 다섯 가지이다.
#
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

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
