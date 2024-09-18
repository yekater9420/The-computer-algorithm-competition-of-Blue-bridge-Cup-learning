# 深度优先算法解决岛屿数量问题
'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
UP--->https://www.bilibili.com/video/BV16M411M72d?p=5&vd_source=c4c31c471fa6e78618db0c0a142f20fb
'''
'''
python中True为 1，False为 0
真为1,假为0
'''
'''
先向上,再向下,再向左,再向右
'''
grid = [ [1 , 1 , 1 , 0 , 0 , 0 , 0 ],
         [1 , 1 , 0 , 1 , 0 , 0 , 0 ],
         [0 , 0 , 0 , 0 , 0 , 1 , 0 ],
         [0 , 0 , 0 , 0 , 1 , 1 , 1 ] ]

m = 4 ; n = 7
'''
或者是:
m = len(grid) ; n = len(grid[0])
'''

def DFS(x , y):
    # 检测x , y是否越界
    if x < 0 or x == m or y < 0 or y == n or grid[x][y] == 0:
        return 0

    # 进行检测标记
    grid[x][y] = 0
    DFS(x + 1 , y) #向右
    DFS(x - 1 , y) #向左
    DFS(x , y + 1) #向下
    DFS(x , y - 1) #向上

#设计计数器
cunt = 0
for i in range(m) :
    for j in range(n) :
        if grid[i][j] == 1 :
            cunt += 1
            DFS(i , j)

print(cunt)
