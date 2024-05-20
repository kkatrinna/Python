from tkinter import *
from tkinter import ttk

def finish():
    root.destroy()
    print('Закрытие приложения')
  
root = Tk()
root.title('Приложение на Tkinter')
root.geometry('300x250')

label = Label(text='Hello students KS 54')


root.resizable(False, False)
root.minsize(300, 300)
root.maxsize(500, 500)

icon = PhotoImage(file = 'favicon.png')
root.iconphoto(False, icon)
'''
root.attributes('-alpha', 0.8)
'''
'''
clicks = 0

def click_button():
    global clicks
    clicks+=1
    btn['text'] = f'Clicks {clicks}'

btn = ttk.Button(text='Click', command=click_button)
btn.pack()
btn['text']='Send'
btnText=btn['text']
print(btnText)
'''
'''
def print_info(widget, depth=0):
    widget_class=widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   "*depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth+1)
 
root.update()
print_info(root)

btn=ttk.Button(text='Click Me', state=['disabled'])
btn.pack(expand = True, anchor='nw', padx=[20, 60], pady=30)

btn=ttk.Button(text='Click')
btn.pack(fill=X)
'''

'''
btn1 = ttk.Button(text="BOTTOM")
btn1.pack(side=BOTTOM)
 
btn2 = ttk.Button(text="RIGHT")
btn2.pack(side=RIGHT)
 
btn3 = ttk.Button(text="LEFT")
btn3.pack(side=LEFT)
 
btn4 = ttk.Button(text="TOP")
btn4.pack(side=TOP)

btn = ttk.Button(text='Click')
btn.place(relx=0.4, rely=0.25)
'''
'''
btn = ttk.Button(text="Click me")
btn.place(relx=.5, rely=.5, anchor="c", width=80, height=40)

btn = ttk.Button(text="Click me")
btn.place(relx=0.8, rely=0.8, anchor="c", relwidth=0.33, relheight=0.25)
'''
'''
for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)
 

for r in range(3):
    for c in range(3):
        btn = ttk.Button(text=f"({r},{c})")
        btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4)
'''
'''
for c in range(2): root.columnconfigure(index=c, weight=1)
for r in range(2): root.rowconfigure(index=r, weight=1)
 
btn1 = ttk.Button(text="button1")
btn1.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)
 
btn3 = ttk.Button(text="button3")
btn3.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)
 
btn4 = ttk.Button(text="button4")
btn4.grid(row=1, column=1, ipadx=6,  ipady=6, padx=5, pady=5)
'''
'''
for c in range(2): root.columnconfigure(index=c, weight=1)
for r in range(2): root.rowconfigure(index=r, weight=1)
 
btn2 = ttk.Button(text="button 2")

btn2.grid(row=0, column=1, rowspan=2, ipadx=6, ipady=55, padx=5, pady=5)
 
btn1 = ttk.Button(text="button 1")
btn1.grid(row=0, column=0, ipadx=6, ipady=6, padx=5, pady=5)
 
btn3 = ttk.Button(text="button 3")
btn3.grid(row=1, column=0, ipadx=6,  ipady=6, padx=5, pady=5)
'''
'''
for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)
 
for r in range(3):
    for c in range(3):
        btn = ttk.Button(text=f"({r},{c})")
        btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4, sticky=NSEW)
'''
'''
def click():
    print('Hello')
btn = ttk.Button(text='Click Me', command=click)

def entered(event): 
    btn["text"] ="Entered"
 
def left(event): 
    btn["text"] ="Left"
 
btn = ttk.Button(text="Click")
btn.pack(anchor=CENTER, expand=1)
 
btn.bind("<Enter>", entered)
btn.bind("<Leave>", left)
'''
'''
def single_click(event): 
    btn["text"] ="Single Click"
 
def double_click(event): 
    btn["text"] ="Double Click"
 
btn = ttk.Button(text="Click")
btn.pack(anchor=CENTER, expand=1)
 
btn.bind("<ButtonPress-1>", single_click)
btn.bind("<Double-ButtonPress-1>", double_click)
'''
'''
clicks=0
def clicked(event): 
    global clicks
    clicks = clicks + 1
    btn["text"] =f"{clicks} Clicks"
btn = ttk.Button(text="Click")
btn.pack(anchor=CENTER, expand=1)
root.bind_class("TButton", "<Double-ButtonPress-1>", clicked)
 
label = ttk.Label(text="Hello STUDENT KS54", font=("Arial", 14))
label.pack()
'''
'''
python_logo = PhotoImage(file="favicon.png")
 
label = ttk.Label(image=python_logo, text="Python", compound="top")
label.pack()

label = ttk.Label(text="Hello Tkinter", borderwidth=2, relief="ridge", padding=8)
label.pack(expand=True)

label = ttk.Label(text="Hello Tkinter", background="#FFCDD2", foreground="#B71C1C", padding=8)
label.pack(expand=True)

ttk.Entry().pack(anchor=NW, padx=8, pady= 8)
'''
'''
def show_message():
    label["text"] = entry.get()     
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
  
btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)
 
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
'''
'''
def clear():
    entry.delete(0, END)
def display():
    label["text"] = entry.get()
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
entry.insert(0, "Hello World")
 
display_button = ttk.Button(text="Display", command=display)
display_button.pack(side=LEFT, anchor=N, padx=6, pady=6)
 
clear_button = ttk.Button(text="Clear", command=clear)
clear_button.pack(side=LEFT, anchor=N, padx=6, pady=6)

def is_valid(newval):
    result=  re.match("^\+{0,1}\d{0,11}$", newval) is not None
    if not result and len(newval) <= 12:
        errmsg.set("Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")
    else:
        errmsg.set("")
    return result
check = (root.register(is_valid), "%P")
 
phone_entry = ttk.Entry(validate="key", validatecommand=check) 
phone_entry.pack(padx=5, pady=5, anchor=NW)
'''
'''
message = StringVar()
 
label = ttk.Label(textvariable=message)
label.pack(anchor=NW, padx=6, pady=6)
 
entry = ttk.Entry(textvariable=message)
entry.pack(anchor=NW, padx=6, pady=6)
 
button = ttk.Button(textvariable=message)
button.pack(side=LEFT, anchor=N, padx=6, pady=6)


def click_button():
    value = clicks.get()
    clicks.set(value + 1)   
clicks = IntVar(value=0)  
btn = ttk.Button(textvariable=clicks, command=click_button)
btn.pack(anchor=CENTER, expand=1)
'''
'''
def check(*args):
    print(name)
    if name.get()=="admin":
        result.set("запрещенное имя")
    else: 
        result.set("норм")

name = StringVar()
result = StringVar()
name_entry = ttk.Entry(textvariable=name) 
name_entry.pack(padx=5, pady=5, anchor=NW)
check_label = ttk.Label(textvariable=result)
check_label.pack(padx=5, pady=5, anchor=NW) 
name.trace_add("write", check)
'''
'''
from tkinter.messagebox import showinfo
enabled = IntVar()  
enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
enabled_label = ttk.Label(textvariable=enabled)
enabled_label.pack(padx=6, pady=6, anchor=NW)

def checkbutton_changed():
    if enabled.get() == 1:
        showinfo(title="Info", message="Включено")
    else:
        showinfo(title="Info", message="Отключено")
 
enabled = IntVar()
  
enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled, command=checkbutton_changed)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
'''

