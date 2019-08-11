# 二分查找


# 1. 非递归算法
def binary_search_loop(lis, num):
    left = 0
    right = len(lis) - 1
    while left <= right:  # 循环条件
        mid = (left + right) // 2  # 获取中间位置数字的索引（序列前提是有序的）
        if num < lis[mid]:  # 如果查询数字比中间数字小，那就去二分后的左边找
            right = mid - 1  # 来到左边后，需要将右边的边界换为mid - 1
        elif num > lis[mid]:  # 如果查询的数字比中间的数字大，那么去二分后的右边找
            left = mid + 1  # 来到右边后，需要将左边的边界换为mid + 1
        else:
            return mid  # 如果查询到的正好是中间值，返回该值的索引
    return -1  # 如果循环结束，左边大于了右边，代表没有找到


# 2. 递归算法
def binary_search_recurr(lis, left, right, num):
    if left > right:  # 递归结束条件
        return -1
    mid = (left + right) // 2
    if num < lis[mid]:
        right = mid - 1
    elif num > lis[mid]:
        left = mid + 1
    else:
        return mid
    # 这里之所以会有return是因为必须接收值，不然返回None
    # 回溯到最后一层的时候，如果没有return，那么将会返回None
    return binary_search_recurr(lis, left, right, num)


lis = [11, 32, 51, 21, 42, 9, 5, 6, 7, 8]
print(lis)
lis.sort()
print(lis)
print(binary_search_loop(lis, 5))
print(binary_search_recurr(lis, 0, len(lis)-1, 5))