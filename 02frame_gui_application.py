import tkinter as tk
from tkinter import ttk
import os
root=tk.Tk()
root.title("frame")

label_frame=tk.LabelFrame(root,text="Fill the data")
label_frame.grid(row=0,column=0,padx=2,pady=2)

# create lebel

label_create=['Enter your name : ','Enter your email : ','Enter your age : ','Select your gender : ','Select your state : ','Select your city : ']

for i in range(len(label_create)):
    create_label = "label" + str(i)
    create_label = ttk.Label(label_frame,text=label_create[i])
    create_label.grid(row=i,column=0, sticky=tk.W,padx=2,pady=2)

# create entrybox
name_var=tk.StringVar()
user_info = {
    "name" : tk.StringVar(),
    "email" : tk.StringVar(),
    "age" : tk.StringVar(),
    "gender" : tk.StringVar(),
    "state" : tk.StringVar(),
    "city" : tk.StringVar()
}
counter = 0
for i in user_info:
    entry_box = "entry" + i
    entry_box = ttk.Entry(label_frame, width=16, textvariable = user_info[i])
    entry_box.grid(column=1, row=counter, padx=2, pady=2)
    counter += 1

def don ():
    print(user_info['name'].get())
    print(user_info['email'].get())
    print(user_info['age'].get())
    print(user_info['gender'].get())
    print(user_info['state'].get())
    print(user_info['name'].get())
    

    
submit_btn=ttk.Button(root,text="Submit",command=don)
submit_btn.grid(row=1,columnspan=2)

root.mainloop()