import turtle

# 创建一个新的turtle对象
t = turtle.Turtle()

# 设置画笔的速度
t.speed(1)

# 设置画笔的大小
t.pensize(20)

# 定义像素艺术的颜色
colors = [["red", "green"], ["blue", "yellow"]]

# 画出像素艺术
for i in range(2):
    for j in range(2):
        # 设置画笔的颜色
        t.pencolor(colors[i][j])

        # 画一个点
        t.dot()

        # 移动到下一个位置
        t.forward(40)

    # 移动到下一行
    t.backward(80)
    t.right(90)
    t.forward(40)
    t.left(90)

# 隐藏turtle
t.hideturtle()

# 结束绘图
turtle.done()