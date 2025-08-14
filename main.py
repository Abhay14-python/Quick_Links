import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import webbrowser
# this is the button function ----------------------- #
def open_website():
    if combo.get() == "Exercise":
        webbrowser.open("https://musclewiki.com")
    elif combo.get() == "Study":
        webbrowser.open("https://www.khanacademy.org")
    elif combo.get() == "Learning Python":
        webbrowser.open("https://www.w3schools.com/python")
    elif combo.get() == "Reading":
        webbrowser.open("https://openlibrary.org")

# this is the combo box function ------------------------ #
def label_edit():
    button["state"] = "normal"
    if combo.get() == items[1]:
        combo_label_text.set("Best website for Exercising purposes is Musclewiki")
    elif combo.get() == items[2]:
        combo_label_text.set("Best website for Studying purposes is Khan Academy")
    elif combo.get() == items[3]:
        combo_label_text.set("Best website for Python learning purposes is W3Schools")
    elif combo.get() == items[4]:
        combo_label_text.set("Best website for Reading purposes is Open Library")
    elif combo.get() == items[0]:
        button["state"] = "disabled"
        combo_label_text.set(" ")

# window -------------------------------- #
window = ttk.Window(themename = "cyborg")
window.geometry("650x300")
window.title("Combo and Spin")

# label ----------------------------------- #
label = ttk.Label(
    window , 
    text = "What do you want to do?" , 
    font = "Calibri 30 bold"
)
label.pack(pady = 10)
# combobox ---------------------------------- #
time_string = tk.StringVar(value = "Choose")
items = ("Choose" , "Exercise" , "Study" , "Learning Python" , "Reading")
combo = ttk.Combobox(
    window , 
    textvariable = time_string)
combo["values"] = items
# combo.configure(values = items)
combo.pack(pady = 10)

# events ----------------------------------------- #
combo.bind(
    "<<ComboboxSelected>>" , 
    lambda event: label_edit()
)
combo_label_text = tk.StringVar()
combo_label = ttk.Label(
    window , 
    text = " " , 
    font = "Calibri 20" , 
    textvariable = combo_label_text
)
combo_label.pack(pady = 10)

# button -------------------------------------------- #
button = ttk.Button(
    window , 
    text = "Open Website" , 
    state = "disabled" , 
    command = open_website , 
    bootstyle = "Solid blue-outline"
)
button.pack(pady = 10)
# run ------------------------------------------------- #

window.mainloop()


print("Thanks for your support!")
