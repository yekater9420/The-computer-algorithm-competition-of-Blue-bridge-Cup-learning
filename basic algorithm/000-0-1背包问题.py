#0-1背包问题
'''
0-1 Knapsack Problem
'''

'''
解法:
1.递归解法  Recursive Solution
2.中间结果记忆  Memorize Intermediate Results
'''

# 提供中间记忆存贮,来减少递归的次数

UP = 'https://www.bilibili.com/video/BV16M411M72d/?p=2&spm_id_from=333.880.my_history.page.click&vd_source=c4c31c471fa6e78618db0c0a142f20fb'

weigth = [0 , 1 , 2 , 4 , 2 , 5]
value = [0 , 5 , 3 , 5 , 3 , 2]


def KP(n , C):    #为选择的第几个 C为总容量
    if memo[n][C] != 0 :        #递归终止条件
        for row in memo:
            print(row)
        print('-' *40)
        return  memo[n][C]
    if n == 0 or C == 0:
        result = 0
    elif weigth[n] > C :         #不选择这个物品
        result = KP(n - 1, C)
    else:
        tmp_1 = KP(n - 1, C)
        tmp_2 = value[n] + KP(n - 1, C - weigth[n])
        result = max(tmp_1 , tmp_2)
    memo[n][C] = result
    return result


#输入题目中要求条件
n = 5 ; C = 10
#定义一个二维列表,用于储存数据
memo = [ [0] * (C + 1) for x in range(n + 1) ]

#求出结果
res = KP(n , C)
print('-' *20)
print(res)
print('-' *20)

'''
memo = [ [0] * (C + 1) for x in range(n + 1) ]
这段Python代码创建了一个二维列表（矩阵），用于存储动态规划问题的中间结果。具体来说，这段代码创建了一个大小为 `(n+1) x (C+1)` 的矩阵，其中 `n` 和 `C` 是两个变量，通常代表问题的规模或约束条件。

### 实现原理
1. **列表推导式**：外层和内层都使用了列表推导式来创建矩阵。
2. **初始化值**：矩阵中的每个元素都被初始化为 `0`。

### 用途
这种矩阵通常用于动态规划问题中，用于存储子问题的解，从而避免重复计算。例如，在背包问题、最长公共子序列（LCS）问题等中，都会用到这种矩阵来存储中间结果。

### 注意事项
1. **变量 `n` 和 `C` 的定义**：在使用这段代码之前，需要定义 `n` 和 `C` 的值，它们分别代表问题的规模和约束条件。
2. **矩阵大小**：矩阵的大小为 `(n+1) x (C+1)`，这意味着矩阵的行数是 `n+1`，列数是 `C+1`。这是为了处理从 `0` 到 `n` 或 `C` 的所有情况。
3. **初始化为 `0`**：矩阵中的所有元素初始化为 `0`，这通常意味着初始状态或边界条件。在动态规划算法中，这个初始状态可能代表某种默认值或未计算状态。

### 示例
假设 `n = 3` 且 `C = 4`，那么这段代码将创建一个 `4x5` 的矩阵（因为 `n+1=4`，`C+1=5`），所有元素都初始化为 `0`：

```
[
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]
]
```

这个矩阵可以用来存储动态规划算法中的中间结果，例如在背包问题中，矩阵中的每个元素可能表示在给定容量下，能够装入的最大价值。
'''
'''
这段代码实现了一个经典的动态规划问题——0-1背包问题。0-1背包问题是一个经典的优化问题，目标是选择一些物品放入背包中，使得这些物品的总价值最大，同时不超过背包的容量限制。

### 实现原理

1. **定义问题**：给定一组物品，每个物品有一个重量和一个价值，以及一个容量为C的背包。目标是选择一些物品放入背包中，使得这些物品的总价值最大，同时不超过背包的容量限制。

2. **状态定义**：使用一个二维数组`memo`来存储子问题的解。`memo[i][j]`表示在前i个物品中选择，使得总重量不超过j的情况下的最大价值。

3. **状态转移方程**：
   - 如果第i个物品的重量大于背包的容量j，那么不能选择这个物品，最大价值就是前i-1个物品在容量j下的最大价值，即`memo[i][j] = memo[i-1][j]`。
   - 如果第i个物品的重量小于等于背包的容量j，那么可以选择这个物品或者不选择这个物品。选择这个物品的最大价值是`value[i] + memo[i-1][j - weigth[i]]`，不选择这个物品的最大价值是`memo[i-1][j]`。取两者中的较大值作为`memo[i][j]`。

4. **边界条件**：当没有物品可选或者背包容量为0时，最大价值为0。

### 用途

这段代码可以用于解决各种优化问题，例如物品选择、资源分配、任务调度等，只要问题可以转化为0-1背包问题。

### 注意事项

1. **初始化**：在调用`KP`函数之前，需要初始化`memo`数组，并将所有元素设为0。

2. **时间复杂度**：该算法的时间复杂度为O(n*C)，其中n是物品的数量，C是背包的容量。

3. **空间复杂度**：该算法的空间复杂度也是O(n*C)。

4. **递归与迭代**：这段代码使用递归的方式实现动态规划，也可以使用迭代的方式实现，迭代的方式可以减少递归带来的额外开销。

5. **优化**：可以使用滚动数组来优化空间复杂度，将二维数组`memo`压缩为一维数组。
'''

'''
这段代码实现了一个经典的动态规划问题——0-1背包问题。0-1背包问题是一个经典的优化问题，目标是选择一些物品放入背包中，使得这些物品的总价值最大，同时不超过背包的容量限制。

### 递归逻辑

1. **递归终止条件**：当没有物品可选或者背包容量为0时，最大价值为0。这对应于代码中的`if n == 0 or C == 0:`部分。

2. **递归调用**：对于每个物品，有两种选择：选择这个物品或者不选择这个物品。如果选择这个物品，那么最大价值就是`value[n] + KP(n - 1, C - weigth[n])`，其中`value[n]`是第n个物品的价值，`KP(n - 1, C - weigth[n])`是前n-1个物品在剩余容量下的最大价值。如果不选择这个物品，那么最大价值就是`KP(n - 1, C)`，即前n-1个物品在当前容量下的最大价值。

3. **递归返回值**：对于每个子问题，递归调用`KP`函数来计算最大价值，并将结果存储在`memo`数组中，以避免重复计算。

4. **记忆化搜索**：通过使用`memo`数组来存储子问题的解，可以避免重复计算，从而提高算法的效率。这对应于代码中的`if memo[n][C] != 0 :`部分。

### 递归与迭代

这段代码使用递归的方式实现动态规划，也可以使用迭代的方式实现，迭代的方式可以减少递归带来的额外开销。迭代的方式通常使用一个循环来模拟递归的过程，通过逐步计算子问题的解，并更新`memo`数组。

### 优化

可以使用滚动数组来优化空间复杂度，将二维数组`memo`压缩为一维数组。这是因为每次计算`memo[i][j]`时，只需要用到`memo[i-1][j]`和`memo[i-1][j-weights[i]]`，所以可以将`memo`数组压缩为一维数组，每次计算时更新这个一维数组即可。
'''

n , C = list(map(int , input().split(',')))


