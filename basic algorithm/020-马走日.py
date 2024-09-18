# 马走日
up = 'https://www.bilibili.com/video/BV16M411M72d?p=8&vd_source=c4c31c471fa6e78618db0c0a142f20fb'
url = 'https://www.bilibili.com/video/BV16M411M72d?p=9&vd_source=c4c31c471fa6e78618db0c0a142f20fb'
'''
马走日问题:
马在中国象棋以日字形规则移动。
请编写一段程序，给定n*m大小的棋盘，以及马的初始位置(x，y)，要求不能重复经过棋盘上的同一个点，计算马可以有多少途径遍历棋盘上的所有点。
输 入
第一行为整数T(T<10)，表示测试数据组数。
每一组测试数据包含一行，为四个整数，分别为棋盘的大小以及初始位置坐标n,m,x,y。(0<=x<=n-1,0<=y<=m-1，m<10,n<10)
输出
每组测试数据包含一行，为一个整数，表示马能遍历棋盘的途径总数，0为无法遍历一次样例输入
5400
样例输出
32
'''
# 代码
m , n = 5 , 4

dirs = [(2 , 1) , (1 , 2) ,
        (-2 , 1) , (-1 , 2) ,
        (-2 , -1) , (-1 , -2) ,
        (2 , -1) , (1 , -2) ]       #马走8个位置

#棋盘,生产棋盘二维列表
board = [ [0] * n for x in range(m)]   # m行 n列   取值范围: 行 0--->m-1 , 列 0--->n-1  0为标记没有走过,1为标记已经走过

#设置计数器,表示路径数量(不重复)
cnt = 0
def move(x , y ,step) :
    global cnt
    if step == m * n :
        cnt = cnt + 1
        return 1
    for i in range(8) :
        next_x = x + dirs[i][0]   #行的偏移
        next_y = y + dirs[i][1]   #列的偏移

        # 检测是否越界
        if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n  and board[next_x][next_y] == 0 :
            board[next_x][next_y] = 1   #标记为已经走过
            move(next_x, next_y, step + 1)   # 递归下一位置,往下走一步
            board[next_x][next_y] = 0   # 回溯,标记为未走过



a , b = 0 , 0
#设置起点面板,用1表示已经走过
board[a][b] = 1
move(a , b , 1)
print(cnt)

'''
在提交程序时候,由于不能手动输入数据,所有的数据需要通过 input()函数传入进来
因此,需要对数据进行一个切片
例如: t = int(input())  # 读取测试数据组数,由于我们传入数据为整型数字,所以,需要使用 int()函数进行转换
     for i in range(t) :
        m , n , a , b = map(int , input().split())   # 读取每组测试数据
'''
'''
t = map(int , input().split())
'''









