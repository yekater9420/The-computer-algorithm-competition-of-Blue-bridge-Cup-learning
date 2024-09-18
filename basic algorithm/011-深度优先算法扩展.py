# 深度优先算法扩展
#被污染 0  , 没有被污染 1        没有被包围的独立海域是指该快海域的上下左右被已经污染的海水包围
'''
UP--->https://www.bilibili.com/video/BV16M411M72d?p=4&vd_source=c4c31c471fa6e78618db0c0a142f20fb
'''
UP = 'https://www.bilibili.com/video/BV16M411M72d?p=4&vd_source=c4c31c471fa6e78618db0c0a142f20fb'
list = [ [1 , 1 , 0 , 0 , 0] ,
         [1 , 0 , 1 , 0 , 0] ,
         [1 , 0 , 0 , 0 , 0] ,
         [1 , 1 , 0 , 1 , 1] ]
m = 4 ; n = 5  # m行, n列

def dfs(x , y):
    if x < 0 or x ==m or y < 0 or y == n or list[x][y] == 0:
        return 0

    # 无污染的点   状态更改,进行标记,发现要求的标记为1,防止第二次检测
    list[x][y] = 0
    dfs(x - 1, y)  # 左
    dfs(x + 1, y)  # 右
    dfs(x, y - 1)  # 上
    dfs(x, y + 1)  # 下

cnt = 0
for i in range(m) :
    for j in range(n) :
        if list[i][j] == 1 :
            cnt += 1
            dfs(i, j)

print(cnt)


