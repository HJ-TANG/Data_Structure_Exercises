"""
题目：T个测试用例。每个测试用例，给定一个全部是大写字母组成的字符串，允许你至多可将两个字符改成字符'N'，求更改后，由连续‘N’组成的串的最长长度。
思路：双指针+计数。双指针左右夹逼，夹逼区间的宽的最大值即为所求。
计数器count记录非N字符的个数，当计数器超过2时，左指针后移，一直移到计数器不超过2为止。时间复杂度O(n)
"""


def fun(string):
    len_string = len(string)
    count = 0
    begin = 0
    end = 0
    length = 0

    while end < len_string:
        if string[end] != 'N':
            count += 1
        end += 1
        while count > 2:  # 这个循环将begin和end间的非N字符控制在两个以内
            if string[begin] != 'N':
                count -= 1
            begin += 1
        length = max(length, end - begin)  # 得到最大长度

    return length


s = 'ANCBNNNNBNCNC'
print(fun(s))