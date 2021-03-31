from tkinter import *
window = Tk()
# imports the package to show the window and defines it

window.title('Color Switching!')
# window title

btn_end = Button(window , text = 'Exit' , command = exit)
# the end button

def tog() :
	if window.cget('bg') == 'blue' :
		window.configure(bg = 'red')
	else :
		window.configure(bg = 'blue')
# the window will come blank, but if you press "Color Switch", it will turn blue

btn_tog = Button(window , text = 'Color Switch!' , command = tog)
# press da button!

btn_tog.pack(padx = 120 , pady = 20)
btn_end.pack(padx = 120 , pady = 20)
# defines the buttons measurments 

window.mainloop()
