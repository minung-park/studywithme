import sys

input_cmd = sys.stdin.readline()
cmds = input_cmd.split(" ")
n = int(cmds[0])
m = int(cmds[1])

string_collections = []
for i in range(n):
    input_str = sys.stdin.readline()
    string_collections.append(input_str)

check_collections = {}
for i in range(m):
    input_str = sys.stdin.readline()
    str_cnt = check_collections.get(input_str, 0)
    if str_cnt == 0:
        check_collections[input_str] = 1
    else:
        check_collections[input_str] += 1

ans = 0
for strs in string_collections:
    ans += check_collections.get(strs, 0)

print(ans)
