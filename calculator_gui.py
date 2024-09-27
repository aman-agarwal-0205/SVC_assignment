import tkinter
from tkinter import *
import math

calc = Tk()

calc.title("CALCULATOR")

# p = PhotoImage(file = "Python_codes\Personal_projects\images\OIP.png")
# calc.iconphoto(False, p)
''' # uploading the photo saved in the same location as the program file and using it as our app logo.'''


frame1 = LabelFrame(calc, bg= 'white')
frame2 = LabelFrame(calc, bg = 'white')
frame1.grid(row=0,column=0)
frame2.grid(row=1,column=0)

''' # we have created 2 frames. 1 for the entrybox and the other for the remaining buttons.
    # without doing so, the alignment of the entrybox was disturbing the alignment of the other buttons.'''


ent = Entry(frame1, text = "0", width = 26, borderwidth= 2, font=('Arial', 24), foreground= "grey")
ent.configure(justify= 'right')
# ent.insert(0, "0") 
''' # we used 'configure' and 'justify' to change the alignment of the text in entrybox to right. '''
ent.grid()


def bt_click(num):
    global current
    current = ent.get()
    '''  # we store the entered number in 'current' variable using 'get' keyword.'''
    ent.delete(0, END)   
    ent.insert(0, str(current) + str(num)) 
    
    ''' 
    # we are storing using this step to display the numbers in the correct order.
    # this step helps to display the current number on the right side and the previously entered numbers on the left.
    # else it would display the new number on the left side and the previously entered number on the right.
    '''



'''
# except for 'factorial', in all other operational functions we take the first number(term) from the user.
# after user has chosen the operation they want to perform, the second number(term) is stored in the 'equal' function.
# from there we perform the operations that we want to perform.
# we have declared 'f_num' and 'maths' as global variables to as they are needed outside the function as well.
# the entire first number is stored in 'f_num' (until the user chooses the operation)
# 'maths' is used  to check the 'if-else' condition and display the respective function.
# when one function-button is clicked and that function is called, we delete the previously entered numbers and then take the second number from the user.
'''


def sqrt():
    f_num = int(ent.get())
    ent.delete(0, END)
    sqrt = math.sqrt(f_num)
    ent.insert(0, int(sqrt))



def fact():
    f_num = int(ent.get())
    ent.delete(0, END)
    fact = math.factorial(f_num)
    ent.insert(0, int(fact))
    ''' # here we take the input of the number from the user and then directly display the answer from the function.
        # we have used the 'math' module. '''


def all_clr():
    ent.delete(0, END) 
    ''' # we clear all the content displayed on the entrybox. '''

    
def add():
    first_number = ent.get()
    global f_num
    global maths 
    maths = 'Add'
    f_num = float(first_number)
    ent.delete(0, END)


def sub():
    first_number = ent.get()
    global f_num
    global maths 
    maths = 'Sub'
    f_num = float(first_number)
    ent.delete(0, END)


def mult():
    first_number = ent.get()
    global f_num
    global maths 
    maths = 'Mult'
    f_num = int(first_number)
    ent.delete(0, END)


def div():
    first_number = ent.get()
    global f_num
    global maths 
    maths = 'Div'
    f_num = float(first_number)
    ent.delete(0, END)


def perc():
    first_number = ent.get()
    global f_num
    global maths
    maths = 'Perc'
    f_num = float(first_number)
    ent.delete(0, END)


def power():
    first_number = float(ent.get())
    global f_num
    global maths 
    maths = 'Power'
    f_num = float(first_number)
    ent.delete(0, END)


def back():
    numlen = len(ent.get())
    ent.delete(numlen - 1)
    if numlen == 1:
        ent.insert(0, "0")
        


def exp():
    first_number = float(ent.get())
    global f_num
    global maths 
    maths = 'Exp'
    f_num = int(first_number)
    ent.delete(0, END)


def bt_0_0():
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, int(str(current) + str('00')))