from tkinter.messagebox import showinfo
'''
def checkbutton_changed():
    showinfo(title="Info", message=enabled.get())
enabled = StringVar()
enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled, offvalue="Отключено", onvalue="Включено", command=checkbutton_changed)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)

enabled_on = "Включено"
enabled_off = "Отключено"
enabled = StringVar(value=enabled_on)  
enabled_checkbutton = ttk.Checkbutton(textvariable=enabled, variable=enabled, offvalue=enabled_off, onvalue=enabled_on)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
'''
'''
def select():
    result = "Выбрано: "
    if python.get() == 1: result = f"{result} Python"
    if javascript.get() == 1: result = f"{result} JavaScript"
    if java.get() == 1: result = f"{result} Java"
    languages.set(result)
position = {"padx":6, "pady":6, "anchor":NW}
languages = StringVar()
languages_label = ttk.Label(textvariable=languages)
languages_label.pack(**position)
python = IntVar()
python_checkbutton = ttk.Checkbutton(text="Python", variable=python, command=select)
python_checkbutton.pack(**position)
javascript = IntVar()
javascript_checkbutton = ttk.Checkbutton(text="JavaScript", variable=javascript, command=select)
javascript_checkbutton.pack(**position)
java = IntVar()
java_checkbutton = ttk.Checkbutton(text="Java", variable=java, command=select)
java_checkbutton.pack(**position)
'''

