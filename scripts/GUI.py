#imports the tkinter library used to generate and moderate the GUI
import tkinter as tk
#imports the random library used to generate the random color in the change_ui_color function
import random

#creates the GUI and assigns it to root
root = tk.Tk()
#assigns the GUI a title
root.title("GUI Practice")

#takes care of the window size and resizability
root.geometry("1700x950")
root.minsize(1450,750)
root.state('zoomed')

#configures the amount of columns in a frame
def columnconfigure(self, columns):
    for i in range(columns):
        self.columnconfigure(i, weight=1)

#configures the amount of rows in a frame
def rowconfigure(self, rows):
    for i in range(rows):
        self.rowconfigure(i, weight=1)

#Main title start

#creates the main title frame
main_title_frame = tk.LabelFrame(root, bg="LightGray")

#sets its column configurations
columnconfigure(main_title_frame, 1)

#Creates the main title content components
main_title = tk.Label(main_title_frame, text="GUI Practice", font=("Arial", 50), bg="LightGray", pady= 50)
main_subtitle = tk.Label(main_title_frame, text="Made By Barak", font=("Arial", 25), bg="LightGray", pady=10)

#grids the main title content components
main_title.grid(row=0, column=0)
main_subtitle.grid(row=1, column=0)

main_title_frame.pack(fill="x", ipady=25, padx=300, pady=50)

#Main frame end


#Sub Widgets start

#creates variables necessary for the plus and minus functions
widget1_number_text = tk.IntVar()
widget1_number = 0
widget1_number_text.set(widget1_number)

#adds a number to the widget 1 number value
def add():
    global widget1_number
    widget1_number += 1
    widget1_number_text.set(widget1_number)

#adds a number to the widget 1 number value
def subtract():
    global widget1_number
    if widget1_number != 0:
        widget1_number -= 1
        widget1_number_text.set(widget1_number)

#transfers an rbg value to a hex value, necessery for the change_ui_color function
def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

#changes the UI color to a random color
def change_ui_color():
    color = (rgb2hex(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    root.configure(bg=color)
    sub_widgets_frame.configure(bg=color)

#changes the UI color back to its default white color
def default_UI_color():
    color = "#ffffff"
    root.configure(bg=color)
    sub_widgets_frame.configure(bg=color)

#creates the sub widgets frame
sub_widgets_frame = tk.LabelFrame(root, bg="White", borderwidth=0)
#sets its column configurations
columnconfigure(sub_widgets_frame, 3)

#Creates the widget 1 frame
widget1frame = tk.LabelFrame(sub_widgets_frame, bg="LightGray")
#sets its row and column configurations
rowconfigure(widget1frame, 10)
columnconfigure(widget1frame, 3)

#Loads arrows images
right_arrow_image = tk.PhotoImage(file="../assets/right.png")
left_arrow_image = tk.PhotoImage(file="../assets/left.png")

#Creates the widget 1 content components
widget1_title = tk.Label(widget1frame, text="Value", font=("Ariel", 38), bg="LightGray")
widget1_downbutton = tk.Button(widget1frame, image=left_arrow_image, bg="LightGray", command=subtract)
widget1_upbutton = tk.Button(widget1frame, image=right_arrow_image, bg="LightGray", command=add)
widget1_number_label = tk.Label(widget1frame, textvariable=widget1_number_text, font=("Arial", 25), bg="LightGray")

#grids each component in the right row and column
widget1_title.grid(row=0, column=1)
widget1_downbutton.grid(row=3, column=0, padx=25, pady=62.5)
widget1_upbutton.grid(row=3, column=2, padx=25)
widget1_number_label.grid(row=3, column=1)

#grids the widget
widget1frame.grid(row=0, column=0, sticky="wn", ipady=50)

#Creates the widget 2 frame
widget2frame = tk.LabelFrame(sub_widgets_frame, bg="LightGray")
#sets its row configurations
rowconfigure(widget2frame, 2)

#Creates the widget 2 content components
widget2_title = tk.Label(widget2frame, bg="LightGray", text="Did you know?", font=("Arial", 40))
widget2_content = tk.Label(widget2frame, bg="LightGray", text="I'm more of a backend developer than a front end developer (better at logical coding than UI designing)", font=("Arial", 22), wraplength=216)

#grids each component in the right row and column
widget2_title.grid(row=0, column=0)
widget2_content.grid(row=1,column=0)
widget2frame.grid(row=0, column=1, sticky="n", ipady=5)


#Creates the widget 3 frame
widget3frame = tk.LabelFrame(sub_widgets_frame, bg="LightGray")
#sets its row and column configurations
rowconfigure(widget3frame, 10)
columnconfigure(widget3frame, 1)

#Creates the widget 3 content components
widget3_title = tk.Label(widget3frame, bg="LightGray", text="UI Color", font=("Arial", 40))
widget3_change_color_button = tk.Button(widget3frame, bg="#0099ff", text="Change Color", font=("Arial", 20), command=change_ui_color)
widget3_default_color_button = tk.Button(widget3frame,  bg="#0099ff", text="Default Color", font=("Arial", 20), command=default_UI_color)

#grids each component in the right row and column
widget3_title.grid(row=0, column=0)
widget3_change_color_button.grid(row=4,column=0)
widget3_default_color_button.grid(row=7, column=0, pady=25, ipadx=5)
widget3frame.grid(row=0, column=2, sticky="ne", ipadx=73, ipady=59)

sub_widgets_frame.pack(fill="x", anchor="center", padx=300)
#sub widgets end

#creates the buttom frame
buttom_frame = tk.LabelFrame(root, bg="LightGray")
rowconfigure(buttom_frame, 3)
columnconfigure(buttom_frame, 3)

#created the buttom content
buttom_content = tk.Label(buttom_frame, bg="LightGray", text="I 🖤 my code, hope you do too!", font=("Arial", 40))

#grid the buttom content
buttom_content.grid(row=1, column=1)

#packs the buttom frame in the right location
buttom_frame.pack(fill="x", anchor="center", padx=300, pady=50, ipady=100)

#starts the root's main loop
root.mainloop()

