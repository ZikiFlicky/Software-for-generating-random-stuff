from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import pyperclip

# answer for text box

# official background color
bg_color = '#%02x%02x%02x' % (65, 75, 75)
# create screen
root = Tk()
root.title("Ziki random app")
root.configure(bg = bg_color)
icon = PhotoImage(file = r'ZikiLogo.png')
root.iconphoto(False, icon)
# button style
style = ttk.Style()
style.theme_use("vista")
style.configure("BW.TButton", borderwidth = 0, relief = 'flat')
print(ttk.Style().theme_names())
#Make screen size not changable
root.resizable(False, False)
# set size to be 600 by 600
root.geometry("600x600")
# create random number
randnumber = int
# list for random list
rand_list = list()
place_in_list = 0
def close_start_menu():
    rand_num_button.place_forget()
    rand_list_button.place_forget()
    generate_color_menu.place_forget()
    questionbutton.place_forget()
def ready_rand_num():
    # stops placing the menu buttons
    close_start_menu()
    # places text boxes
    min_num_text.place(x = 180, y = 160, anchor = "center")
    max_num_text.place(x = 420, y = 160, anchor = "center")
    min_num_box.place(x = 180, y = 200, anchor = "center")
    max_num_box.place(x = 420, y = 200, anchor = "center")
    # place back button
    back_button.place(x = 10, y = 10, anchor = "nw")
    get_random_number.place(x = 300, y = 400, anchor = ("center"))
def press_back():
    rand_num_button.place(x=300, y=100, anchor="center")
    rand_list_button.place(x = 300, y = 300, anchor = "center")
    generate_color_menu.place(x=300, y=500, anchor="center")
    questionbutton.place(x=600, y=0, anchor="ne")

    # when going back everything is removed from screen
    error_length_text.place_forget()
    color_display.place_forget()
    get_hex.place_forget()
    get_rgb.place_forget()
    get_color_button.place_forget()
    get_arg_text.place_forget()
    get_arg_entry.place_forget()
    get_arg_button.place_forget()
    warning_text.place_forget()
    rand_arg_text.place_forget()
    generate_again.place_forget()
    length_list_text.place_forget()
    length_list_entry.place_forget()
    get_length_button.place_forget()
    back_button.place_forget()
    min_num_text.place_forget()
    max_num_text.place_forget()
    min_num_box.place_forget()
    max_num_box.place_forget()
    get_random_number.place_forget()
    writeNum.place_forget()

    get_arg_entry.delete(0, 'end')
def get_random_num():
    global randnumber, min_num_box, max_num_box, writeNum
    # close_start_menu()
    writeNum.place_forget()
    try:
        writeNum = Label(root, text = (random.randint(int(min_num_box.get()), int(max_num_box.get()))), font = ("Courier New", "25"), fg = "OrangeRed4", bg = bg_color)
    except:# if error (not inputing a number), write "Please input numbers"
        writeNum = Label(root, text = ("Please input numbers"), font = ("Courier New", "25"), fg = "OrangeRed4", bg = bg_color)
    writeNum.place(x = 300, y = 500, anchor = "center")


def rand_list_prep():
    close_start_menu()
    back_button.place(x = 10, y = 10, anchor = "nw")
    length_list_text.place(x = 300, y = 200, anchor = "center")
    length_list_entry.place(x = 300, y = 300, anchor = "center")
    get_length_button.place(x = 300, y = 400, anchor = "center")
def rand_list_start():# after inputting length of list
    global rand_list, place_in_list,  get_arg_text
    if str(length_list_entry.get()).isdigit():
        length_list_entry.place_forget()
        length_list_text.place_forget()
        get_length_button.place_forget()
        rand_list = list()
        for num in range(int(length_list_entry.get())):
            rand_list.append(None)
        get_arg_text = Label(root, text = f'Enter argument 1 / {len(rand_list)}:', font = ("Courier New", "25"), bg = bg_color)
        get_arg_text.place(x = 300, y = 200, anchor = "center")
        get_arg_entry.place(x = 300, y = 300, anchor = "center")
        get_arg_button.place(x = 300, y = 400, anchor = "center")
        error_length_text.place_forget()
    else:
        error_length_text.place(x = 300, y = 500, anchor = "center" )
def get_arg():#adding an argument
    global place_in_list, rand_list, rand_arg_text, get_arg_text
    if place_in_list < len(rand_list):
        get_arg_text.place_forget()
        get_arg_text = Label(root, text = f'Enter argument {place_in_list + 2} / {len(rand_list)}:', font = ("Courier New", "25"), bg = bg_color)
        get_arg_text.place(x = 300, y = 200, anchor = "center")
        if not get_arg_entry.get() in rand_list:
            rand_list[place_in_list] = str(get_arg_entry.get())
            place_in_list += 1
            warning_text.place_forget()
        else:
            warning_text.place(x = 300, y = 500, anchor = "center")
    if place_in_list == len(rand_list):
        rand_arg_text = Label(root, text = random.choice(rand_list), wraplength = 600,font = ("Courier New", "30"), fg = "RoyalBlue1", bg = bg_color)
        rand_arg_text.place(x = 300, y = 300, anchor = "center")
        get_arg_text.place_forget()
        get_arg_entry.place_forget()
        get_arg_button.place_forget()
        generate_again.place(x = 300, y = 200, anchor = "center")
        place_in_list = 0
    get_arg_entry.delete(0, "end")