'''
position = {"padx":6, "pady":6, "anchor":NW}
python = "Python"
java = "Java"
javascript = "JavaScript"
lang = StringVar(value=java)   
header = ttk.Label(textvariable=lang)
header.pack(**position)
python_btn = ttk.Radiobutton(text=python, value=python, variable=lang)
python_btn.pack(**position)
  
javascript_btn = ttk.Radiobutton(text=javascript, value=javascript, variable=lang)
javascript_btn.pack(**position)
java_btn = ttk.Radiobutton(text=java, value=java, variable=lang)
java_btn.pack(**position)
'''
'''
position = {"padx":6, "pady":6, "anchor":NW}
languages = ["Python", "JavaScript", "Java", "C#"]
selected_language = StringVar() 
 
header = ttk.Label(text="Выберите язык")
header.pack(**position)
 
def select():
    header.config(text=f"Выбран {selected_language.get()}")
 
for lang in languages:
    lang_btn = ttk.Radiobutton(text=lang, value=lang, variable=selected_language, command=select)
    lang_btn.pack(**position)
'''
'''
from itertools import chain
position = {"padx":6, "pady":6, "anchor":NW}
 
python = "Python"
java = "Java"
csharp = "C#"
lang = StringVar(value=java)  
header = ttk.Label(textvariable=lang)
header.pack(**position)
 
languages = [
    {"name": "Python", "img": PhotoImage(file="./favicon.png")},
    {"name": "C#", "img": PhotoImage(file="./csharp.png")},
    {"name": "Java", "img": PhotoImage(file="./java.png")}
]

lang = StringVar(value=languages[0]["name"])
header = ttk.Label(textvariable=lang)
header.pack(**position) 
for l in languages:
    btn = ttk.Radiobutton(value=l["name"], text=l["name"], variable=lang, image=l["img"], compound="top")
    btn.pack(**position)
'''
'''
lbl = ttk.Label(text="Hello")
lbl.pack()

frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
name_label = ttk.Label(frame, text="Введите имя")
name_label.pack(anchor=NW)
 
name_entry = ttk.Entry(frame)
name_entry.pack(anchor=NW)
 
frame.pack(anchor=NW, fill=X, padx=5, pady=5)
'''
'''
def create_frame(label_text):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    label = ttk.Label(frame, text=label_text)
    label.pack(anchor=NW)
    entry = ttk.Entry(frame)   
    entry.pack(anchor=NW)
    return frame

name_frame = create_frame("Введите имя")
name_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
 
email_frame = create_frame("Введите email")
email_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
'''
'''
languages = ["Python", "JavaScript", "C#", "Java"]
languages_var = Variable(value=languages)
 
languages_listbox = Listbox(listvariable=languages_var)
 
languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
'''
'''
def delete():
    selection = languages_listbox.curselection()
    languages_listbox.delete(selection[0])
def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)
root.columnconfigure(index=0, weight=4)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
root.rowconfigure(index=2, weight=1)
language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)
languages_listbox = Listbox()
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
languages_listbox.insert(END, "Python")
languages_listbox.insert(END, "C#")
ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)
'''
'''
def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)
root.columnconfigure(index=0, weight=4)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
languages = ["Python", "C#"]
languages_var = StringVar(value=languages)
language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)
languages_listbox = Listbox(listvariable=languages_var)
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=5)
'''
'''
def add():
    new_language = language_entry.get()
    languages.append(new_language)
    languages_var.set(languages)
root.columnconfigure(index=0, weight=4)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
languages = ["Python", "C#"]
languages_var = StringVar(value=languages)
language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)
languages_listbox = Listbox(listvariable=languages_var)
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=5)
'''
'''
def selected(event):
    selected_indices = languages_listbox.curselection()
    selected_langs = ",".join([languages_listbox.get(i) for i in selected_indices])
    msg = f"вы выбрали: {selected_langs}"
    selection_label["text"] = msg
languages = ["Python", "JavaScript", "C#", "Java"]
languages_var = Variable(value=languages)
selection_label = ttk.Label()
selection_label.pack(anchor=NW, fill=X, padx=5, pady=5)
languages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED)
languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
languages_listbox.bind("<<ListboxSelect>>", selected)
'''
'''
languages = ["Python", "C#", "Java", "JavaScript"]
languages_var = StringVar(value=languages)
languages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED)
languages_listbox.pack(expand=1, fill=BOTH)
languages_listbox.select_set(first=1, last=2)
'''
'''
languages = ['Python', 'JavaScript', 'C#', 'Java', 'C++', 'Rust', 'Kotlin',
             'Swift', 'PHP', 'Visual Basic.NET', 'F#', 'Ruby', 'R', 'Go', 'C',
             'T-SQL', 'PL-SQL', 'Typescript', 'Assembly', 'Frtran']
languages_var = StringVar(value=languages)
listbox = Listbox(listvariable=languages_var)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox["yscrollcommand"]=scrollbar.set

listbox.yview_scroll(number=1, what="units")
'''

