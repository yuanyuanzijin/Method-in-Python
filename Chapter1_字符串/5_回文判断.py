## 题目描述：给定一个字符串，如何判断这个字符串是否是回文串？
s = 'abfgfba'
## 解法一：两头往中间扫
def isPalindrome(s):
    if not s:
        return False

    p1 = 0
    p2 = len(s) - 1
    while p1 < p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True

print(isPalindrome(s))

## 解法二：中间往两头扫
def isPalindrome2(s):
    if not s:
        return 0
    
    m = len(s) >> 1
    if len(s) & 1:
        p1 = m
        p2 = m
    else:
        p1 = m
        p2 = m+1
    
    while p1 >= 0:
        if s[p1] != s[p2]:
            return False
        p1 -= 1
        p2 += 1
    return True

print(isPalindrome2(s))
