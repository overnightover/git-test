def print_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = print_triangle(n-1)
        row = [1]
        for i in range(1, n-1):
            row.append(triangle[n-2][i-1] + triangle[n-2][i])
        row.append(1)
        triangle.append(row)
        return triangle

def display_triangle(triangle):
    for row in triangle:
        for num in row:
            print(num, end=" ")
        print()

# 输入杨辉三角的行数
num_rows = int(input("请输入杨辉三角的行数: "))

triangle = print_triangle(num_rows)
display_triangle(triangle)