'''
languages = ["Python", 'C#', 'Java', 'JavaScript']
combobox = ttk.Combobox(values=languages)
combobox.pack(anchor=NW, padx=6, pady=6)
languages_var = StringVar(value=languages[0])   
 
label = ttk.Label(textvariable=languages_var)
label.pack(anchor=NW, padx=6, pady=6)
 
combobox = ttk.Combobox(textvariable=languages_var, values=languages)
combobox.pack(anchor=NW, padx=6, pady=6)


def selected(event):
    selection = combobox.get()
    print(selection)
    label["text"] = f"вы выбрали: {selection}"
label = ttk.Label()
label.pack(anchor=NW, fill=X, padx=5, pady=5)
 
combobox = ttk.Combobox(values=languages, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", selected)
'''
'''
verticalScale = ttk.Scale(orient=VERTICAL, length=200, from_=1.0, to=100.0, value=50)
verticalScale.pack()
horizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, value=50)
horizontalScale.pack()

val = IntVar(value=10)
 
ttk.Label(textvariable=val).pack(anchor=NW)
 
horizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, variable=val)
horizontalScale.pack(anchor=NW)
'''
'''
def change(newVal):
    label['text'] = newVal
label = ttk.Label()
spinbox_var =StringVar(value= 22)
label.pack(anchor = NW)
scale = ttk.Scale(orient = HORIZONTAL, length=200, from_=2.0, to=100.0,
                  command = change)
scale.pack(anchor=NW)

spinbox = ttk.Spinbox(from_= 1.0, to =100.0)
spinbox.pack(anchor=NW)
'''
'''
def change():
    label["text"] = spinbox.get()
label = ttk.Label()
label.pack(anchor=NW)
spinbox = ttk.Spinbox(from_=1.0, to=100.0, command=change)
spinbox.pack(anchor=NW)
'''
'''
spinbox_var=StringVar()
languages=['Python', "JavaScript", 'C#', 'Java', "C++"]
label = ttk.Label(textvariable=spinbox_var)
label.pack(anchor=NW) 
spinbox = ttk.Spinbox(textvariable=spinbox_var, values=languages)
spinbox.pack(anchor=NW)
'''
'''
value_var = IntVar(value=30)
progressbar =  ttk.Progressbar(orient="horizontal", variable=value_var)
progressbar.pack(fill=X, padx=6, pady=6)
label = ttk.Label(textvariable=value_var)
label.pack(anchor=NW, padx=6, pady=6)
'''
'''
value_var = IntVar()
 
progressbar =  ttk.Progressbar(orient="horizontal", variable=value_var)
progressbar.pack(fill=X, padx=6, pady=6)
 
label = ttk.Label(textvariable=value_var)
label.pack(anchor=NW, padx=6, pady=6)
 
def start(): progressbar.start(1000)
def stop(): progressbar.stop()
start_btn = ttk.Button(text="Start", command=start)
start_btn.pack(anchor=SW, side=LEFT, padx=6, pady=6)
stop_btn = ttk.Button(text="Stop", command=stop)
stop_btn.pack(anchor=SE, side=RIGHT, padx=6, pady=6)
'''

progressbar =  ttk.Progressbar(orient="horizontal", mode="indeterminate")
progressbar.pack(fill=X, padx=10, pady=10)
start_btn = ttk.Button(text="Start", command=progressbar.start)
start_btn.pack(anchor=SW, side=LEFT, padx=10, pady=10)
stop_btn = ttk.Button(text="Stop", command=progressbar.stop)
stop_btn.pack(anchor=SE, side=RIGHT, padx=10, pady=10)














root.protocol('WM_DELETE_WINDOW', finish)
root.mainloop()
