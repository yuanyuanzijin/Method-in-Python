## 题目描述：给定一个字符串，求它的最长回文子串的长度
s = "dabffbasd"
## 解法一：中心扩展法
def LongestPalindrome(s):
    if not s:
        return 0

    maxcount = 0
    for i in range(1, len(s)-1):
        p1 = i-1
        p2 = i+1
        count = 1
        while p1 >= 0 and p2 <= len(s)-1:
            if s[p1] != s[p2]:
                break
            count += 2
            p1 -= 1
            p2 += 1
        maxcount = max(maxcount, count)

    for i in range(len(s)-1):
        p1 = i
        p2 = i+1
        count = 0
        while p1 >= 0 and p2 <= len(s)-1:
            if s[p1] != s[p2]:
                break
            count += 2
            p1 -= 1
            p2 += 1
        maxcount = max(maxcount, count)

    return maxcount

print(LongestPalindrome(s))

## 方法二：Manacher算法

