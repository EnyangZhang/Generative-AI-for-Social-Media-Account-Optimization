# import tkinter as tk
# from tkinter import scrolledtext
# from api_request import get_todays_post
#
# # 定义按钮点击事件的回调函数
# def on_button_click():
#     result = get_todays_post()
#     result_text.delete(1.0, tk.END)
#     result_text.insert(tk.END, result)
#
# # 创建主窗口
# root = tk.Tk()
# root.title("Xiaohongshu Daily Post Generator")
#
# # 创建按钮
# generate_button = tk.Button(root, text="Today's post on RED", command=on_button_click)
# generate_button.pack(pady=10)
#
# # 创建显示API响应的文本框
# result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
# result_text.pack(pady=10)
#
# # 运行主循环
# root.mainloop()

import tkinter as tk
from tkinter import scrolledtext
from api_request import get_todays_post, send_custom_request

# 定义按钮点击事件的回调函数
def on_button_click():
    result = get_todays_post()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# 定义发送按钮点击事件的回调函数
def on_send_button_click():
    user_input = user_entry.get()
    if user_input.strip():
        result = send_custom_request(user_input)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)

# 创建主窗口
root = tk.Tk()
root.title("Xiaohongshu Daily Post Generator")

# 创建按钮
generate_button = tk.Button(root, text="Today's post on RED", command=on_button_click)
generate_button.pack(pady=10)

# 创建显示API响应的文本框
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
result_text.pack(pady=10)

# 创建用户输入框和发送按钮
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

user_entry = tk.Entry(input_frame, width=50)
user_entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(input_frame, text="Send", command=on_send_button_click)
send_button.pack(side=tk.RIGHT, padx=5)

# 运行主循环
root.mainloop()