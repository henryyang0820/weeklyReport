import tkinter as tk
from tkinter import ttk

dict = {}

win = tk.Tk()
win.title('测试组周报填写')
# 开始时间
stlabel = ttk.Label(win, text='开始时间：')
stlabel.grid(column=0, row=1)
start_time_value = tk.StringVar()
start_time_value_entry = ttk.Entry(win, textvariable=start_time_value)
start_time_value_entry.grid(column=1, row=1)
# 结束时间
ftlabel = ttk.Label(win, text='结束时间：')
ftlabel.grid(column=2, row=1)
finish_time_name = tk.StringVar()
entry_fday_name = ttk.Entry(win, textvariable=finish_time_name)
entry_fday_name.grid(column=3, row=1)
# 选择测试还是配置
ch_var = tk.StringVar()
ch_label = ttk.Label(win, text='工作任务')
ch_label.grid(column=2, row=2)
# 执行人
nameLabel = ttk.Label(win, text='执行人：')
nameLabel.grid(column=0, row=2)
person_name = tk.StringVar()
entry_name = ttk.Entry(win, textvariable=person_name)
entry_name.grid(column=1, row=2)

# 计划人天
planlabel = ttk.Label(win, text='计划人天：')
planlabel.grid(column=0, row=3)
plan_day_name = tk.StringVar()
entry_pday_name = ttk.Entry(win, textvariable=plan_day_name)
entry_pday_name.grid(column=1, row=3)
# 实际人天
finishlabel = ttk.Label(win, text='实际人天：')
finishlabel.grid(column=2, row=3)
finish_day_name = tk.StringVar()
entry_fday_name = ttk.Entry(win, textvariable=finish_day_name)
entry_fday_name.grid(column=3, row=3)
# 本周工作内容
day1 = ttk.Label(win, text='day1：')
day1.grid(column=0, row=6)
day2 = ttk.Label(win, text='day2：')
day2.grid(column=0, row=7)
day3 = ttk.Label(win, text='day3：')
day3.grid(column=0, row=8)
day4 = ttk.Label(win, text='day4：')
day4.grid(column=0, row=9)
day5 = ttk.Label(win, text='day5：')
day5.grid(column=0, row=10)
this_week_jobs = ttk.Label(win, text='本周工作内容：')
this_week_jobs.grid(column=2, row=5)
this_week_content = tk.StringVar()
day1_content = tk.Text(win, height=3)
day1_content.grid(column=2, row=6)
day2_content = tk.Text(win, height=3)
day2_content.grid(column=2, row=7)
day3_content = tk.Text(win, height=3)
day3_content.grid(column=2, row=8)
day4_content = tk.Text(win, height=3)
day4_content.grid(column=2, row=9)
day5_content = tk.Text(win, height=3)
day5_content.grid(column=2, row=10)

# 下周工作计划
next_week_jobs = ttk.Label(win, text='下周工作计划：')
next_week_jobs.grid(column=2, row=11)
next_week_content_edittext = tk.Text(win, width=60, height=5)
next_week_content_edittext.grid(column=2, row=12)

# 下周计划开始时间
next_week_start_time = ttk.Label(win, text='开始时间：(写在下方）')
next_week_start_time.grid(column=1, row=11)
next_week_start_time_text = tk.Text(win, width=12, height=1)
next_week_start_time_text.grid(column=1, row=12)
# 下周计划结束时间
next_week_finish_time = ttk.Label(win, text='结束时间：(写在下方）')
next_week_finish_time.grid(column=3, row=11)
next_week_finish_time_text = tk.Text(win, width=12, height=1)
next_week_finish_time_text.grid(column=3, row=12)
# 下下周工作计划
next2_week_jobs = ttk.Label(win, text='下周工作计划：')
next2_week_jobs.grid(column=2, row=13)
next2_week_content_edittext = tk.Text(win, width=60, height=5)
next2_week_content_edittext.grid(column=2, row=14)

# 下周计划开始时间
next2_week_start_time = ttk.Label(win, text='开始时间：(写在下方）')
next2_week_start_time.grid(column=1, row=13)
next2_week_start_time_text = tk.Text(win, width=12, height=1)
next2_week_start_time_text.grid(column=1, row=14)
# 下周计划结束时间
next2_week_finish_time = ttk.Label(win, text='结束时间：(写在下方）')
next2_week_finish_time.grid(column=3, row=13)
next2_week_finish_time_text = tk.Text(win, width=12, height=1)
next2_week_finish_time_text.grid(column=3, row=14)

# todo 此处后续做数据处理22
def doData():
	dict = {'start_time_value':start_time_value.get(),
			'finish_time_name':finish_time_name.get(),
			'test_apply':ch_var.get(),'person_name':person_name.get(),
			'plan_day_name':plan_day_name.get(),'finish_day_name':finish_day_name.get(),
			'day1_content':day1_content.get(index1=1.0,index2=100.0),
			'day2_content':day2_content.get(index1=1.0,index2=100.0),
			'day3_content':day3_content.get(index1=1.0,index2=100.0),
			'day4_content':day4_content.get(index1=1.0,index2=100.0),
			'day5_content':day5_content.get(index1=1.0,index2=100.0),
			'next_week_start_time_text':next_week_start_time_text.get(index1=1.0,index2=100.0),
			'next_week_finish_time_text':next_week_finish_time_text.get(index1=1.0,index2=100.0),
			'next_week_content_edittext':next_week_content_edittext.get(index1=1.0,index2=100.0),
			'next2_week_start_time_text': next2_week_start_time_text.get(index1=1.0,index2=100.0),
			'next2_week_finish_time_text': next2_week_finish_time_text.get(index1=1.0,index2=100.0),
			'next2_week_content_edittext': next2_week_content_edittext.get(index1=1.0,index2=100.0)

			}
	print(dict)

def clickMe():
	action.configure(doData())


action = tk.Button(win, text="提交周报", command=clickMe)
action.grid(column=3, row=8)


# 更改配置或者测试
def change_selection():
	ch_label.config(text=ch_var.get())


r1 = tk.Radiobutton(win, text='测试', variable=ch_var, value='测试', command=change_selection)
r1.grid(column=3, row=2)
r2 = tk.Radiobutton(win, text='配置', variable=ch_var, value='配置与维护', command=change_selection)
r2.grid(column=4, row=2)

win.mainloop()
