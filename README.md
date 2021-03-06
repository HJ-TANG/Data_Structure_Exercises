# Data_Structure_Exercises

# 算法与数据结构相关练习

## 分类索引

面试题_数字表示剑指offer第二版的题号，四位数字表示leetcode题库的题号，其他的在文件夹*其他常见算法题*中。

其中《剑指Offer》书中相关试题的Python实现主要参考《剑指offer（第二版）》和[MKYAN的博客](https://www.cnblogs.com/yanmk/p/9130681.html)。

**哈希表：**

- 面试题50：第一个只出现一次的字符

**链表：**

- 面试题06：从尾到头打印链表 （单向链表的增删改查，栈，递归）
- 面试题18：删除链表的节点（O(1)内删除节点，python函数的引用传递机制）
- 面试题22：链表中倒数第k个节点（代码的鲁棒性（空指针，越界输入等），一次使用多个指针遍历链表）
- 面试题23：链表中环的入口节点
- 面试题24：反转链表（提前想好测试用例，注意其递归实现）
- 面试题25：合并两个排序的链表
- 面试题35：复杂链表的复制（深拷贝、浅拷贝，分解复杂问题，遍历链表时的边界条件（用node.next当条件遍历时最后一个节点不会被遍历到），复制不要修改原对象）
- 面试题36：二叉搜索树与双向链表
- 面试题52：两个链表的第一个公共节点（栈的特点，设置多个指针）
- 面试题62：圆圈中最后剩下的数字

**二叉树：**

- 二叉树的七种遍历方式
- 面试题07：重建二叉树（二叉树前序、中序、后序、层序遍历，复杂问题分解，递归的出口）
- 面试题08：二叉树的下一个节点（二叉树的中序遍历，通过画图和举例解决复杂问题）
- 面试题26：树的子结构（二叉树的前序遍历，递归）
- 面试题27：二叉树的镜像
- 面试题28：对称的二叉树
- 面试题32：从上到下打印二叉树
- 面试题33：二叉搜索树的后序遍历序列
- 面试题34：二叉树中和为某一值的路径
- 面试题37：序列化二叉树
- 面试题54：二叉搜索树的第k大节点
- 面试题55：二叉树的深度

**堆栈、队列：**

- 面试题09：用两个栈实现队列（用两个队列实现栈）
- 面试题30：包含min函数的栈
- 面试题31：栈的压入弹出序列

**查找、排序：**
- 面试题03：数组中重复的数字（一维数组，哈希表，二分查找）
- 面试题04：二维数组中的查找（二维有序数组，查找顺序）
- 面试题11：旋转数组的最小数字
- 面试题39：数组中出现次数超过一半的数字（快排，第k小的数问题）
- 面试题40：最小的k个数（冒泡，快排，最大堆的调整）
- 面试题53：在排序数组中查找数字

**递归-回溯法：**

- 面试题12：矩阵中的路径
- 面试题13：机器人的运动范围
- 面试题38：字符串的排列
- [0077：组合](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0077_组合.ipynb)
- [0039：组合总和](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0039_组合总和.ipynb)
- [0040：组合总和II](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0047_组合总和II.ipynb)
- [0046：全排列](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0046_全排列.ipynb)
- [0047：全排列II](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0047_全排列II.ipynb)
- [0784：字母大小写全排列](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0784_字母大小写全排列.ipynb)

**动态规划：**

- 面试题10：斐波那契数列、青蛙跳台阶、变态跳台阶等（递归和循环的效率问题，问题的推广）
- 面试题42：连续子数组的最大和 （同[LeetCode0053：最大子序和](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0053_最大子序和.ipynb)）
- [0121：买卖股票的最佳时机](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0121_买卖股票的最佳时机.ipynb)
- [0122：买卖股票的最佳时机II](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0122_买卖股票的最佳时机II.ipynb)
- [0309：最佳买卖股票时机含冷冻期](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0309_最佳买卖股票时机含冷冻期.ipynb)
- [0714：买卖股票的最佳时机含手续费](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0714_买卖股票的最佳时机含手续费.ipynb)
- [0188：买卖股票的最佳时机IV](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0188_买卖股票的最佳时机IV.ipynb)
- [0123：买卖股票的最佳时机III](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0123_买卖股票的最佳时机III.ipynb)
- 动态规划_伐木
- 动态规划求编辑距离
- 动态规划求有向无环图最长路径
- [0523：连续的子数组和](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0523_连续的子数组和.ipynb) （思路一，数组的前缀和）
- [0718：最长重复子数组](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0718_最长重复子数组.ipynb)  (思路二，最长公共前缀)

**滑动窗口：**

- [0438：找到字符串中所有字母异位词](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0438_找到字符串中所有字母异位词.ipynb)
- [0003：无重复字符的最长子串](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0003_无重复字符的最长子串.ipynb)
- [0053：最大子序和](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0053_最大子序和.ipynb)
- [0076：最小覆盖子串](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0076_最小覆盖子串.ipynb)
- [0209：长度最小的子数组](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0209_长度最小的子数组.ipynb)

**重叠区间：**

- [0056：合并区间](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0056_合并区间.ipynb)
- 1094：拼车

**其他：**

- 面试题05：替换空格（列表类变量的处理顺序）
- 面试题29：顺时针打印矩阵
- 面试题39：数组中出现超过一半的数字
- 面试题40：最小的k个数
- 面试题56：数组中出现的数字
- [0011：盛水最多的容器](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0011_盛水最多的容器.ipynb) （双指针）
- [0628：三个数的最大乘积](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0628_三个数的最大乘积.ipynb)
- [0067：二进制求和](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0067_二进制求和.ipynb)
- [0287：找到数组中的重复数字](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0287_找到数组中的重复数字.ipynb)
- [0892：三维形体的表面积](https://github.com/HJ-TANG/Data_Structure_Exercises/blob/master/LeetCode/LeetCode_0892_三维形体的表面积.ipynb)


