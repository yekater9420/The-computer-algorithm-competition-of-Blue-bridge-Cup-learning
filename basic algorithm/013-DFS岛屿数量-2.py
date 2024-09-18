# 深度优先算法
# 如果我不替换为0,而是替换为2,或者是其他的部分呢?
up = 'https://www.bilibili.com/video/BV16M411M72d?p=5&vd_source=c4c31c471fa6e78618db0c0a142f20fb'
url = 'https://www.bilibili.com/video/BV16M411M72d?p=7&vd_source=c4c31c471fa6e78618db0c0a142f20fb'

grid = [ [1 , 1 , 1 , 0 , 0 , 0 , 0 ],
         [1 , 1 , 0 , 1 , 0 , 0 , 0 ],
         [0 , 0 , 0 , 0 , 0 , 1 , 0 ],
         [0 , 0 , 0 , 0 , 1 , 1 , 1 ] ]

m = len(grid)  #行
n = len(grid[0]) #列

def mark_current_island(x , y):  #mark标记,将题目中的1--->2 , current当前的位置(x ,y) , island岛屿
    if x <0 or x >=m or y <0 or y >=n or grid[x][y] != 1:  ## grid[x][y] != 1表示当前的位置不是岛屿,而是海洋  o水域,1陆地,2标记
         return  # 越界条件有4个或者是附近的陆地已经标记过

    grid[x][y] = 2  #进行标记
    print(x , y) #打印标记位次
    mark_current_island(x - 1 , y)
    mark_current_island(x + 1 , y)
    mark_current_island(x , y - 1)
    mark_current_island(x , y + 1)
'''
mark_current_island(0 , 0)
for row in grid:
    print(row)
'''
count = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            mark_current_island(i, j)
            count += 1

print('---------')
for row in grid:
    print(row)
print('---------')
print(count)
print('---------')




