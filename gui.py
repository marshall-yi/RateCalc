import tkinter
import tkinter.filedialog
import tkinter.messagebox

import model
from tkinter import ttk


def select_import_path():
    p = tkinter.filedialog.askopenfilename()
    import_path.set(p)


def select_output_path():
    p = tkinter.filedialog.askdirectory()
    output_path.set(p)


def do_job():
    pass


def show_version_info():
    msg = """
    费用计算工具 V1.0
    Python版本 3.6
    """
    tkinter.messagebox.showinfo(title='版本信息', message=msg)


def go(*args):
    value = select_list.get()


def add_contacts():
    new_window = tkinter.Toplevel()
    new_window.title('新增联系人')
    # new_window.geometry(size)


def calc():
    pass


def get_contact():
    data = model.query_all_custom()
    custom_nams = []
    remarks = []
    for d in data:
        c, r = d
        custom_nams.append(c)
        remarks.append(r)
    return custom_nams, remarks


def center_window(window, width, height):
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    print(size)
    window.geometry(size)


window = tkinter.Tk()
window.title('费用计算工具')
# window.iconbitmap('/home/zoulf/mycode/RateCalc/logo.ico')
center_window(window, 600, 300)
window.maxsize(600, 300)
window.minsize(300, 240)

# 菜单
menubar = tkinter.Menu(window)
file_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='文件', menu=file_menu)
file_menu.add_command(label='新增联系人', command=do_job)
file_menu.add_command(label='编辑联系人', command=do_job)
file_menu.add_separator()
file_menu.add_command(label='退出', command=window.quit)
help_menu = tkinter.Menu(file_menu, tearoff=0)
menubar.add_cascade(label='帮助', menu=help_menu)
help_menu.add_command(label='版本信息', command=show_version_info)

# 下拉列表及新增按钮
remarks = []
select_list = tkinter.ttk.Combobox(window, width=30)
select_list["values"], remarks = get_contact()
select_list.bind("<<ComboboxSelected>>", go)
tkinter.Label(window, text='请选择联系人:').grid(row=0, column=0, pady=10, padx=10)
select_list.grid(row=0, column=1, pady=10, padx=5)
edit_button = tkinter.Button(window, text='编辑', command=add_contacts).grid(row=0, column=2, pady=10, padx=5)
add_button = tkinter.Button(window, text='新增', command=add_contacts).grid(row=0, column=3, pady=10, padx=5)

# 下划线
canvas = tkinter.Canvas(window, bg='black', height=1, width=600)
canvas.grid(row=1, column=0, columnspan=4, pady=10)

# 文件导入按钮
import_path = tkinter.StringVar()
output_path = tkinter.StringVar()
tkinter.Label(window, text="导入文件路径:").grid(row=2, column=0, pady=10)
tkinter.Entry(window, textvariable=import_path, width=50).grid(row=2, column=1, columnspan=2, pady=10)
tkinter.Button(window, text="路径选择", command=select_import_path).grid(row=2, column=3, pady=10)

tkinter.Label(window, text="输出文件夹路径:").grid(row=3, column=0, pady=10)
tkinter.Entry(window, textvariable=output_path, width=50).grid(row=3, column=1, columnspan=2, pady=10)
tkinter.Button(window, text="路径选择", command=select_output_path).grid(row=3, column=3, pady=10)

# 开始计算按钮
tkinter.Button(window, text="计算", command=calc, width=40).grid(row=4, column=0, columnspan=4, pady=20)

window.config(menu=menubar)
window.mainloop()