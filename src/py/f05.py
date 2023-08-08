# 水仙花数是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身。例如：1^3 + 5^3 + 3^3 = 153。

# 在Python中，我们可以使用一个简单的循环来找出所有的水仙花数。以下是一个示例代码：
for num in range(100, 1000):
    # 将数字转换为字符串，方便获取每一位数字和位数
    str_num = str(num)
    n = len(str_num)
    # 计算每一位数字的n次幂之和
    sum_of_powers = sum(int(digit) ** n for digit in str_num)
    # 如果这个和等于原来的数字，那么这个数字就是水仙花数
    if sum_of_powers == num:
        print(num)
