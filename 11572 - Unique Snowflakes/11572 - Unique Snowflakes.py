from sys import stdin as s
from collections import deque
def main():
    cases = int(s.readline().strip())
    while cases:
        cant = int(s.readline().strip())
        dic = {}
        queue = deque()
        res = 0
        while cant:
            snowflake = s.readline().strip()
            if snowflake not in dic or dic[snowflake] == False:
                dic[snowflake] = True
                queue.append(snowflake)
            else:
                res = max(res, len(queue))
                queue.append(snowflake)
                while dic[snowflake]:
                    value = queue.popleft()
                    dic[value] = False
                dic[snowflake] = True
            cant -= 1
        res = max(res, len(queue))
        print(res)
        cases -= 1
main()