import tkinter as tk
#https://www.runoob.com/python/python-gui-tkinter.html    学习资料

window = tk.Tk()  # 创建窗口
window.title("this is a test")  # 窗口标题
window.geometry('500x400')  # 窗口大小，小写字母x
# 窗口的label
k = tk.Label(window,
             text='this is a window created by tkinter',  # 文本
             bg='green',  # 字体的背景颜色
             font=('Arial', 12),  # 字体和大小
             width=30, height=2  # 字体所占的宽度和高度
             )
k.pack()

# 添加按钮
b = tk.Button(
    window,
    text='button',
    width=5, height=2,
    command=None # 执行函数体，而不是得到函数执行的结果
)
b.pack()


e = tk.Entry(window, show='*')
e.pack()
t = tk.Text(window, height=2)
t.pack()

var = e.get()  # 可以得到输入的内容

t.insert('insert', var)  # 在文本框的光标处插入var

t.insert('end', var)  # 在末尾插入var
k.pack()  # 固定


# 以上是窗口的主体
window.mainloop()  # 结束（不停循环刷新）