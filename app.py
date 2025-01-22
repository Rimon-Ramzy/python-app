from tkinter import *

# ------------- ROOT CONFIG -------------
root = Tk()
root.geometry("800x600")
root.title("my app")
root.config(bg="sky blue")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)


# ------------- PROFILE CONFIG -------------
profile = Tk()
profile.withdraw()
profile.geometry("800x600")
profile.title("User Data")
profile.config(bg="sky blue")


# ------------- SIGNUP CONFIG -------------
signup_profile = Tk()
signup_profile.withdraw()
signup_profile.geometry("800x600")
signup_profile.title("Sign Up")
signup_profile.config(bg="sky blue")
signup_profile.grid_columnconfigure(0, weight=1)
signup_profile.grid_columnconfigure(1, weight=1)
signup_profile.grid_columnconfigure(2, weight=1)
signup_profile.grid_rowconfigure(0, weight=1)
signup_profile.grid_rowconfigure(1, weight=1)
signup_profile.grid_rowconfigure(2, weight=1)
signup_profile.grid_rowconfigure(3, weight=1)
signup_profile.grid_rowconfigure(4, weight=1)
signup_profile.grid_rowconfigure(5, weight=1)



def open_profile(data):
    root.withdraw()
    signup_profile.withdraw()

    profile.deiconify()
    email_entry.delete(0, END)

    logout_btn = Button(profile, text="Logout", font=("Arial", 16), command=logout_fun)
    logout_btn.place(x= 700, y= 10)

    label = Label(profile, text=f"Hello: {data}", font=("Arial", 16))
    label.place(x= 320, y= 100)

    profile.mainloop()

def login_fun(name):
    user_data = name
    open_profile(user_data)

def logout_fun() :
  profile.withdraw()
  root.deiconify()

def signup_fun():
  root.withdraw()
  signup_profile.deiconify()
  #Name
  name_label_sign = Label(signup_profile, text="User Name:", font=("Roboto", 20), bg="sky blue")
  name_label_sign.grid(row=1, column=0)
  #Name Entry
  name_frame_sign = Frame(signup_profile, padx=5, pady=8, bg="lightblue")
  name_frame_sign.grid(row=1, column=1)
  name_entry_sign = Entry(name_frame_sign, width=40, font=80, bg="sky blue")
  name_entry_sign.pack()
  #Email
  email_label_sign = Label(signup_profile, text="Email:", font=("Roboto", 20), bg="sky blue")
  email_label_sign.grid(row=2, column=0)
  #Email Entry
  email_frame_sign = Frame(signup_profile, padx=5, pady=8, bg="lightblue")
  email_frame_sign.grid(row=2, column=1)
  email_entry_sign = Entry(email_frame_sign, width=40, font=80, bg="sky blue")
  email_entry_sign.pack()
  #Password
  pass_label_sign = Label(signup_profile, text="Paaword:", font=("Roboto", 20), bg="sky blue")
  pass_label_sign.grid(row=3, column=0)
  #Password Entry
  pass_frame_sign = Frame(signup_profile, padx=5, pady=8, bg="lightblue")
  pass_frame_sign.grid(row=3, column=1)
  pass_entry_sign = Entry(pass_frame_sign, show="*", width=40, font=80, bg="sky blue")
  pass_entry_sign.pack()
  #Signup Button
  signup_btn = Button(signup_profile, text="Sign Up",font=("Roboto", 20), bg = "sky blue", command=lambda: login_fun(name_entry_sign.get()))
  signup_btn.grid(row=4, column=0, columnspan=3, sticky="we" , padx= 50)
  #Go To Login
  login_frame = Frame(signup_profile)
  login_frame.grid(row=5, column=0, columnspan=3)
  login_btn_go = Button(login_frame, text="Login", font=("Roboto", 10), bg="sky blue", command=back_to_login)
  login_label_go = Label(login_frame, text="If you have an account already, ", font=("Roboto", 10), bg="sky blue")
  login_label_go.pack(side="left")
  login_btn_go.pack(side="left")

  signup_profile.mainloop()


def back_to_login() :
  signup_profile.withdraw()
  root.deiconify()



#---------- LOGIN PAGE ----------
title =Label(root, text="hello!", font=("Roboto", 30), fg="black", bg="sky blue")
title.grid(row=0, column=1,sticky="nsew")
#Email
email_label = Label(root, text="Email:", font=("Roboto", 20), bg="sky blue")
email_label.grid(row=1, column=0)
#Email Entry
email_frame = Frame(root, padx=5, pady=8, bg="lightblue")
email_frame.grid(row=1, column=1)
email_entry = Entry(email_frame, width=40, font=80, bg="sky blue")
email_entry.pack()
#Password
pass_label = Label(root, text="Paaword:", font=("Roboto", 20), bg="sky blue")
pass_label.grid(row=2, column=0)
#Password Entry
pass_frame = Frame(root, padx=5, pady=8, bg="lightblue")
pass_frame.grid(row=2, column=1)
pass_entry = Entry(pass_frame, show="*", width=40, font=80, bg="sky blue")
pass_entry.pack()
#Login Button
login_btn = Button(root, text="Login",font=("Roboto", 20), bg = "sky blue", command=lambda: login_fun(email_entry.get()))
login_btn.grid(row=3, column=0, columnspan=3, sticky="we" , padx= 50)
login_btn.grid(row=3, column=0, columnspan=3)
#signup button
signup = Label(root, text= "If don't have account", font=("Roboto", 10), bg="sky blue")
signup.grid(row=4, column=2)
signup_btn = Button(root, text="Sign Up",font=("Roboto", 10), bg = "sky blue", command= signup_fun)
signup_btn.grid(row=5, column=2)


root.mainloop()