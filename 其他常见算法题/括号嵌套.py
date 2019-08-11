import re

p = re.compile(r'[(](.*)[)]')


def de_bucket_1(s):
    if '(' not in s:
        return s
    pres = re.search(p, s)
    res = de_bucket_1(s[pres.start()+1:pres.end()-1])
    return s[:pres.start()] + res * int(s[pres.end()]) + s[pres.end()+1:]


def solution1(string):
    """
    解决不了括号并排的情况，如(BG)2(BC)5D
    """
    s1 = de_bucket_1(string)
    temp = ''
    nums = re.finditer('\d+', s1)
    i = 0
    for num in nums:
        string = s1[i:num.span()[0]]
        temp += string[:-1] + string[-1] * int(num.group())
        i = num.span()[1]
    temp += s1[i:]
    return temp


def de_bucket_2(sss):
    while '(' in sss:
        left = sss.rfind('(')
        right = left + sss[left:].find(')')
        s = sss[left + 1:right]
        nums = re.search('\d+', sss[right:])
        temp = s * int(nums.group())
        sss = sss[:left] + temp + sss[right+len(nums.group())+1:]
    return sss


def solution2(string):
    s1 = de_bucket_2(string)
    temp = ''
    nums = re.finditer('\d+', s1)
    i = 0
    for num in nums:
        string = s1[i:num.span()[0]]
        temp += string[:-1] + string[-1] * int(num.group())
        i = num.span()[1]
    temp += s1[i:]
    return temp


# 旭东的写法1（有bug）
# def solution(string):
#     if ')' not in string:
#         for i in range(len(string)):
#             if string[i].isdigit():
#                 break
#         return string[:i]*int(string[i]) + string[i+1:]
#     i = 0
#     j = len(string)-1
#     while string[i] != '(':
#         i += 1
#     while string[j] != ')':
#         j -= 1
#     res = solution(string[i+1: j])
#     return res*int(string[j+1]) + string[j+2:]


# print(solution1('BG2(BC)5D'))
strings = ['(AB2)3(BFD)2',
           'BG2(BC)10D',
           'A11B',
           '(AA)2A',
           '((A2B)2)2G',
           '(YUANFUDAO)2JIAYOU',
           'A2BC4D2']
for s in strings:
    print(solution2(s))


"""
测试用例：
A11B
(AA)2A
((A2B)2)2G
(YUANFUDAO)2JIAYOU
A2BC4D2
"""