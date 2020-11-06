from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog ,messagebox


window=Tk()
window.title("File Handling")
window.configure(background="blue", relief="solid")
window.geometry("700x500")

def create_file():

    text_file= open('/home/user/Desktop/myweekendactivities.txt', "w")

    text_file.write("This is a text file\n")
    

    text_file.close()
    




def clear_function():
    entry1.delete(1.0,END)
    #use this for clearing. use 'destroy' to exit.


#define function to stop and exit the program.
def close_window():
  window.destroy()
    


def display_file():
    text_file=open('/home/user/Desktop/myweekendactivities.txt',"r")
    entry1.insert(END, text_file.read())




def append_file():
      text_file= open('/home/user/Desktop/myweekendactivities.txt',"a")
      text_file.write(entry1.get("1.0","end-1c")+"\n")
      text_file.close()





def save_file():
     text_file=open('/home/user/Desktop/myweekendactivities.txt',"w")
     text_file.write(entry1.get(1.0, END))
     text_file.close()



lb1=Label(window,text="My Weekeend Activities:", font="arial 18 bold")
lb1.pack()


entry1=Text(window,width=40, height=10)
entry1.pack(pady=20)

open_button=Button(window, text="Create Textfile", command=create_file)
open_button.place(x=100,y=260)

display_button=Button(window, text="Display", command=display_file)
display_button.place(x=240,y=260)

append_button=Button(window, text="Append Data", command=append_file)
append_button.place(x=405,y=260)

my_clearbutton=Button(window,text="Clear", command=clear_function)
my_clearbutton.place(x=330,y=260)

exit_button = Button (text = "Exit", command = close_window)
exit_button.place(x=530,y=260)


window.mainloop()
