# 深度优先算法
'''
深度优先算法,DFS Depth First Search
'''

UP = "https://www.bilibili.com/video/BV16M411M72d?p=4&vd_source=c4c31c471fa6e78618db0c0a142f20fb"

list = [[1, 1, 3],
        [2, 3, 4],
        [1, 0, 1]]

m = 3 ; n = 3  # m行,n列 均为3


def dfs(i, j, value):
    if i < 0 or i == m:  # 判断行是否越界,若越界,返回0
        return 0
    if j < 0 or j == n:  # 判断列是否越界,若越界,返回0
        return 0
    if list[i][j] >= value:  # 判断当前值是否大于等于value,若大于等于,返回0,即判断是否递减
        return 0  # 不是递减的,不满足,返回0

    if (i, j) in dp:  # 判断当前坐标是否在dp中,若在,直接返回dp中的值
        return dp[(i, j)]

    res = 1  # 这一点,当前是1

    res = max(res, 1 + dfs(i - 1, j, list[i][j]))  # 向上走
    res = max(res, 1 + dfs(i + 1, j, list[i][j]))  # 向下走
    res = max(res, 1 + dfs(i, j - 1, list[i][j]))  # 向左走
    res = max(res, 1 + dfs(i, j + 1, list[i][j]))  # 向右走
    dp[(i, j)] = res

    return res


dp = {}  # 这里设立一个空的字典(dictionary),并将结果赋值给变量dp
'''
在Python中，字典是一种可变容器模型，可以存储任意类型对象，如数字、字符串、列表、字典等，且每个键值对（key-value pair）中的键必须是唯一的
'''

for x in range(m):
    for y in range(n):
        res = dfs(x, y, 100)

print(dp)
print('*' * 20)
print(max(dp.values()))
print('*' * 20)

'''
不用字典储存结果的运行结果:
1 1 2
3 4 5
2 1 2
'''
'''
使用字典储存结果的运行结果:
{ (0, 0): 1, (0, 1): 1, (0, 2): 2, (1, 0): 2, (1, 1): 3, (1, 2): 4, (2, 0): 2, (2, 1): 1, (2, 2): 2 }
'''
