from tkinter import *
import tkinter.messagebox as box
# this will import the packages needed to make the window appear

window = Tk()
window.title('🌈 Pick your favorite color!')
# define the window and it's title

frame = Frame(window)
book = StringVar()
# final definition and the definition of the choices

radio_1 = Radiobutton(frame, text = '🔴 Red', \
	variable = book, value = '🔴 a fiery red')
radio_2 = Radiobutton(frame, text = '🟠 Orange', \
	variable = book, value = '🟠 a warm orange')
radio_3 = Radiobutton(frame, text = '🟡 Yellow', \
	variable = book, value = '🟡 a sunny yellow')
# the buttons to pick from

radio_1.select()
# this button will be pre-selected upon running

def dialog() :
	box.showinfo('Your favorite color...' , \
	'Your favorite color is... \n' + book.get())
# pressing the button (code on line 29) shows this pop-up

btn = Button(frame , text = 'Pick it!' , command = dialog)
# the selection button

btn.pack(side = RIGHT, padx = 5)
radio_1.pack(side = LEFT)
radio_2.pack(side = LEFT)
radio_3.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)
# defines the geometry and dimensions of the window

window.mainloop()
# puts the window into function and a loop