def equal():
    sec_number =float(ent.get())
    ent.delete(0, END)
    if maths == 'Add':    
        ent.insert(0, float(f_num + sec_number))

    elif maths == 'Sub':
        ent.insert(0, float(f_num - sec_number))
    
    elif maths == 'Div':
        ent.insert(0, float(f_num/sec_number))

    elif maths == 'Mult':
        ent.insert(0, float(f_num*sec_number))

    elif maths == 'Perc':
        ent.insert(0, (float((f_num/sec_number)*100),"%"))
        
    elif maths == 'Power':
        ent.insert(0, float(math.pow(f_num, sec_number))) 

    elif maths == 'Exp':
        ent.insert(0, float(math.exp(sec_number)))



# def play_music():
#     mixer.music.load("Python_codes\\Personal_projects\\audio.aup3")
#     mixer.music.play()


def  button(hover, leave):

    '''
    # we are calling two parameters 'hover' and 'leave' to change the color of the button when we bring the cursor on the button.
    # we are calling the 'frame2' for the buttons.
    # text --> to display the text on the button.
    # padx, pady --> to change the dimensions of the button x and y axis respectively.
    # command --> to provide the button a command for it to perform; like calling a function.
    # lambda --> used when we pass a value through the command.
    # relief --> used to change the border-type of buttons.
    # activebackground --> this changes the color of the button when the button is clicked.
    '''


    bt_1 = Button(frame2, text = '1', padx = 40, pady = 25, command = lambda: bt_click(1), relief = 'flat', activebackground= 'grey', bg= 'white')
    bt_2 = Button(frame2, text = '2', padx = 40, pady = 25, command = lambda: bt_click(2), relief = 'flat', activebackground= 'grey', bg= 'white')
    bt_3 = Button(frame2, text = '3', padx = 40, pady = 25, command = lambda: bt_click(3), relief = 'flat', activebackground= 'grey', bg= 'white')
    bt_4 = Button(frame2, text = '4', padx = 40, pady = 25, command = lambda: bt_click(4), relief = 'flat', activebackground= 'grey', bg= 'white')
    bt_5 = Button(frame2, text = '5', padx = 40, pady = 25, command = lambda: bt_click(5), relief = 'flat', activebackground= 'grey', bg= 'white')
    bt_6 = Button(frame2, text = '6', padx = 40, pady = 25, command = lambda: bt_click(6), relief = 'flat', activebackground= 'grey', bg= 'white')
    bt_6 = Button(frame2, text = '6', padx = 40, pady = 25, command = lambda: bt_click(6), relief = 'flat', activebackground= 'grey', bg= 'white')
    bt_7 = Button(frame2, text = '7', padx = 40, pady = 25, command = lambda: bt_click(7), relief = 'flat', activebackground= 'grey', bg= 'white')
    bt_8 = Button(frame2, text = '8', padx = 40, pady = 25, command = lambda: bt_click(8), relief = 'flat', activebackground= 'grey', bg= 'white')
    bt_9 = Button(frame2, text = '9', padx = 40, pady = 25, command = lambda: bt_click(9), relief = 'flat', activebackground= 'grey', bg= 'white')   
    bt_0 = Button(frame2, text = '0', padx = 40, pady = 25, command = lambda: bt_click(0), relief = 'flat', activebackground= 'grey', bg= 'white') 
    bt_00 = Button(frame2, text = '00', padx = 40, pady = 25, command = bt_0_0, relief = 'flat', activebackground= 'grey', bg= 'white')
    bt_dot = Button(frame2, text = '.', font = ('', 20), padx = 33, pady = 15, command= lambda: bt_click('.'), activebackground= 'grey', bg= 'white')

    bt_equal = Button(frame2, text = '=', font = ('', 15), padx = 80, pady = 25, command= equal, activebackground= 'grey', bg= 'white')
    bt_add = Button(frame2, text = '+', font = ('', 16), padx = 34, pady = 25, command= add, activebackground= 'grey', bg= 'white')
    bt_sub = Button(frame2, text = '-', font = ('', 16), padx = 33, pady = 20, command= sub, activebackground= 'grey', bg= 'white')
    bt_mult = Button(frame2, text = 'X', font = ('', 14), padx = 34, pady = 26, command= mult, activebackground= 'grey', bg= 'white')
    bt_div = Button(frame2, text = '÷', font = ('', 20), padx = 27, pady = 12, command= div, activebackground= 'grey', bg= 'white')
    bt_perc = Button(frame2, text = '%', font = ('', 13), padx = 34, pady = 25, command= perc, activebackground= 'grey', bg= 'white')
    bt_fact = Button(frame2, text = '!', font = ('', 14), padx = 37, pady = 20, command = fact, activebackground= 'grey', bg= 'white')
    bt_sqrt = Button(frame2, text = '√', font = ('', 14), padx = 34, pady = 20, command = sqrt, activebackground= 'grey', bg= 'white')
    bt_all_clear = Button(frame2, text = 'AC', font = ('', 15), padx =24, pady = 23, command= all_clr, activebackground= 'grey', bg= 'white')
    bt_exit = Button(frame2, text = '☠', font = ('', 20), padx= 20, pady = 15, command = exit, activebackground= 'grey', bg= 'white') 
    '''  #we can use '.destroy' keyword in place of 'exit' to exit the app. '''
    bt_back = Button(frame2, text = '⌫', padx = 25, font = ('', 14), pady = 20, command= back, activebackground= 'grey', bg= 'white')  
    bt_power = Button(frame2, text = 'x^', font = ('', 13), padx = 32, pady = 27, command= power, activebackground= 'grey', bg= 'white')
    bt_exp = Button(frame2, text = 'e^', font = ('', 13), padx = 31, pady = 27, command= exp, activebackground= 'grey', bg= 'white')
    '''
    # '.bind' --> used to make the button change color when the cursor hovers over the button.
    # '<Enter>' --> the function works when the cursor enters the button.
    # '<Leave>' --> the function works when the cursor leaves the button.
    # lambda e: bt.config --> used to change the configuration 'background' of the button.
    '''



    bt_1.bind("<Enter>", func = lambda e: bt_1.config(background= hover))
    bt_1.bind("<Leave>", func = lambda e: bt_1.config(background= leave))

    bt_2.bind("<Enter>", func = lambda e: bt_2.config(background= hover))
    bt_2.bind("<Leave>", func = lambda e: bt_2.config(background= leave))
    
    bt_3.bind("<Enter>", func = lambda e: bt_3.config(background= hover))
    bt_3.bind("<Leave>", func = lambda e: bt_3.config(background= leave))

    bt_4.bind("<Enter>", func = lambda e: bt_4.config(background= hover))
    bt_4.bind("<Leave>", func = lambda e: bt_4.config(background= leave))
    
    bt_5.bind("<Enter>", func = lambda e: bt_5.config(background= hover))
    bt_5.bind("<Leave>", func = lambda e: bt_5.config(background= leave))

    bt_6.bind("<Enter>", func = lambda e: bt_6.config(background= hover))
    bt_6.bind("<Leave>", func = lambda e: bt_6.config(background= leave))

    bt_7.bind("<Enter>", func = lambda e: bt_7.config(background= hover))
    bt_7.bind("<Leave>", func = lambda e: bt_7.config(background= leave))

    bt_8.bind("<Enter>", func = lambda e: bt_8.config(background= hover))
    bt_8.bind("<Leave>", func = lambda e: bt_8.config(background= leave))

    bt_9.bind("<Enter>", func = lambda e: bt_9.config(background= hover))
    bt_9.bind("<Leave>", func = lambda e: bt_9.config(background= leave))

    bt_0.bind("<Enter>", func = lambda e: bt_0.config(background= hover))
    bt_0.bind("<Leave>", func = lambda e: bt_0.config(background= leave))

    bt_00.bind("<Enter>", func = lambda e: bt_00.config(background= hover))
    bt_00.bind("<Leave>", func = lambda e: bt_00.config(background= leave))

    bt_add.bind("<Enter>", func = lambda e: bt_add.config(background= hover))
    bt_add.bind("<Leave>", func = lambda e: bt_add.config(background= leave))

    bt_mult.bind("<Enter>", func = lambda e: bt_mult.config(background= hover))
    bt_mult.bind("<Leave>", func = lambda e: bt_mult.config(background= leave))

    bt_sub.bind("<Enter>", func = lambda e: bt_sub.config(background= hover))
    bt_sub.bind("<Leave>", func = lambda e: bt_sub.config(background= leave))

    bt_div.bind("<Enter>", func = lambda e: bt_div.config(background= hover))
    bt_div.bind("<Leave>", func = lambda e: bt_div.config(background= leave))

    bt_perc.bind("<Enter>", func = lambda e: bt_perc.config(background= hover))
    bt_perc.bind("<Leave>", func = lambda e: bt_perc.config(background= leave))

    bt_fact.bind("<Enter>", func = lambda e: bt_fact.config(background= hover))
    bt_fact.bind("<Leave>", func = lambda e: bt_fact.config(background= leave))

    bt_equal.bind("<Enter>", func = lambda e: bt_equal.config(background= hover))
    bt_equal.bind("<Leave>", func = lambda e: bt_equal.config(background= leave))

    bt_power.bind("<Enter>", func = lambda e: bt_power.config(background= hover))
    bt_power.bind("<Leave>", func = lambda e: bt_power.config(background= leave))

    bt_exit.bind("<Enter>", func = lambda e: bt_exit.config(background= hover))
    bt_exit.bind("<Leave>", func = lambda e: bt_exit.config(background= leave))

    bt_exp.bind("<Enter>", func = lambda e: bt_exp.config(background= hover))
    bt_exp.bind("<Leave>", func = lambda e: bt_exp.config(background= leave))

    bt_back.bind("<Enter>", func = lambda e: bt_back.config(background= hover))
    bt_back.bind("<Leave>", func = lambda e: bt_back.config(background= leave))
    
    bt_dot.bind("<Enter>", func = lambda e: bt_dot.config(background= hover))
    bt_dot.bind("<Leave>", func = lambda e: bt_dot.config(background= leave))

    bt_all_clear.bind("<Enter>", func = lambda e: bt_all_clear.config(background= hover))
    bt_all_clear.bind("<Leave>", func = lambda e: bt_all_clear.config(background= leave))

    bt_sqrt.bind("<Enter>", func = lambda e: bt_sqrt.config(background= hover))
    bt_sqrt.bind("<Leave>", func = lambda e: bt_sqrt.config(background= leave))

    ''' # grid --> used to locate the button in respect to rows and columns. '''

    bt_7.grid(row = 3, column = 0)
    bt_8.grid(row = 3, column = 1)
    bt_9.grid(row = 3, column = 2)
    bt_perc.grid(row = 1, column = 0) 
    bt_power.grid(row = 3, column= 3) 

    bt_4.grid(row = 4, column = 0)
    bt_5.grid(row = 4, column = 1)
    bt_6.grid(row = 4, column = 2)
    bt_add.grid(row = 2, column = 0)
    bt_exp.grid(row = 4, column = 3)

    bt_1.grid(row = 6, column = 0)
    bt_2.grid(row = 6, column = 1)
    bt_3.grid(row = 6, column = 2)
    bt_mult.grid(row = 2, column = 1)

    bt_0.grid(row = 7, column = 0)
    bt_00.grid(row = 7, column = 1)
    bt_sub.grid(row = 6, column = 3)
    bt_dot.grid(row = 7, column = 2)
        
    bt_equal.grid(row = 2, column = 2, columnspan= 2)
    bt_fact.grid(row = 1, column = 1)
    bt_div.grid(row = 1, column = 2)
    bt_back.grid(row = 1, column= 4)

    bt_all_clear.grid(row = 7,  column= 3)
    bt_exit.grid(row = 7, column = 4)
    bt_sqrt.grid(row= 1, column= 3)
   


button("grey", "white")
''' # we call the 'button' funtion with the attributes for changing the color while hovering the cursor. '''

calc.config(bg= 'black')

calc.mainloop()