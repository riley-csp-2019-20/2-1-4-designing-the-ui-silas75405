import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.wm_title("authorization")



# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")


lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack(padx=50)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack(padx=50)

ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack()

#functions
def test_button():
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_display_pass.config(text = password)


button_login = tk.Button(frame_login, text="Login", command = test_button)
button_login.pack()

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

lbl_display_pass = tk.Label(frame_auth, text = "test")
lbl_display_pass.pack()

frame_login.tkraise()

root.mainloop()