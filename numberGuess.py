import tkinter
from tkinter import *
import random
from tkinter import messagebox



root = Tk()
root.geometry("400x400")



# Game Variables:

random_number = random.randint(1,10)
user_input = None
total_attemps = 10
used_attemps = 0
selected_difficulty = None
entry = None

attemps_grid = [
	["EASY",10,10],
	["MEDIUM",5,50],
	["HARD",3,100]
]




def check_answer():
	global used_attemps
	global total_attemps
	global selected_difficulty
	global user_input

	if selected_difficulty == None:
		messagebox.showerror("Error!","Please select a difficulty.")
	else:
		if entry.get() == '':
			messagebox.showerror(title="Null Input",message="Please enter a number.")
			return
		user_input = int(entry.get())


		print(user_input)
		print(random_number)
		if user_input == random_number:
			print("Correct Answer")
			messagebox.showinfo(title="Correct Answer",message="Congratulations! You did it correctly.")
			root.quit()

		else:

			used_attemps +=1
			if used_attemps == total_attemps:
				messagebox.showerror("You Lost!",f"Game Over. Correct Answer was {random_number}")
				root.quit()
			else:
				messagebox.showerror(title="Wrong Answer",message=f"Wrong! You now have {total_attemps-used_attemps} attemps left.")
				load_gui()





def select_difficulty(difficulty):
	global selected_difficulty
	global total_attemps
	global used_attemps
	global random_number
	selected_difficulty = difficulty
	used_attemps = 0
	for diff in attemps_grid:
		if diff[0] == difficulty:
			total_attemps = diff[1]
			random_number = random.randint(0,diff[2])

	print(random_number)

	load_gui()
	return None


def load_gui():
	global entry
	global root
	global selected_difficulty
	header = Label(root,text="                       Welcome to the game!"                        )
	header.grid(row=0,column=1)

	diff_frame = LabelFrame(root,padx="50",pady="20")
	diff_frame.grid(row=1,column=1,padx="70",pady="10")

	easy_button = Button(diff_frame,text="EASY", command = lambda: select_difficulty("EASY"))
	easy_button.grid(row=0,column=1)

	medium_button = Button(diff_frame,text="MEDIUM", command = lambda: select_difficulty("MEDIUM"))
	medium_button.grid(row=1,column=1)

	hard_button = Button(diff_frame,text="HARD", command = lambda: select_difficulty("HARD"))
	hard_button.grid(row=2,column=1)


	diff_label = Label(root,text=f"               Selected Difficulty:{selected_difficulty}              ")
	diff_label.grid(row=4,column=1)


	users_frame = LabelFrame(root, padx="20",pady="20")
	users_frame.grid(row=5,column=1,padx="100",pady="30")
	entry = Entry(users_frame)
	entry.grid(row=0,column=1)

	rem_attemps = Label(users_frame,text=f"Remaining Attemps:{total_attemps-used_attemps}")
	rem_attemps.grid(row=1,column=1)

	check_button = Button(users_frame,text="Check",command=check_answer)
	check_button.grid(row=2,column=1)


load_gui()



root.mainloop()