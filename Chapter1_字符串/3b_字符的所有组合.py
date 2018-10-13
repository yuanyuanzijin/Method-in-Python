## 题目描述：输入一个字符串，打印出该字符串中字符的所有组合。例如输入字符串abc，则输出由字符a、b、c、ab、ac、bc、abc。

## 方法一：递归实现
def calAllcombination(s):
    l = list(s)
    if not l:
        return
    combination(l)

def combination(l, index=0, hist=[]):
    if index == len(l):
        if hist:
            print(''.join(hist))
        return
    combination(l, index+1, hist)
    combination(l, index+1, hist+[l[index]])

calAllcombination('abc')

