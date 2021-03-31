from tkinter import *
import tkinter.messagebox as box
import random
window = Tk()
window.title('Pick an operation and your favorite color!')
frame = Frame(window)
book = StringVar()
# all of the packages defined and the title

def mult():
  a = random.randint(1, 10)
  b = random.randint(1, 10)
  ab = a * b
  rab = f"{a} * {b} = {ab}"
  box.showinfo('Success!', \
	'The result:\n' + rab)

def add():
  c = random.randint(20, 30)
  d = random.randint(40, 50)
  cd = c + d
  rcd = f"{c} + {d} = {cd}"
  box.showinfo('Success!', \
	'The result:\n' + rcd)

def exp():
  e = random.randint(1, 10)
  g = random.randint(1, 10)
  eg = e ** g
  reg = f"{e} ** {g} = {eg}"
  box.showinfo('Success!', \
	'The result:\n' + reg)

def color() :
  if window.cget('bg') == 'yellow' :
    window.configure(bg = 'red')
  elif window.cget('bg') == 'red':
    window.configure(bg = 'orange')
  else :
    window.configure(bg = 'yellow')

def dialog() :
	box.showinfo('Your favorite color...' , \
	'Your favorite color is... \n' + book.get())
# custom defined functions for each operation occuring

bt1 = Button(window, text = 'Multiply!', command = mult)
# each time returns a random result from the mult function line 11

bt2 = Button(window, text = 'Addition!', command = add)
# each time returns a random result from the add function line 19

bt3 = Button(window, text = 'Exponentiate!', command = exp)
# each time returns a random result from the exp function line 27

ra1 = Radiobutton(frame, text = 'Red', \
	variable = book, value = 'a fiery red', command = color)
ra2 = Radiobutton(frame, text = 'Orange', \
	variable = book, value = 'a warm orange', command = color)
ra3 = Radiobutton(frame, text = 'Yellow', \
	variable = book, value = 'a sunny yellow', command = color)
# randomly toggles color from color function line 35

sub = Button(frame , text = 'Pick it!' , command = dialog)
# all of the buttons defined

bt1.pack(side = BOTTOM)
bt2.pack(side = BOTTOM)
bt3.pack(side = BOTTOM)
sub.pack(side = BOTTOM, padx = 5)
ra1.pack(side = BOTTOM)
ra2.pack(side = BOTTOM)
ra3.pack(side = BOTTOM)
# defines the positions of the buttons

frame.pack(padx = 160, pady = 30)
window.mainloop()
# defines the window's main dimensions and runs it
