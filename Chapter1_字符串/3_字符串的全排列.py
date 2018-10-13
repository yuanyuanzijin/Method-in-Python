## 题目描述：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，则输出由字符a、b、c 所能排列出来的所有字符串abc、acb、bac、bca、
## cab 和 cba。

## 方法一：递归实现
def calAllPermutation(s):
    l = list(s)
    if not l:
        return
    permutation(l, 0, len(l)-1)

def permutation(l, start, end):
    if start == end:
        print(''.join(l))
        return

    for i in range(start, end+1):
        l[start], l[i] = l[i], l[start]
        permutation(l, start+1, end)
        l[i], l[start] = l[start], l[i]

calAllPermutation('abc')

## 方法二：字典序排列
def calAllPermutation2(s):
    l = list(s)
    next_index = list(range(len(s)))
    while True:
        c = [l[i] for i in next_index]
        print(''.join(c))
        if not get_next_index(next_index):
            break

def get_next_index(pre_index):
    for i in range(len(pre_index)-2, -1, -1):
        if pre_index[i] < pre_index[i+1]:
            break
    else:
        return False

    for j in range(len(pre_index)-1, i, -1):
        if pre_index[j] > pre_index[i]:
            break

    pre_index[i], pre_index[j] = pre_index[j], pre_index[i]
    for k in range(i+1, (i+len(pre_index))//2+1):
        pre_index[k], pre_index[len(pre_index)+i-k] = pre_index[len(pre_index)+i-k], pre_index[k]
    
    return True

calAllPermutation2('abc')
