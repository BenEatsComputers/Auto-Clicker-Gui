import pyautogui
from tkinter import *

root = Tk()
root.configure(bg="#000000")
root.title("Auto Clicker")

noc_entry = Entry(width=20)

def start():
	try:
		num_of_clicks = int(noc_entry.get())

		for i in range(0, num_of_clicks+1):
			pyautogui.click()
	except:
		pass

top_label = Label(text="Enter amount of clicks", bg="#000000", fg="#FFFFFF")
top_label.config(font=("Arial", 20))

button = Button(text="Start", fg="#FFFFFF", bg="#000000", borderwidth=1, command=start)
button.config(font=("Arial", "20"))

top_label.grid(row=0, column=0)
button.grid(row=0, column=1)
noc_entry.grid()

root.mainloop()