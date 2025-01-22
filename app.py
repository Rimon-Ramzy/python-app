from tkinter import *


root = Tk()
root.geometry("800x600")




def login_fun() :
  title['bg'] = "red"

def signup_fun() :
  title['bg'] = "gold"

title =Label(root, text="hello!")
title.grid(row=0, column=1)
#Email
email_label = Label(root, text="Email:")
email_label.grid(row=1, column=0)
#Email Entry
email_frame = Frame(root)
email_frame.grid(row=1, column=1)
email_entry = Entry(email_frame, width=40)
email_entry.pack()
#Password
pass_label = Label(root, text="Paaword:")
pass_label.grid(row=2, column=0)
#Password Entry
pass_frame = Frame(root)
pass_frame.grid(row=2, column=1)
pass_entry = Entry(pass_frame, show="*", width=40)
pass_entry.pack()

#Login Button
login_btn = Button(root, text="Login", command=login_fun)
login_btn.grid(row=3, column=0)
login_btn.grid(row=3, column=0)

signup = Label(root, text= "If don't have account")
signup.grid(row=4, column=2)
signup_btn = Button(root, text="Sign Up", command= signup_fun)
signup_btn.grid(row=5, column=2)


root.mainloop()