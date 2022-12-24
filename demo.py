import tkinter as tk
from tkinter import Label, ttk
from unicodedata import name
win = tk.Tk()
win.title('GUI')

#creating label

name_label = ttk.Label(win, text='enter your name: ')
name_label.grid(row=0 ,column=0, sticky=tk.W)

email_label = ttk.Label(win, text='enter your email: ')
email_label.grid(row=1 ,column=0, sticky=tk.W)

age_label = ttk.Label(win, text='enter your age: ')
age_label.grid(row=2 ,column=0, sticky=tk.W)

gender_label = ttk.Label(win, text='select your gender: ')
gender_label.grid(row=3 ,column=0, sticky=tk.W)


#create entry box

name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=16, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=16, textvariable=age_var)
age_entrybox.grid(row=2, column=1)

#create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=14, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.grid(row=3, column=1)
gender_combobox.current(0)

#radio button
usertype = tk.StringVar()
radio_tbn1 = ttk.Radiobutton(win, text='Student', value='Student', variable=usertype)
radio_tbn1.grid(row=4, column=0)

radio_tbn2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype)
radio_tbn2.grid(row=4, column=1)

#check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text='check if you want to subscribe to our newsletter', variable=checkbtn_var)
checkbtn.grid(row=5, columnspan=3)



#create a button

def action():
    user_name = name_var.get()
    user_email = email_var.get()
    user_age = age_var.get()
    print(f'{user_name} is {user_email} and your age is {user_age}')
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() ==0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'

    print(user_gender, user_type, subscribed)

    with open('file.txt', 'a') as f:
        f.write(f'{user_name}, {user_email}, {user_age}, {user_gender}, {user_type}, {subscribed}\n')

    name_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    name_label.configure(foreground='red')

    submit_btn.configure(foreground = 'blue')

submit_btn = ttk.Button(text='Submit', command=action)
submit_btn.grid(row=6, column=0)





win.mainloop()