def rand_again():
    global rand_arg_text, get_arg_text
    get_arg_text.place_forget()
    rand_arg_text.place_forget()
    rand_arg_text = Label(root, text = random.choice(rand_list), font = ("Courier New", "30"), wraplength = 600, fg = "RoyalBlue1", bg = bg_color)
    rand_arg_text.place(x = 300, y = 300, anchor = "center")
def setup_color():
    close_start_menu()
    get_color_button.place(x = 300, y = 300, anchor = "center")
    back_button.place(x = 10, y = 10, anchor = "nw")
def get_color():
    global color_display, R, G, B
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    color_display.place_forget()
    color_display = Label(root, text = "▣", font = ("Courier New", "100"), fg = '#%02x%02x%02x' % (R, G, B), bg = bg_color)
    color_display.place(x = 300, y = 500, anchor = "center")
    get_hex.place(x = 300, y = 200, anchor = "center")
    get_rgb.place(x = 300, y = 100, anchor = "center")
def copy_hex():
    global R, G, B
    pyperclip.copy('#%02x%02x%02x' % (R, G, B))
def copy_rgb():
    global R, G, B
    pyperclip.copy(f'{R}, {G}, {B}')
def show_message_box():
    yesno = messagebox.askyesno("אלון אוכל מאוד", """Thanks for using my software!!!
I really appreciate it.
Do you enjoy the application?""")
    if yesno:
        messagebox.showinfo("Thanks!", """I really appreciate your support!
Enjoy the app!""")
    else:
        messagebox.askretrycancel("Try again", "Please try again")
        show_message_box()
# menu:
questionimage = PhotoImage(file = "Question_mark.png")
questionbutton = ttk.Button(root, image = questionimage, takefocus = False, command = show_message_box)
rand_num_button = Button(root, text = "Generate random number" , font  = ("Courier New", "20"), command = ready_rand_num)
back_button = Button(root, text = "⏎", font = ("Courier New", "20"), width = 4, height = 1, command = press_back, fg = "cyan4")
rand_list_button = Button(root, text = "Generate random list" , font = ("Courier New", "20"), command = rand_list_prep)
generate_color_menu = Button(root, text = "Generate random color", font = ("Courier New", "20"), command = setup_color)
# inside random number
min_num_box = Entry(root, font = ("Courier New", "15"))
max_num_box = Entry(root, font = ("Courier New", "15"))
min_num_text = Label(root, text = ("Minimum number"), font = ("Courier New", "15"), bg = bg_color)
max_num_text = Label(root, text = ("Maximum number"), font = ("Courier New", "15"), bg = bg_color)
get_random_number = Button(root, text = ("Get a random number"), font = ("Courier New", "25"), wraplength = 600, command = get_random_num)
writeNum = Label(root, font = ("Courier New", "25"))
# inside random list (//1//)
length_list_text = Label(root, text = "Length of list:", font = ("Courier New", "25"), bg = bg_color)
length_list_entry = Entry(root, font = ("Courier New", "15"))
get_length_button = Button(root, text = "Continue", font = ("Courier New", "15"), command = rand_list_start)
error_length_text = Label(root, text = "Please input a number", font = ("Courier New", "20"), fg = "tomato", bg = bg_color)
# inside random list (//2//)
get_arg_text = Label(root, font = ("Courier New", "25"))
get_arg_entry = Entry(root, font = ("Courier New", "15"))
get_arg_button = Button(root, text = "get argument", font = ("Courier New", "20"), command = get_arg)
warning_text = Label(root, text = "You can't duplicate an input", font = ("Courier New", "15"), fg = "tomato", bg = bg_color)
rand_arg_text = Label(root, font = ("Courier New", "20"), wraplength = 600, fg = "RoyalBlue1", bg = bg_color)
generate_again = Button(root, text = "↺", font = ("arial", "30"), width = 3, height = 1, command = rand_again)
# random color generator
get_color_button = Button(root, text = "Get a random color", font = ("Courier New", "20"), command = get_color)
color_display = Label(root, text = "▣", font = ("Impact", "100"), bg = bg_color)
get_hex = Button(root, text = "Copy hex to clipboard", font = ("Courier New", "20"), command = copy_hex)
get_rgb = Button(root, text = "Copy RGB to clipboard", font = ("Courier New", "20"), command = copy_rgb)
# place everything at the beginning
press_back()
root.mainloop()