## 题目描述：输入一个由数字组成的字符串，请把它转换成整数并输出。

def strToInt(s):
    # write code here
    cond1 = (len(s) == 0)
    cond2 = (len(s) == 1) and (s[0] in ['+', '-'])
    if cond1 or cond2:
        errorFlag = True
        return 0

    flag = 0
    p = 0
    if s[0] in ['+', '-']:
        p += 1
        if s[0] == '-':
            flag = 1
    
    num = 0
    while p < len(s):
        first = ord(s[p]) - 48
        if first not in range(0, 10):
            errorFlag = True
            return 0
        num = num * 10 + first
        p += 1
    return num if not flag else -num

print(strToInt(input()))
