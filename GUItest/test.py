import tkinter as tk

# create a tkinter window
window = tk.Tk()

# set the window size to 500x500
window.geometry('500x500')

# create a button widget in the middle of the window with the text 'Talk to Chat'
button = tk.Button(window, text='Talk to Chat', bg='light green', width=15, height=2)

# add a hover effect to the button
def change_color(event):
    button.config(bg='red')
def change_color_back(event):
    button.config(bg='light green')
button.bind('<Enter>', change_color)
button.bind('<Leave>', change_color_back)

# place the button in the middle of the window
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# start the tkinter event loop
window.mainloop()
