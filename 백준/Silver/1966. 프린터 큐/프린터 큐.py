import sys
from collections import deque
from typing import List


def print_doc(pri: List, total_num: int, doc_num: int):
    pri = [int(i) for i in pri]
    doc = list()
    for i in range(total_num):
        doc.append(i)

    ans = []
    for i, v in enumerate(pri):
        current_max_val = max(pri)
        current_max_idx = pri.index(current_max_val)
        pri = pri[current_max_idx:] + pri[:current_max_idx]
        doc = doc[current_max_idx:] + doc[:current_max_idx]
        # print(pri)
        # print(doc)

        pri.pop(0)
        ans.append(doc.pop(0))

    final_ans = ans.index(doc_num)+1
    return final_ans


if __name__ == '__main__':
    input = sys.stdin.readline()
    total_examples = int(input)
    sample_deq = deque()
    for _ in range(total_examples):
        cmds = sys.stdin.readline()
        cmds = str(cmds).split()
        n = int(cmds[0])
        m = int(cmds[1])
        pri_list = sys.stdin.readline()
        pri_list = str(pri_list).split()

        a = print_doc(pri_list, n, m)
        print(a)