from math import *
from tkinter import *
from builtins import float
from decimal import Decimal
from tkinter import ttk
import pyperclip
from winsound import *
import threading
import os

global path
path ='\\'.join(os.path.realpath(__file__).split("\\")[:-1])
backslesh = ' \ '
backslesh=backslesh.replace(" ", "")
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
def discriminant():
	disc_wind=Tk()
	disc_wind.title("Discriminant")
	disc_wind.geometry("600x320")
	disc_wind.resizable(0, 0)
	disc_wind.focus_force()
	disc_wind.configure(bg="#D3D3D3")
	# icon=PhotoImage(file="icons\\discriminant.gif")
	# disc_wind.tk.call("wm", "iconphoto", disc_wind._w, icon)

	def calc():
		if a_entry.get() == "" or b_entry.get() == "":
			pass
		else:
			a=(a_entry.get() if a_entry.get()!="" else "")
			b=(b_entry.get() if b_entry.get()!="" else "")
			c=(c_entry.get() if c_entry.get()!="" else 0)
			try:
				a=int(a)
				b=int(b)
				c=int(c)
				D=b**2-4*a*c
				if D>=0:
					x1=(-b+(D**0.5))/2*a
					x2=(-b-(D**0.5))/2*a
					text="Discriminant = b^2 - 4 * a * c"
					text+="\nDiscriminant is ("+str(b)+"^2) -4 * ("+str(a)+") * ("+str(c)+") = "+str(D)

					text+="\n\nX1 = ( -b + scrt( D ) ) / 2 * a"
					text+="\nX1 = ( "+str(-b)+"+"+"scrt( "+str(D)+" ) ) / 2 * "+str(a)+" = "+str(x1)

					text+="\n\nX2 = ( -b - scrt( D ) ) / 2 * a"
					text+="\nX2 = ( "+str(-b)+"-"+"scrt( "+str(D)+" ) ) / 2 * "+str(a)+" = "+str(x2)

					result_text.configure(state="normal")
					result_text.delete(1.0, END)
					result_text.insert(1.0, text)
					result_text.configure(state="disabled")
				else:
					result_text.configure(state="normal")
					result_text.delete(1.0, END)
					result_text.insert(1.0, "Discriminant less then 0")
					result_text.configure(state="disabled")				
			except:
				pass

	frame=Frame(disc_wind, bg="#D3D3D3")
	frame.place(x=0, y=50, height=320, width=600)

	a_entry=Entry(frame, relief=FLAT, justify='center', font=("Courier", 30))
	a_entry.place(x=5, y=5, height=50, width=100)

	sqrt_x_label=Label(frame, text="x^2+", font=("Courier", 44), bg="#D3D3D3")
	sqrt_x_label.place(x=105, y=-3)

	b_entry=Entry(frame, relief=FLAT, justify='center', font=("Courier", 30))
	b_entry.place(x=250, y=5, height=50, width=100)

	x_label=Label(frame, text="x+", font=("Courier", 44), bg="#D3D3D3")
	x_label.place(x=350, y=-3)

	c_entry=Entry(frame, relief=FLAT, justify='center', font=("Courier", 30))
	c_entry.place(x=425, y=5, height=50, width=100)

	equal_0_label=Label(frame, text="=0", font=("Courier", 44), bg="#D3D3D3")
	equal_0_label.place(x=525, y=-3)

	Button(frame, text="calculate", font=("Courier", 15), relief=GROOVE, command=calc).place(x=225, y=70, width=150)

	result_text=Text(frame, state="disabled")
	result_text.place(x=5, y=120, height=140, width=590)

	global calc_menu_but_clilcs
	calc_menu_but_clilcs=0
	def menu_lab_config(event):
		menu_lab["bg"]="#B5B5B5"
		disc_wind.configure(cursor="hand2")
	def menu_lab_config_cancel(event):
		global calc_menu_but_clilcs
		if(calc_menu_but_clilcs%2==0):
			menu_lab["bg"]="#D3D3D3"
		disc_wind.configure(cursor="arrow")
	def menu_lab_comm(event):
		global calc_menu_but_clilcs
		if(calc_menu_but_clilcs%2==0):
			menu_lab["bg"]="#B5B5B5"
			menu_lab.configure(relief="solid")
			calc_menu_frame.place(x=-2, y=40, height=280, width=300)
		else:
			calc_menu_frame.place(x=-300, y=40, height=280, width=300)
			menu_lab.configure(relief="flat")
		calc_menu_but_clilcs+=1
	def calc_frmae_motion(event):
		disc_wind.configure(cursor="arrow")
	menu_lab=Label(disc_wind, text=" ≡ ", font=("Times", "24"), bg="#D3D3D3")
	menu_lab.bind("<Motion>", menu_lab_config)
	menu_lab.bind("<Leave>", menu_lab_config_cancel)
	menu_lab.bind("<Button-1>", menu_lab_comm)
	menu_lab.grid(row=0, sticky=W) 
	menu_lab_name=Label(disc_wind, text="Discriminant", font=("Times", "24"), bg="#D3D3D3")
	menu_lab_name.place(x=40)

	calc_menu_frame=Frame(disc_wind, bg="#B5B5B5", highlightthickness=2, highlightbackground="black", highlightcolor="black")
	calc_menu_frame.bind("<Motion>", calc_frmae_motion)
	calc_menu_frame.place(x=-300, y=40, height=280, width=300)

	def standart_calculator_button_motion(event):
		standart_calculator_button["bg"]="#D0D0D0"
	def standart_calculator_button_leave(event):
		standart_calculator_button["bg"]="#B5B5B5"
	def standart_calculator_button_comm():
		disc_wind.destroy()
		standart_calculator()
	standart_calculator_button=Button(calc_menu_frame, command=standart_calculator_button_comm, bg="#B5B5B5", text="Standart", relief=FLAT, font=("Times", "15"))
	standart_calculator_button.bind("<Motion>", standart_calculator_button_motion)
	standart_calculator_button.bind("<Leave>", standart_calculator_button_leave)
	standart_calculator_button.place(x=0, y=5, width=296)

	def programmer_calculator_button_motion(event):
		programmer_calculator_button["bg"]="#D0D0D0"
	def programmer_calculator_button_leave(event):
		programmer_calculator_button["bg"]="#B5B5B5"
	def programmer_calculator_button_comm():
		disc_wind.destroy()
		programmer_calc()
	programmer_calculator_button=Button(calc_menu_frame, command=programmer_calculator_button_comm, bg="#B5B5B5", text="Programmer", relief=FLAT, font=("Times", "15"))
	programmer_calculator_button.bind("<Motion>", programmer_calculator_button_motion)
	programmer_calculator_button.bind("<Leave>", programmer_calculator_button_leave)
	programmer_calculator_button.place(x=0, y=37, width=296)

	disc_wind.mainloop()
