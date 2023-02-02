import tkinter as tk
import random

root = tk.Tk()

root.title("GUI Practice")

root.geometry("980x600")
root.minsize(980,350)
root.state('zoomed')

#Main Widget
titleframe = tk.LabelFrame(root, bg="LightGray")

titleframe.columnconfigure(0, weight=1)

title = tk.Label(titleframe, text="GUI Practice", font=("Arial", 50), bg="LightGray", pady= 50)
subtitle = tk.Label(titleframe, text="Made By Barak", font=("Arial", 25), bg="LightGray", pady=10)

title.grid(row=0, column=0)
subtitle.grid(row=1, column=0)

titleframe.pack(fill="x", ipady=25, padx=300, pady=50)





#Sub Widgets


def columnconfigure(self, columns):
    for i in range(columns):
        self.columnconfigure(i, weight=1)

def rowconfigure(self, rows):
    for i in range(rows):
        self.rowconfigure(i, weight=1)

widget1_number_text = tk.IntVar()
widget1_number = 0
widget1_number_text.set(widget1_number)



def plus_number():
    global widget1_number
    widget1_number += 1
    widget1_number_text.set(widget1_number)


def minus_number():
    global widget1_number
    if widget1_number != 0:
        widget1_number -= 1
        widget1_number_text.set(widget1_number)
def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def change_UI_color():
    color = (rgb2hex(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    root.configure(bg=color)
    sub_widgetsframe.configure(bg=color,  borderwidth=0)

def default_UI_color():
    color = "#ffffff"
    root.configure(bg=color)
    sub_widgetsframe.configure(bg=color,  borderwidth=0)

sub_widgetsframe = tk.LabelFrame(root, bg="White")
columnconfigure(sub_widgetsframe, 3)

#creates the widget 1 frame
widget1frame = tk.LabelFrame(sub_widgetsframe, bg="LightGray")
rowconfigure(widget1frame, 2)
columnconfigure(widget1frame, 3)

#load arrows images
right_arrow_image = tk.PhotoImage(file="assets/right.png")
left_arrow_image = tk.PhotoImage(file="assets/left.png")

widget1_title = tk.Label(widget1frame, text="Value", font=("Ariel", 38), bg="LightGray")
widget1_downbutton = tk.Button(widget1frame, image=left_arrow_image, bg="LightGray", command=minus_number)
widget1_upbutton = tk.Button(widget1frame, image=right_arrow_image, bg="LightGray", command=plus_number)
widget1_number_label = tk.Label(widget1frame, textvariable=widget1_number_text, font=("Arial", 25), bg="LightGray")

widget1_title.grid(row=0, column=1)
widget1_downbutton.grid(row=1, column=0, padx=25)
widget1_upbutton.grid(row=1, column=2, padx=25)
widget1_number_label.grid(row=1, column=1)

widget1frame.grid(row=0, column=0, sticky="wn", ipady=112)
#size = 346^2


widget2frame = tk.LabelFrame(sub_widgetsframe, bg="LightGray")
rowconfigure(widget2frame, 2)

widget2_title = tk.Label(widget2frame, bg="LightGray", text="Did you know?", font=("Arial", 40))
widget2_content = tk.Label(widget2frame, bg="LightGray", text="I'm more of a backend developer than a front end developer (better at logical coding than UI designing)", font=("Arial", 25), wraplength=275)


widget2_title.grid(row=0, column=0)
widget2_content.grid(row=1,column=0)
widget2frame.grid(row=0, column=1, sticky="n", ipady=4)
# size = 346px^2


widget3frame = tk.LabelFrame(sub_widgetsframe, bg="LightGray")
rowconfigure(widget3frame, 3)
columnconfigure(widget3frame, 1)

color_entry = tk.StringVar()
widget3_title = tk.Label(widget3frame, bg="LightGray", text="UI Color", font=("Arial", 40))
widget3_change_color_button = tk.Button(widget3frame, bg="#0099ff", text="Change Color", font=("Arial", 20), command=change_UI_color)
widget3_default_color_button = tk.Button(widget3frame,  bg="#0099ff", text="Default Color", font=("Arial", 20), command=default_UI_color)

widget3_title.grid(row=0, column=0)
widget3_change_color_button.grid(row=1,column=0)
widget3_default_color_button.grid(row=2, column=0, pady=25)
widget3frame.grid(row=0, column=2, sticky="ne", ipadx=73, ipady=59)
#size = 346px^2

sub_widgetsframe.pack(fill="x", anchor="center", padx=300)


root.mainloop()