def programmer_calc():
	programmer_calc_wind=Tk()
	# iconmain = PhotoImage(file='icons\\calc.gif')
	programmer_calc_wind.title("Calculator")
	# programmer_calc_wind.tk.call('wm', 'iconphoto', programmer_calc_wind._w, iconmain)
	programmer_calc_wind.geometry("600x386")
	programmer_calc_wind.resizable(width=False, height=False)
	programmer_calc_wind.configure(background='#D3D3D3')
	programmer_calc_wind.config(cursor="arrow")
	programmer_calc_wind.focus_force()
	####################################################################################################################
	global calc_menu_but_clilcs_programmer
	calc_menu_but_clilcs_programmer=0
	def menu_lab_motion(event):
		menu_lab["bg"]="#B5B5B5"
		programmer_calc_wind.configure(cursor="hand2")
	def menu_lab_leave(event):
		global calc_menu_but_clilcs_programmer
		if(calc_menu_but_clilcs_programmer%2==0):
			menu_lab["bg"]="#D3D3D3"
		programmer_calc_wind.configure(cursor="arrow")
	def menu_lab_comm(event):
		global calc_menu_but_clilcs_programmer
		if(calc_menu_but_clilcs_programmer%2==0):
			menu_lab["bg"]="#B5B5B5"
			menu_lab.configure(relief="solid")
			calc_menu_frame.place(x=-2, y=40)
		else:
			calc_menu_frame.place(x=-300, y=40)
			menu_lab.configure(relief="flat")
		calc_menu_but_clilcs_programmer+=1
	def calc_frmae_motion(event):
		programmer_calc_wind.configure(cursor="arrow")
	menu_lab=Label(programmer_calc_wind, text=" ≡ ", font=("Times", "24"), bg="#D3D3D3")
	menu_lab.grid(row=0, sticky=W)
	menu_lab.bind("<Motion>", menu_lab_motion)
	menu_lab.bind("<Leave>", menu_lab_leave)
	menu_lab.bind("<Button-1>", menu_lab_comm) 
	menu_lab_name=Label(programmer_calc_wind, text="Programmer", font=("Times", "24"), bg="#D3D3D3")
	menu_lab_name.place(x=40)
	def back_to_main_menu_config(event):
		back_to_main_menu["bg"]="#7D7D7D"
		programmer_calc_wind.config(cursor="hand2")
	def back_to_main_menu_config_close(event):
		back_to_main_menu["bg"]="#4A4A4A"
		programmer_calc_wind.config(cursor="arrow")
	def back_to_main_menu():
		programmer_calc_wind.destroy()
		Main_menu()
	def back_to_main_menu_ev(event):
		programmer_calc_wind.destroy()
		Main_menu()
	back_to_main_menu = Button(programmer_calc_wind, text = "< Back to Main Menu", bg="#4A4A4A", command=back_to_main_menu)
	back_to_main_menu.bind("<Motion>", back_to_main_menu_config)
	back_to_main_menu.bind("<Leave>", back_to_main_menu_config_close)
	back_to_main_menu.place(x=3, y=350)
	programmer_calc_wind.bind("<Escape>", back_to_main_menu_ev)
	# calc_menu_frame
	###########################################################################################################################################
	###########################################################################################################################################
	def convet_int(number, base):
		less_then_base_int_array=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "$", "_"]
		error_index=0
		btn=0
		while(error_index<len(number)):
			if base<=less_then_base_int_array.index(str(number)[error_index]):
				btn=1
				error_index+=1
			else:
				error_index+=1
		if(btn==0):
			final_array=[]
			for n in range(len(number)):
				final_array.append(less_then_base_int_array.index(number[n]))

			final_int_num=0
			index=0
			final_array_reverse=final_array[::-1]
			while(index<len(final_array_reverse)):
				final_int_num+=final_array_reverse[index]*(int(base)**index)
				index+=1
			return final_int_num
		elif(btn==1):
			return	"..."
	def convet_fl(number, base):
		global less_then_base_array
		less_then_base_array=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "$", "_"]
		error_index_fl=0
		btnfl=0
		replace=number[0:-1].replace(".","")
		while(error_index_fl<len(replace)):
			if base<=less_then_base_array.index(str(replace)[error_index_fl]):
				btnfl=1
				error_index_fl+=1
			else:
				error_index_fl+=1
		if(btnfl==0):
			if "." not in number:
				error_label_bottom["text"]="Please input float number"

			number_array_final=[]
			n=0
			while(n<len(number)):
				number_array_final.append(number[n])
				n+=1
			
			final_array=[]
			for n in range(len(number)):
				if number[n]==".":
					final_array.append(".")
				else:
					final_array.append(less_then_base_array.index(number[n]))


			final_array_int_past_reverse=(final_array[:final_array.index(".")])[::-1]

			final_array_fl_past=final_array[final_array.index(".")+1:]

			index=0
			int_past=0
			while(index<len(final_array_int_past_reverse)):
				int_past+=final_array_int_past_reverse[index]*(base**index)
				index+=1

			fl_a_len_index=len(final_array_fl_past)-1
			fl_past_array=0
			while(fl_a_len_index>=0):
				fl_past_array+=final_array_fl_past[fl_a_len_index]*(base**(-fl_a_len_index))
				fl_a_len_index-=1
			base_10_num=int_past+float(fl_past_array/base)
			return base_10_num

		elif(btnfl==1):
			return "..."
	def convert_to_base(base_10_num, base, digits):
		global less_then_base_array
		fl_base_10_num=int(float(base_10_num))%base
		int_base_10_num=int(float(base_10_num))//base
		final_num_array_int=[]
		final_num_array_int.append(str(fl_base_10_num))
		while(int_base_10_num>0):
			fl_base_10_num=int_base_10_num%base
			int_base_10_num=int_base_10_num//base
			final_num_array_int.append(str(fl_base_10_num))
		#############################################################################
		#float#######################################################################
		num = float(base_10_num)
		number=int(num)
		num=num-number
		final_fl_sum_array=[]
		for b in range(digits):
			num=num*base
			integer=int(num)
			num-=integer
			final_fl_sum_array.append(str(integer))
		#############################################################################
		array_semi_final=final_num_array_int[::-1]+["."]+final_fl_sum_array

		final_array_final=[]
		for n in range(len(array_semi_final)):
			if array_semi_final[n]==".":
				final_array_final.append(".")
			else:
				final_array_final.append(less_then_base_array[int(array_semi_final[n])])

		final_index=0
		final_num=''
		while(final_index<len(final_array_final)):
			final_num+=final_array_final[final_index]
			final_index+=1

		while (final_num[len(final_num)-1]=="0"):
			final_num=final_num[:-1]
		return final_num

	def calculate():
		base=int(base_enter.get())
		digits=int(digits_enter.get())
		input_number=text.get()
		list_input_number=list(input_number)
		n=0
		while ( "(" in list_input_number or ")" in list_input_number or "+" in list_input_number or "-" in list_input_number or "/" in list_input_number or "^" in list_input_number or "%" in list_input_number or "*" in list_input_number):
			if(list_input_number[n]=="(" or list_input_number[n]==")" or list_input_number[n]=="+" or list_input_number[n]=="-" or list_input_number[n]=="/" or list_input_number[n]=="^" or list_input_number[n]=="%" or list_input_number[n]=="*"):
				list_input_number[n]="#"
			n+=1

		input_number_with_numbersign="".join(list_input_number)
		list_input_numbersign=list(input_number_with_numbersign)
		###############################################
		n=0
		while (n<len(list_input_numbersign)):
			if(list_input_numbersign[n]!="#"):
				list_input_numbersign[n]="_"
			n+=1
		n=0
		while(n<len(list_input_numbersign)):
			if(list_input_numbersign[n]=="#"):
				list_input_numbersign[n]=input_number[n]
			n+=1
		list_input_numbersign="".join(list_input_numbersign)
		while(True):
			if("__" not in list_input_numbersign):
				break
			else:
				list_input_numbersign=list_input_numbersign.replace("__", "_")
		list_input_numbersign=list(list_input_numbersign)
		###############################################

		while(True):
			if("##" not in input_number_with_numbersign):
				break
			else:
				input_number_with_numbersign=input_number_with_numbersign.replace("##", "#")
		array_with_values=[]
		while(input_number_with_numbersign!=""):
			if("#" in input_number_with_numbersign):
				array_with_values.append(input_number_with_numbersign[:input_number_with_numbersign.find("#")])
				input_number_with_numbersign=input_number_with_numbersign[input_number_with_numbersign.find("#")+1:]
			else:
				array_with_values.append(input_number_with_numbersign[:])
				input_number_with_numbersign=""

		def remove_values_from_list(the_list, val):
				while val in the_list:
					the_list.remove(val)
		remove_values_from_list(array_with_values, val="")
		n=0
		while(n<len(array_with_values)):
			if "." in array_with_values[n]:
				array_with_values[n]=str(convet_fl(array_with_values[n], base))
			else:
				array_with_values[n]=str(convet_int(array_with_values[n], base))
			n+=1
		n=0
		n1=0
		base_10_string=""
		while(n<len(list_input_numbersign) or n1<len(array_with_values)):
			if(list_input_numbersign[n]!="_"):
				base_10_string+=list_input_numbersign[n]
			else:
				base_10_string+=array_with_values[n1]
				n1+=1
			n+=1
		try:
			if("^" in base_10_string):
				base_10_string=base_10_string.replace("^", "**")
			base_answer=convert_to_base(base_10_num=str(eval(base_10_string)), base=base, digits=digits)
			if(base_answer[len(base_answer)-1]=="."):
				base_answer=base_answer[:-1]

			base_10_string=base_10_string+"="+str(eval(base_10_string))

		except TypeError:
			base_10_string="ERROR"
			base_answer="ERROR"

		except OverflowError:
			base_10_string="Result too large"
			base_answer="Result too large"	
		except SyntaxError:
			base_10_string="ERROR"
			base_answer="ERROR"


		answer_label_base.delete(0, END)
		answer_label_base.insert(0, base_answer)

		answer_label_for_10.delete(0, END)
		answer_label_for_10.insert(0, base_10_string)


	text=Entry(programmer_calc_wind, font=("Arial", "15"), fg="#383838")
	text.place(x=5, y=80, width=590, height=40)
	text.insert(0, "1101.101*(1101+110.1)^(110.11/1101)%1101")

	def text_enter_delete(event):
		text.delete(0, END)
		text.focus_set()
	programmer_calc_wind.bind("<Delete>", text_enter_delete)

	Scr=Scrollbar(programmer_calc_wind, command=text.xview, orient=HORIZONTAL)
	text.configure(xscrollcommand=Scr.set)
	Scr.place(x=5, y=121, width=590)

	base_enter=Entry(programmer_calc_wind)
	base_enter.place(x=5, y=50, width=50, height=20)
	base_enter.insert(0, "2")
	base_label=Label(programmer_calc_wind, text=" < Base", bg="#D3D3D3")
	base_label.place(x=60, y=50)

	digits_enter=Entry(programmer_calc_wind)
	digits_enter.place(x=5, y=150, width=50, height=20)
	digits_enter.insert(0, "10")
	digits_label=Label(programmer_calc_wind, text=" < Digits", bg="#D3D3D3")
	digits_label.place(x=60, y=150)

	decimal_label=Label(programmer_calc_wind, text="Decimal[10]", font=("Arial", "14"), bg="#D3D3D3", fg="#414141")
	decimal_label.place(x=5, y=250)
	answer_label_for_10=Entry(programmer_calc_wind, font=("Arial", "13"), fg="#505050")
	answer_label_for_10.place(x=5, y=280, height=30, width=590)

	answer_label_base=Entry(programmer_calc_wind, font=("Arial", "13"), fg="#505050")
	answer_label_base.place(x=5, y=205, height=30, width=590)

	def calc_button_motion(event):
		calc_button["bg"]="#828282"
		programmer_calc_wind.configure(cursor="hand2")
	def calc_button_leave(event):
		calc_button["bg"]="#BBBBBB"
		programmer_calc_wind.configure(cursor="arrow")

	calc_button=Button(programmer_calc_wind, text="Calculate", command=calculate, relief=GROOVE, font=("Times", "14"), bg="#BBBBBB")
	calc_button.bind("<Motion>", calc_button_motion)
	calc_button.bind("<Leave>", calc_button_leave)
	calc_button.place(x=500, y=155)

	def calculate_ev(event):
		calculate()
	programmer_calc_wind.bind("<Return>", calculate_ev)

	def discriminant_calculator_button_motion(event):
		discriminant_calculator_button["bg"]="#D0D0D0"
	def discriminant_calculator_button_leave(event):
		discriminant_calculator_button["bg"]="#B5B5B5"
	def discriminant_calculator_button_comm():
		programmer_calc_wind.destroy()
		discriminant()

	def standart_calculator_button_motion(event):
		standart_calculator_button["bg"]="#D0D0D0"
	def standart_calculator_button_leave(event):
		standart_calculator_button["bg"]="#B5B5B5"
	def standart_calculator_button_comm():
		programmer_calc_wind.destroy()
		standart_calculator()

	calc_menu_frame=Frame(programmer_calc_wind, bg="#B5B5B5", highlightthickness=2, highlightbackground="black", highlightcolor="black")
	calc_menu_frame.bind("<Motion>", calc_frmae_motion)
	calc_menu_frame.place(x=-300, y=40, height=320, width=300)

	discriminant_calculator_button=Button(calc_menu_frame, command=discriminant_calculator_button_comm, bg="#B5B5B5", text="Discriminant", relief=FLAT, font=("Times", "15"))
	discriminant_calculator_button.bind("<Motion>", discriminant_calculator_button_motion)
	discriminant_calculator_button.bind("<Leave>", discriminant_calculator_button_leave)
	discriminant_calculator_button.place(x=0, y=37, width=296)

	standart_calculator_button=Button(calc_menu_frame, command=standart_calculator_button_comm, bg="#B5B5B5", text="Standart", relief=FLAT, font=("Times", "15"))
	standart_calculator_button.bind("<Motion>", standart_calculator_button_motion)
	standart_calculator_button.bind("<Leave>", standart_calculator_button_leave)
	standart_calculator_button.place(x=0, y=5, width=296)

	programmer_calc_wind.mainloop()
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
def standart_calculator():
	standart_calc_wind=Tk()
	standart_calc_wind.focus_force()
	standart_calc_wind.geometry("386x530")
	standart_calc_wind.title("Calculator")
	# iconmain = PhotoImage(file='icons\\calc.gif')
	# standart_calc_wind.tk.call('wm', 'iconphoto', standart_calc_wind._w, iconmain)
	standart_calc_wind.resizable(width=False, height=False)
	standart_calc_wind.configure(background='#D3D3D3')
	standart_calc_wind.config(cursor="arrow")
	rad_deg_conv_str="Degrees"

	global rad_to_degrees_var
	rad_to_degrees_var="Degrees"
	def rad_deg_conv():
		global rad_to_degrees_var
		if Radians_Degrees_convert_button["text"]=="Degrees":
			Radians_Degrees_convert_button["text"]="Radians"
			rad_to_degrees_var="Radians"

		elif Radians_Degrees_convert_button["text"]=="Radians":
			Radians_Degrees_convert_button["text"]="Degrees"
			rad_to_degrees_var="Degrees"

	Radians_Degrees_convert_button=Button(standart_calc_wind, text="Degrees", font=("Times", 10,"italic"), command=rad_deg_conv, relief=GROOVE)
	Radians_Degrees_convert_button.place(x=318, y=190)
	#########################################################################################################
	def but_open_brecket_conf(event):
		but_open_brecket.configure(bg="#2C2C2C")
		but_open_brecket.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_open_brecket_cancel(event):
		but_open_brecket.configure(bg="#D0D0D0")
		but_open_brecket.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_open_brecket_comm():
		a=ent_question.get()
		ent_question.configure(state="normal")

		if (len(a)>0):
			if(a[-1]!=")"):
				ent_question.insert(END, ent_answer.get()+"(")
		elif(a=="" or a[-1]=="+" or a[-1]=="-" or a[-1]=="*" or a[-1]=="/" or a[-1]=="%" or a[-1]=="^"):
			ent_question.insert(END, ent_answer.get()+"(")
		ent_answer.delete(0, END); 

		ent_question.configure(state="disabled")
	but_open_brecket = Button(standart_calc_wind, text="(", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_open_brecket_comm)
	but_open_brecket.bind("<Motion>", but_open_brecket_conf)
	but_open_brecket.bind("<Leave>", but_open_brecket_cancel)
	but_open_brecket.place(x=3, y=457, width=76, height=40)
	#########################################################################################################
	def but_close_brecket_conf(event):
		but_close_brecket.configure(bg="#2C2C2C")
		but_close_brecket.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_close_brecket_cancel(event):
		but_close_brecket.configure(bg="#D0D0D0")
		but_close_brecket.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_close_brecket_comm():
		ent_question.configure(state="normal")
		
		if( "(" in ent_question.get() and ")" in ent_question.get()):
			a=ent_question.get()
			open_bracket_number=a.count("(")
			close_bracket_number=a.count(")")
			if open_bracket_number>close_bracket_number:     
				ent_question.insert(END, ent_answer.get()+")")
		elif( ")" not in ent_question.get() and "(" in ent_question.get()):
			ent_question.insert(END, ent_answer.get()+")")
		ent_answer.delete(0, END)

		ent_question.configure(state="disabled")
	but_close_brecket = Button(standart_calc_wind, text=")", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_close_brecket_comm)
	but_close_brecket.bind("<Motion>", but_close_brecket_conf)
	but_close_brecket.bind("<Leave>", but_close_brecket_cancel)
	but_close_brecket.place(x=80, y=457, width=76, height=40)
	#########################################################################################################
	def but_0_conf(event):
		but_0.configure(bg="#2C2C2C")
		but_0.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_0_cancel(event):
		but_0.configure(bg="#F0F0F0")
		but_0.configure(fg="black")
		standart_calc_wind.configure(cursor="arrow")
	def but_0_comm():
		ent_answer.configure(state="normal")
		if(ent_answer.get()=="ERROR"):
			ent_answer.delete(0, END)
			ent_answer.insert(END, "0")
		else:
			ent_answer.insert(END, "0")
		ent_answer.configure(state="disabled")
	but_0 = Button(standart_calc_wind, text="0", font=("Arial", "16", "bold"), relief=FLAT, command=but_0_comm)
	but_0.bind("<Motion>", but_0_conf)
	but_0.bind("<Leave>", but_0_cancel)
	but_0.place(x=156, y=457, width=76, height=40)
	#########################################################################################################
	def but_point_conf(event):
		but_point.configure(bg="#2C2C2C")
		but_point.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_point_cancel(event):
		but_point.configure(bg="#D0D0D0")
		but_point.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_point_comm():
		ent_answer.configure(state="normal")
		if ent_answer.get()=="":
			ent_answer.insert(END, "0.")
		if ("." not in ent_answer.get() ):
			ent_answer.insert(END, ".")
		ent_answer.configure(state="disabled")
	but_point = Button(standart_calc_wind, text=".", font=("Arial", "16", "bold"), relief=FLAT, bg="#D0D0D0", command=but_point_comm)
	but_point.bind("<Motion>", but_point_conf)
	but_point.bind("<Leave>", but_point_cancel)
	but_point.place(x=232, y=457, width=76, height=40)
	#########################################################################################################
	def but_equal_conf(event):
		but_equal.configure(bg="#2C2C2C")
		but_equal.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_equal_cancel(event):
		but_equal.configure(bg="#D0D0D0")
		but_equal.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_equal_comm():
		ent_answer.configure(state="normal")
		ent_question.configure(state="normal")
		try:
			def Tg(x):
				return Sin(x)/Cos(x)
			def Ctg(x):
				return 1/Tg(x)
			def Sin(x):
				if(x%180==0):
					return 0
				else:
					return sin(radians(x))
			def Cos(x):
				if(x%90==0):
					return 0
				else:
					return cos(radians(x))
			def tg(x):
				return sin(x)/cos(x)
			def ctg(x):
				return 1/tg(x)
			def scrt(x):
				return x**0.5
			def defact(x):
				i=1
				intx=x//i
				while(intx>1):
					i+=1
					intx=intx//i
				if(x-factorial(i)==0):
					return i
				else:
					return "ERROR"
			a=ent_question.get()
			if(ent_answer.get()!="" and a!=""):
				answer=ent_answer.get()
				ent_answer.delete(0, END); ent_answer.insert(END,  eval( ent_question.get()+answer ) )
			elif ent_answer.get()=="" and a!="":
				ent_answer.delete(0, END)
				ent_answer.insert(END,  eval(a) )
			ent_question.delete(0, END)
		except ZeroDivisionError:
			ent_answer.delete(0, END); ent_answer.insert(END,  "∞" )
			ent_question.delete(0, END)
		except:
			ent_answer.delete(0, END); ent_answer.insert(END,  "ERROR" ); 
			ent_question.delete(0, END)
		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")

	but_equal = Button(standart_calc_wind, text="=", font=("Times", "24"), relief=FLAT, bg="#D0D0D0", command=but_equal_comm)
	but_equal.bind("<Motion>", but_equal_conf)
	but_equal.bind("<Leave>", but_equal_cancel)
	but_equal.place(x=308, y=457, width=76, height=40)
	#########################################################################################################
	def but_plus_minus_conf(event):
		but_plus_minus.configure(bg="#2C2C2C")
		but_plus_minus.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_plus_minus_cancel(event):
		but_plus_minus.configure(bg="#D0D0D0")
		but_plus_minus.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_plus_minus_comm():
		ent_answer.configure(state="normal")
		ent_question.configure(state="normal")
		try:
			def Tg(x):
				return Sin(x)/Cos(x)
			def Ctg(x):
				return 1/Tg(x)
			def Sin(x):
				if(x%180==0):
					return 0
				else:
					return sin(radians(x))
			def Cos(x):
				if(x%90==0):
					return 0
				else:
					return cos(radians(x))
			def tg(x):
				return sin(x)/cos(x)
			def ctg(x):
				return 1/tg(x)
			def scrt(x):
				return x**0.5
			def defact(x):
				i=1
				intx=x//i
				while(intx>1):
					i+=1
					intx=intx//i
				if(x-factorial(i)==0):
					return i
				else:
					return "ERROR"
			if(ent_question.get()!="" and ent_answer.get()!=""):
				ent_answer.delete(0, END); ent_answer.insert(END, -( eval( ent_question.get()+ent_answer.get() ) ) )
			else:
				answer=ent_answer.get()
				ent_answer.delete(0, END)
				ent_answer.insert(END, str( -( int( answer ) ) ) )
			ent_question.delete(0, END)

		except ZeroDivisionError:
			ent_answer.delete(0, END)
			ent_answer.insert(END,  "∞" )
			ent_question.delete(0, END)
		except:
			ent_answer.delete(0, END)
			ent_answer.insert(END,  "ERROR" )
			ent_question.delete(0, END)
		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")
	but_plus_minus = Button(standart_calc_wind, text="±", font=("Times", "20"), relief=FLAT, bg="#D0D0D0", command=but_plus_minus_comm)
	but_plus_minus.bind("<Motion>", but_plus_minus_conf)
	but_plus_minus.bind("<Leave>", but_plus_minus_cancel)
	but_plus_minus.place(x=3, y=417, width=76, height=40)
	#########################################################################################################
	def but_1_conf(event):
		but_1.configure(bg="#2C2C2C")
		but_1.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_1_cancel(event):
		but_1.configure(bg="#F0F0F0")
		but_1.configure(fg="black")
		standart_calc_wind.configure(cursor="arrow")
	def but_1_comm():
		ent_answer.configure(state="normal")
		if(ent_answer.get()=="ERROR"):
			ent_answer.delete(0, END)
			ent_answer.insert(END, "1" )
		else:
			ent_answer.insert(END, "1" )
		ent_answer.configure(state="disabled")
	but_1 = Button(standart_calc_wind, text="1", font=("Arial", "16", "bold"), relief=FLAT, command=but_1_comm)
	but_1.bind("<Motion>", but_1_conf)
	but_1.bind("<Leave>", but_1_cancel)
	but_1.place(x=80, y=417, width=76, height=40)
	#########################################################################################################
	def but_2_conf(event):
		but_2.configure(bg="#2C2C2C")
		but_2.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_2_cancel(event):
		but_2.configure(bg="#F0F0F0")
		but_2.configure(fg="black")
		standart_calc_wind.configure(cursor="arrow")
	def but_2_comm():
		ent_answer.configure(state="normal")
		if(ent_answer.get()=="ERROR"):
			ent_answer.delete(0, END)
			ent_answer.insert(END, "2" )
		else:
			ent_answer.insert(END, "2" )
		ent_answer.configure(state="disabled") 
	but_2 = Button(standart_calc_wind, text="2", font=("Arial", "16", "bold"), relief=FLAT, command=but_2_comm)
	but_2.bind("<Motion>", but_2_conf)
	but_2.bind("<Leave>", but_2_cancel)
	but_2.place(x=156, y=417, width=76, height=40)
	#########################################################################################################
	def but_3_conf(event):
		but_3.configure(bg="#2C2C2C")
		but_3.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_3_cancel(event):
		but_3.configure(bg="#F0F0F0")
		but_3.configure(fg="black")
		standart_calc_wind.configure(cursor="arrow")
	def but_3_comm():
		ent_answer.configure(state="normal")
		if(ent_answer.get()=="ERROR"):
			ent_answer.delete(0, END)
			ent_answer.insert(END, "3" )
		else:
			ent_answer.insert(END, "3" )
		ent_answer.configure(state="disabled")
	but_3 = Button(standart_calc_wind, text="3", font=("Arial", "16", "bold"), relief=FLAT, command=but_3_comm)
	but_3.bind("<Motion>", but_3_conf)
	but_3.bind("<Leave>", but_3_cancel)
	but_3.place(x=232, y=417, width=76, height=40)
	#########################################################################################################
	def but_plus_conf(event):
		but_plus.configure(bg="#2C2C2C")
		but_plus.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_plus_cancel(event):
		but_plus.configure(bg="#D0D0D0")
		but_plus.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_plus_comm():
		a=ent_question.get()
		ent_question.configure(state="normal")
		ent_answer.configure(state="normal")
		if (len(a)>0):
			if((a[-1]=="+" or a[-1]=="-" or a[-1]=="/" or a[-1]=="*" or a[-1]=="%") and ent_answer.get()==""):
				if(a[-2]=="*"):
					ent_question.delete(0, END)
					ent_question.insert(END, a[:-2]+"+" )
				else:
					ent_question.delete(0, END)
					ent_question.insert(END, a[:-1]+"+" )

			elif((a[-1]=="+" or a[-1]=="-" or a[-1]=="/" or a[-1]=="*" or a[-1]=="%") and ent_answer.get()!=""):
				ent_question.insert(END, ent_answer.get()+"+" )
				ent_answer.delete(0, END)

			elif(a[-1]==")" or a[-1]=="("):
				ent_question.insert(END, ent_answer.get()+"+" )
				ent_answer.delete(0, END)

		elif (ent_answer.get()!="" and ent_answer.get()!="ERROR"):
			ent_question.insert(END, ent_answer.get()+"+" )
			ent_answer.delete(0, END)

		elif (ent_question.get()==""):
			ent_question.delete(0, END)
			ent_question.insert(END, ent_answer.get()+"+" )
			ent_answer.delete(0, END)

		else:
			ent_question.insert(END, "+" )
		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")

	but_plus = Button(standart_calc_wind, text="+", font=("Times", "20"), relief=FLAT, bg="#D0D0D0", command=but_plus_comm)
	but_plus.bind("<Motion>", but_plus_conf)
	but_plus.bind("<Leave>", but_plus_cancel)
	but_plus.place(x=308, y=417, width=76, height=40)
	#########################################################################################################
	def but_sqrt_conf(event):
		but_sqrt.configure(bg="#2C2C2C")
		but_sqrt.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_sqrt_cancel(event):
		but_sqrt.configure(bg="#D0D0D0")
		but_sqrt.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_sqrt_comm():
		a=ent_question.get()
		ent_question.configure(state="normal")
		ent_answer.configure(state="normal")
		if (len(a)>0):
			if (a[-1]!=")" or a[-1] not in range(10)):
				ent_question.insert(END, "scrt("+ent_answer.get()+")" )
				ent_answer.configure(state="normal"); ent_answer.delete(0, END)
		elif(a==""):
			ent_question.insert(END, "scrt("+ent_answer.get()+")" )
			ent_answer.delete(0, END)
		ent_question.configure(state="disabled")
		ent_answer.configure(state="disabled")
	but_sqrt = Button(standart_calc_wind, text="√", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_sqrt_comm)
	but_sqrt.bind("<Motion>", but_sqrt_conf)
	but_sqrt.bind("<Leave>", but_sqrt_cancel)
	but_sqrt.place(x=3, y=377, width=76, height=40)
	#########################################################################################################
	def but_4_conf(event):
		but_4.configure(bg="#2C2C2C")
		but_4.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_4_cancel(event):
		but_4.configure(bg="#F0F0F0")
		but_4.configure(fg="black")
		standart_calc_wind.configure(cursor="arrow")
	def but_4_comm():
		ent_answer.configure(state="normal")
		if(ent_answer.get()=="ERROR"):
			ent_answer.delete(0, END)
			ent_answer.insert(END, "4" )
		else:
			ent_answer.insert(END, "4" )
		ent_answer.configure(state="disabled")
	but_4 = Button(standart_calc_wind, text="4", font=("Arial", "16", "bold"), relief=FLAT, command=but_4_comm)
	but_4.bind("<Motion>", but_4_conf)
	but_4.bind("<Leave>", but_4_cancel)
	but_4.place(x=80, y=377, width=76, height=40)
	#########################################################################################################
	def but_5_conf(event):
		but_5.configure(bg="#2C2C2C")
		but_5.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_5_cancel(event):
		but_5.configure(bg="#F0F0F0")
		but_5.configure(fg="black")
		standart_calc_wind.configure(cursor="arrow")
	def but_5_comm():
		ent_answer.configure(state="normal")
		if(ent_answer.get()=="ERROR"):
			ent_answer.delete(0, END)
			ent_answer.insert(END, "5" )
		else:
			ent_answer.insert(END, "5" )
		ent_answer.configure(state="disabled")
	but_5 = Button(standart_calc_wind, text="5", font=("Arial", "16", "bold"), relief=FLAT, command=but_5_comm)
	but_5.bind("<Motion>", but_5_conf)
	but_5.bind("<Leave>", but_5_cancel)
	but_5.place(x=156, y=377, width=76, height=40)
	#########################################################################################################
	def but_6_conf(event):
		but_6.configure(bg="#2C2C2C")
		but_6.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_6_cancel(event):
		but_6.configure(bg="#F0F0F0")
		but_6.configure(fg="black")
		standart_calc_wind.configure(cursor="arrow")
	def but_6_comm():
		ent_answer.configure(state="normal")
		if(ent_answer.get()=="ERROR"):
			ent_answer.delete(0, END)
			ent_answer.insert(END, "6" )
		else:
			ent_answer.insert(END, "6" )
		ent_answer.configure(state="disabled")
	but_6 = Button(standart_calc_wind, text="6", font=("Arial", "16", "bold"), relief=FLAT, command=but_6_comm)
	but_6.bind("<Motion>", but_6_conf)
	but_6.bind("<Leave>", but_6_cancel)
	but_6.place(x=232, y=377, width=76, height=40)
	#########################################################################################################
	def but_minus_conf(event):
		but_minus.configure(bg="#2C2C2C")
		but_minus.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_minus_cancel(event):
		but_minus.configure(bg="#D0D0D0")
		but_minus.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_minus_comm():
		a=ent_answer.get()
		ent_answer.configure(state="normal")
		ent_question.configure(state="normal")

		if(a==""):
			ent_answer.insert(END, "-" )

		elif (a[-1]=="-"):
			ent_answer.insert(END, "-" )

		elif (a!="ERROR"):
			ent_question.insert(END, ent_answer.get()+"-" )
			ent_answer.delete(0, END)

		elif(a!=""):
			label_for_question["text"]+="-"+label_for_answer["text"]
		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")

	but_minus = Button(standart_calc_wind, text="–", font=("Times", "20"), relief=FLAT, bg="#D0D0D0", command=but_minus_comm)
	but_minus.bind("<Motion>", but_minus_conf)
	but_minus.bind("<Leave>", but_minus_cancel)
	but_minus.place(x=308, y=377, width=76, height=40)
	#########################################################################################################
	def but_factorial_conf(event):
		but_factorial.configure(bg="#2C2C2C")
		but_factorial.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_factorial_cancel(event):
		but_factorial.configure(bg="#D0D0D0")
		but_factorial.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_factorial_comm():
		a=ent_question.get()
		ent_question.configure(state="normal")
		ent_answer.configure(state="normal")

		if (len(a)>0):
			if (a[-1]!=")" or a[-1] not in range(10)):
				ent_question.insert(END, "factorial("+ent_answer.get()+")" )
				ent_answer.delete(0, END)

		elif(a==""):
			ent_question.insert(END, "factorial("+ent_answer.get()+")" )
			ent_answer.delete(0, END)
		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")

	but_factorial = Button(standart_calc_wind, text="n → n!", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_factorial_comm)
	but_factorial.bind("<Motion>", but_factorial_conf)
	but_factorial.bind("<Leave>", but_factorial_cancel)
	but_factorial.place(x=3, y=337, width=76, height=40)
	#########################################################################################################
	def but_7_conf(event):
		but_7.configure(bg="#2C2C2C")
		but_7.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_7_cancel(event):
		but_7.configure(bg="#F0F0F0")
		but_7.configure(fg="black")
		standart_calc_wind.configure(cursor="arrow")
	def but_7_comm():
		ent_answer.configure(state="normal")
		if(ent_answer.get()=="ERROR"):
			ent_answer.delete(0, END)
			ent_answer.insert(END, "7" )
		else:
			ent_answer.insert(END, "8" )
		ent_answer.configure(state="disabled")
	but_7 = Button(standart_calc_wind, text="7", font=("Arial", "16", "bold"), relief=FLAT, command=but_7_comm)
	but_7.bind("<Motion>", but_7_conf)
	but_7.bind("<Leave>", but_7_cancel)
	but_7.place(x=80, y=337, width=76, height=40)
	#########################################################################################################
	def but_8_conf(event):
		but_8.configure(bg="#2C2C2C")
		but_8.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_8_cancel(event):
		but_8.configure(bg="#F0F0F0")
		but_8.configure(fg="black")
		standart_calc_wind.configure(cursor="arrow")
	def but_8_comm():
		ent_answer.configure(state="normal")
		if(ent_answer.get()=="ERROR"):
			ent_answer.delete(0, END)
			ent_answer.insert(END, "8" )
		else:
			ent_answer.insert(END, "8" )
		ent_answer.configure(state="disabled")
	but_8 = Button(standart_calc_wind, text="8", font=("Arial", "16", "bold"), relief=FLAT, command=but_8_comm)
	but_8.bind("<Motion>", but_8_conf)
	but_8.bind("<Leave>", but_8_cancel)
	but_8.place(x=156, y=337, width=76, height=40)
	#########################################################################################################
	def but_9_conf(event):
		but_9.configure(bg="#2C2C2C")
		but_9.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_9_cancel(event):
		but_9.configure(bg="#F0F0F0")
		but_9.configure(fg="black")
		standart_calc_wind.configure(cursor="arrow")
	def but_9_comm():
		ent_answer.configure(state="normal")
		if(ent_answer.get()=="ERROR"):
			ent_answer.delete(0, END)
			ent_answer.insert(END, "9" )
		else:
			ent_answer.insert(END, "9" )
		ent_answer.configure(state="disabled")
	but_9 = Button(standart_calc_wind, text="9", font=("Arial", "16", "bold"), relief=FLAT, command=but_9_comm)
	but_9.bind("<Motion>", but_9_conf)
	but_9.bind("<Leave>", but_9_cancel)
	but_9.place(x=232, y=337, width=76, height=40)
	#########################################################################################################
	def but_x_conf(event):
		but_x.configure(bg="#2C2C2C")
		but_x.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_x_cancel(event):
		but_x.configure(bg="#D0D0D0")
		but_x.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_x_comm():
		a=ent_question.get()
		ent_answer.configure(state="normal")
		ent_question.configure(state="normal")

		if (len(a)>0):
			if((a[-1]=="+" or a[-1]=="-" or a[-1]=="/" or a[-1]=="*" or a[-1]=="%") and ent_answer.get()==""):
				if (len(a)>0):
					if(a[-2]=="*"):
						ent_question.delete(0, END)
						ent_question.insert(END, a[:-2]+"*" )
					else:
						ent_question.delete(0, END)
						ent_question.insert(END, a[:-1]+"*" )

			elif((a[-1]=="+" or a[-1]=="-" or a[-1]=="/" or a[-1]=="*" or a[-1]=="%") and ent_answer.get()!=""):
				ent_question.insert(END, ent_answer.get()+"*" )
				ent_answer.delete(0, END)

			elif(a[-1]==")" or a[-1]=="("):
				ent_question.insert(END, ent_answer.get()+"*" )
				ent_answer.delete(0, END)

		elif (ent_answer.get()!="" and ent_answer.get()!="ERROR"):
			ent_question.insert(END, ent_answer.get()+"*" )
			ent_answer.delete(0, END)

		elif (ent_question.get()==""):
			ent_question.delete(0, END)
			ent_question.insert(END, ent_answer.get()+"*" )
			ent_answer.delete(0, END); 

		else:
			ent_question.insert(END, "*" )
		ent_question.configure(state="disabled")
		ent_answer.configure(state="disabled")

	but_x = Button(standart_calc_wind, text="×", font=("Times", "20"), relief=FLAT, bg="#D0D0D0", command=but_x_comm)
	but_x.bind("<Motion>", but_x_conf)
	but_x.bind("<Leave>", but_x_cancel)
	but_x.place(x=308, y=337, width=76, height=40)
	#########################################################################################################
	def but_sin_conf(event):
		but_sin.configure(bg="#2C2C2C")
		but_sin.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_sin_cancel(event):
		but_sin.configure(bg="#D0D0D0")
		but_sin.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_sin_comm():
		global rad_to_degrees_var
		ent_answer.configure(state="normal")
		ent_question.configure(state="normal")

		if rad_to_degrees_var=="Degrees":
			a=ent_question.get()

			if (len(a)>0):
				if (a[-1]!=")" or a[-1] not in range(10)):
					ent_question.insert(END, "Sin("+ent_answer.get()+")" )

			elif(a==""):
				ent_question.insert(END, "Sin("+ent_answer.get()+")" )


		elif rad_to_degrees_var=="Radians":
			a=ent_question.get()

			if (len(a)>0):
				if (a[-1]!=")" or a[-1] not in range(10)):
					ent_question.insert(END, "sin("+ent_answer.get()+")" )

			elif(a==""):
				ent_question.insert(END, "sin("+ent_answer.get()+")" )

		ent_answer.delete(0, END)
		ent_answer.configure(state="disabled") 
		ent_question.configure(state="disabled")

	but_sin = Button(standart_calc_wind, text="sin", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_sin_comm)
	but_sin.bind("<Motion>", but_sin_conf)
	but_sin.bind("<Leave>", but_sin_cancel)
	but_sin.place(x=3, y=297, width=76, height=40)
	#########################################################################################################
	def but_cos_conf(event):
		but_cos.configure(bg="#2C2C2C")
		but_cos.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_cos_cancel(event):
		but_cos.configure(bg="#D0D0D0")
		but_cos.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_cos_comm():
		global rad_to_degrees_var
		ent_question.configure(state="normal")
		ent_answer.configure(state="normal")

		if rad_to_degrees_var=="Degrees":
			a=ent_question.get()

			if (len(a)>0):
				if (a[-1]!=")" or a[-1] not in range(10)):
					ent_question.insert(END, "Cos("+ent_answer.get()+")" )
			elif(a==""):
				ent_question.insert(END, "Cos("+ent_answer.get()+")" )


		elif rad_to_degrees_var=="Radians":
			a=ent_question.get()

			if (len(a)>0):
				if (a[-1]!=")" or a[-1] not in range(10)):
					ent_question.insert(END, "cos("+ent_answer.get()+")" )

			elif(a==""):
				ent_question.insert(END, "cos("+ent_answer.get()+")" )
			
		ent_answer.delete(0, END)
		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")

	but_cos = Button(standart_calc_wind, text="cos", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_cos_comm)
	but_cos.bind("<Motion>", but_cos_conf)
	but_cos.bind("<Leave>", but_cos_cancel)
	but_cos.place(x=80, y=297, width=76, height=40)
	#########################################################################################################
	def but_tg_conf(event):
		but_tg.configure(bg="#2C2C2C")
		but_tg.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_tg_cancel(event):
		but_tg.configure(bg="#D0D0D0")
		but_tg.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_tg_comm():
		global rad_to_degrees_var
		if rad_to_degrees_var=="Degrees":
			a=ent_question.get()
			ent_answer.configure(state="normal")
			ent_question.configure(state="normal")

			if (len(a)>0):
				if (a[-1]!=")" or a[-1] not in range(10)):
					ent_question.insert(END, "Tg("+ent_answer.get()+")" )

			elif(a==""):
				ent_question.insert(END, "Tg("+ent_answer.get()+")" )


		elif rad_to_degrees_var=="Radians":
			a=ent_question.get()

			if (len(a)>0):
				if (a[-1]!=")" or a[-1] not in range(10)):
					ent_question.insert(END, "tg("+ent_answer.get()+")" )

			elif(a==""):
				nt_question.insert(END, "tg("+ent_answer.get()+")" )

		ent_answer.delete(0, END)
		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")

	but_tg = Button(standart_calc_wind, text="tg", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_tg_comm)
	but_tg.bind("<Motion>", but_tg_conf)
	but_tg.bind("<Leave>", but_tg_cancel)
	but_tg.place(x=156, y=297, width=76, height=40)
	#########################################################################################################
	def but_ctg_conf(event):
		but_ctg.configure(bg="#2C2C2C")
		but_ctg.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_ctg_cancel(event):
		but_ctg.configure(bg="#D0D0D0")
		but_ctg.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_ctg_comm():
		global rad_to_degrees_var
		ent_answer.configure(state="normal")
		ent_question.configure(state="normal")

		if rad_to_degrees_var=="Degrees":
			a=ent_question.get()

			if (len(a)>0):
				if (a[-1]!=")" or a[-1] not in range(10)):
					ent_question.insert(END, "Ctg("+ent_answer.get()+")" )

			elif(a==""):
				ent_question.insert(END, "Ctg("+ent_answer.get()+")" )


		elif rad_to_degrees_var=="Radians":
			a=ent_question.get()

			if (len(a)>0):
				if (a[-1]!=")" or a[-1] not in range(10)):
					ent_question.insert(END, "ctg("+ent_answer.get()+")" )

			elif(a==""):
				ent_question.insert(END, "ctg("+ent_answer.get()+")" )
		ent_answer.delete(0, END)
		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")

	but_ctg = Button(standart_calc_wind, text="ctg", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_ctg_comm)
	but_ctg.bind("<Motion>", but_ctg_conf)
	but_ctg.bind("<Leave>", but_ctg_cancel)
	but_ctg.place(x=232, y=297, width=76, height=40)
	#########################################################################################################
	def but_div_conf(event):
		but_div.configure(bg="#2C2C2C")
		but_div.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_div_cancel(event):
		but_div.configure(bg="#D0D0D0")
		but_div.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_div_comm():

		a=ent_question.get()
		ent_question.configure(state="normal")
		ent_answer.configure(state="normal")

		if (len(a)>0):
			if((a[-1]=="+" or a[-1]=="-" or a[-1]=="/" or a[-1]=="*" or a[-1]=="%") and ent_answer.get()==""):
				if (len(a)>0):
					if(a[-2]=="*"):
						ent_question.delete(0, END)
						ent_question.insert(END, a[:-2]+"/" )
					else:
						ent_question.delete(0, END)
						ent_question.insert(END, a[:-1]+"/" )

			elif((a[-1]=="+" or a[-1]=="-" or a[-1]=="/" or a[-1]=="*" or a[-1]=="%") and ent_answer.get()!=""):
				ent_question.insert(END, ent_answer.get()+"/" )
				ent_answer.delete(0, END)

			elif(a[-1]==")" or a[-1]=="("):
				ent_question.insert(END, ent_answer.get()+"/" )
				ent_answer.delete(0, END)

		elif (ent_answer.get()!="" and ent_answer.get()!="ERROR"):
			ent_question.insert(END, ent_answer.get()+"/" )
			ent_answer.delete(0, END)

		elif (ent_question.get()==""):
			ent_question.delete(0, END)
			ent_question.insert(END, ent_answer.get()+"/" )
			ent_answer.delete(0, END)

		else:
			ent_question.insert(END, "/" )

		ent_question.configure(state="disabled")
		ent_answer.configure(state="disabled")


	but_div = Button(standart_calc_wind, text="÷", font=("Times", "24"), relief=FLAT, bg="#D0D0D0", command=but_div_comm)
	but_div.bind("<Motion>", but_div_conf)
	but_div.bind("<Leave>", but_div_cancel)
	but_div.place(x=308, y=297, width=76, height=40)
	#########################################################################################################
	def but_deg_conf(event):
		but_deg.configure(bg="#2C2C2C")
		but_deg.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_deg_cancel(event):
		but_deg.configure(bg="#D0D0D0")
		but_deg.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_deg_comm():
		a=ent_question.get()
		ent_question.configure(state="normal")
		ent_answer.configure(state="normal")

		if (len(a)>0):
			if((a[-1]=="+" or a[-1]=="-" or a[-1]=="/" or a[-1]=="*" or a[-1]=="%") and ent_answer.get()==""):
				if (len(a)>0):
					if(a[-2]=="*"):
						ent_question.delete(0, END)
						ent_question.insert(END, a[:-2]+"**" )
					else:
						ent_question.delete(0, END)
						ent_question.insert(END, a[:-1]+"**" )

			elif((a[-1]=="+" or a[-1]=="-" or a[-1]=="/" or a[-1]=="*" or a[-1]=="%") and ent_answer.get()!=""):
				ent_question.insert(END, ent_answer.get()+"**" )
				ent_answer.delete(0, END)

			elif(a[-1]==")" or a[-1]=="("):
				ent_question.configure(state="normal"); ent_question.insert(END, ent_answer.get()+"**" )
				ent_answer.configure(state="normal"); ent_answer.delete(0, END)

		elif (ent_answer.get()!="" and ent_answer.get()!="ERROR"):
			ent_question.insert(END, ent_answer.get()+"**" )
			ent_answer.delete(0, END)

		elif (ent_question.get()==""):
			ent_question.delete(0, END)
			ent_question.insert(END, ent_answer.get()+"**" )
			ent_answer.delete(0, END)

		else:
			ent_question.configure(state="normal"); ent_question.insert(END, "**" ); 

		ent_question.configure(state="disabled")
		ent_answer.configure(state="disabled")

	but_deg = Button(standart_calc_wind, text="^", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_deg_comm)
	but_deg.bind("<Motion>", but_deg_conf)
	but_deg.bind("<Leave>", but_deg_cancel)
	but_deg.place(x=3, y=257, width=76, height=40)
	#########################################################################################################
	def but_pi_conf(event):
		but_pi.configure(bg="#2C2C2C")
		but_pi.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_pi_cancel(event):
		but_pi.configure(bg="#D0D0D0")
		but_pi.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_pi_comm():
		ent_answer.configure(state="normal")
		ent_answer.delete(0, END)
		ent_answer.insert(END, "3.14159265359")
		ent_answer.configure(state="disabled")
	but_pi = Button(standart_calc_wind, text="π", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_pi_comm)
	but_pi.bind("<Motion>", but_pi_conf)
	but_pi.bind("<Leave>", but_pi_cancel)
	but_pi.place(x=80, y=257, width=76, height=40)
	#########################################################################################################
	def but_e_conf(event):
		but_e.configure(bg="#2C2C2C")
		but_e.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_e_cancel(event):
		but_e.configure(bg="#D0D0D0")
		but_e.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_e_comm():
		a=ent_question.get()
		ent_question.configure(state="normal")
		ent_answer.configure(state="normal")

		if (len(a)>0):
			if (a[-1]!=")" or a[-1] not in range(10)):
				ent_question.insert(END, "exp("+ent_answer.get()+")" )

		elif(a==""):
			ent_question.insert(END, "exp("+ent_answer.get()+")" ); 
		ent_answer.delete(0, END)

		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")

	but_e = Button(standart_calc_wind, text="exp", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_e_comm)
	but_e.bind("<Motion>", but_e_conf)
	but_e.bind("<Leave>", but_e_cancel)
	but_e.place(x=156, y=257, width=76, height=40)
	#########################################################################################################
	def but_log_conf(event):
		but_log.configure(bg="#2C2C2C")
		but_log.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_log_cancel(event):
		but_log.configure(bg="#D0D0D0")
		but_log.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_log_comm():
		a=ent_question.get()
		ent_question.configure(state="normal")
		ent_answer.configure(state="normal")

		if (len(a)>0):
			if (a[-1]!=")" or a[-1] not in range(10)):
				ent_question.insert(END, "log("+ent_answer.get()+")" )

		elif(a==""):
			ent_question.insert(END, "log("+ent_answer.get()+")" )
		ent_answer.delete(0, END); 

		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")

	but_log = Button(standart_calc_wind, text="Log", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_log_comm)
	but_log.bind("<Motion>", but_log_conf)
	but_log.bind("<Leave>", but_log_cancel)
	but_log.place(x=232, y=257, width=76, height=40)
	#########################################################################################################
	def but_mod_conf(event):
		but_mod.configure(bg="#2C2C2C")
		but_mod.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_mod_cancel(event):
		but_mod.configure(bg="#D0D0D0")
		but_mod.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_mod_comm():

		a=ent_question.get()
		ent_question.configure(state="normal")
		ent_answer.configure(state="normal")

		if (len(a)>0):
			if((a[-1]=="+" or a[-1]=="-" or a[-1]=="/" or a[-1]=="*" or a[-1]=="%") and ent_answer.get()==""):
				if (len(a)>0):
					if(a[-2]=="*"):
						ent_question.delete(0, END)
						ent_question.insert(END, a[:-2]+"%" )
					else:
						ent_question.delete(0, END)
						ent_question.insert(END, a[:-1]+"%" )

			elif((a[-1]=="+" or a[-1]=="-" or a[-1]=="/" or a[-1]=="*" or a[-1]=="%") and ent_answer.get()!=""):
				ent_question.insert(END, ent_answer.get()+"%" )
				ent_answer.delete(0, END)

			elif(a[-1]==")" or a[-1]=="("):
				ent_question.insert(END, ent_answer.get()+"%" )
				ent_answer.delete(0, END)

		elif (ent_answer.get()!="" and ent_answer.get()!="ERROR"):
			ent_question.insert(END, ent_answer.get()+"%" )
			ent_answer.delete(0, END)

		elif (ent_question.get()==""):
			ent_question.delete(0, END); ent_question.insert(END, ent_answer.get()+"%" )
			ent_answer.delete(0, END); 

		else:
			ent_question.configure(state="normal"); ent_question.insert(END, "%" ); 

		ent_question.configure(state="disabled")
		ent_answer.configure(state="disabled")

	but_mod = Button(standart_calc_wind, text="Mod", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_mod_comm)
	but_mod.bind("<Motion>", but_mod_conf)
	but_mod.bind("<Leave>", but_mod_cancel)
	but_mod.place(x=308, y=257, width=76, height=40)
	#########################################################################################################
	def but_back_conf(event):
		but_back.configure(bg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_back_cancel(event):
		but_back.configure(bg="#D0D0D0")
		standart_calc_wind.configure(cursor="arrow")
	def but_back_comm():
		ent_question.configure(state="normal")
		ent_answer.configure(state="normal")
		if(ent_answer.get()==""):
			question=(ent_question.get())[:-1]
			ent_question.delete(0, END)
			ent_question.insert(END, question )
		else:
			answer=(ent_answer.get())[:-1]
			ent_answer.delete(0, END); ent_answer.insert(END, answer )

		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")

	but_back = Button(standart_calc_wind, text="⌫", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_back_comm)
	but_back.bind("<Motion>", but_back_conf)
	but_back.bind("<Leave>", but_back_cancel)
	but_back.place(x=232, y=217, width=76, height=40)
	#########################################################################################################
	def but_c_conf(event):
		but_c.configure(bg="#000000")
		but_c.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_c_cancel(event):
		but_c.configure(bg="#D0D0D0")
		but_c.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_c_comm():
		ent_question.configure(state="normal")
		ent_answer.configure(state="normal")
		ent_question.delete(0, END)
		ent_answer.delete(0, END)
		ent_answer.configure(state="disabled")
		ent_question.configure(state="disabled")
	but_c = Button(standart_calc_wind, text="C", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_c_comm)
	but_c.bind("<Motion>", but_c_conf)
	but_c.bind("<Leave>", but_c_cancel)
	but_c.place(x=308, y=217, width=76, height=40)
	#########################################################################################################
	def but_bf_conf(event):
		but_bf.configure(bg="#2C2C2C")
		but_bf.configure(fg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def but_bf_cancel(event):
		but_bf.configure(bg="#D0D0D0")
		but_bf.configure(fg="#000000")
		standart_calc_wind.configure(cursor="arrow")
	def but_bf_comm():

		a=ent_question.get()
		ent_answer.configure(state="normal")
		ent_question.configure(state="normal")

		if (len(a)>0):
			if (a[-1]!=")" or a[-1] not in range(10)):
				ent_question.insert(END, "defact("+ent_answer.get()+")" )

		elif(a==""):
			ent_question.insert(END, "defact("+ent_answer.get()+")" )
		ent_answer.delete(0, END)
		ent_question.configure(state="disabled")
		ent_answer.configure(state="disabled")


	but_bf = Button(standart_calc_wind, text="n! → n", font=("16"), relief=FLAT, bg="#D0D0D0", command=but_bf_comm)
	but_bf.bind("<Motion>", but_bf_conf)
	but_bf.bind("<Leave>", but_bf_cancel)
	but_bf.place(x=156, y=217, width=76, height=40)
	#######################################################################################################################
	#######################################################################################################################
	def KeyPress(event):
		def but_open_brecket_conf_key(event):
			but_open_brecket.configure(bg="#2C2C2C")
			but_open_brecket.configure(fg="#FFFFFF")
			but_open_brecket_comm()

		def but_close_brecket_conf_key(event):
			but_close_brecket.configure(bg="#2C2C2C")
			but_close_brecket.configure(fg="#FFFFFF")
			but_close_brecket_comm()

		def but_0_conf_key(event):
			but_0.configure(bg="#2C2C2C")
			but_0.configure(fg="#FFFFFF")
			but_0_comm()

		def but_point_conf_key(event):
			but_point.configure(bg="#2C2C2C")
			but_point.configure(fg="#FFFFFF")
			but_point_comm()

		def but_equal_conf_key(event):
			but_equal.configure(bg="#2C2C2C")
			but_equal.configure(fg="#FFFFFF")
			but_equal_comm()

		def but_plus_minus_conf_key(event):
			but_plus_minus.configure(bg="#2C2C2C")
			but_plus_minus.configure(fg="#FFFFFF")
			but_plus_minus_comm()

		def but_1_conf_key(event):
			but_1.configure(bg="#2C2C2C")
			but_1.configure(fg="#FFFFFF")
			but_1_comm()

		def but_2_conf_key(event):
			but_2.configure(bg="#2C2C2C")
			but_2.configure(fg="#FFFFFF")
			but_2_comm()

		def but_3_conf_key(event):
			but_3.configure(bg="#2C2C2C")
			but_3.configure(fg="#FFFFFF")
			but_3_comm()

		def but_plus_conf_key(event):
			but_plus.configure(bg="#2C2C2C")
			but_plus.configure(fg="#FFFFFF")
			but_plus_comm()


		def but_sqrt_conf_key(event):
			but_sqrt.configure(bg="#2C2C2C")
			but_sqrt.configure(fg="#FFFFFF")
			but_sqrt_comm()

		def but_4_conf_key(event):
			but_4.configure(bg="#2C2C2C")
			but_4.configure(fg="#FFFFFF")
			but_4_comm()

		def but_5_conf_key(event):
			but_5.configure(bg="#2C2C2C")
			but_5.configure(fg="#FFFFFF")
			but_5_comm()

		def but_6_conf_key(event):
			but_6.configure(bg="#2C2C2C")
			but_6.configure(fg="#FFFFFF")
			but_6_comm()

		def but_minus_conf_key(event):
			but_minus.configure(bg="#2C2C2C")
			but_minus.configure(fg="#FFFFFF")
			but_minus_comm()

		def but_factorial_conf_key(event):
			but_factorial.configure(bg="#2C2C2C")
			but_factorial.configure(fg="#FFFFFF")
			but_factorial_comm()
	 
		def but_7_conf_key(event):
			but_7.configure(bg="#2C2C2C")
			but_7.configure(fg="#FFFFFF")
			but_7_comm()

		def but_8_conf_key(event):
			but_8.configure(bg="#2C2C2C")
			but_8.configure(fg="#FFFFFF")
			but_8_comm()

		def but_9_conf_key(event):
			but_9.configure(bg="#2C2C2C")
			but_9.configure(fg="#FFFFFF")
			but_9_comm()

		def but_x_conf_key(event):
			but_x.configure(bg="#2C2C2C")
			but_x.configure(fg="#FFFFFF")  
			but_x_comm()

		def but_sin_conf_key(event):
			but_sin.configure(bg="#2C2C2C")
			but_sin.configure(fg="#FFFFFF")
			global rad_to_degrees_var
			but_sin_comm()
	  
		def but_cos_conf_key(event):
			but_cos.configure(bg="#2C2C2C")
			but_cos.configure(fg="#FFFFFF")
			global rad_to_degrees_var
			but_cos_comm()
 
		def but_tg_conf_key(event):
			but_tg.configure(bg="#2C2C2C")
			but_tg.configure(fg="#FFFFFF")
			global rad_to_degrees_var
			but_tg_comm()
			
		def but_ctg_conf_key(event):
			but_ctg.configure(bg="#2C2C2C")
			but_ctg.configure(fg="#FFFFFF")
			global rad_to_degrees_var
			but_ctg_comm()

		def but_div_conf_key(event):
			but_div.configure(bg="#2C2C2C")
			but_div.configure(fg="#FFFFFF")
			but_div_comm()

		def but_deg_conf_key(event):
			but_deg.configure(bg="#2C2C2C")
			but_deg.configure(fg="#FFFFFF")
			but_deg_comm()

		def but_pi_conf_key(event):
			but_pi.configure(bg="#2C2C2C")
			but_pi.configure(fg="#FFFFFF")
			but_pi_comm()
		
		def but_e_conf_key(event):
			but_e.configure(bg="#2C2C2C")
			but_e.configure(fg="#FFFFFF")
			but_e_comm()

		def but_log_conf_key(event):
			but_log.configure(bg="#2C2C2C")
			but_log.configure(fg="#FFFFFF")
			but_log_comm()
	 
		def but_mod_conf_key(event):
			but_mod.configure(bg="#2C2C2C")
			but_mod.configure(fg="#FFFFFF")
			but_mod_comm()

		def but_back_conf_key(event):
			but_back.configure(bg="#FFFFFF")
			but_back_comm()

		def but_c_conf_key(event):
			but_c.configure(bg="#000000")
			but_c.configure(fg="#FFFFFF")
			but_c_comm()
		
		def but_bf_conf_key(event):
			but_bf.configure(bg="#2C2C2C")
			but_bf.configure(fg="#FFFFFF")
			but_bf_comm()

		def copy(event):
			copy_answer.configure(bg="#FFFFFF")
			pyperclip.copy(ent_answer.get())

		def paste(event):
			paste_answer.configure(bg="#FFFFFF")
			ent_answer.configure(state="normal"); ent_answer.delete(0, END); ent_answer.insert(0, pyperclip.paste() ); ent_answer.configure(state="disabled")

		standart_calc_wind.bind(chr(40), but_open_brecket_conf_key)
		standart_calc_wind.bind(chr(41), but_close_brecket_conf_key)
		standart_calc_wind.bind("0", but_0_conf_key)
		standart_calc_wind.bind(chr(46), but_point_conf_key)
		standart_calc_wind.bind("<Return>", but_equal_conf_key)
		standart_calc_wind.bind("<Tab>", but_plus_minus_conf_key)
		standart_calc_wind.bind("1", but_1_conf_key)
		standart_calc_wind.bind("2", but_2_conf_key)
		standart_calc_wind.bind("3", but_3_conf_key)
		standart_calc_wind.bind(chr(43), but_plus_conf_key)
		standart_calc_wind.bind(chr(122), but_sqrt_conf_key)
		standart_calc_wind.bind("4", but_4_conf_key)
		standart_calc_wind.bind("5", but_5_conf_key)
		standart_calc_wind.bind("6", but_6_conf_key)
		standart_calc_wind.bind(chr(45), but_minus_conf_key)
		standart_calc_wind.bind(chr(91), but_factorial_conf_key)
		standart_calc_wind.bind("7", but_7_conf_key)
		standart_calc_wind.bind("8", but_8_conf_key)
		standart_calc_wind.bind("9", but_9_conf_key)
		standart_calc_wind.bind(chr(42), but_x_conf_key)
		standart_calc_wind.bind(chr(115), but_sin_conf_key)
		standart_calc_wind.bind(chr(99), but_cos_conf_key)
		standart_calc_wind.bind(chr(116), but_tg_conf_key)
		standart_calc_wind.bind(chr(103), but_ctg_conf_key)
		standart_calc_wind.bind(chr(47), but_div_conf_key)
		standart_calc_wind.bind(chr(94), but_deg_conf_key)
		standart_calc_wind.bind(chr(112), but_pi_conf_key)
		standart_calc_wind.bind(chr(101), but_e_conf_key)
		standart_calc_wind.bind(chr(108), but_log_conf_key)
		standart_calc_wind.bind(chr(37), but_mod_conf_key)
		standart_calc_wind.bind("<BackSpace>", but_back_conf_key)
		standart_calc_wind.bind("<Delete>", but_c_conf_key)
		standart_calc_wind.bind(chr(93), but_bf_conf_key)
		standart_calc_wind.bind("<Control-c>", copy)
		standart_calc_wind.bind("<Control-v>", paste)

	def KeyRelease(event):
		but_open_brecket.configure(bg="#D0D0D0")
		but_open_brecket.configure(fg="#000000")
		but_close_brecket.configure(bg="#D0D0D0")
		but_close_brecket.configure(fg="#000000")
		but_point.configure(bg="#D0D0D0")
		but_point.configure(fg="#000000")
		but_0.configure(bg="#F0F0F0")
		but_0.configure(fg="black")
		but_equal.configure(bg="#D0D0D0")
		but_equal.configure(fg="#000000")
		but_plus_minus.configure(bg="#D0D0D0")
		but_plus_minus.configure(fg="#000000")
		but_1.configure(bg="#F0F0F0")
		but_1.configure(fg="black")
		but_2.configure(bg="#F0F0F0")
		but_2.configure(fg="black")
		but_3.configure(bg="#F0F0F0")
		but_3.configure(fg="black")
		but_plus.configure(bg="#D0D0D0")
		but_plus.configure(fg="#000000")
		but_sqrt.configure(bg="#D0D0D0")
		but_sqrt.configure(fg="#000000")
		but_4.configure(bg="#F0F0F0")
		but_4.configure(fg="black")
		but_5.configure(bg="#F0F0F0")
		but_5.configure(fg="black")
		but_6.configure(bg="#F0F0F0")
		but_6.configure(fg="black")
		but_minus.configure(bg="#D0D0D0")
		but_minus.configure(fg="#000000")
		but_factorial.configure(bg="#D0D0D0")
		but_factorial.configure(fg="#000000")
		but_7.configure(bg="#F0F0F0")
		but_7.configure(fg="black")
		but_8.configure(bg="#F0F0F0")
		but_8.configure(fg="black")
		but_9.configure(bg="#F0F0F0")
		but_9.configure(fg="black")
		but_x.configure(bg="#D0D0D0")
		but_x.configure(fg="#000000")
		but_sin.configure(bg="#D0D0D0")
		but_sin.configure(fg="#000000")
		but_cos.configure(bg="#D0D0D0")
		but_cos.configure(fg="#000000")
		but_tg.configure(bg="#D0D0D0")
		but_tg.configure(fg="#000000")
		but_ctg.configure(bg="#D0D0D0")
		but_ctg.configure(fg="#000000")
		but_div.configure(bg="#D0D0D0")
		but_div.configure(fg="#000000")
		but_deg.configure(bg="#D0D0D0")
		but_deg.configure(fg="#000000")
		but_pi.configure(bg="#D0D0D0")
		but_pi.configure(fg="#000000")
		but_e.configure(bg="#D0D0D0")
		but_e.configure(fg="#000000")
		but_log.configure(bg="#D0D0D0")
		but_log.configure(fg="#000000")
		but_mod.configure(bg="#D0D0D0")
		but_mod.configure(fg="#000000")
		but_back.configure(bg="#D0D0D0")
		but_c.configure(bg="#D0D0D0")
		but_c.configure(fg="#000000")
		but_bf.configure(bg="#D0D0D0")
		but_bf.configure(fg="#000000")
		copy_answer.configure(bg="#A6A6A6")
		paste_answer.configure(bg="#A6A6A6")
	standart_calc_wind.bind("<KeyPress>", KeyPress)
	standart_calc_wind.bind("<KeyRelease>", KeyRelease)
	#######################################################################################################################
	#########################################################################################################

	##Scrollbar()
	Scr_question=Scrollbar(standart_calc_wind, orient=HORIZONTAL)
	##Entry()
	ent_question=Entry(standart_calc_wind, cursor="arrow", relief=FLAT, font=16, justify='right')
	##Entry disableting
	ent_question.configure(state='disabled')
	##Scr command
	Scr_question.configure(command=ent_question.xview)
	##Entry xscrollcommand
	ent_question.configure(xscrollcommand=Scr_question.set)
	##Place
	Scr_question.place(x=0, y=45, width=386, height=45)
	ent_question.place(x=17, y=45, width=352, height=40)

	##Scrollbar()
	Scr_answer=Scrollbar(standart_calc_wind, orient=HORIZONTAL)
	##Entry()
	ent_answer=Entry(standart_calc_wind, cursor="arrow", relief=FLAT, font=16, justify='right')
	##Entry disableting
	ent_answer.configure(state='disabled')
	##Scr command
	Scr_answer.configure(command=ent_answer.xview)
	##Entry xscrollcommand
	ent_answer.configure(xscrollcommand=Scr_answer.set)
	##Place
	Scr_answer.place(x=0, y=120, width=386, height=45)
	ent_answer.place(x=17, y=120, width=352, height=40)


	#################################################################################################################################
	def copy_answer_Motion(event):
		copy_answer.configure(bg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def copy_answer_Leave(event):
		standart_calc_wind.configure(cursor="arrow")
		copy_answer.configure(bg="#A6A6A6")
	def copy_answer_text():
		pyperclip.copy(ent_answer.get())
	copy_answer=Button(standart_calc_wind, command=copy_answer_text, text="⎘", font=("Times", "24"), relief=GROOVE, bg="#A6A6A6")
	copy_answer.bind("<Motion>", copy_answer_Motion)
	copy_answer.bind("<Leave>", copy_answer_Leave)
	copy_answer.place(x=0, y=190, width=38, height=40)

	def paste_answer_Motion(event):
		paste_answer.configure(bg="#FFFFFF")
		standart_calc_wind.configure(cursor="hand2")
	def paste_answer_Leave(event):
		standart_calc_wind.configure(cursor="arrow")
		paste_answer.configure(bg="#A6A6A6")
	def paste_answer_text():
		ent_answer.configure(state="normal"); ent_answer.delete(0, END); ent_answer.insert(0, pyperclip.paste() ); ent_answer.configure(state="disabled")
	paste_answer=Button(standart_calc_wind, command=paste_answer_text, text="⎗", font=("Times", "24"), relief=GROOVE, bg="#A6A6A6")
	paste_answer.bind("<Motion>", paste_answer_Motion)
	paste_answer.bind("<Leave>", paste_answer_Leave)
	paste_answer.place(x=40, y=190, width=38, height=40)

	c_p_lab=Label(standart_calc_wind, text="C          P", bg="#D3D3D3")
	c_p_lab.place(x=12, y=230)
	global calc_menu_but_clilcs
	calc_menu_but_clilcs=0
	def menu_lab_config(event):
		menu_lab["bg"]="#B5B5B5"
		standart_calc_wind.configure(cursor="hand2")
	def menu_lab_config_cancel(event):
		global calc_menu_but_clilcs
		if(calc_menu_but_clilcs%2==0):
			menu_lab["bg"]="#D3D3D3"
		standart_calc_wind.configure(cursor="arrow")
	def menu_lab_comm(event):
		global calc_menu_but_clilcs
		if(calc_menu_but_clilcs%2==0):
			menu_lab["bg"]="#B5B5B5"
			menu_lab.configure(relief="solid")
			calc_menu_frame.place(x=-2, y=40, height=455, width=300)
		else:
			calc_menu_frame.place(x=-300, y=40, height=455, width=300)
			menu_lab.configure(relief="flat")
		calc_menu_but_clilcs+=1
	def calc_frmae_motion(event):
		standart_calc_wind.configure(cursor="arrow")
	menu_lab=Label(standart_calc_wind, text=" ≡ ", font=("Times", "24"), bg="#D3D3D3")
	menu_lab.bind("<Motion>", menu_lab_config)
	menu_lab.bind("<Leave>", menu_lab_config_cancel)
	menu_lab.bind("<Button-1>", menu_lab_comm)
	menu_lab.grid(row=0, sticky=W) 
	menu_lab_name=Label(standart_calc_wind, text="Standart", font=("Times", "24"), bg="#D3D3D3")
	menu_lab_name.place(x=40)

	calc_menu_frame=Frame(standart_calc_wind, bg="#B5B5B5", highlightthickness=2, highlightbackground="black", highlightcolor="black")
	calc_menu_frame.bind("<Motion>", calc_frmae_motion)
	calc_menu_frame.place(x=-300, y=40, height=455, width=300)

	def discriminant_calculator_button_motion(event):
		discriminant_calculator_button["bg"]="#D0D0D0"
	def discriminant_calculator_button_leave(event):
		discriminant_calculator_button["bg"]="#B5B5B5"
	def discriminant_calculator_button_comm():
		standart_calc_wind.destroy()
		discriminant()
	discriminant_calculator_button=Button(calc_menu_frame, command=discriminant_calculator_button_comm, bg="#B5B5B5", text="Discriminant", relief=FLAT, font=("Times", "15"))
	discriminant_calculator_button.bind("<Motion>", discriminant_calculator_button_motion)
	discriminant_calculator_button.bind("<Leave>", discriminant_calculator_button_leave)
	discriminant_calculator_button.place(x=0, y=37, width=296)

	def programmer_calculator_button_motion(event):
		programmer_calculator_button["bg"]="#D0D0D0"
	def programmer_calculator_button_leave(event):
		programmer_calculator_button["bg"]="#B5B5B5"
	def programmer_calculator_button_comm():
		standart_calc_wind.destroy()
		programmer_calc()
	programmer_calculator_button=Button(calc_menu_frame, command=programmer_calculator_button_comm, bg="#B5B5B5", text="Programmer", relief=FLAT, font=("Times", "15"))
	programmer_calculator_button.bind("<Motion>", programmer_calculator_button_motion)
	programmer_calculator_button.bind("<Leave>", programmer_calculator_button_leave)
	programmer_calculator_button.place(x=0, y=5, width=296)
 #############################################################################################################################################
	def back_to_main_menu_config(event):
		back_to_main_menu["bg"]="#7D7D7D"
		standart_calc_wind.config(cursor="hand2")
	def back_to_main_menu_config_close(event):
		back_to_main_menu["bg"]="#4A4A4A"
		standart_calc_wind.config(cursor="arrow")
	def back_to_main_menu():
		standart_calc_wind.destroy()
		Main_menu()
	def back_to_main_menu_ev(event):
		standart_calc_wind.destroy()
		Main_menu()
	back_to_main_menu = Button(standart_calc_wind, text = "< Back to Main Menu", bg="#4A4A4A", command=back_to_main_menu)
	back_to_main_menu.bind("<Motion>", back_to_main_menu_config)
	back_to_main_menu.bind("<Leave>", back_to_main_menu_config_close)
	back_to_main_menu.place(x=3, y=504)
	standart_calc_wind.bind("<Escape>", back_to_main_menu_ev)

	def info_label_motion(event):
		standart_calc_wind.configure(cursor="question_arrow")
		info_frame.place(x=140, y=38, height=450, width=300)
		info_label.configure(bg="#F0F0F0")
		info_label.configure(relief="solid")
	def info_label_leave(event):
		standart_calc_wind.configure(cursor="arrow")
		info_frame.place(x=390, y=40, height=0, width=0)
		info_label.configure(bg="#D3D3D3")
		info_label.configure(relief="flat")
	info_label=Label(standart_calc_wind, text="i", font=("Times", "24", "italic"), bg="#D3D3D3")
	info_label.bind("<Motion>", info_label_motion)
	info_label.bind("<Leave>", info_label_leave)
	info_label.place(x=340, y=0, width=50, height=42)

	info_frame=Frame(standart_calc_wind, highlightthickness=2, highlightbackground="black", highlightcolor="black")
	info_frame.place(x=390, y=0, height=0, width=0)

	information_label=Label(info_frame, text="S ⇒ sin\nC ⇒ cos\nT ⇒ tg\nG ⇒ ctg\n[ ⇒ n→n!\n] ⇒ n1→n\nL ⇒ log\nZ ⇒ √\nTab ⇒ ±\n% ⇒ mod\nE ⇒ exp\nP ⇒ π\nBackspace ⇒ ⌫\n Del ⇒ C\n Ctrl+C ⇒ ⎘\n Ctrl+V ⇒ ⎗", font=("Times", "18", "italic"))
	information_label.place(x=35, y=0)
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
def num_sys():
	num_sys_wind=Tk()
	num_sys_wind.geometry('995x455')
	num_sys_wind.title("Numeral System")
	num_sys_wind.resizable(width=False, height=False)
	num_sys_wind.configure(background='#819196')
	file_name='icons\\numsys.gif'
	iconmain = PhotoImage(file=file_name)
	#num_sys_wind.tk.call('wm', 'iconphoto', num_sys_wind._w, iconmain)
	num_sys_wind.config(cursor="arrow")
	num_sys_wind.focus_force()
	################################################################################################################
	input_the_integer_number = Label(num_sys_wind, text="Input the integer number", background='#819196')
	input_the_integer_number.place(x=10, y=10)

	output_int_num = Label(num_sys_wind, text="Output", background='#819196')
	output_int_num.place(x=927, y=10)

	input_base_label_right = Label(num_sys_wind, text="<< Input the base", background='#819196')
	input_base_label_right.place(x=603, y=10)

	input_base_label_left = Label(num_sys_wind, text="Input the base >>", background='#819196')
	input_base_label_left.place(x=280, y=10)
	##################################################################################################################
	int_num_sys_enter_left = Entry(num_sys_wind, width="5", background='#B1B4B5')
	int_num_sys_enter_left.place(x=380, y=10)
	int_num_sys_enter_left.insert(0, "2")

	int_num_left = Text(num_sys_wind, width="50", height="10", background="#C5C8C9")
	int_num_left.place(x=10, y=30)

	int_num_left_scr_bar=Scrollbar(num_sys_wind, command=int_num_left.yview, orient=VERTICAL)
	int_num_left.configure(yscrollcommand=int_num_left_scr_bar.set)
	int_num_left_scr_bar.place(x=413, y=29, height = 165)
	##################################################################################
	int_num_sys_enter_right = Entry(num_sys_wind, width="5", background='#B1B4B5')
	int_num_sys_enter_right.place(x=570, y=10)
	int_num_sys_enter_right.insert(0, "10")

	int_num_right = Text(num_sys_wind, width="50", height="10", background="#C5C8C9")
	int_num_right.place(x=570, y=30)

	int_num_right_scr_bar=Scrollbar(num_sys_wind, command=int_num_right.yview, orient=VERTICAL)
	int_num_right.configure(yscrollcommand=int_num_right_scr_bar.set)
	int_num_right_scr_bar.place(x=974, y=29, height = 165)
	#################################################################################################################
	error_label = Label(num_sys_wind, text="Input the number bases\n and number", background='#819196')

	def back_to_main_menu_button_config(event):
		back_to_main_menu_button["bg"]="#7D7D7D"
		num_sys_wind.config(cursor="hand2")
	def back_to_main_menu_button_config_cancel(event):
		back_to_main_menu_button["bg"]="#4A4A4A"
		num_sys_wind.config(cursor="arrow")
	def Main_menu_back():
		num_sys_wind.destroy()
		Main_menu()
	def Main_menu_back_ev(event):
		num_sys_wind.destroy()
		Main_menu()		
	back_to_main_menu_button = Button(num_sys_wind, text="< Back to Main Menu", bg="#4A4A4A", command=Main_menu_back)
	back_to_main_menu_button.bind("<Motion>", back_to_main_menu_button_config)
	back_to_main_menu_button.bind("<Leave>", back_to_main_menu_button_config_cancel)
	back_to_main_menu_button.place(x=10, y=420)
	num_sys_wind.bind("<Escape>", Main_menu_back_ev)
	##################################################
	def convet_int():
		try:
			left_sys = int_num_sys_enter_left.get()
			left_sys=int(left_sys)
			right_sys = int_num_sys_enter_right.get()
			right_sys=int(right_sys)
			left_num_input = int_num_left.get("1.0", END)
	####################################################
			less_then_base_int_array=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "$", "_"]
			error_index=0
			base=left_sys
			btn=0
			while(error_index<len(left_num_input[0:-1])):
				if base<=less_then_base_int_array.index(str(left_num_input)[error_index]):
					btn=1
					error_index+=1
				else:
					error_index+=1
	####################################################
			if(left_sys=='' or right_sys==''):
				error_label["text"]="Input the number bases"

			elif(left_sys < 2 or left_sys > 64 or right_sys < 2 or right_sys > 64):
				error_label["text"]="Please choose the base\n less then 65\n and\n bigger then 1"
				error_label.place(x=430, y=10)
				int_num_left__to__int_num_right_but.place(x=465, y=100)
			elif(btn==0):
				error_label["text"]=''
				int_num_left__to__int_num_right_but.place(x=470, y=50)
				base=left_sys
	
				final_array = []
				left_num_input=left_num_input[:-1]
				for n in range(len(left_num_input)):
					final_array.append(less_then_base_int_array.index(left_num_input[n]))

				final_num=0
				index=0
				final_array_reverse=final_array[::-1]
				while(index<len(final_array_reverse)):
					final_num+=final_array_reverse[index]*(int(base)**index)
					index+=1

				base_two=right_sys
				base_final_num_array=[]

				fl_num_base=int(final_num)%base_two
				int_num_base=int(final_num)//base_two
				base_final_num_array.append(fl_num_base)
				while(int_num_base>0):
					fl_num_base=int_num_base%base_two
					int_num_base=int_num_base//base_two
					base_final_num_array.append(fl_num_base)
				base_final_num_array=base_final_num_array[::-1]

				final_array_findal=[]
				for n in range(len(base_final_num_array)):
					final_array_findal.append(less_then_base_int_array[(base_final_num_array[n])])
				fin_ind=0
				final=''
				while(fin_ind<len(final_array_findal)):
					final+=str(final_array_findal[fin_ind])
					fin_ind+=1

				int_num_right.delete('1.0', END)
				int_num_right.insert(END, final)
			elif(btn==1):
				error_label["text"]="Input Error"
				error_label.place(x=470, y=10)
				int_num_right.delete('1.0', END)
		except:
			error_label["text"]="Input the correct\n number bases\n and number"
			error_label.place(x=450, y=1)

	def but_config(event):
		int_num_left__to__int_num_right_but["bg"]="#B8B8B8"
		num_sys_wind.config(cursor="hand2")

	def but_config_close(event):
		int_num_left__to__int_num_right_but["bg"]="#819196"
		num_sys_wind.config(cursor="arrow")

	int_num_left__to__int_num_right_but = Button(num_sys_wind, text=" Convert ", command=convet_int, bg="#819196")
	int_num_left__to__int_num_right_but.bind('<Motion>', but_config)
	int_num_left__to__int_num_right_but.bind('<Leave>', but_config_close)
	int_num_left__to__int_num_right_but.place(x=470, y=50)

	###########################################################################

	input_the_float_number = Label(num_sys_wind, text="Input the float number", background='#819196')
	input_the_float_number.place(x=10, y=210)

	output_fl_num = Label(num_sys_wind, text="Output", background='#819196')
	output_fl_num.place(x=927, y=210)

	output_fl_number_base = Label(num_sys_wind, text="<< Digits after the decimal point", background='#819196')
	output_fl_number_base.place(x=605, y=395)

	input_base_label_right_bottom = Label(num_sys_wind, text="<< Input the base", background='#819196')
	input_base_label_right_bottom.place(x=603, y=210)

	input_base_label_left_bottom = Label(num_sys_wind, text="Input the base >>", background='#819196')
	input_base_label_left_bottom.place(x=280, y=210)
	##################################################################################################################
	fl_num_sys_enter_left = Entry(num_sys_wind, width="5", background='#B1B4B5')
	fl_num_sys_enter_left.place(x=380, y=210)
	fl_num_sys_enter_left.insert(0, "2")

	fl_num_left = Text(num_sys_wind, width="50", height="10", background="#C5C8C9")
	fl_num_left.place(x=10, y=230)

	fl_num_left_scr_bar=Scrollbar(num_sys_wind, command=fl_num_left.yview, orient=VERTICAL)
	fl_num_left.configure(yscrollcommand=fl_num_left_scr_bar.set)
	fl_num_left_scr_bar.place(x=413, y=229, height = 165)
	##################################################################################
	fl_num_sys_enter_right = Entry(num_sys_wind, width="5", background='#B1B4B5')
	fl_num_sys_enter_right.place(x=570, y=210)
	fl_num_sys_enter_right.insert(0, "10")

	output_fl_number_base_entry = Entry(num_sys_wind, width="5", background='#B1B4B5')
	output_fl_number_base_entry.place(x=570, y=395)
	output_fl_number_base_entry.insert(0, "20")

	fl_num_right = Text(num_sys_wind, width="50", height="10", background="#C5C8C9")
	fl_num_right.place(x=570, y=230)

	fl_num_right_scr_bar=Scrollbar(num_sys_wind, command=fl_num_right.yview, orient=VERTICAL)
	fl_num_right.configure(yscrollcommand=fl_num_right_scr_bar.set)
	fl_num_right_scr_bar.place(x=974, y=229, height = 165)
	#################################################################################################################

	error_label_bottom = Label(num_sys_wind, text="Input the number bases\n and number", background='#819196')

	def convet_fl():
		try:
			left_sys_bottom = fl_num_sys_enter_left.get()
			left_sys_bottom=int(left_sys_bottom)

			right_sys_bottom = fl_num_sys_enter_right.get()
			right_sys_bottom=int(right_sys_bottom)

			digits_bottom = output_fl_number_base_entry.get()
			digits_bottom=int(digits_bottom)

			left_num_input_bottom = fl_num_left.get("1.0", END)
			left_num_input_bottom=left_num_input_bottom[:-1]

			a=left_num_input_bottom
			base=left_sys_bottom
			baseout=right_sys_bottom
			a_out=digits_bottom

			less_then_base_fl_array=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "$", "_"]
			error_index_fl=0
			base_fl=left_sys_bottom


			btnfl=0
			replace=left_num_input_bottom.replace(".","")
			while(error_index_fl<len(replace)):
				if base_fl<=less_then_base_fl_array.index(str(replace)[error_index_fl]):
					btnfl=1
					error_index_fl+=1
				else:
					error_index_fl+=1

			if(left_sys_bottom < 2 or left_sys_bottom > 64 or right_sys_bottom < 2 or right_sys_bottom > 64):
				error_label_bottom["text"]="Please choose the base\n less then 65\n and\n bigger then 1"
				error_label_bottom.place(x=430, y=210)
				fl_num_left__to__fl_num_right_but.place(x=465, y=300)
			elif(left_sys_bottom=='' or right_sys_bottom=='' or output_fl_number_base_entry==''):
				error_label_bottom["text"]="Input the number bases and Digits"
				fl_num_left__to__fl_num_right_but.place(x=470, y=250)

			elif(btnfl==0):
				error_label_bottom["text"]=''
				fl_num_left__to__fl_num_right_but.place(x=470, y=250)
				if "." not in left_num_input_bottom:
					error_label_bottom["text"]="Please input float number"

				left_num_input_bottom_array_final=[]
				n=0
				while(n<len(left_num_input_bottom)):
					left_num_input_bottom_array_final.append(left_num_input_bottom[n])
					n+=1

				final_array=[]
				for n in range(len(left_num_input_bottom)):
					if left_num_input_bottom[n]==".":
						final_array.append(".")
					else:
						final_array.append( less_then_base_fl_array.index(left_num_input_bottom[n]) )

				final_array_int_past_reverse=(final_array[:final_array.index(".")])[::-1]

				final_array_fl_past=final_array[final_array.index(".")+1:]

				index=0
				int_past=0
				while(index<len(final_array_int_past_reverse)):
					int_past+=final_array_int_past_reverse[index]*(left_sys_bottom**index)
					index+=1

				fl_a_len_index=len(final_array_fl_past)-1
				fl_past_array=0
				while(fl_a_len_index>=0):
					fl_past_array+=final_array_fl_past[fl_a_len_index]*(left_sys_bottom**(-fl_a_len_index))
					fl_a_len_index-=1
				base_10_num=int_past+float(fl_past_array/left_sys_bottom)

				#integer#######################################################################
				fl_base_10_num=int(base_10_num)%right_sys_bottom
				int_base_10_num=int(base_10_num)//right_sys_bottom
				final_num_array_int=[]
				final_num_array_int.append(str(fl_base_10_num))
				while(int_base_10_num>0):
					fl_base_10_num=int_base_10_num%right_sys_bottom
					int_base_10_num=int_base_10_num//right_sys_bottom
					final_num_array_int.append(str(fl_base_10_num))

				#############################################################################
				#float#######################################################################
				num = float(base_10_num)
				number=int(num)
				num=num-number
				b=0
				final_fl_sum_array=[]
				while (b<a_out):
					num=num*right_sys_bottom
					integer=int(num)
					num-=integer
					final_fl_sum_array.append(str(integer))
					b=b+1

				#############################################################################

				array_semi_final=final_num_array_int[::-1]+["."]+final_fl_sum_array

				final_array_final=[]
				for n in range(len(array_semi_final)):
					if array_semi_final[n]==".":
						final_array_final.append(".")
					else:
						final_array_final.append( less_then_base_fl_array[int(array_semi_final[n])] )

				final_index=0
				final_num=''
				while(final_index<len(final_array_final)):
					final_num+=final_array_final[final_index]
					final_index+=1

				while (final_num[len(final_num)-1]=="0"):
					final_num=final_num[:-1]

				fl_num_right.delete('1.0', END)
				fl_num_right.insert(END, final_num)

			elif(btnfl==1):
				error_label_bottom["text"]="Input Error"
				error_label_bottom.place(x=470, y=210)
				fl_num_right.delete('1.0', END)
		except:
			error_label_bottom["text"]="Input the number bases,\n number and Digits"
			error_label_bottom.place(x=430, y=210)
			fl_num_left__to__fl_num_right_but.place(x=470, y=250)

	def bottom_but_config(event):
		fl_num_left__to__fl_num_right_but["bg"]="#B8B8B8"
		num_sys_wind.config(cursor="hand2")

	def bottom_but_config_close(event):
		fl_num_left__to__fl_num_right_but["bg"]="#819196"
		num_sys_wind.config(cursor="arrow")

	fl_num_left__to__fl_num_right_but = Button(num_sys_wind, text=" Convert ", command=convet_fl, bg="#819196")
	fl_num_left__to__fl_num_right_but.bind('<Motion>', bottom_but_config)
	fl_num_left__to__fl_num_right_but.bind('<Leave>', bottom_but_config_close)
	fl_num_left__to__fl_num_right_but.place(x=470, y=250)
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
def morse():
	morse_wind=Tk()
	morse_wind.title("Morse Converter")
	morse_wind.geometry('990x520')
	# icon = PhotoImage(file='icons\\morse.gif')
	# morse_wind.tk.call('wm', 'iconphoto', morse_wind._w, icon)
	morse_wind.resizable(width=False, height=False)
	morse_wind.configure(background='#819196')
	morse_wind.config(cursor="arrow")
	morse_wind.focus_force()
	######################################
	######################convert functions
	morse_arr=     [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", ".-.-.-", "--..--", "..--..", ".----.", "-.-.--", "-..-.", "---...", "-.-.-.", "-...-", ".-.-.", "-....-", "..--.-", ".-..-.", ".--.-.", "/", "#"]
	Ascii=         ["A" , "B"   , "C"   , "D"  , "E", "F"   , "G"  , "H"   , "I" , "J"   , "K"  , "L"   , "M" , "N" , "O"  , "P"   , "Q"   , "R"  , "S"  , "T", "U"  , "V"   , "W"  , "X"   , "Y"   , "Z"   , "1"    , "2"    , "3"    , "4"    , "5"    , "6"    , "7"    , "8"    , "9"    , "0"    , "."     , ","     , "?"     , "'"     , "!"     , "/"    , ":"     , ";"     , "="    , "+"    , "-"     , "_"     , '"'     , "@"     , " ", ""]
	Ascii_low_case=["a" , "b"   , "c"   , "d"  , "e", "f"   , "g"  , "h"   , "i" , "j"   , "k"  , "l"   , "m" , "n" ,"o"   , "p"   , "q"   , "r"  , "s"  , "t", "u"  , "v"   , "w"  , "x"   , "y"   , "z"]

	def ascii_to_morse(text_input):
		global morse_str
		text=""
		for n in range(len(text_input)):
			if text_input[n] in Ascii_low_case:
				text+=Ascii[Ascii_low_case.index(text_input[n])]
			else:
				text+=text_input[n]

		morse_str=""
		for k in range(len(text)):
			morse_str+=morse_arr[Ascii.index(text[k]) if text[k] in Ascii else len(morse_arr)-1]+" "
		return morse_str

	def morse_to_ascii(morse):
		morse=morse.split(" ")
		text=""
		for k in range(len(morse)):
			text+=Ascii[morse_arr.index(morse[k]) if morse[k] in morse_arr else len(Ascii)-1]
		return text
	######################convert functions
	######################################

	def text_to_morse():
		text_input=ascii_input.get('1.0', END)[:-1]
		morse=ascii_to_morse(text_input)
		
		morse_input.delete('1.0', END)
		morse_input.insert(1.0, morse)

	def morse_to_text():
		morse=morse_input.get('1.0', END)[:-1]
		text=morse_to_ascii(morse)

		ascii_input.delete('1.0', END)
		ascii_input.insert(1.0, text)

 #############################################################################
	def copy_ascii():
		pyperclip.copy(ascii_input.get("1.0", END)[:-1])
	def paste_ascii():
		ascii_input.delete("1.0", END)
		ascii_input.insert(1.0, pyperclip.paste())
	def clear_ascii():
		ascii_input.delete("1.0", END)

	def copy_morse():
		pyperclip.copy(morse_input.get("1.0", END)[:-1])
	def paste_morse():
		morse_input.delete("1.0", END)
		morse_input.insert(1.0, pyperclip.paste())
	def clear_morse():
		morse_input.delete("1.0", END)

	def clear_all():
		morse_input.delete("1.0", END)
		ascii_input.delete("1.0", END)
 ###########################################################################

	###########ASCII Widgets
	ascii_label=Label(morse_wind, text="Input/Output ASCII Text", font=("Times", "11", "italic"), bg="#819196")
	ascii_label.place(x=5, y=5)
	
	ascii_input=Text(morse_wind, bg="#C5C8C9")
	ascii_input.place(x=5, y=35, height=300, width=450)

	ascii_input_scrolbal=Scrollbar(morse_wind, command=ascii_input.yview)
	ascii_input_scrolbal.place(x=455, y=36, height=299)

	ascii_input.configure(yscrollcommand=ascii_input_scrolbal.set)

	ascii_copy_button=Button(morse_wind, text="Copy ASCII", relief=FLAT, bg="#C5C8C9", command=copy_ascii)
	ascii_copy_button.place(x=5, y=350)
	ascii_paste_button=Button(morse_wind, text="Paste ASCII", relief=FLAT, bg="#C5C8C9", command=paste_ascii)
	ascii_paste_button.place(x=5, y=375)
	ascii_clear_button=Button(morse_wind, text="Clear ASCII", relief=FLAT, bg="#C5C8C9", command=clear_ascii)
	ascii_clear_button.place(x=75, y=350)
	##############################
    ##
    ##
	###########Morse Widgets
	morse_label=Label(morse_wind, text="Input/Output Morse Code", font=("Times", "11", "italic"), bg="#819196")
	morse_label.place(x=530, y=5)
	
	morse_input=Text(morse_wind, bg="#C5C8C9")
	morse_input.place(x=520, y=35, height=300, width=450)

	morse_input_scrolbal=Scrollbar(morse_wind, command=morse_input.yview)
	morse_input_scrolbal.place(x=965, y=36, height=299)

	morse_input.configure(yscrollcommand=morse_input_scrolbal.set)

	morse_copy_button=Button(morse_wind, text="Copy Morse", relief=FLAT, bg="#C5C8C9", command=copy_morse)
	morse_copy_button.place(x=907, y=350)
	morse_paste_button=Button(morse_wind, text="Paste Morse", relief=FLAT, bg="#C5C8C9", command=paste_morse)
	morse_paste_button.place(x=907, y=375)
	morse_clear_button=Button(morse_wind, text="Clear Morse", relief=FLAT, bg="#C5C8C9", command=clear_morse)
	morse_clear_button.place(x=833, y=350)
	##############################
	################################################
	ascii_to_morse_button=Button(morse_wind, text="Text to Morse", relief="flat", command=text_to_morse)
	ascii_to_morse_button.place(x=450, y=337)
	morse_to_ascii_button=Button(morse_wind, text="Morse to Text", relief="flat", command=morse_to_text)
	morse_to_ascii_button.place(x=450, y=362)
	clear_all_button=Button(morse_wind, text="Clear ALL", relief="flat", command=clear_all)
	clear_all_button.place(x=461, y=387)
	################################################
	global stop_var, n
	stop_var=0
	n=0
	def play(space, slesh, morse_str, symbhol=70):
		global n, stop_var
		space=space_entry.get()
		symbhol=symbhol_entry.get()
		slesh=slesh_entry.get()
		if stop_var==0:
			try:
				if morse_str[n]==".":
					PlaySound(path + "\\Sounds\\Morse\\dot.wav", SND_FILENAME)
					morse_wind.after(symbhol, lambda: play(space, slesh, morse_str, symbhol))

				elif morse_str[n]=="-":
					PlaySound(path + "\\Sounds\\Morse\\-.wav", SND_FILENAME)
					morse_wind.after(symbhol, lambda: play(space, slesh, morse_str, symbhol))

				elif morse_str[n]==" ":
					morse_wind.after(space, lambda: play(space, slesh, morse_str, symbhol))

				elif morse_str[n]=="/":
					morse_wind.after(slesh, lambda: play(space, slesh, morse_str, symbhol))
				n+=1
			except IndexError:
				n=0
		else:
			stop_var=0
			n=0

	def stop():
		global stop_var
		stop_var=1
	#################################################################################################################
	space_label=Label(morse_wind, text="after space(millisecond)", font="Arial", bg="#819196", fg="#0F0F0F")
	space_label.place(x=320, y=427)
	space_entry=Entry(morse_wind, bg="#C5C8C9")
	space_entry.insert(0, "500")
	space_entry.place(x=490, y=425, height=28 , width=50)
	space=space_entry.get()
	#################################################################################################################
	slesh_label=Label(morse_wind, text="after slesh  (millisecond)", font="Arial", bg="#819196", fg="#0F0F0F")
	slesh_label.place(x=320, y=457)
	slesh_entry=Entry(morse_wind, bg="#C5C8C9")
	slesh_entry.insert(0, "50")
	slesh_entry.place(x=490, y=455, height=28 , width=50)
	slesh=slesh_entry.get()
	#################################################################################################################
	symbhol_label=Label(morse_wind, text="after . or -   (millisecond)", font="Arial", bg="#819196", fg="#0F0F0F")
	symbhol_label.place(x=320, y=487)
	symbhol_entry=Entry(morse_wind, bg="#C5C8C9")
	symbhol_entry.insert(0, "100")
	symbhol_entry.place(x=490, y=485, height=28 , width=50)
	#################################################################################################################

	second_milisecond=Label(morse_wind, text="1 second = 1000 millisecond", bg="#96A9AF", font=("Arial", "16"))
	second_milisecond.place(x=570, y=456)

	play_sound_button=Button(morse_wind, text="►", font=("Arial"), fg="#232424", bg="#78797A", command=lambda: play(int(space), int(slesh), morse_input.get('1.0', END)[:-1]))
	play_sound_button.place(x=250, y=425, height=40, width=40)

	stop_sound_button=Button(morse_wind, text="◼", font=("Arial"), fg="#232424", bg="#78797A", command=stop)
	stop_sound_button.place(x=250, y=470, height=40, width=40)

	def back_to_main_menu_config(event):
		back_to_main_menu["bg"]="#7D7D7D"
		morse_wind.config(cursor="hand2")
	def back_to_main_menu_config_close(event):
		back_to_main_menu["bg"]="#4A4A4A"
		morse_wind.config(cursor="arrow")
	def Main_menu_back():
		morse_wind.destroy()
		Main_menu()
	def Main_menu_back_ev(event):
		morse_wind.destroy()
		Main_menu()
	back_to_main_menu = Button(morse_wind, text = "< Back to Main Menu", bg="#4A4A4A", command=Main_menu_back)
	back_to_main_menu.bind("<Motion>", back_to_main_menu_config)
	back_to_main_menu.bind("<Leave>", back_to_main_menu_config_close)
	back_to_main_menu.place(x=0, y=490)

	morse_wind.bind("<Escape>", Main_menu_back_ev)
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
def binary_system():
	binary_wind=Tk()
	binary_wind.title("Binary System")
	binary_wind.geometry('990x455')
	# file_name="icons\\binary.gif".replace(" ", "")
	# icon = PhotoImage(file=file_name)
	# binary_wind.tk.call('wm', 'iconphoto', binary_wind._w, icon)
	binary_wind.resizable(width=False, height=False)
	binary_wind.configure(background='#819196')
	binary_wind.config(cursor="arrow")
	binary_wind.focus_force()

	binary_array=['00100000', '00100001', '00100010', '00100011', '00100100', '00100101', '00100110', '00100111', 
				  '00101000', '00101001', '00101010', '00101011', '00101100', '00101101', '00101110', '00101111',
				  '00110000', '00110001', '00110010', '00110011', '00110100', '00110101', '00110110', '00110111', 
				  '00111000', '00111001', '00111010', '00111011', '00111100', '00111101', '00111110', '00111111', 
				  '01000000', '01000001', '01000010', '01000011', '01000100', '01000101', '01000110', '01000111', 
				  '01001000', '01001001', '01001010', '01001011', '01001100', '01001101', '01001110', '01001111', 
				  '01010000', '01010001', '01010010', '01010011', '01010100', '01010101', '01010110', '01010111', 
				  '01011000', '01011001', '01011010', '01011011', '01011100', '01011101', '01011110', '01011111', 
				  '01100000', '01100001', '01100010', '01100011', '01100100', '01100101', '01100110', '01100111', 
				  '01101000', '01101001', '01101010', '01101011', '01101100', '01101101', '01101110', '01101111', 
				  '01110000', '01110001', '01110010', '01110011', '01110100', '01110101', '01110110', '01110111', 
				  '01111000', '01111001', '01111010', '01111011', '01111100', '01111101', '01111110', ""        ]
	ascii_array =[" "       , "!"       , '"'       , "#"       , "$"       , '%'       , '&'       , "'"       , 
				  '('       , ')'       , '*'       , '+'       , ','       , '-'       , '.'       , '/'       , 
				  '0'       , '1'       , '2'       , '3'       , '4'       , '5'       , '6'       , '7'       , 
				  '8'       , '9'       , ':'       , ';'       , '<'       , '='       , '>'       , '?'       , 
				  '@'       , 'A'       , 'B'       , 'C'       , 'D'       , 'E'       , 'F'       , 'G'       , 
				  'H'       , 'I'       , 'J'       , 'K'       , 'L'       , 'M'       , 'N'       , 'O'       , 
				  'P'       , 'Q'       , 'R'       , 'S'       , 'T'       , 'U'       , 'V'       , 'W'       , 
				  'X'       , 'Y'       , 'Z'       , '['       , '\\'      , ']'       , '^'       , '_'       , 
				  '`'       , 'a'       , 'b'       , 'c'       , 'd'       , 'e'       , 'f'       , 'g'       , 
				  'h'       , 'i'       , 'j'       , 'k'       , 'l'       , 'm'       , 'n'       , 'o'       , 
				  'p'       , 'q'       , 'r'       , 's'       , 't'       , 'u'       , 'v'       , 'w'       , 
				  'x'       , 'y'       , 'z'       , "{"       , "|"       , "}"       , "~"       , ""        ]

	def texttobinary():
		delimiter = Number_delimiter_entry.get()
		text=binaryenter.get('1.0', END).replace("\n", '')
		binary=""
		for n in range(len(text)):
			binary+=binary_array[ascii_array.index(text[n])] + delimiter
		binary=binary[:-len(delimiter)]
		textenter.delete('1.0', END)
		textenter.insert(1.0, binary)

	def binarytotext():
		binary=(  (  textenter.get('1.0', END)[:-1].rstrip()  ).lstrip()  ).split(Number_delimiter_entry.get())
		text=""
		for n in range(len(binary)):
			text+=ascii_array[binary_array.index(binary[n])]
		binaryenter.delete('1.0', END)
		binaryenter.insert(1.0, text)


	#ASCII buttons
	def clear_ascii():
		binaryenter.delete('1.0', END)
	def copy_ascii():
		pyperclip.copy(binaryenter.get('1.0', END))
	def paste_ascii():
		binaryenter.delete('1.0', END)
		binaryenter.insert(1.0, pyperclip.paste()[:-1] )
	#ASCII buttons
	#Binary code buttons
	def clear_binary():
		textenter.delete('1.0', END)
	def copy_binary():
		pyperclip.copy(textenter.get('1.0', END))
	def paste_binary():
		textenter.delete('1.0', END)
		textenter.insert(1.0, pyperclip.paste()[:-1])
	#Binary code buttons
	def clear_all():
		textenter.delete('1.0', END)
		binaryenter.delete('1.0', END)    
	########################################################
	def pastetxtbut_config(event):
		pastetxtbut["bg"]="#B8B8B8"
		binary_wind.config(cursor="hand2")

	def pastetxtbut_config_close(event):
		pastetxtbut["bg"]="#819196"
		binary_wind.config(cursor="arrow")
	########
	def copytxtbut_config(event):
		copytxtbut["bg"]="#B8B8B8"
		binary_wind.config(cursor="hand2")

	def copytxtbut_config_close(event):
		copytxtbut["bg"]="#819196"
		binary_wind.config(cursor="arrow")
	########
	def cleartxtbut_config(event):
		cleartxtbut["bg"]="#B8B8B8"
		binary_wind.config(cursor="hand2")

	def cleartxtbut_config_close(event):
		cleartxtbut["bg"]="#819196"
		binary_wind.config(cursor="arrow")
	##################
	def bintotextbut_config(event):
		bintotextbut["bg"]="#B8B8B8"
		binary_wind.config(cursor="hand2")

	def bintotextbut_config_close(event):
		bintotextbut["bg"]="#819196"
		binary_wind.config(cursor="arrow")
	########
	def clearallbut_config(event):
		clearallbut["bg"]="#B8B8B8"
		binary_wind.config(cursor="hand2")

	def clearallbut_config_close(event):
		clearallbut["bg"]="#819196"
		binary_wind.config(cursor="arrow")
	########
	def txttobinbut_config(event):
		txttobinbut["bg"]="#B8B8B8"
		binary_wind.config(cursor="hand2")

	def txttobinbut_config_close(event):
		txttobinbut["bg"]="#819196"
		binary_wind.config(cursor="arrow")
	#################
	def pastebinbut_config(event):
		pastebinbut["bg"]="#B8B8B8"
		binary_wind.config(cursor="hand2")

	def pastebinbut_config_close(event):
		pastebinbut["bg"]="#819196"
		binary_wind.config(cursor="arrow")
	#######
	def copybinbut_config(event):
		copybinbut["bg"]="#B8B8B8"
		binary_wind.config(cursor="hand2")

	def copybinbut_config_close(event):
		copybinbut["bg"]="#819196"
		binary_wind.config(cursor="arrow")
	#######
	def clearbinbut_config(event):
		clearbinbut["bg"]="#B8B8B8"
		binary_wind.config(cursor="hand2")

	def clearbinbut_config_close(event):
		clearbinbut["bg"]="#819196"
		binary_wind.config(cursor="arrow")

 #####################################################################

	Number_delimiter_label=Label(binary_wind, text="Delimiter", font=("Arial", "12"), bg="#94A6AC")
	Number_delimiter_label.place(x=600, y=353)
	Number_delimiter_entry=Entry(binary_wind, font=("Arial", "14"), bg="#94A6AC")
	Number_delimiter_entry.insert(0, " ")
	Number_delimiter_entry.place(x=730, y=350, width=50, height=30)



 #####################################################################
	###########################################################
	#label input ASCII text
	binarylab=Label(binary_wind, text='Input / Output    ASCII    text', font=15, bg="#819196")
	binarylab.grid(row=0, column=0, sticky=W+E)
	#label input binary code
	textlab=Label(binary_wind, text='Input / Output    Binary    code', font=15, bg="#819196")
	textlab.grid(row=0, column=3, sticky=W+E)
	#binary text
	binaryenter=Text(width=53, height=20, background="#C5C8C9")
	#vertycal scrollbar
	binaryenterscry=Scrollbar(binary_wind, command=binaryenter.yview)
	#binary text configure vertycal
	binaryenter.configure(yscrollcommand=binaryenterscry.set)
	#grids
	binaryenter.grid(row=1, column=0, sticky=W)
	binaryenterscry.grid(row=1, column=1, sticky=N+S+W)

	#buttons for text
	pastetxtbut=Button(binary_wind, text="Paste ASCII text", bg="#819196", command=paste_ascii)###
	pastetxtbut.bind("<Motion>", pastetxtbut_config)###
	pastetxtbut.bind("<Leave>", pastetxtbut_config_close)###
	pastetxtbut.grid(row=2, column=0, sticky=W)###

	copytxtbut=Button(binary_wind, text="Copy ASCII text", bg="#819196", command=copy_ascii)###
	copytxtbut.bind("<Motion>", copytxtbut_config)###
	copytxtbut.bind("<Leave>", copytxtbut_config_close)###
	copytxtbut.grid(row=3, column=0, sticky=W)###

	cleartxtbut=Button(binary_wind, text="Clear ASCII text", bg="#819196", command=clear_ascii)###
	cleartxtbut.bind("<Motion>", cleartxtbut_config)###
	cleartxtbut.bind("<Leave>", cleartxtbut_config_close)###
	cleartxtbut.grid(row=4, column=0, sticky=W)###
	#butons for text

	#buttons for convert
	bintotextbut=Button(binary_wind, text="Binary to ASCII", bg="#819196", command=binarytotext)###
	bintotextbut.bind("<Motion>", bintotextbut_config)###
	bintotextbut.bind("<Leave>", bintotextbut_config_close)###
	bintotextbut.grid(row=3, column=2)###

	clearallbut=Button(binary_wind, text="Clear All", height = 1, width = 11, bg="#819196", command=clear_all)###
	clearallbut.bind("<Motion>", clearallbut_config)###
	clearallbut.bind("<Leave>", clearallbut_config_close)###    
	clearallbut.grid(row=4, column=2,)###

	txttobinbut=Button(binary_wind, text="ASCII to Binary", bg="#819196", command=texttobinary)###
	txttobinbut.bind("<Motion>", txttobinbut_config)###
	txttobinbut.bind("<Leave>", txttobinbut_config_close)### 
	txttobinbut.grid(row=2, column=2)###
	#buttons for convert

	#buttons for binary
	pastebinbut=Button(binary_wind, text="Paste Binary Code", bg="#819196", command=paste_binary)###
	pastebinbut.bind("<Motion>", pastebinbut_config)###
	pastebinbut.bind("<Leave>", pastebinbut_config_close)### 
	pastebinbut.grid(row=2, column=3, sticky=E)###

	copybinbut=Button(binary_wind, text="Copy Binary Code", bg="#819196", command=copy_binary)###
	copybinbut.bind("<Motion>", copybinbut_config)###
	copybinbut.bind("<Leave>", copybinbut_config_close)### 
	copybinbut.grid(row=3, column=3, sticky=E)###

	clearbinbut=Button(binary_wind, text="Clear Binary Code", bg="#819196", command=clear_binary)###
	clearbinbut.bind("<Motion>", clearbinbut_config)###
	clearbinbut.bind("<Leave>", clearbinbut_config_close)### 
	clearbinbut.grid(row=4, column=3, sticky=E)###
	#butons for binary

	textenter=Text(width=54, height=20, background="#C5C8C9")
	#vertycal scrollbar
	textenterscry=Scrollbar(binary_wind, command=textenter.yview)
	#binary text configure vertycal
	textenter.configure(yscrollcommand=textenterscry.set)

	textenter.grid(row=1, column=3, sticky=E)
	textenterscry.grid(row=1, column=4, sticky=N+S+W)
 ##############################################################################################################################
	def back_to_main_menu_config(event):
		back_to_main_menu["bg"]="#7D7D7D"
		binary_wind.config(cursor="hand2")
	def back_to_main_menu_config_close(event):
		back_to_main_menu["bg"]="#4A4A4A"
		binary_wind.config(cursor="arrow")
	def Main_menu_back():
		binary_wind.destroy()
		Main_menu()
	def Main_menu_back_ev(event):
		binary_wind.destroy()
		Main_menu()
	back_to_main_menu = Button(binary_wind, text = "< Back to Main Menu", bg="#4A4A4A", command=Main_menu_back)
	back_to_main_menu.bind("<Motion>", back_to_main_menu_config)
	back_to_main_menu.bind("<Leave>", back_to_main_menu_config_close)
	back_to_main_menu.grid(column=0, row=5, sticky=W)
	binary_wind.bind("<Escape>", Main_menu_back_ev)
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
def Main_menu():
	main_menu=Tk()
	main_menu.title("Main Menu")
	main_menu.geometry("500x400")
	# iconmain = PhotoImage(file='icons\\main.gif')
	# main_menu.tk.call('wm', 'iconphoto', main_menu._w, iconmain)
	main_menu.resizable(width=False, height=False)
	main_menu.configure(background='#CDCDCD')
	title_label=Label(main_menu, text="...ProfMath...", font=("Times", "21", "italic"), bg="#C4C4C4")
	title_label.place(x=0, y=0, height=40, width=500)
	main_menu.focus_force()
 #################################################################################################################################################
	def binary_to_ascii_button_conf(event):
		binary_to_ascii_button.configure(font=("Times", "16"))
		binary_to_ascii_button.configure(bg="#949494")
		binary_to_ascii_button.configure(fg="#121212")
		main_menu.configure(cursor="hand2")
	def binary_to_ascii_button_cancel(event):
		binary_to_ascii_button.configure(font=("Times", "14"))
		binary_to_ascii_button.configure(bg="#CDCDCD")
		binary_to_ascii_button.configure(fg="#383838")
		main_menu.configure(cursor="arrow")
	def binary_system_global_func():
		main_menu.destroy()
		binary_system()
	binary_to_ascii_button=Button(main_menu, bg="#CDCDCD", text="ASCII⇔Binary\n Converter", font=("Times", "14"), relief=GROOVE, fg="#383838", command=binary_system_global_func)
	binary_to_ascii_button.bind("<Motion>", binary_to_ascii_button_conf)
	binary_to_ascii_button.bind("<Leave>", binary_to_ascii_button_cancel)
	binary_to_ascii_button.place(x=5, y=55, height=60, width=150)
 #################################################################################################################################################
	def morse_button_conf(event):
		morse_button.configure(font=("Times", "16"))
		morse_button.configure(bg="#949494")
		morse_button.configure(fg="#121212")
		main_menu.configure(cursor="hand2")
	def morse_button_cancel(event):
		morse_button.configure(font=("Times", "14"))
		morse_button.configure(bg="#CDCDCD")
		morse_button.configure(fg="#383838")
		main_menu.configure(cursor="arrow")
	def morse_global_func():
		main_menu.destroy()
		morse()		
	morse_button=Button(main_menu, bg="#CDCDCD", text="ASCII⇔Morse\n Converter", font=("Times", "14"), relief=GROOVE, fg="#383838", command=morse_global_func)
	morse_button.bind("<Motion>", morse_button_conf)
	morse_button.bind("<Leave>", morse_button_cancel)
	morse_button.place(x=345, y=55, height=60, width=150)
 #################################################################################################################################################
	def num_sys_button_conf(event):
		num_sys_button.configure(font=("Times", "16"))
		num_sys_button.configure(bg="#949494")
		num_sys_button.configure(fg="#121212")
		main_menu.configure(cursor="hand2")
	def num_sys_button_cancel(event):
		num_sys_button.configure(font=("Times", "14"))
		num_sys_button.configure(bg="#CDCDCD")
		num_sys_button.configure(fg="#383838")
		main_menu.configure(cursor="arrow")
	def num_sys_global_func():
		main_menu.destroy()
		num_sys()
	num_sys_button=Button(main_menu, bg="#CDCDCD", text="Number System\n Converter", font=("Times", "14"), relief=GROOVE, fg="#383838", command=num_sys_global_func)
	num_sys_button.bind("<Motion>", num_sys_button_conf)
	num_sys_button.bind("<Leave>", num_sys_button_cancel)
	num_sys_button.place(x=5, y=120, height=60, width=150)
 #################################################################################################################################################
	def calc_button_conf(event):
		calc_button.configure(font=("Times", "16"))
		calc_button.configure(bg="#949494")
		calc_button.configure(fg="#121212")
		main_menu.configure(cursor="hand2")
	def calc_button_cancel(event):
		calc_button.configure(font=("Times", "14"))
		calc_button.configure(bg="#CDCDCD")
		calc_button.configure(fg="#383838")
		main_menu.configure(cursor="arrow")
	def calc_global_func():
		main_menu.destroy()
		standart_calculator()
	calc_button=Button(main_menu, bg="#CDCDCD", text="Calculator", font=("Times", "14"), relief=GROOVE, fg="#383838", command=calc_global_func)
	calc_button.bind("<Motion>", calc_button_conf)
	calc_button.bind("<Leave>", calc_button_cancel)
	calc_button.place(x=345, y=120, height=60, width=150)
	main_menu.mainloop()
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
Main_menu()